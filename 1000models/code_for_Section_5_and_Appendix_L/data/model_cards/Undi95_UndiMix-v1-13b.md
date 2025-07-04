Command used :
```shell
python ties_merge.py TheBloke/Llama-2-13B-fp16 .UndiMix-v1-13b  --merge The-Face-Of-Goonery/Huginn-13b-v1.2 --merge Doctor-Shotgun/llama-2-13b-chat-limarp-v2-merged
```

Testing around...

<!-- description start -->
## Description

This repo contains fp16 files of my personal mix : "UndiMix".

It can be hot, serious, playful, and can use emoji thanks to llama-2-13b-chat-limarp-v2-merged.

<!-- description end -->
<!-- description start -->
## Models used


- TheBloke/Llama-2-13B-fp16 (base)
- Undi95/MythoMax-L2-Kimiko-v2-13b
- The-Face-Of-Goonery/Huginn-13b-v1.2
- Doctor-Shotgun/llama-2-13b-chat-limarp-v2-merged
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
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Undi95__UndiMix-v1-13b)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 52.56   |
| ARC (25-shot)         | 59.47          |
| HellaSwag (10-shot)   | 82.45    |
| MMLU (5-shot)         | 55.83         |
| TruthfulQA (0-shot)   | 49.78   |
| Winogrande (5-shot)   | 75.45   |
| GSM8K (5-shot)        | 10.01        |
| DROP (3-shot)         | 34.95         |
