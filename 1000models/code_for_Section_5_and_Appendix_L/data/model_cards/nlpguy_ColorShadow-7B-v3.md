# ColorShadow-7B-v3

This is a Gradient-SLERP merge between ColorShadow-7B and Terminis-7B performed using mergekit.

Here is the config file used:

```
slices:
  - sources:
      - model: nlpguy/ColorShadow-7B
        layer_range: [0, 32]
      - model: Q-bert/Terminis-7B
        layer_range: [0, 32]
merge_method: slerp
base_model: nlpguy/ColorShadow-7B
parameters:
  t:
    - filter: self_attn
      value: [1, 0.5, 0.7, 0.3, 0]
    - filter: mlp
      value: [0, 0.5, 0.3, 0.7, 1]
    - value: 0.5 # fallback for rest of tensors
dtype: float16
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_nlpguy__ColorShadow-7B-v3)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |67.29|
|AI2 Reasoning Challenge (25-Shot)|67.58|
|HellaSwag (10-Shot)              |85.04|
|MMLU (5-Shot)                    |60.57|
|TruthfulQA (0-shot)              |62.88|
|Winogrande (5-shot)              |80.11|
|GSM8k (5-shot)                   |47.54|

