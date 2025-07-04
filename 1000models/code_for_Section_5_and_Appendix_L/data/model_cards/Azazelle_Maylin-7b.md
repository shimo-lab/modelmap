# Model Card for Maylin-7b
<!-- Provide a quick summary of what the model is/does. -->
DARE merge intended to help the Argetsu model be more coherent and less horny.

.yaml file for mergekit
```.yaml:
models:
  - model: mistralai/Mistral-7B-v0.1
    # no parameters necessary for base model
  - model: SanjiWatsuki/Sonya-7B #200
    parameters:
      weight: 0.45
      density: 0.75
  - model: Azazelle/Argetsu #175
    parameters:
      weight: 0.39
      density: 0.70
  - model: Azazelle/Tippy-Toppy-7b #100
    parameters:
      weight: 0.22
      density: 0.52
merge_method: dare_ties
base_model: mistralai/Mistral-7B-v0.1
parameters:
  int8_mask: true
dtype: bfloat16
```