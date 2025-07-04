
models:
  - model: meta-math/MetaMath-Mistral-7B
    parameters:
      weight: 0.5
  - model: mlabonne/NeuralHermes-2.5-Mistral-7B
    parameters:
      weight: 0.3
merge_method: linear
dtype: float16