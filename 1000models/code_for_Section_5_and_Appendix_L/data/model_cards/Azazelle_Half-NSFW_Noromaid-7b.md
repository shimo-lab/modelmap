# Model Card for Half-NSFW_Noromaid-7b

<!-- Provide a quick summary of what the model is/does. -->

Slerp merge of Noromaid-7b-v0.2 and NSFW_DPO_Noromaid-7b.

.yaml file for mergekit

```.yaml:
slices:
  - sources:
      - model: NeverSleep/Noromaid-7b-v0.2
        layer_range: [0, 32]
      - model: athirdpath/NSFW_DPO_Noromaid-7b
        layer_range: [0, 32]
merge_method: slerp
base_model: mistralai/Mistral-7B-v0.1
parameters:
  t:
    - filter: self_attn
      value: [0.07, 0.53, 0.35, 0.72, 1]
    - filter: mlp
      value: [0.93, 0.47, 0.65, 0.28, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: float16
```