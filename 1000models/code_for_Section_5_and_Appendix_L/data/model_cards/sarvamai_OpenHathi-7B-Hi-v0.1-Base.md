This repository is the first model in the OpenHathi series of models that will be released by Sarvam AI. This is a 7B parameter, based on Llama2, trained on Hindi, English, and Hinglish. More details about the model, its training procedure, and evaluations can be found [here](https://www.sarvam.ai/blog/announcing-openhathi-series).

Note: this is a base model and not meant to be used as is. We recommend first finetuning it on task(s) you are interested in.

```
# Usage
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

tokenizer = LlamaTokenizer.from_pretrained('sarvamai/OpenHathi-7B-Hi-v0.1-Base')
model = LlamaForCausalLM.from_pretrained('sarvamai/OpenHathi-7B-Hi-v0.1-Base', torch_dtype=torch.bfloat16)

prompt = "मैं एक अच्छा हाथी हूँ"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate
generate_ids = model.generate(inputs.input_ids, max_length=30)
tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```