The Llama 2 sequel to my [original experiment](https://huggingface.co/Gryphe/MythoLogic-13b) with gradient merges using [the following script](https://github.com/Gryphe/BlockMerge_Gradient). Its three models ([Hermes](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b), [Chronos](https://huggingface.co/elinas/chronos-13b-v2) and [Airoboros](https://huggingface.co/jondurbin/airoboros-l2-13b-gpt4-2.0)) are almost evenly divided over the layer structure this time. Airoboros was the "wildcard model" due to its superior ability to understand complex instructions.

Quantized models are available from TheBloke: [GGML](https://huggingface.co/TheBloke/MythoLogic-L2-13B-GGML) - [GPTQ](https://huggingface.co/TheBloke/MythoLogic-L2-13B-GPTQ) (You're the best!)

## Model details

As before, the main objective was to create an all-round model with improved roleplaying capabilities. MythoLogic-L2 differs from its predecessor in that it focuses primarily on the understanding of instructions and personalities of complex character cards.

Illustrated below are the gradients used for this specific L2 recipe, with the top of the image representing layer 0 and the bottom layer 40.

![](MythoLogic-L2.png)

## Prompt Format

This model primarily uses (and was heavily tested with) Alpaca formatting, so for optimal model performance, use:
```
<System prompt/Character Card>

### Instruction:
Your instruction or question here.
For roleplay purposes, I suggest the following - Write <CHAR NAME>'s next reply in a chat between <YOUR NAME> and <CHAR NAME>. Write a single reply only.

### Response:
```

---
license: other
---