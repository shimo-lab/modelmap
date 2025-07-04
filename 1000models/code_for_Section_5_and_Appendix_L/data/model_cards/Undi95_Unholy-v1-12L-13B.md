
![image/png](https://cdn-uploads.huggingface.co/production/uploads/63ab1241ad514ca8d1430003/ysQGHLh1dd6I40rVK_jk2.png)

[HIGHLY EXPERIMENTAL]

(Sister model: https://huggingface.co/Undi95/Unholy-v1-10L-13B)

Use at your own risk, I'm not responsible for any usage of this model, don't try to do anything this model tell you to do.

Uncensored.

If you are censored, it's maybe because of keyword like "assistant", "Factual answer", or other "sweet words" like I call them that trigger the censoring accross all the layer of the model (since they're all trained on some of them in a way).

12L : This is a test project, uukuguy/speechless-llama2-luban-orca-platypus-13b and jondurbin/spicyboros-13b-2.2 was used for a merge, then, I deleted the first 8 layers to add 8 layers of MLewd at the beginning, and do the same from layers 16 to 20, trying to break all censoring possible, before merging the output with MLewd at 0.33 weight.

<!-- description start -->
## Description

This repo contains fp16 files of Unholy v1, an uncensored model.

<!-- description end -->
<!-- description start -->
## Models used

- uukuguy/speechless-llama2-luban-orca-platypus-13b
- jondurbin/spicyboros-13b-2.2
- Undi95/MLewd-L2-13B-v2-3

<!-- description end -->
<!-- prompt-template start -->
## Prompt template: Alpaca

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:
```

Exemple:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63ab1241ad514ca8d1430003/jaZzEcPP0IET6_KX7J5Hm.png)
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Undi95__Unholy-v1-12L-13B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 50.65   |
| ARC (25-shot)         | 63.57          |
| HellaSwag (10-shot)   | 83.75    |
| MMLU (5-shot)         | 58.08         |
| TruthfulQA (0-shot)   | 51.09   |
| Winogrande (5-shot)   | 77.27   |
| GSM8K (5-shot)        | 11.07        |
| DROP (3-shot)         | 9.73         |
