```yaml
slices:
  - sources:
      - model: Q-bert/MetaMath-Cybertron-Starling
        layer_range: [0, 32]
      - model: maywell/Synatra-7B-v0.3-RP
        layer_range: [0, 32]
merge_method: slerp
base_model: Q-bert/MetaMath-Cybertron-Starling
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: float16
```