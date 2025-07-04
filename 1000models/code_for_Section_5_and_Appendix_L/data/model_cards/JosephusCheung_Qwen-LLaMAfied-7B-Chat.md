
NEW VERSIONS: [https://huggingface.co/CausalLM/14B](https://huggingface.co/CausalLM/14B)


This is the LLaMAfied replica of [Qwen/Qwen-7B-Chat](https://huggingface.co/Qwen/Qwen-7B-Chat) (Original Version before 25.09.2023), recalibrated to fit the original LLaMA/LLaMA-2-like model structure.

You can use LlamaForCausalLM for model inference, which is the same as LLaMA/LLaMA-2 models (using GPT2Tokenizer converted from the original tiktoken, by [vonjack](https://huggingface.co/vonjack)).

The model has been edited to be white-labelled, meaning the model will no longer call itself a Qwen.

Up until now, the model has undergone numerical alignment of weights and preliminary reinforcement learning in order to align with the original model. Some errors and outdated knowledge have been addressed through model editing methods. This model remains completely equivalent to the original version, without having any dedicated supervised finetuning on downstream tasks or other extensive conversation datasets.

PROMPT FORMAT: [chatml](https://github.com/openai/openai-python/blob/main/chatml.md)

CURRENT MMLU: 53.48

CURRENT CEval (val): 54.13

```
MMLU - stem ACC: 46.40 Humanities ACC: 47.61 other ACC: 61.31 social ACC: 61.78 AVERAGE ACC:53.48

CEval (val) - STEM acc: 45.28 Social Science acc: 66.19 Humanities acc: 58.76 Other acc: 54.62 Hard acc:28.64 AVERAGE acc:54.13
```

Issue: Compared to the original Qwen-7B-Chat scoring 53.90 in MMLU and 54.18 in CEval (val), the our scores dropped slightly [-0.42 in MMLU, -0.05 in CEval (val)] due to insufficient realignment.


这是 [通义千问 Qwen/Qwen-7B-Chat](https://huggingface.co/Qwen/Qwen-7B-Chat) (在 25.09.2023 之前的原始版本) 的 LLaMA 化版本，经过重新校准以适应原始的类似 LLaMA/LLaMA-2 的模型结构。

您可以使用 LlamaCausalLM 进行模型推理，和 LLaMA/LLaMA-2 保持一致（使用由 [vonjack](https://huggingface.co/vonjack) 从原始 tiktoken 转换而来的 GPT2Tokenizer 分词器）。

模型已经被编辑实现白标化，不再自称通义千问。

到目前为止，该模型已经进行了权重的数值对齐和初步的强化学习，以与原始模型保持一致。 一些错误和过时的知识已通过模型编辑方法得到解决。 该模型与原始版本完全等效，尚未对下游任务或其他广泛的对话数据集进行任何专门的监督微调。

PROMPT 格式: [chatml](https://github.com/openai/openai-python/blob/main/chatml.md)

当前的 MMLU: 53.48

当前的 CEval (val): 54.13

```
MMLU - stem ACC: 46.40 Humanities ACC: 47.61 other ACC: 61.31 social ACC: 61.78 AVERAGE ACC:53.48

CEval (val) - STEM acc: 45.28 Social Science acc: 66.19 Humanities acc: 58.76 Other acc: 54.62 Hard acc:28.64 AVERAGE acc:54.13
```

问题：相比原本的 Qwen-7B-Chat 的 MMLU 分数 53.90 和 CEval (val) 分数 54.18，由于不够充分的重新对齐，分数都略有下降 [-0.42 in MMLU, -0.05 in CEval (val)]。