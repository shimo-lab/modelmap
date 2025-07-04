
This is the LLaMAfied replica of [Qwen/Qwen-VL-Chat](https://huggingface.co/Qwen/Qwen-VL-Chat) (Original Version before 25.09.2023), recalibrated to fit the original LLaMA/LLaMA-2-like model structure.

You can use LlamaForCausalLM for model inference, which is the same as LLaMA/LLaMA-2 models (using GPT2Tokenizer converted from the original tiktoken, by [vonjack](https://huggingface.co/vonjack)).

The model has been edited to be white-labelled, meaning the model will no longer call itself a Qwen.

Up until now, the model has undergone numerical alignment of weights and preliminary reinforcement learning in order to align with the original model. Some errors and outdated knowledge have been addressed through model editing methods. This model remains completely equivalent to the original version, without having any dedicated supervised finetuning on downstream tasks or other extensive conversation datasets.

PROMPT FORMAT: [chatml](https://github.com/openai/openai-python/blob/main/chatml.md)