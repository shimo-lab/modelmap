**UPDATE:** There's an improved version now! [Check it MythoMax!](https://huggingface.co/Gryphe/MythoMax-L2-13b)

A requested variant of [MythoLogic-L2](https://huggingface.co/Gryphe/MythoLogic-L2-13b) and [Huginn](https://huggingface.co/The-Face-Of-Goonery/Huginn-13b-FP16) using a highly experimental tensor type merge technique.

This model is proficient at both roleplaying and storywriting due to its unique nature. 

Quantized models are available from TheBloke: [GGML](https://huggingface.co/TheBloke/MythoMix-L2-13B-GGML) - [GPTQ](https://huggingface.co/TheBloke/MythoMix-L2-13B-GPTQ) (You're the best!)

## Model details

The idea behind this merge is that each layer is composed of several tensors, which are in turn responsible for specific functions. Using MythoLogic-L2's robust understanding as its input and Huginn's extensive writing capability as its output seems to have resulted in a model that exceeds at both, confirming my theory. (More details to be released at a later time)

This type of merge is incapable of being illustrated, as each of its 360 tensors has an unique ratio applied to it. As with my prior merges, gradients were part of these ratios to further finetune its behaviour.

## Prompt Format

This model primarily uses Alpaca formatting, so for optimal model performance, use:
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