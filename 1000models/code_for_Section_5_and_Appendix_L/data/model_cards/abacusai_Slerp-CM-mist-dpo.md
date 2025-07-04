
![image/png](https://cdn-uploads.huggingface.co/production/uploads/64c14f6b02e1f8f67c73bd05/V6OaYzWhNsFGwrl1M_ZjE.png)

This model is a [Slerp Merge](https://github.com/cg123/mergekit/blob/main/mergekit/merge_methods/slerp.py) of [cookinai/CatMacaroni-Slerp](https://huggingface.co/cookinai/CatMacaroni-Slerp) and [mncai/mistral-7b-dpo-v5](https://huggingface.co/mncai/mistral-7b-dpo-v5).

# Evaluation Results

### HuggingFace Leaderboard

| Average | ARC | HellaSwag | MMLU | TruthfulQA | Winogrande | GSM8K |
| --- | --- | --- | --- | --- | --- | --- |
| 73.1    | 69.62 | 87.09 | 64.81 | 62.82 | 81.45 | 72.78 |

The model did achieve an improvement in TruthfulQA over `cookinai/CatMacaroni-Slerp` and GSM8K over `mncai/mistral-7b-dpo-v5`
which was the goal of the merge leading to an average score that was a better than both. It is unclear why the TruthfulQA metric
is still meaningfully lower than the base `mncai/mistral-7b-dpo-v5`.

# Training Details

.yaml file for mergekit

```yaml
slices:
  - sources:
      - model: cookinai/CatMacaroni-Slerp
        layer_range: [0, 32]
      - model: mncai/mistral-7b-dpo-v5
        layer_range: [0, 32]
merge_method: slerp
base_model: mncai/mistral-7b-dpo-v5
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: float16
```
# Bias, Risks, and Limitations

The model has not been evaluated for safety and is only intended for research and experiments.