# h2oGPT Model Card
## Summary

H2O.ai's `h2ogpt-oig-oasst1-256-6_9b` is a 6.9 billion parameter instruction-following large language model licensed for commercial use.

- Base model: [EleutherAI/pythia-6.9b](https://huggingface.co/EleutherAI/pythia-6.9b)
- Fine-tuning dataset: [h2oai/h2ogpt-oig-oasst1-instruct-cleaned-v1](https://huggingface.co/datasets/h2oai/h2ogpt-oig-oasst1-instruct-cleaned-v1)
- Data-prep and fine-tuning code: [H2O.ai Github](https://github.com/h2oai/h2ogpt)
- Training logs: [zip](https://huggingface.co/h2oai/h2ogpt-oig-oasst1-256-6_9b/blob/main/pythia-6.9b.h2ogpt-oig-oasst1-instruct-cleaned-v1.json.1_epochs.5fc91911bc2bfaaf3b6c2de577c4b0ae45a07a4a.9.zip)

## Usage

To use the model with the `transformers` library on a machine with GPUs, first make sure you have the `transformers` and `accelerate` libraries installed.

```bash
pip install transformers==4.28.1
pip install accelerate==0.18.0
```

```python
import torch
from transformers import pipeline

generate_text = pipeline(model="h2oai/h2ogpt-oig-oasst1-256-6_9b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto", prompt_type='human_bot')

res = generate_text("Why is drinking water so healthy?", max_new_tokens=100)
print(res[0]["generated_text"])
```

Alternatively, if you prefer to not use `trust_remote_code=True` you can download [instruct_pipeline.py](https://huggingface.co/h2oai/h2ogpt-oig-oasst1-256-6_9b/blob/main/h2oai_pipeline.py),
store it alongside your notebook, and construct the pipeline yourself from the loaded model and tokenizer:

```python
import torch
from h2oai_pipeline import H2OTextGenerationPipeline
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("h2oai/h2ogpt-oig-oasst1-256-6_9b", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("h2oai/h2ogpt-oig-oasst1-256-6_9b", torch_dtype=torch.bfloat16, device_map="auto")
generate_text = H2OTextGenerationPipeline(model=model, tokenizer=tokenizer, prompt_type='human_bot')

res = generate_text("Why is drinking water so healthy?", max_new_tokens=100)
print(res[0]["generated_text"])
```

## Model Architecture

```
GPTNeoXForCausalLM(
  (gpt_neox): GPTNeoXModel(
    (embed_in): Embedding(50432, 4096)
    (layers): ModuleList(
      (0-31): 32 x GPTNeoXLayer(
        (input_layernorm): LayerNorm((4096,), eps=1e-05, elementwise_affine=True)
        (post_attention_layernorm): LayerNorm((4096,), eps=1e-05, elementwise_affine=True)
        (attention): GPTNeoXAttention(
          (rotary_emb): RotaryEmbedding()
          (query_key_value): Linear(in_features=4096, out_features=12288, bias=True)
          (dense): Linear(in_features=4096, out_features=4096, bias=True)
        )
        (mlp): GPTNeoXMLP(
          (dense_h_to_4h): Linear(in_features=4096, out_features=16384, bias=True)
          (dense_4h_to_h): Linear(in_features=16384, out_features=4096, bias=True)
          (act): GELUActivation()
        )
      )
    )
    (final_layer_norm): LayerNorm((4096,), eps=1e-05, elementwise_affine=True)
  )
  (embed_out): Linear(in_features=4096, out_features=50432, bias=False)
)
```

## Model Configuration

```json
GPTNeoXConfig {
  "_name_or_path": "h2oai/h2ogpt-oig-oasst1-256-6_9b",
  "architectures": [
    "GPTNeoXForCausalLM"
  ],
  "bos_token_id": 0,
  "custom_pipelines": {
    "text-generation": {
      "impl": "h2oai_pipeline.H2OTextGenerationPipeline",
      "pt": "AutoModelForCausalLM"
    }
  },
  "eos_token_id": 0,
  "hidden_act": "gelu",
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 16384,
  "layer_norm_eps": 1e-05,
  "max_position_embeddings": 2048,
  "model_type": "gpt_neox",
  "num_attention_heads": 32,
  "num_hidden_layers": 32,
  "rotary_emb_base": 10000,
  "rotary_pct": 0.25,
  "tie_word_embeddings": false,
  "torch_dtype": "float16",
  "transformers_version": "4.28.1",
  "use_cache": true,
  "use_parallel_residual": true,
  "vocab_size": 50432
}

```
