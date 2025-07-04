Re:MythoMax (ReMM) is a recreation trial of the original [MythoMax-L2-B13](https://huggingface.co/Gryphe/MythoMax-L2-13b) with updated models.

This merge use SLERP [TESTING] to merge ReML and Huginn v1.2.

Command useds and explaination :
```shell
Due to hardware limitation, some merge was done in 2 part.

- Recreate ReML : Mythologic (v2) (Chronos/Hermes/Airboros)
=> Replacing Chronos by The-Face-Of-Goonery/Chronos-Beluga-v2-13bfp16 (0.30)
=> Replacing Airoboros by jondurbin/airoboros-l2-13b-2.1 (last version) (0.40)
=> Keeping NousResearch/Nous-Hermes-Llama2-13b (0.30)

Part 1: python ties_merge.py TheBloke/Llama-2-13B-fp16 ./ReML-L2-13B-part1  --merge The-Face-Of-Goonery/Chronos-Beluga-v2-13bfp16 --density 0.42 --merge jondurbin/airoboros-l2-13b-2.1 --density 0.56 --cuda

Part 2: python ties_merge.py TheBloke/Llama-2-13B-fp16 ./ReML-L2-13B --merge NousResearch/Nous-Hermes-Llama2-13b --density 0.30 --merge Undi95/ReML-L2-13B-part1 --density 0.70 --cuda

With that :
- Recreate ReMM : MythoMax (v2) (Mythologic/Huginn v1)
=> Replacing Mythologic by the one above (0.5)
=> Replacing Huginn by The-Face-Of-Goonery/Huginn-13b-v1.2 (hottest) (0.5)

Part 3: python slerpmergelm.py "The-Face-Of-Goonery_Huginn-13b-v1.2" "Undi95_ReML-L2-13B" "result"
```

Version of SLERP used is different to accept usage on notebook : https://github.com/Undi95/LLM-SLERP-MergeTest/tree/main (Thanks @Vali)

<!-- description start -->
## Description

This repo contains fp16 files of ReMM-SLERP, a recreation of the original MythoMax, but updated and merged with SLERP.
<!-- description end -->
<!-- description start -->
## Models used


- TheBloke/Llama-2-13B-fp16 (base)
- The-Face-Of-Goonery/Chronos-Beluga-v2-13bfp16
- jondurbin/airoboros-l2-13b-2.1
- NousResearch/Nous-Hermes-Llama2-13b
- The-Face-Of-Goonery/Huginn-13b-v1.2
- ReML-L2-13B (Private recreation trial of an updated Mythologic-L2-13B)
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
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Undi95__ReMM-SLERP-L2-13B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 50.99   |
| ARC (25-shot)         | 60.92          |
| HellaSwag (10-shot)   | 83.56    |
| MMLU (5-shot)         | 55.33         |
| TruthfulQA (0-shot)   | 51.97   |
| Winogrande (5-shot)   | 75.22   |
| GSM8K (5-shot)        | 9.17        |
| DROP (3-shot)         | 20.76         |
