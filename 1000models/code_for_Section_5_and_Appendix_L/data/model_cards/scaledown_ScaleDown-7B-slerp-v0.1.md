
# ScaleDown-7B-slerp-v0.1

This model is a merge of the following models made with [mergekit](https://github.com/cg123/mergekit):
 * [OpenPipe/mistral-ft-optimized-1218](https://huggingface.co/OpenPipe/mistral-ft-optimized-1218)
 * [jondurbin/bagel-dpo-7b-v0.1](https://huggingface.co/jondurbin/bagel-dpo-7b-v0.1)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: OpenPipe/mistral-ft-optimized-1218
        layer_range: [0, 32]
      - model: jondurbin/bagel-dpo-7b-v0.1
        layer_range: [0, 32]
merge_method: slerp
base_model: OpenPipe/mistral-ft-optimized-1218
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
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_scaledown__ScaleDown-7B-slerp-v0.1)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |71.57|
|AI2 Reasoning Challenge (25-Shot)|68.00|
|HellaSwag (10-Shot)              |85.70|
|MMLU (5-Shot)                    |65.26|
|TruthfulQA (0-shot)              |61.90|
|Winogrande (5-shot)              |81.37|
|GSM8k (5-shot)                   |67.17|

