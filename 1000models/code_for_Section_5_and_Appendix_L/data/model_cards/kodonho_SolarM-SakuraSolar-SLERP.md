
# Solar based model with gradient slerp 

This is an English mixed Model based on
* [DopeorNope/SOLARC-M-10.7B]
* [kyujinpy/Sakura-SOLRCA-Math-Instruct-DPO-v2]


gpu code example

```
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import math

## v2 models
model_path = "kodonho/SolarM-SakuraSolar-SLERP"

tokenizer = AutoTokenizer.from_pretrained(model_path, use_default_system_prompt=False)
model = AutoModelForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float32, device_map='auto',local_files_only=False, load_in_4bit=True
)
print(model)
prompt = input("please input prompt:")
while len(prompt) > 0:
  input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")

  generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=500,repetition_penalty=1.2
  )
  print(tokenizer.decode(generation_output[0]))
  prompt = input("please input prompt:")
```

CPU example

```
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import math

## v2 models
model_path = "kodonho/SolarM-SakuraSolar-SLERP"

tokenizer = AutoTokenizer.from_pretrained(model_path, use_default_system_prompt=False)
model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.bfloat16, device_map='cpu'
)
print(model)
prompt = input("please input prompt:")
while len(prompt) > 0:
  input_ids = tokenizer(prompt, return_tensors="pt").input_ids

  generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=500,repetition_penalty=1.2
  )
  print(tokenizer.decode(generation_output[0]))
  prompt = input("please input prompt:")

```

