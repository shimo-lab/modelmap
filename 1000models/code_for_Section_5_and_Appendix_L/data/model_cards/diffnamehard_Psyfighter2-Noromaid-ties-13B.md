Merge of [KoboldAI/LLaMA2-13B-Psyfighter2](https://huggingface.co/KoboldAI/LLaMA2-13B-Psyfighter2) and [NeverSleep/Noromaid-13b-v0.1.1](https://huggingface.co/NeverSleep/Noromaid-13b-v0.1.1)

.yaml file for mergekit

```
models:
  - model: LLaMA2-13B-Psyfighter2
  - model: Noromaid-13b-v0.1.1
    parameters:
      density: 0.65
      weight: [0, 0.3, 0.7, 1]
merge_method: ties
base_model: LLaMA2-13B-Psyfighter2
parameters:
  normalize: true
  int8_mask: true
dtype: float16
```

| Metric | Value |
| --- | --- |
| Avg. | 59.47 |
| ARC (25-shot) | 61.86 |
| HellaSwag (10-shot) | 84.58 |
| MMLU (5-shot) | 57.04 |
| TruthfulQA (0-shot) | 50.66 |
| Winogrande (5-shot) | 75.37 |
| GSM8K (5-shot) | 27.29 |