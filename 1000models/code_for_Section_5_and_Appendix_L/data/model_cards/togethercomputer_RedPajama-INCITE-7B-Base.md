
# RedPajama-INCITE-7B-Base

RedPajama-INCITE-7B-Base was developed by Together and leaders from the open-source AI community including Ontocord.ai, ETH DS3Lab, AAI CERC, Université de Montréal, MILA - Québec AI Institute, Stanford Center for Research on Foundation Models (CRFM), Stanford Hazy Research research group and LAION. 
The training was done on 3,072 V100 GPUs provided as part of the INCITE 2023 project on Scalable Foundation Models for Transferrable Generalist AI, awarded to MILA, LAION, and EleutherAI in fall 2022, with support from the Oak Ridge Leadership Computing Facility (OLCF) and INCITE program. 

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
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Base")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Base", torch_dtype=torch.float16)
model = model.to('cuda:0')
# infer
prompt = "Alan Turing is"
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
input_length = inputs.input_ids.shape[1]
outputs = model.generate(
    **inputs, max_new_tokens=128, do_sample=True, temperature=0.7, top_p=0.7, top_k=50, return_dict_in_generate=True
)
token = outputs.sequences[0, input_length:]
output_str = tokenizer.decode(token)
print(output_str)
"""
widely considered to be the father of modern computer science and artificial intelligence. He was a brilliant mathematician and cryptographer, who worked for the British government during World War II. He was instrumental in breaking the German Enigma code, and is credited with helping to shorten the war by two years...
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
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Base")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Base", device_map='auto', torch_dtype=torch.float16, load_in_8bit=True)

# infer
prompt = "Alan Turing is"
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
input_length = inputs.input_ids.shape[1]
outputs = model.generate(
    **inputs, max_new_tokens=128, do_sample=True, temperature=0.7, top_p=0.7, top_k=50, return_dict_in_generate=True
)
token = outputs.sequences[0, input_length:]
output_str = tokenizer.decode(token)
print(output_str)
"""
a very well-known name in the world of computer science. It is named after the mathematician Alan Turing. He is famous for his work on the Enigma machine, which was used by the Germans during World War II....
"""```

## CPU Inference

```python
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

MIN_TRANSFORMERS_VERSION = '4.25.1'

# check transformers version
assert transformers.__version__ >= MIN_TRANSFORMERS_VERSION, f'Please upgrade transformers to version {MIN_TRANSFORMERS_VERSION} or higher.'

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Base")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-7B-Base", torch_dtype=torch.bfloat16)
# infer
prompt = "Alan Turing is"
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
input_length = inputs.input_ids.shape[1]
outputs = model.generate(
    **inputs, max_new_tokens=128, do_sample=True, temperature=0.7, top_p=0.7, top_k=50, return_dict_in_generate=True
)
token = outputs.sequences[0, input_length:]
output_str = tokenizer.decode(token)
print(output_str)
"""
one of the most important figures in the history of computing. He is best known for his work on the development of the modern computer and for his code-breaking work during World War II. He was also a brilliant mathematician and philosopher.
"""
```

Please note that since `LayerNormKernelImpl` is not implemented in fp16 for CPU, we use `bfloat16` for CPU inference.

# Uses

## Direct Use 

Excluded uses are described below.

### Misuse, Malicious Use, and Out-of-Scope Use

It is the responsibility of the end user to ensure that the model is used in a responsible and ethical manner.

#### Out-of-Scope Use

`RedPajama-INCITE-7B-Base` is a language model and may not perform well for other use cases outside of its intended scope. 
For example, it may not be suitable for use in safety-critical applications or for making decisions that have a significant impact on individuals or society. 
It is important to consider the limitations of the model and to only use it for its intended purpose.

#### Misuse and Malicious Use

`RedPajama-INCITE-7B-Base` is designed for language modeling.
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

`RedPajama-INCITE-7B-Base`, like other language models, has limitations that should be taken into consideration. 
For example, the model may not always provide accurate or relevant answers, particularly for questions that are complex, ambiguous, or outside of its training data. 
We therefore welcome contributions from individuals and organizations, and encourage collaboration towards creating a more robust and inclusive chatbot.

## Training

**Training Data**

Please refer to [togethercomputer/RedPajama-Data-1T](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)

**Training Procedure**

- **Hardware:** 512 nodes of 6xV100 (IBM Power9), on the OLCF Summit cluster
- **Optimizer:** Apex FusedAdam
- **Parallelism:** Pipeline parallel 12, tensor parallel 2
- **Gradient Accumulations**: 8 (global batch size 4M tokens)
- **Num of Tokens:** 1.001T Tokens
- **Learning rate:** 0.00012

## Benchmark

Please refer to our [blog post](https://together.xyz) for benchmark results.

## Intermediate Checkpoints

We provide 11 intermediate checkpoints that have been released for study.
The checkpoints are organized based on the number of tokens they contain, ranging from 240 billion tokens to 1 trillion tokens.

- [240b_tokens](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/240b_tokens)
- [280b_tokens](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/280b_tokens)
- [400b_tokens](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/400b_tokens)
- [440b_tokens](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/440b_tokens)
- [500b_tokens](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/500b_tokens)
- [600b_tokens](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/600b_tokens)
- [700b_tokens](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/700b_tokens)
- [720b_tokens](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/720b_tokens)
- [960b_tokens](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/960b_tokens)
- [1t_tokens](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/1t_tokens)
- [latest](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base/tree/main)

## Community

Join us on [Together Discord](https://discord.gg/6ZVDU8tTD4)