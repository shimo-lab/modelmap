import os
import gc
import torch
from typing import List, Dict, Tuple, Optional
from rich.progress import track
from transformers import AutoTokenizer, AutoModelForCausalLM


class LikelihoodCalculator:
    def __init__(
            self,
            model_name: str,
            dtype: torch.dtype = torch.float16, 
            cache_dir: Optional[str] = None,
            local_files_only: Optional[bool] = False,
            trust_remote_code: Optional[bool] = False,
            hf_token: Optional[str] = None
    ):
        self.model_name = model_name
        self.dtype = dtype
        self.cache_dir = cache_dir
        self.local_files_only = local_files_only
        self.trust_remote_code = trust_remote_code
        self.hf_token = hf_token
        self._use_cache = True
        self._over_length_indices = []
    
    def _load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            cache_dir = self.cache_dir,
            local_files_only = self.local_files_only,
            trust_remote_code = self.trust_remote_code,
            token = self.hf_token
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map = "auto",
            cache_dir = self.cache_dir,
            torch_dtype = self.dtype,
            output_hidden_states = False,
            output_attentions = False,
            local_files_only = self.local_files_only,
            trust_remote_code = self.trust_remote_code,
            token = self.hf_token
        )
        self.model.eval()
        self._set_device()
        self._set_max_length()
    
    def _set_device(self):
        if hasattr(self.model, 'hf_device_map') and self.model.hf_device_map:
            module_names = list(self.model.hf_device_map.keys())
            first_module = module_names[0]
            self.input_device = self.model.hf_device_map[first_module]
            last_module = module_names[-1]
            self.output_device = self.model.hf_device_map[last_module]
        else:
            self.input_device = next(iter(self.model.parameters())).device
            self.output_device = self.input_device
    
    def _set_max_length(self):
        if hasattr(self.model.config, 'max_position_embeddings'): 
            self.max_length = self.model.config.max_position_embeddings
        elif hasattr(self.model.config, 'n_positions'):
            self.max_length = self.model.config.n_positions
        else:
            self.max_length = getattr(self.model.config, 'max_sequence_length', 2048)

    def _calculate_likelihood(self, tokenized_data: List[Tuple[int, torch.Tensor]]) -> List[Dict]:
        results = []
        for idx, tokens in track(tokenized_data, total=len(tokenized_data)):
            tokens = tokens.to(self.input_device)
            current_textdata = {
                "index": idx,
                "num-tokens": int(tokens.shape[1])
            }
            with torch.no_grad():
                try:
                    output = self.model(tokens, use_cache=self._use_cache)
                except Exception as e:
                    output = self.model(tokens, use_cache=False)
                    self._use_cache = False
                logits = output.logits
                log_probs = torch.log_softmax(logits, dim=-1)
                next_tokens = tokens[0, 1:].to(log_probs.device)
                ## Log-probs of the next tokens at each position
                token_log_probs = [
                    float(log_probs[0, i, next_tokens[i]])
                    for i in range(tokens.shape[1]-1)
                ]
                ## Log-likelihood of the text
                log_likelihood = sum(token_log_probs)
                current_textdata["log-likelihood"] = log_likelihood
                current_textdata["token-log-probs"] = token_log_probs
            results.append(current_textdata)
        return results
    
    def _tokenize(self, texts: List[Tuple[int, str]]) -> List[Tuple[int, torch.Tensor]]:
        tokenized_data = []
        for idx, text in texts:
            if len(self.tokenizer.encode(text)) > self.max_length:
                self._over_length_indices.append(idx)
            tokenized = self.tokenizer.encode(
                text,
                return_tensors = 'pt',
                truncation = True,
                max_length = self.max_length
            )
            tokenized_data.append((idx, tokenized))
        return tokenized_data
    
    def _clear_cache(self):
        if hasattr(self, 'model'):
            del self.model
        if hasattr(self, 'tokenizer'):
            del self.tokenizer
        torch.cuda.empty_cache()
        gc.collect()
    
    def __call__(self, texts: List[Tuple[int, str]]) -> List[Dict]:
        self._load_model()
        tokenized_data = self._tokenize(texts)
        likelihoods = self._calculate_likelihood(tokenized_data)
        self._clear_cache()
        return likelihoods