With Llama 3 released, it's time for MythoMax to slowly fade away... [Let's do it in style!](https://suno.com/song/3d69cd72-e893-4193-866f-385f47778ce0)

An improved, potentially even perfected variant of MythoMix, my [MythoLogic-L2](https://huggingface.co/Gryphe/MythoLogic-L2-13b) and [Huginn](https://huggingface.co/The-Face-Of-Goonery/Huginn-13b-FP16) merge using a highly experimental tensor type merge technique. The main difference with MythoMix is that I allowed more of Huginn to intermingle with the single tensors located at the front and end of a model, resulting in increased coherency across the entire structure.

The script and the acccompanying templates I used to produce both can [be found here](https://github.com/Gryphe/BlockMerge_Gradient/tree/main/YAML).

This model is proficient at both roleplaying and storywriting due to its unique nature.

Quantized models are available from TheBloke: [GGUF](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGUF) - [GPTQ](https://huggingface.co/TheBloke/MythoMax-L2-13B-GPTQ) - [AWQ](https://huggingface.co/TheBloke/MythoMax-L2-13B-AWQ) (You're the best!)

## Model details

The idea behind this merge is that each layer is composed of several tensors, which are in turn responsible for specific functions. Using MythoLogic-L2's robust understanding as its input and Huginn's extensive writing capability as its output seems to have resulted in a model that exceeds at both, confirming my theory. (More details to be released at a later time)

This type of merge is incapable of being illustrated, as each of its 363 tensors had an unique ratio applied to it. As with my prior merges, gradients were part of these ratios to further finetune its behaviour.

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