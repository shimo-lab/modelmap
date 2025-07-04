# Hebrew-Mistral-7B

Hebrew-Mistral-7B is an open-source Large Language Model (LLM) pretrained in hebrew and english pretrained with 7B billion parameters, based on Mistral-7B-v1.0 from Mistral.

It has an extended hebrew tokenizer with 64,000 tokens and is continuesly pretrained from Mistral-7B on tokens in both English and Hebrew.

The resulting model is a powerful general-purpose language model suitable for a wide range of natural language processing tasks, with a focus on Hebrew language understanding and generation.

### Usage

Below are some code snippets on how to get quickly started with running the model.

First make sure to `pip install -U transformers`, then copy the snippet from the section that is relevant for your usecase.

### Running on CPU

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("yam-peleg/Hebrew-Mistral-7B")
model = AutoModelForCausalLM.from_pretrained("yam-peleg/Hebrew-Mistral-7B")

input_text = "שלום! מה שלומך היום?"
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))
```

### Running on GPU

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("yam-peleg/Hebrew-Mistral-7B")
model = AutoModelForCausalLM.from_pretrained("yam-peleg/Hebrew-Mistral-7B", device_map="auto")

input_text = "שלום! מה שלומך היום?"
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))
```

### Running with 4-Bit precision

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

tokenizer = AutoTokenizer.from_pretrained("yam-peleg/Hebrew-Mistral-7B")
model = AutoModelForCausalLM.from_pretrained("yam-peleg/Hebrew-Mistral-7B", quantization_config = BitsAndBytesConfig(load_in_4bit=True))

input_text = "שלום! מה שלומך היום?"
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0])
```

### Notice

Hebrew-Mistral-7B is a pretrained base model and therefore does not have any moderation mechanisms.

### Authors
- Trained by Yam Peleg.
- In collaboration with Jonathan Rouach and Arjeo, inc.

