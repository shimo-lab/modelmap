# Model Card for xDAN-SlimOrca
<!-- Provide a quick summary of what the model is/does. -->
Slerp merge of Silicon-Maid-7B, piano-medley-7b, xDAN-L1-Chat-RL-v1, and mistral-7b-slimorcaboros.

.yaml file for mergekit
```.yaml:
slices:
  - sources:
      - model: Azazelle/Silicon-Medley
        layer_range: [0, 32]
      - model: Azazelle/xDAN-SlimOrca
        layer_range: [0, 32]
merge_method: slerp
base_model: mistralai/Mistral-7B-v0.1
parameters:
  t:
    - filter: self_attn
      value: [0.19, 0.59, 0.43, 0.76, 1]
    - filter: mlp
      value: [0.81, 0.41, 0.57, 0.24, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: float16
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Azazelle__SlimMelodicMaid)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |69.70|
|AI2 Reasoning Challenge (25-Shot)|67.15|
|HellaSwag (10-Shot)              |86.01|
|MMLU (5-Shot)                    |64.75|
|TruthfulQA (0-shot)              |60.88|
|Winogrande (5-shot)              |78.61|
|GSM8k (5-shot)                   |60.80|

