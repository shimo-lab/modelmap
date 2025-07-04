Slerp Merge of rwitz2/go-bruins-v2.1.1 and Weyaxi/OpenHermes-2.5-neural-chat-v3-3-Slerp

.yaml file for mergekit

```.yaml:
slices:
  - sources:
      - model: rwitz2/go-bruins-v2.1.1
        layer_range: [0, 32]
      - model: Weyaxi/OpenHermes-2.5-neural-chat-v3-3-Slerp
        layer_range: [0, 32]
merge_method: slerp
base_model: rwitz2/go-bruins-v2.1.1
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: bfloat16
```