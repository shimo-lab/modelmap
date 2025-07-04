
# RedPajama-INCITE-7B-Chat

RedPajama-INCITE-7B-Chat was developed by Together and leaders from the open-source AI community including Ontocord.ai, ETH DS3Lab, AAI CERC, Université de Montréal, MILA - Québec AI Institute, Stanford Center for Research on Foundation Models (CRFM), Stanford Hazy Research research group and LAION. 

It is fine-tuned on OASST1 and Dolly2 to enhance chatting ability.

  - Base Model: [RedPajama-INCITE-7B-Base](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base)
  - Instruction-tuned Version: [RedPajama-INCITE-7B-Instruct](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Instruct)
  - Chat Version: [RedPajama-INCITE-7B-Chat](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Chat)


## Model Details
- **Developed by**: Together Computer.
- **Model type**: Language Model
- **Language(s)**: English
- **License**: Apache 2.0
- **Model Description**: A 6.9B parameter pretrained language model.

# Quick Start

Please note that the model requires `transformers` version >= 4.25.1.

To prompt the chat model, use the following format:
```
<human>: [Instruction]
<bot>:
```

## GPU Inference

This requires a GPU with 16GB memory.

```python
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

MIN_TRANSFORMERS_VERSION = '4.25.1'

# check transformers version
assert transformers.__version__ >= MIN_TRANSFORMERS_VERSION, f'Please upgrade transformers to version {MIN_TRANSFORMERS_VERSION} or higher.'

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Chat")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Chat", torch_dtype=torch.float16)
model = model.to('cuda:0')
# infer
prompt = "<human>: Who is Alan Turing?\n<bot>:"
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
input_length = inputs.input_ids.shape[1]
outputs = model.generate(
    **inputs, max_new_tokens=128, do_sample=True, temperature=0.7, top_p=0.7, top_k=50, return_dict_in_generate=True
)
token = outputs.sequences[0, input_length:]
output_str = tokenizer.decode(token)
print(output_str)
"""
Alan Mathison Turing (23 June 1912  7 June 1954) was an English computer scientist, mathematician, logician, cryptanalyst, philosopher, mathematician, and theoretical biologist.
"""
```

## GPU Inference in Int8

This requires a GPU with 12GB memory.

To run inference with int8, please ensure you have installed accelerate and bitandbytes. You can install them with the following command:

```bash
pip install accelerate
pip install bitsandbytes
```

Then you can run inference with int8 as follows:

```python
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

MIN_TRANSFORMERS_VERSION = '4.25.1'

# check transformers version
assert transformers.__version__ >= MIN_TRANSFORMERS_VERSION, f'Please upgrade transformers to version {MIN_TRANSFORMERS_VERSION} or higher.'

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Chat")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Chat", device_map='auto', torch_dtype=torch.float16, load_in_8bit=True)

# infer
prompt = "<human>: Who is Alan Turing?\n<bot>:"
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
input_length = inputs.input_ids.shape[1]
outputs = model.generate(
    **inputs, max_new_tokens=128, do_sample=True, temperature=0.7, top_p=0.7, top_k=50, return_dict_in_generate=True
)
token = outputs.sequences[0, input_length:]
output_str = tokenizer.decode(token)
print(output_str)
"""
Alan Mathison Turing (23 June 1912 – 7 June 1954) was an English computer scientist, mathematician, logician, cryptanalyst, philosopher, and theoretical biologist.
"""
```

## CPU Inference

```python
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

MIN_TRANSFORMERS_VERSION = '4.25.1'

# check transformers version
assert transformers.__version__ >= MIN_TRANSFORMERS_VERSION, f'Please upgrade transformers to version {MIN_TRANSFORMERS_VERSION} or higher.'

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Chat")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Chat", torch_dtype=torch.bfloat16)
# infer
prompt = "<human>: Who is Alan Turing?\n<bot>:"
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
input_length = inputs.input_ids.shape[1]
outputs = model.generate(
    **inputs, max_new_tokens=128, do_sample=True, temperature=0.7, top_p=0.7, top_k=50, return_dict_in_generate=True
)
token = outputs.sequences[0, input_length:]
output_str = tokenizer.decode(token)
print(output_str)
"""
Alan Mathison Turing, OBE, FRS, (23 June 1912 – 7 June 1954) was an English computer scientist, mathematician, logician, cryptanalyst, philosopher, and theoretical biologist.
"""
```

Please note that since `LayerNormKernelImpl` is not implemented in fp16 for CPU, we use `bfloat16` for CPU inference.


# Uses

## Direct Use 

Excluded uses are described below.

### Misuse, Malicious Use, and Out-of-Scope Use

It is the responsibility of the end user to ensure that the model is used in a responsible and ethical manner.

#### Out-of-Scope Use

`RedPajama-INCITE-7B-Chat` is a language model and may not perform well for other use cases outside of its intended scope. 
For example, it may not be suitable for use in safety-critical applications or for making decisions that have a significant impact on individuals or society. 
It is important to consider the limitations of the model and to only use it for its intended purpose.

#### Misuse and Malicious Use

`RedPajama-INCITE-7B-Chat` is designed for language modeling.
Misuse of the model, such as using it to engage in illegal or unethical activities, is strictly prohibited and goes against the principles of the project.

Using the model to generate content that is cruel to individuals is a misuse of this model. This includes, but is not limited to:

- Generating fake news, misinformation, or propaganda
- Promoting hate speech, discrimination, or violence against individuals or groups
- Impersonating individuals or organizations without their consent
- Engaging in cyberbullying or harassment
- Defamatory content
- Spamming or scamming
- Sharing confidential or sensitive information without proper authorization
- Violating the terms of use of the model or the data used to train it
- Creating automated bots for malicious purposes such as spreading malware, phishing scams, or spamming

## Limitations

`RedPajama-INCITE-7B-Chat`, like other language models, has limitations that should be taken into consideration. 
For example, the model may not always provide accurate or relevant answers, particularly for questions that are complex, ambiguous, or outside of its training data. 
We therefore welcome contributions from individuals and organizations, and encourage collaboration towards creating a more robust and inclusive chatbot.

## Training

**Training Data**

Please refer to [togethercomputer/RedPajama-Data-1T](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)

**Training Procedure**

- **Hardware:** 8 A100
- **Optimizer:** Adam
- **Gradient Accumulations**: 1
- **Num of Tokens:** 79M tokens
- **Learning rate:** 1e-5

## Community

Join us on [Together Discord](https://discord.gg/6ZVDU8tTD4)