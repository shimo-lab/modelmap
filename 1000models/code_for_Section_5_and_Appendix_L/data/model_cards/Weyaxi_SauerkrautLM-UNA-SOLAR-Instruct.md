![image/png](https://cdn-uploads.huggingface.co/production/uploads/6468ce47e134d050a58aa89c/8uLgxLFWSN4fGPCS8Qinq.png)

# SauerkrautLM-UNA-SOLAR-Instruct

This is the model for SauerkrautLM-UNA-SOLAR-Instruct. I used [mergekit](https://github.com/cg123/mergekit) to merge models.

🥳 As of **December 24 2023**, this model holds the **first place position** on the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard).

<h2><details><summary>Screenshot</summary><img src=https://cdn-uploads.huggingface.co/production/uploads/6468ce47e134d050a58aa89c/cVhjAJhuPoNgHo7CDCmA-.png></img></details></h2>

# Prompt Template(s)

```
### User:
{user}

### Assistant:
{asistant}
```

# Yaml Config to reproduce

```yaml
slices:
  - sources:
      - model: VAGOsolutions/SauerkrautLM-SOLAR-Instruct
        layer_range: [0, 48]
      - model: fblgit/UNA-SOLAR-10.7B-Instruct-v1.0
        layer_range: [0, 48]

merge_method: slerp
base_model: upstage/SOLAR-10.7B-Instruct-v1.0

parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
tokenizer_source: union

dtype: bfloat16
```

# Quantizationed versions

Quantizationed versions of this model is available thanks to [TheBloke](https://hf.co/TheBloke).

##### GPTQ

- [TheBloke/SauerkrautLM-UNA-SOLAR-Instruct-GPTQ](https://huggingface.co/TheBloke/SauerkrautLM-UNA-SOLAR-Instruct-GPTQ)

##### GGUF

- [TheBloke/SauerkrautLM-UNA-SOLAR-Instruct-GGUF](https://huggingface.co/TheBloke/SauerkrautLM-UNA-SOLAR-Instruct-GGUF)

##### AWQ

- [TheBloke/SauerkrautLM-UNA-SOLAR-Instruct-AWQ](https://huggingface.co/TheBloke/SauerkrautLM-UNA-SOLAR-Instruct-AWQ)


# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Weyaxi__SauerkrautLM-UNA-SOLAR-Instruct)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |74.26|
|AI2 Reasoning Challenge (25-Shot)|70.90|
|HellaSwag (10-Shot)              |88.30|
|MMLU (5-Shot)                    |66.15|
|TruthfulQA (0-shot)              |71.80|
|Winogrande (5-shot)              |83.74|
|GSM8k (5-shot)                   |64.67|

If you would like to support me:

[☕ Buy Me a Coffee](https://www.buymeacoffee.com/weyaxi)