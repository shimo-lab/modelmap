import torch
from datetime import datetime

from typing import Optional, List
from .io.text_data import TextDataLoader
from .io.logp_data import LikelihoodDataManager
from .logging.logger import LoggerLikelihood
from .calculator.likelihood import LikelihoodCalculator
from _config import get_log_likelihood_dir


class RunnerLikelihood:
    def __init__(
            self,
            textdata_name: str,
            modelname_list: List[str],
            dtype: torch.dtype = torch.float16,
            log_name: Optional[str] = None,
            textindex_list: Optional[list] = None,
            models_dir: Optional[str] = None,
            trust_remote_code: Optional[bool] = False,
            local_files_only: Optional[bool] = False,
            hf_token: Optional[str] = None
    ):
        self.textdata_name = textdata_name
        self.modelname_list = modelname_list
        self.dtype = dtype
        self.dtype_str = str(dtype).split('.')[-1]
        self.textindex_list = textindex_list
        self.models_dir = models_dir
        self.trust_remote_code = trust_remote_code
        self.local_files_only = local_files_only
        self.hf_token = hf_token

        # Load texts
        if textindex_list is None:
            self.textindex_list = list(range(0, 10000))
        loader = TextDataLoader(textdata_name)
        self.texts = loader.get_texts(textindex_list)

        # Set up logger
        log_dir = get_log_likelihood_dir()
        if log_name is None:
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_name = f"{textdata_name}_{now}.log"
        self.logger = LoggerLikelihood(log_dir, log_name)
    
    def _get_uncomputed_texts(self, model_name: str):
        data_manager = LikelihoodDataManager(self.textdata_name, model_name, self.dtype_str)
        computed_idx = data_manager.load_computed_idx()
        uncomputed_idx = sorted(list(set(self.textindex_list) - set(computed_idx)))
        if not uncomputed_idx:
            return None
        else:
            uncomputed_texts = [idx_text for idx_text in self.texts if idx_text[0] in uncomputed_idx]
            return uncomputed_texts
    
    def _compute_likelihood(self, model_name: str):
        data_manager = LikelihoodDataManager(self.textdata_name, model_name, self.dtype_str)
        texts_to_process = self._get_uncomputed_texts(model_name)
        if texts_to_process is None:
            self.logger.log_finish(model_name, "FINISH (already computed)")
        else:
            try:
                caculator = LikelihoodCalculator(
                    model_name = model_name,
                    dtype = self.dtype,
                    cache_dir = self.models_dir,
                    local_files_only = self.local_files_only,
                    trust_remote_code = self.trust_remote_code,
                )
                results = caculator(texts_to_process)
                data_manager.save_results(results)
                self.logger.log_finish(model_name, "FINISH")
            except Exception as e:
                self.logger.log_error(model_name, "ERROR", str(e))
    
    def _write_header(self):
        self.logger.write(f"------------------------")
        self.logger.write(f"Textdata: {self.textdata_name}")
        self.logger.write(f"Number of texts: {len(self.texts)}")
        self.logger.write(f"Number of models: {len(self.modelname_list)}")
        self.logger.write(f"Dtype: {self.dtype}")
        self.logger.write(f"------------------------")
    
    def run(self):
        self._write_header()
        for model_name in self.modelname_list:
            self._compute_likelihood(model_name)