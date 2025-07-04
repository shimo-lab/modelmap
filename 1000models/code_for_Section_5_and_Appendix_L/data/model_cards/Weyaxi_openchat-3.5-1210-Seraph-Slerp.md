# openchat-3.5-1210-Seraph-Slerp

This is the model for openchat-3.5-1210-Seraph-Slerp. I used [mergekit](https://github.com/cg123/mergekit) to merge models.

# Yaml Config

```yaml

slices:
  - sources:
      - model: openchat/openchat-3.5-1210
        layer_range: [0, 32]
      - model: Weyaxi/Seraph-7B
        layer_range: [0, 32]

merge_method: slerp
base_model: mistralai/Mistral-7B-v0.1

parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
tokenizer_source: union

dtype: bfloat16

```