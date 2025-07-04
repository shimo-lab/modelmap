
![image/png](https://cdn-uploads.huggingface.co/production/uploads/63ab1241ad514ca8d1430003/G05yXK7WRJjM6NkQyZvvr.png)

THIS MODEL IS MADE FOR LEWD

SEXUAL, CRUDE AND KINKY CONTENT IN OUTPUT CAN AND WILL HAPPEN. YOU'RE WARNED

This is an attempt to make an uncensored Llama2-chat that can RP.

Added the "magic touch" of MythoMax/Huginn/You call it.

In addition, [LimaRP v3](https://huggingface.co/lemonilia/LimaRP-Llama2-13B-v3-EXPERIMENT) was used, is it recommanded to read the documentation.

This was requested.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63ab1241ad514ca8d1430003/DNm7aymc9oU_92HXBEIq0.png)


<!-- description start -->
## Description

This repo contains fp16 files of MLewd-Chat-v2-13B, very hot and lewd model based on Llama2-chat.

<!-- description end -->
<!-- description start -->
## Models and loras used

- Undi95/MLewd-L2-13B-Part3 (checkpoint of MLewd without LORA)
- posicube/Llama2-chat-AYT-13B
- zattio770/120-Days-of-LORA-v2-13B
- royallab/Pygmalion-2-13b-SuperCOT
- Undi95/MMSoul-13b-lora
- The-Face-Of-Goonery/Huginn-13b-FP16
- lemonilia/LimaRP-Llama2-13B-v3-EXPERIMENT

<!-- description end -->
<!-- prompt-template start -->
## Prompt template: Alpaca

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:

```

## LimaRP v3 usage and suggested settings

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63ab1241ad514ca8d1430003/ZC_iP2KkcEcRdgG_iyxYE.png)

You can follow these instruction format settings in SillyTavern. Replace tiny with your desired response length:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63ab1241ad514ca8d1430003/PIn8_HSPTJEMdSEpNVSdm.png)

Special thanks to Sushi and Shena ♥ | I love U Kubernetes.

If you want to support me, you can [here](https://ko-fi.com/undiai).
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Undi95__MLewd-Chat-v2-13B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 52.72   |
| ARC (25-shot)         | 61.86          |
| HellaSwag (10-shot)   | 83.81    |
| MMLU (5-shot)         | 57.0         |
| TruthfulQA (0-shot)   | 54.51   |
| Winogrande (5-shot)   | 75.77   |
| GSM8K (5-shot)        | 10.46        |
| DROP (3-shot)         | 25.63         |
