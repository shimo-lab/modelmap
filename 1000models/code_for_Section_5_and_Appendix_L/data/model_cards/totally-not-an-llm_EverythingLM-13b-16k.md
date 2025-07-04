
# EverythingLM-13b-16k

Introducing EverythingLM, a llama-2 based, general-purpose 13b model with 16k context thanks to LlongMa.  The model is trained on the EverythingLM dataset, more info can be found on the dataset page.

The model is completely uncensored.

This model is an early test of the EverythingLM dataset and some new experimental principles, so don't consider it SOTA.

### GGML quants: 
https://huggingface.co/TheBloke/EverythingLM-13B-16K-GGML

Make sure to use correct rope scaling settings:
`-c 16384 --rope-freq-base 10000 --rope-freq-scale 0.25`
### GPTQ quants: 
https://huggingface.co/TheBloke/EverythingLM-13B-16K-GPTQ

### Notable features:
- Automatically triggered CoT reasoning.
- Verbose and detailed replies.
- Creative stories.
- Better prompt understanding.

### Prompt format:
It is a modified Vicuna format, the same used in many of ehartford's models.
```
You are a helpful AI assistant.

USER: <prompt>
ASSISTANT:
```

Training took about 1 hour using QLoRa on 1xA100, so this model can be recreated for about $3.  QLoRa model can be found here: https://huggingface.co/totally-not-an-llm/EverythingLM-13b-peft.

### Model quirks:
- Due to the nature of the dataset, it does better with more detail.  I've found it gives much better stories when I provide more requirements.
- It really likes to use numbered lists.  I don't necessarilly have a problem with this but it's something to note when training on the dataset.
- It likes to write fairy tales over anything else, which is strange.  This can easily be fixed by prompting.
- Occasionally it will fall into repetition, this seems to be a commmon issue with llama-2 models.
- Haven't tested pushing it all the way to 16k context.

### Future plans:
- Native finetune.
- Other model sizes.
- Improve dataset by:
  - Regenerating using gpt-4.
  - A bit more data with more diversity.
- Refactor dataset generation script.
- Test some model merges using this model.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_totally-not-an-llm__EverythingLM-13b-16k)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 45.7   |
| ARC (25-shot)         | 56.57          |
| HellaSwag (10-shot)   | 80.58    |
| MMLU (5-shot)         | 50.18         |
| TruthfulQA (0-shot)   | 47.46   |
| Winogrande (5-shot)   | 72.77   |
| GSM8K (5-shot)        | 6.44        |
| DROP (3-shot)         | 5.89         |
