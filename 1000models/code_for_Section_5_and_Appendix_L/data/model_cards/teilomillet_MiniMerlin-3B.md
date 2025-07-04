SFT on a synthetic custom (french) dataset (2k), from general question answering, problem solving to code question.
It's a POC.


```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

model = AutoModelForCausalLM.from_pretrained(
    "teilomillet/MiniMerlin-3B",
    revision="0.1",
    return_dict=True,
    torch_dtype=torch.bfloat16,
    device_map='auto'
)

tokenizer = AutoTokenizer.from_pretrained("teilomillet/MiniMerlin-3B")
tokenizer.pad_token = tokenizer.eos_token

text = "[|User|] Comment faire un bon plat ? </s>[|Assistant|]"
inputs = tokenizer(text, return_tensors="pt").to(0)

outputs = model.generate(**inputs, max_new_tokens=800)
print(tokenizer.decode(outputs[0], skip_special_tokens=False))
```