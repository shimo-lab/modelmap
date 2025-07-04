
# Helios-10.7B

This model is a merge of the following models made with [mergekit](https://github.com/cg123/mergekit):
 * [jeonsworld/CarbonVillain-en-10.7B-v4](https://huggingface.co/jeonsworld/CarbonVillain-en-10.7B-v4)
 * [kekmodel/StopCarbon-10.7B-v5](https://huggingface.co/kekmodel/StopCarbon-10.7B-v5)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: jeonsworld/CarbonVillain-en-10.7B-v4
        layer_range: [0, 32]
      - model: kekmodel/StopCarbon-10.7B-v5
        layer_range: [0, 32]
merge_method: slerp
base_model: jeonsworld/CarbonVillain-en-10.7B-v4
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_occultml__Helios-10.7B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |42.19|
|AI2 Reasoning Challenge (25-Shot)|38.91|
|HellaSwag (10-Shot)              |46.60|
|MMLU (5-Shot)                    |41.40|
|TruthfulQA (0-shot)              |55.52|
|Winogrande (5-shot)              |70.72|
|GSM8k (5-shot)                   | 0.00|

