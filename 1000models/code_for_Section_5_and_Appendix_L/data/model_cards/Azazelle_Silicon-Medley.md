# Model Card for Silicon-Medley

<!-- Provide a quick summary of what the model is/does. -->

Slerp merge of Silicon-Maid-7B and piano-medley-7b.

.yaml file for mergekit

```.yaml:
slices:
  - sources:
      - model: SanjiWatsuki/Silicon-Maid-7B
        layer_range: [0, 32]
      - model: chargoddard/piano-medley-7b
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