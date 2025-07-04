# Model Card for smol_bruin-7b

<!-- Provide a quick summary of what the model is/does. -->

Slerp merge of go-bruins-v2 and smol-7b.

.yaml file for mergekit

```.yaml:
slices:
  - sources:
      - model: rwitz/go-bruins-v2
        layer_range: [0, 32]
      - model: rishiraj/smol-7b
        layer_range: [0, 32]
merge_method: slerp
base_model: mistralai/Mistral-7B-v0.1
parameters:
  t:
    - filter: self_attn
      value: [0.44, 0.72, 0.61, 0.83, 1]
    - filter: mlp
      value: [0.56, 0.28, 0.39, 0.17, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: float16
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Azazelle__smol_bruin-7b)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |71.05|
|AI2 Reasoning Challenge (25-Shot)|67.58|
|HellaSwag (10-Shot)              |86.48|
|MMLU (5-Shot)                    |65.05|
|TruthfulQA (0-shot)              |55.65|
|Winogrande (5-shot)              |81.14|
|GSM8k (5-shot)                   |70.43|

