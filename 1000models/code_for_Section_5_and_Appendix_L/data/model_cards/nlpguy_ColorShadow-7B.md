# ColorShadow-7B

This is a Gradient-SLERP merge between diffnamehard/Mistral-CatMacaroni-slerp-7B and cookinai/Valkyrie-V1 performed using mergekit.

Here is the config file used:

```
  slices:
    - sources:
        - model: diffnamehard/Mistral-CatMacaroni-slerp-7B
          layer_range: [0, 32]
        - model: cookinai/Valkyrie-V1
          layer_range: [0, 32]
  merge_method: slerp
  base_model: diffnamehard/Mistral-CatMacaroni-slerp-7B
  parameters:
    t:
      - filter: self_attn
        value: [0, 0.5, 0.3, 0.7, 1]
      - filter: mlp
        value: [1, 0.5, 0.7, 0.3, 0]
      - value: 0.5 # fallback for rest of tensors
  dtype: float16
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_nlpguy__ColorShadow-7B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |68.34|
|AI2 Reasoning Challenge (25-Shot)|67.83|
|HellaSwag (10-Shot)              |85.15|
|MMLU (5-Shot)                    |61.69|
|TruthfulQA (0-shot)              |59.56|
|Winogrande (5-shot)              |80.58|
|GSM8k (5-shot)                   |55.19|

