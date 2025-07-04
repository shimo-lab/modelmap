
# Overview
Fine-tuned [Llama-2 7B](https://huggingface.co/TheBloke/Llama-2-7B-fp16) with an uncensored/unfiltered Wizard-Vicuna conversation dataset (originally from [ehartford/wizard_vicuna_70k_unfiltered](https://huggingface.co/datasets/ehartford/wizard_vicuna_70k_unfiltered)).
Used QLoRA for fine-tuning. Trained for one epoch on a 24GB GPU (NVIDIA A10G) instance, took ~19 hours to train.

The version here is the fp16 HuggingFace model.

## GGML & GPTQ versions
Thanks to [TheBloke](https://huggingface.co/TheBloke), he has created the GGML and GPTQ versions:
* https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML
* https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GPTQ

## Running in Ollama
https://ollama.com/library/llama2-uncensored

# Prompt style
The model was trained with the following prompt style:
```
### HUMAN:
Hello

### RESPONSE:
Hi, how are you?

### HUMAN:
I'm fine.

### RESPONSE:
How can I help you?
...
```

# Training code
Code used to train the model is available [here](https://github.com/georgesung/llm_qlora).

To reproduce the results:
```
git clone https://github.com/georgesung/llm_qlora
cd llm_qlora
pip install -r requirements.txt
python train.py configs/llama2_7b_chat_uncensored.yaml
```

# Fine-tuning guide
https://georgesung.github.io/ai/qlora-ift/

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_georgesung__llama2_7b_chat_uncensored)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 43.39   |
| ARC (25-shot)         | 53.58          |
| HellaSwag (10-shot)   | 78.66    |
| MMLU (5-shot)         | 44.49         |
| TruthfulQA (0-shot)   | 41.34   |
| Winogrande (5-shot)   | 74.11   |
| GSM8K (5-shot)        | 5.84        |
| DROP (3-shot)         | 5.69         |