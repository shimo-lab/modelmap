
Brouz was here first. (he said)

Re:MythoMax v2 (ReMM v2) is a recreation trial of the original [MythoMax-L2-B13](https://huggingface.co/Gryphe/MythoMax-L2-13b) with updated models.

This merge use SLERP merging method to merge ReML v2 and Huginn v1.2.

Explaination :
```shell
- ReML-v2: (Chronos-Beluga v2/Hermes/Airboros 2.1)
=> Keeping The-Face-Of-Goonery/Chronos-Beluga-v2-13bfp16
=> Replacing jondurbin/airoboros-l2-13b-2.1 by jondurbin/spicyboros-13b-2.2 (last version)
=> Keeping NousResearch/Nous-Hermes-Llama2-13b

With that :
- ReMM-v2: (ReML/Huginn v1.2)
=> Replacing ReMM by the one above (ReML v2)
=> Keeping The-Face-Of-Goonery/Huginn-13b-v1.2 (hottest)
```

<!-- description start -->
## Description

This repo contains fp16 files of ReMM v2, a recreation of the original MythoMax, but updated and merged with SLERP.
<!-- description end -->
<!-- description start -->
## Models used


- The-Face-Of-Goonery/Chronos-Beluga-v2-13bfp16
- jondurbin/spicyboros-13b-2.2 
- NousResearch/Nous-Hermes-Llama2-13b
- The-Face-Of-Goonery/Huginn-13b-v1.2
- ReML-v2-L2-13B (Private recreation trial of an updated Mythologic-L2-13B)
<!-- description end -->
<!-- prompt-template start -->
## Prompt template: Alpaca

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:

```

Special thanks to Sushi kek
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Undi95__ReMM-v2-L2-13B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 50.57   |
| ARC (25-shot)         | 61.95          |
| HellaSwag (10-shot)   | 84.0    |
| MMLU (5-shot)         | 56.14         |
| TruthfulQA (0-shot)   | 50.81   |
| Winogrande (5-shot)   | 75.85   |
| GSM8K (5-shot)        | 13.19        |
| DROP (3-shot)         | 12.08         |
