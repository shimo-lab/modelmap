
Re:MythoMax v2.1 (ReMM v2.1) is a recreation trial of the original [MythoMax-L2-B13](https://huggingface.co/Gryphe/MythoMax-L2-13b) with updated models.

This merge use SLERP merging method to merge ReML v2.1 and Huginn v1.2.

Explaination :
```shell
- ReML-v2.1: (Chronos-Beluga v2/Hermes/Airboros 2.2)
=> Keeping The-Face-Of-Goonery/Chronos-Beluga-v2-13bfp16
=> Replacing jondurbin/spicyboros-13b-2.2 by jondurbin/airoboros-l2-13b-2.2 (last version)
=> Keeping NousResearch/Nous-Hermes-Llama2-13b

With that :
- ReMM-v2.1: (ReML v2.1/Huginn v1.2)
=> Replacing ReML by the one above (ReML v2.1)
=> Keeping The-Face-Of-Goonery/Huginn-13b-v1.2
```

<!-- description start -->
## Description

This repo contains fp16 files of ReMM v2.1, a recreation of the original MythoMax, but updated and merged with SLERP.
<!-- description end -->
<!-- description start -->
## Models used


- The-Face-Of-Goonery/Chronos-Beluga-v2-13bfp16
- jondurbin/airoboros-l2-13b-2.2
- NousResearch/Nous-Hermes-Llama2-13b
- The-Face-Of-Goonery/Huginn-13b-v1.2
- ReML-v2.1-L2-13B (Private recreation trial of an updated Mythologic-L2-13B)
<!-- description end -->
<!-- prompt-template start -->
## Prompt template: Alpaca

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:

```

Special thanks to Sushi.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Undi95__ReMM-v2.1-L2-13B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 50.41   |
| ARC (25-shot)         | 61.43          |
| HellaSwag (10-shot)   | 83.92    |
| MMLU (5-shot)         | 55.95         |
| TruthfulQA (0-shot)   | 50.3   |
| Winogrande (5-shot)   | 75.93   |
| GSM8K (5-shot)        | 12.74        |
| DROP (3-shot)         | 12.62         |
