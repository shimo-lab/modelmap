
# GML-Mistral-merged-v1

Quick attempt to reproduce [zyh3826/GML-Mistral-merged-v1](https://huggingface.co/zyh3826/GML-Mistral-merged-v1).

This model is a merge of the following models made with [mergekit](https://github.com/cg123/mergekit):
 * [quantumaikr/quantum-v0.01](https://huggingface.co/quantumaikr/quantum-v0.01)
 * [mncai/mistral-7b-dpo-v5](https://huggingface.co/mncai/mistral-7b-dpo-v5)

## 🧩 Configuration

```yaml
slices:
  - sources:
    - model: quantumaikr/quantum-v0.01
      layer_range: [0, 32]
  - sources:
    - model: mncai/mistral-7b-dpo-v5
      layer_range: [24, 32]
merge_method: passthrough
dtype: bfloat16
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_mlabonne__GML-Mistral-merged-v1)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |48.54|
|AI2 Reasoning Challenge (25-Shot)|43.77|
|HellaSwag (10-Shot)              |57.89|
|MMLU (5-Shot)                    |64.13|
|TruthfulQA (0-shot)              |51.58|
|Winogrande (5-shot)              |73.88|
|GSM8k (5-shot)                   | 0.00|

