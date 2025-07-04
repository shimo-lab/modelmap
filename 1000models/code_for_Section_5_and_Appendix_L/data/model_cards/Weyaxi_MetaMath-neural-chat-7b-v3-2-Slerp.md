# MetaMath-neural-chat-7b-v3-2-Slerp

This is the model for MetaMath-neural-chat-7b-v3-2-Slerp. I used [mergekit](https://github.com/cg123/mergekit) to merge models.

# Yaml Config to reproduce

```yaml

slices:
  - sources:
      - model: meta-math/MetaMath-Mistral-7B
        layer_range: [0, 32]
      - model: Intel/neural-chat-7b-v3-2
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
dtype: float16

```