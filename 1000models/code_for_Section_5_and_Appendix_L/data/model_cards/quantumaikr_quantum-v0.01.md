
# quantumaikr/quantum-v0.01

## Usage

Start chatting with `quantumaikr/quantum-v0.01` using the following code snippet:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

tokenizer = AutoTokenizer.from_pretrained("quantumaikr/quantum-v0.01")
model = AutoModelForCausalLM.from_pretrained("quantumaikr/quantum-v0.01", torch_dtype=torch.float16, device_map="auto")

system_prompt = "You are QuantumLM, an AI that follows instructions extremely well. Help as much as you can. Remember, be safe, and don't do anything illegal."

message = "Write me a poem please"
prompt = f"[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{message}[/INST]"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
output = model.generate(**inputs, do_sample=True, temperature=0.7, top_p=0.95, top_k=30, max_new_tokens=2048)

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



Contact us : hi@quantumai.kr

