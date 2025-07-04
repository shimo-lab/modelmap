
**Python-Code-13B**

Large Language Models (LLMs) are good with code generations. Sometimes LLMs do make mistakes in code generation. How about if they can give detailed explanation along with the code.
This is what I have tried over here. The base Llama-2 model was used for training purpose. It is trained on around 23000+ set of codes. Each set having 2 conversations.
This data was generated using GPT-3.5, GPT-4 etc. This conversation is in Vicuna/ShareGPT format. Each set, along with code, has detailed explanation. 
I have released the [data](https://huggingface.co/datasets/ajibawa-2023/Python-Code-23k-ShareGPT).

**Training:**
Entire dataset was trained on Azure 4 x A100 80GB. For 3 epoch, training took 13 hours. DeepSpeed codebase was used for training purpose. This was trained on Llama-2 by Meta.

This is a full fine tuned model. Links for quantized models are given below.


**GPTQ GGML & AWQ**

GPTQ: [Link](https://huggingface.co/TheBloke/Python-Code-13B-GPTQ)

GGUF: [Link](https://huggingface.co/TheBloke/Python-Code-13B-GGUF)

AWQ: [Link](https://huggingface.co/TheBloke/Python-Code-13B-AWQ)


**Example Prompt:**
```
This is a conversation with your helpful AI assistant. AI assistant can generate Python Code along with necessary explanation.

Context
You are a helpful AI assistant.

USER: <prompt>
ASSISTANT:
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ajibawa-2023__Python-Code-13B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 47.16   |
| ARC (25-shot)         | 58.79          |
| HellaSwag (10-shot)   | 81.66    |
| MMLU (5-shot)         | 54.78         |
| TruthfulQA (0-shot)   | 42.83   |
| Winogrande (5-shot)   | 74.03   |
| GSM8K (5-shot)        | 9.55        |
| DROP (3-shot)         | 8.5         |
