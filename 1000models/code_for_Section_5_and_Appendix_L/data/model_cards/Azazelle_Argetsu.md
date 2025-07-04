# Model Card for Argetsu
<!-- Provide a quick summary of what the model is/does. -->
Slerp merge of lots of models.

.yaml file for mergekit
```.yaml:
slices:
  - sources:
      - model: Azazelle/SlimMelodicMaid
        layer_range: [0, 32]
      - model: Azazelle/Dumb-Maidlet
        layer_range: [0, 32]
merge_method: slerp
base_model: mistralai/Mistral-7B-v0.1
parameters:
  t:
    - filter: self_attn
      value: [0.2, 0.6, 0.44, 0.76, 1]
    - filter: mlp
      value: [0.8, 0.4, 0.56, 0.24, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: float16
```