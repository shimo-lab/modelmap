[WIP]

Origin repository [JosephusCheung/Qwen-LLaMAfied-7B-Chat](https://huggingface.co/JosephusCheung/Qwen-LLaMAfied-7B-Chat).


This is the LLaMAfied version of [Qwen/Qwen-7B-Chat](https://huggingface.co/Qwen/Qwen-7B-Chat), recalibrated to fit the original LLaMA/LLaMA-2-like model structure.

You can use LlamaForCausalLM for model inference, which is the same as LLaMA/LLaMA-2 models.

I converted the tokenizer from tiktoken format to huggingface format, so you do not need to allow external codes when loading anymore.

The model has been edited to be white-labelled, meaning the model will no longer call itself a Qwen.

SPOILOR: Further finetuning is in progress, the current version is a work-in-progress, some knowledge may be biased and illusory due to structural changes. Will be updated very, very sooooooooooon.

PROMPT FORMAT: [chatml](https://github.com/openai/openai-python/blob/main/chatml.md)

CURRENT MMLU: 50.36

Issue: Compared to the original Qwen-Chat scoring 53.9, the MMLU score dropped slightly (-3.54) due to insufficient realignment.