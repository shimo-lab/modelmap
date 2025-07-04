# Model Card for Argetsu
<!-- Provide a quick summary of what the model is/does. -->
Experimental DARE (no idea if this is decent).

.yaml file for mergekit
```.yaml:
models:
  - model: Dans-DiscountModels/Dans-07YahooAnswers-7b
    # no parameters necessary for base model
  - model: Azazelle/Maylin-7b #200
    parameters:
      weight: 0.45
      density: 0.75
  - model: Azazelle/smol_bruin-7b #175
    parameters:
      weight: 0.39
      density: 0.70
  - model: SanjiWatsuki/Kunoichi-7B #100
    parameters:
      weight: 0.22
      density: 0.52
merge_method: dare_ties
base_model: Dans-DiscountModels/Dans-07YahooAnswers-7b
parameters:
  int8_mask: true
dtype: bfloat16
```