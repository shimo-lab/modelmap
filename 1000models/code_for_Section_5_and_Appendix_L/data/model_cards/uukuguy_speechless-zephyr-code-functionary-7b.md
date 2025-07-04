
<p><h1> speechless-zephyr-code-functionary-7b </h1></p>

[4,5,8-bit GGUF models for CPU+GPU inference](https://huggingface.co/uukuguy/speechless-zephyr-code-functionary-7b/tree/main/GGUF)

This model is the one of the moloras (Mixture-of-Multi-LoRAs) experiments.

Extract LoRA modules from below models (all based Mistral-7B-v0.1), each LoRA module has its own unique skills. By using multi-loras, they can be combined together statically or dynamically to form a versatile new model.

- HuggingFaceH4/zephyr-7b-beta (Uncensored Model)
- meetkai/functionary-small-v2.2 (Execute functions/plugins)
- uukuguy/speechless-code-mistral-7b-v1.0 (Enhance Coding)

The entire process is completed through the use of extract-lora, merge-lora, and lora-hub provided by multi-loras.

The router of mixture-of-multi-loras enables an automatic assembling of LoRA modules, using a gradientfree approach to obtain the coefficients of LoRA modules and requiring only a handful of inference steps for unseen tasks.

Code: https://github.com/uukuguy/multi_loras

## LM-Evaluation-Harness

[Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

| Metric | Value |
| --- | --- |
| ARC | 61.52 |
| HellaSwag | 83.88 |
| MMLU | 64.71 |
| TruthfulQA | 44.99 |
| Winogrande | 78.69 |
| GSM8K | 43.82 |
| Average | 62.93 |

