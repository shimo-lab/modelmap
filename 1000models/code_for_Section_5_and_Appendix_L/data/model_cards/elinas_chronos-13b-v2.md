
# chronos-13b-v2

This is the FP16 PyTorch / HF version of **chronos-13b-v2** based on the **LLaMA v2 Base** model.

Only use this version for further quantization or if you would like to run in full precision, as long as you have the VRAM required.

This model is primarily focused on chat, roleplay, storywriting, with good reasoning and logic.

Chronos can generate very long outputs with coherent text, largely due to the human inputs it was trained on, and it supports context length up to 4096 tokens.

This model uses Alpaca formatting, so for optimal model performance, use it to start the dialogue or story, and if you use a frontend like SillyTavern ENABLE instruction mode:
```
### Instruction:
Your instruction or question here.
### Response:
```
Not using the format will make the model perform significantly worse than intended.

## Other Versions
[4bit GPTQ Quantized version](https://huggingface.co/elinas/chronos-13b-v2-GPTQ)

[GGML Versions provided by @TheBloke](https://huggingface.co/TheBloke/Chronos-13B-v2-GGML)

**Support My Development of New Models**
<a href='https://ko-fi.com/Q5Q6MB734' target='_blank'><img height='36' style='border:0px;height:36px;' 
src='https://storage.ko-fi.com/cdn/kofi1.png?v=3' border='0' alt='Support Development' /></a>
