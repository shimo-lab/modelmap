
### 12th December 2023

We are ranked *6th* on the overall leaderboard and **1st** in the 7B leaderboard! 🔥🔥🔥

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63c06fba8d1175e3399c16e6/LbOzm-1EEBaSv4O1pssyh.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63c06fba8d1175e3399c16e6/Cv5x7rRuM46AlliFdoC_B.png)

Merge AIDC-ai-business/Marcoroni-7B-v3 and rwitz/go-bruins-v2 using slerp merge from https://github.com/cg123/mergekit.

*config.yaml*
```
slices:
  - sources:
      - model: AIDC-ai-business/Marcoroni-7B-v3
        layer_range: [0, 32]
      - model: rwitz/go-bruins-v2
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

Developed by: Trong-Hieu Nguyen-Mau