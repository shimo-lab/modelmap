# Model Card for Dumb-Maidlet
<!-- Provide a quick summary of what the model is/does. -->
Slerp merge of Noromaid-7b-v0.2, NSFW_DPO_Noromaid-7b, go-bruins-v2, and smol-7b.

.yaml file for mergekit
```.yaml:
slices:
  - sources:
      - model: Azazelle/Half-NSFW_Noromaid-7b
        layer_range: [0, 32]
      - model: Azazelle/smol_bruin-7b
        layer_range: [0, 32]
merge_method: slerp
base_model: mistralai/Mistral-7B-v0.1
parameters:
  t:
    - filter: self_attn
      value: [0.22, 0.61, 0.46, 0.77, 1]
    - filter: mlp
      value: [0.78, 0.39, 0.54, 0.23, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: float16
```