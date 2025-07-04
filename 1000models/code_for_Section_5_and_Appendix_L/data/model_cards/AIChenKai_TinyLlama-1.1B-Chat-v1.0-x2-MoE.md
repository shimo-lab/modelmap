Testing model.

Config:
```
base_model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
gate_mode: hidden
dtype: bfloat16
experts:
  - source_model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
    positive_prompts: [""]
  - source_model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
    positive_prompts: [""]
```