<!-- header start -->
<!-- 200823 -->

<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/janhq/jan/assets/89722390/35daac7d-b895-487c-a6ac-6663daaad78e" alt="Jan banner" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>

<p align="center">
    <a href="https://jan.ai/">Jan</a
> 
    - <a href="https://discord.gg/AsJ8krTT3N">Discord</a>
</p>
<!-- header end -->

# Model Description
This model uses the `Slerp` merge method from the best models on 14th Dec on the [
OpenLLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard):
1. [viethq188/LeoScorpius-7B-Chat-DPO](https://huggingface.co/viethq188/LeoScorpius-7B-Chat-DPO)
2. [GreenNode/GreenNodeLM-7B-v1olet](https://huggingface.co/GreenNode/GreenNodeLM-7B-v1olet)

- base model: [GreenNode/GreenNodeLM-7B-v1olet](https://huggingface.co/GreenNode/GreenNodeLM-7B-v1olet)

The yaml config file for this model is here:

```yaml
slices:
  - sources:
      - model: viethq188/LeoScorpius-7B-Chat-DPO
        layer_range: [0, 32] 
      - model: GreenNode/GreenNodeLM-7B-v1olet
        layer_range: [0, 32]
merge_method: slerp
base_model: GreenNode/GreenNodeLM-7B-v1olet
parameters:
  t:
    - filter: lm_head 
      value: [0.55]
    - filter: embed_tokens
      value: [0.7]
    - filter: self_attn
      value: [0.65, 0.35]
    - filter: mlp
      value:  [0.35, 0.65]
    - filter: layernorm
      value: [0.4, 0.6]
    - filter: modelnorm
      value: [0.6]
    - value: 0.5 # fallback for rest of tensors
dtype: bfloat16
```

Thank you [Undi95](https://huggingface.co/Undi95) for the secret sauce and [Charles Goddard](https://huggingface.co/chargoddard) for mergekit.

# Prompt template

Work best on:

```
{system_message}
### Instruction:
{prompt}

### Response:

```

# Run this model
You can run this model using [Jan Desktop](https://jan.ai/) on Mac, Windows, or Linux.

Jan is an open source, ChatGPT alternative that is:

- 💻  **100% offline on your machine**: Your conversations remain confidential, and visible only to you.
- 🗂️ **An Open File Format**: Conversations and model settings stay on your computer and can be exported or deleted at any time.
- 🌐 **OpenAI Compatible**: Local server on port `1337` with OpenAI compatible endpoints
- 🌍 **Open Source & Free**: We build in public; check out our [Github](https://github.com/janhq)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/65713d70f56f9538679e5a56/r7VmEBLGXpPLTu2MImM7S.png)

# About Jan
Jan believes in the need for an open-source AI ecosystem and is building the infra and tooling to allow open-source AIs to compete on a level playing field with proprietary ones.

Jan's long-term vision is to build a cognitive framework for future robots, who are practical, useful assistants for humans and businesses in everyday life.

# Jan Model Merger
This is a test project for merging models.

# Open LLM Leaderboard Evaluation Results

Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_jan-hq__trinity-v1).

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 74.8|
| ARC (25-shot)         | 72.27         |
| HellaSwag (10-shot)   | 88.36   |
| MMLU (5-shot)         | 65.2|
| TruthfulQA (0-shot)   | 69.31 |
| Winogrande (5-shot)   | 82  |
| GSM8K (5-shot)        | 71.65        |

# Acknowlegement
- [mergekit](https://github.com/cg123/mergekit)
- [DARE](https://github.com/yule-BUAA/MergeLM/blob/main/README.md)
- [SLERP](https://github.com/Digitous/LLM-SLERP-Merge)
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)