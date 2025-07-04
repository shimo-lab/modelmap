# Model Card for xDAN-SlimOrca
<!-- Provide a quick summary of what the model is/does. -->
Slerp merge of xDAN-L1-Chat-RL-v1 and mistral-7b-slimorcaboros.

.yaml file for mergekit
```.yaml:
slices:
  - sources:
      - model: xDAN-AI/xDAN-L1-Chat-RL-v1
        layer_range: [0, 32]
      - model: openaccess-ai-collective/mistral-7b-slimorcaboros
        layer_range: [0, 32]
merge_method: slerp
base_model: mistralai/Mistral-7B-v0.1
parameters:
  t:
    - filter: self_attn
      value: [0.14, 0.57, 0.4, 0.74, 1]
    - filter: mlp
      value: [0.86, 0.43, 0.6, 0.26, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: float16
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Azazelle__xDAN-SlimOrca)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |68.04|
|AI2 Reasoning Challenge (25-Shot)|65.61|
|HellaSwag (10-Shot)              |85.70|
|MMLU (5-Shot)                    |63.67|
|TruthfulQA (0-shot)              |57.68|
|Winogrande (5-shot)              |77.66|
|GSM8k (5-shot)                   |57.92|

