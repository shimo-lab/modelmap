# QuantumLM

## Model Description

`QuantumLM` is a Llama2 7B model finetuned on an Wizard-Orca style Dataset

## Usage

Start chatting with `QuantumLM-7B` using the following code snippet:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

tokenizer = AutoTokenizer.from_pretrained("quantumaikr/QuantumLM-7B", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("quantumaikr/QuantumLM-7B", torch_dtype=torch.float16, low_cpu_mem_usage=True, device_map="auto")
system_prompt = "### System:\nYou are QuantumLM, an AI that follows instructions extremely well. Help as much as you can. Remember, be safe, and don't do anything illegal.\n\n"

message = "Write me a poem please"
prompt = f"{system_prompt}### User: {message}\n\n### Assistant:\n"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
output = model.generate(**inputs, do_sample=True, top_p=0.95, top_k=0, max_new_tokens=256)

print(tokenizer.decode(output[0], skip_special_tokens=True))
```

QuantumLM should be used with this prompt format:
```
### System:
This is a system prompt, please behave and help the user.

### User:
Your prompt here

### Assistant
The output of QuantumLM
```



## Use and Limitations

### Intended Use

These models are intended for research only, in adherence with the [CC BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.

### Limitations and bias

Although the aforementioned dataset helps to steer the base language models into "safer" distributions of text, not all biases and toxicity can be mitigated through fine-tuning. We ask that users be mindful of such potential issues that can arise in generated responses. Do not treat model outputs as substitutes for human judgment or as sources of truth. Please use it responsibly.

