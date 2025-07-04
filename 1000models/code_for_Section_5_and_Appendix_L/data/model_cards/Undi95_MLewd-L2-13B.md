
MLewd is a model created to be... Lewd. That's all. Based on ReMM.

There was so much attempt on this model that I can't count them all. Bear with me lmao.

The OG plan: https://pastebin.com/hfJ80rKL

Command useds and explaination :
```shell
Due to hardware limitation, some merge was done in 2 part.

Last mix :
- ReMM (Base) (0.57)
- Doctor-Shotgun/llama-2-13b-chat-limarp-v2-merged (Llama Chat Uncensored) (0.35)
- KoboldAI/LLAMA2-13B-Holodeck-1 (0.08)

Part 1: python ties_merge.py TheBloke/Llama-2-13B-fp16 ./MLewdBase-L2-13B-part1  --merge Undi95/ReMM-L2-13B --density 0.88 --merge KoboldAI/LLAMA2-13B-Holodeck-1 --density 0.12 --cuda

Part 2: python ties_merge.py TheBloke/Llama-2-13B-fp16 ./MLewdBase-L2-13B  --merge Undi95/MLewdBase-L2-13B-part1 --density 0.65 --merge Doctor-Shotgun/llama-2-13b-chat-limarp-v2-merged --density 0.35 --cuda

(MLewd-L2-13B-v1-2 got disqualified)

- Applying LoRA: nRuaif/Kimiko-v2-13B at (0.24) weight on MLewd-L2-13B-v1-1
=> Result: MLewd-L2-13B-v1-3

================== ERP RANKING TEST ===========================

19.42 | MLewd-L2-13B-v1-3.q5_K_M.gguf (-> Best)
19.25 | MLewd-L2-13B-v1-1.q5_K_M.gguf
18.25 | MLewd-L2-13B-v1-2.q5 K M.gguf

================== RETRY ===========================

Mix:
- Undi95/MLewd-L2-13B-v1-3 (0.82)
- Sao10K/Stheno-Inverted-L2-13B (0.18)

!python ties_merge.py TheBloke/Llama-2-13B-fp16 ./MLewd-L2-13B-v1-7 --merge Undi95/MLewd-L2-13B-v1-3 --density 0.82 --merge Sao10K/Stheno-Inverted-L2-13B --density 0.18 --cuda
=> Result: MLewd-L2-13B-v1-7


Final touch (trying my best here) :
MLewd-L2-13B-v1-7 (0.77) + zarakiquemparte/PIPPA-ShareGPT-Subset-QLora-13b (LoRA 0.23)
=> MLewd-L2-13B-v1-7-TRY2

FINAL : MLewd-L2-13B-v1-7-TRY2 (0.82) + BluemoonRP (0.18)
=> MLewd-L2-13B-v1-8-3

RIP to all the version that got trashed.
```

<!-- description start -->
## Description

This repo contains fp16 files of MLewd-L2-13B, a trying-to-be lewd LLM model.
<!-- description end -->
<!-- description start -->
## Models used
- Undi95/ReMM (Base)
- Doctor-Shotgun/llama-2-13b-chat-limarp-v2-merged (Llama Chat Uncensored)
- KoboldAI/LLAMA2-13B-Holodeck-1
- Sao10K/Stheno-Inverted-L2-13B 
## Loras used
- nRuaif/BluemoonRP-L2-13B-This-time-will-be-better/tree/main/lora-out-13b-final-BM/checkpoint-15/adapter_model
- zarakiquemparte/PIPPA-ShareGPT-Subset-QLora-13b
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
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Undi95__MLewd-L2-13B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 46.84   |
| ARC (25-shot)         | 58.28          |
| HellaSwag (10-shot)   | 82.32    |
| MMLU (5-shot)         | 54.67         |
| TruthfulQA (0-shot)   | 48.66   |
| Winogrande (5-shot)   | 73.48   |
| GSM8K (5-shot)        | 1.29        |
| DROP (3-shot)         | 9.18         |
