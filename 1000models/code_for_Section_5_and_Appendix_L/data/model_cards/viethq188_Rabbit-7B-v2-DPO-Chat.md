Merge AIDC-ai-business/Marcoroni-7B-v3, Q-bert/MetaMath-Cybertron-Starling, mistralai/Mistral-7B-Instruct-v0.2 using slerp merge from https://github.com/cg123/mergekit.

After that we trained DPO with HF data.

*config.yaml*
```
slices:
  - sources:
      - model: AIDC-ai-business/Marcoroni-7B-v3
        layer_range: [0, 32]
      - model: Q-bert/MetaMath-Cybertron-Starling
        layer_range: [0, 32]
merge_method: slerp
base_model: AIDC-ai-business/Marcoroni-7B-v3
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 
dtype: float16
```

You can use alpaca template.
```
template_format = """{system}
### Instruction:
{prompt}

### Response:
"""
```