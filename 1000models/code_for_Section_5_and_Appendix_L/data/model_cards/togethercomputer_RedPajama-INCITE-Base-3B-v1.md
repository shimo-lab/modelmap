
# RedPajama-INCITE-Base-3B-v1

RedPajama-INCITE-Base-3B-v1 was developed by Together and leaders from the open-source AI community including Ontocord.ai, ETH DS3Lab, AAI CERC, Université de Montréal, MILA - Québec AI Institute, Stanford Center for Research on Foundation Models (CRFM), Stanford Hazy Research research group and LAION. 
The training was done on 3,072 V100 GPUs provided as part of the INCITE 2023 project on Scalable Foundation Models for Transferrable Generalist AI, awarded to MILA, LAION, and EleutherAI in fall 2022, with support from the Oak Ridge Leadership Computing Facility (OLCF) and INCITE program. 

  - Base Model: [RedPajama-INCITE-Base-3B-v1](https://huggingface.co/togethercomputer/RedPajama-INCITE-Base-3B-v1)
  - Instruction-tuned Version: [RedPajama-INCITE-Instruct-3B-v1](https://huggingface.co/togethercomputer/RedPajama-INCITE-Instruct-3B-v1)
  - Chat Version: [RedPajama-INCITE-Chat-3B-v1](https://huggingface.co/togethercomputer/RedPajama-INCITE-Chat-3B-v1)

## Model Details
- **Developed by**: Together Computer.
- **Model type**: Language Model
- **Language(s)**: English
- **License**: Apache 2.0
- **Model Description**: A 2.8B parameter pretrained language model.

# Quick Start

Please note that the model requires `transformers` version >= 4.25.1.

## GPU Inference

This requires a GPU with 8GB memory.

```python
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

MIN_TRANSFORMERS_VERSION = '4.25.1'

# check transformers version
assert transformers.__version__ >= MIN_TRANSFORMERS_VERSION, f'Please upgrade transformers to version {MIN_TRANSFORMERS_VERSION} or higher.'

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-Base-3B-v1")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-Base-3B-v1", torch_dtype=torch.float16)
model = model.to('cuda:0')

# infer
prompt = "Alan Turing is"
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
input_length = inputs.input_ids.shape[1]
outputs = model.generate(
    **inputs, max_new_tokens=128, do_sample=True, temperature=0.7, top_p=0.7, top_k=50, return_dict_in_generate=True,
)
token = outputs.sequences[0, input_length:]
output_str = tokenizer.decode(token)
print(output_str)
"""
a name that has been synonymous with the computer age since the 1950s. The British mathematician, logician, and cryptanalyst is widely regarded as the father of modern computing. His contributions to the development of the modern computer and the theory of computation have had a profound impact on the world we live in today.
Turing’s contributions to the development of the modern computer were made in the 1940s and 1950s. He is most famous for his work on the Turing machine, a theoretical model of a computing machine that was able to perform all the mathematical operations of a computer. Turing’s work on the...
"""
```

## GPU Inference in Int8

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
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-Base-3B-v1")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-Base-3B-v1", device_map='auto', torch_dtype=torch.float16, load_in_8bit=True)

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
the man who cracked the Enigma code during World War II, and who was later convicted of homosexual acts. He was a brilliant mathematician, and a visionary who foresaw the computer age....
"""
```

## CPU Inference

You can run inference on CPU as follows:

```python
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

MIN_TRANSFORMERS_VERSION = '4.25.1'

# check transformers version
assert transformers.__version__ >= MIN_TRANSFORMERS_VERSION, f'Please upgrade transformers to version {MIN_TRANSFORMERS_VERSION} or higher.'

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-Base-3B-v1")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-Base-3B-v1", torch_dtype=torch.bfloat16)
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
a name that is synonymous with the history of computer science. As the man who invented the Turing machine, the mathematical model that defines the limits of what can be computed, Turing is credited with the invention of the modern computer. Turing was also a mathematician and logician, and his work in these fields led to the development of the field of artificial intelligence...
"""
```

Please note that since `LayerNormKernelImpl` is not implemented in fp16 for CPU, we use `bfloat16` for CPU inference.

# Uses

Excluded uses are described below.

### Misuse, Malicious Use, and Out-of-Scope Use

It is the responsibility of the end user to ensure that the model is used in a responsible and ethical manner.

#### Out-of-Scope Use

`RedPajama-INCITE-Base-3B-v1` is a language model and may not perform well for other use cases outside of its intended scope. 
For example, it may not be suitable for use in safety-critical applications or for making decisions that have a significant impact on individuals or society. 
It is important to consider the limitations of the model and to only use it for its intended purpose.

#### Misuse and Malicious Use

`RedPajama-INCITE-Base-3B-v1` is designed for language modeling.
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

`RedPajama-INCITE-Base-3B-v1`, like other language models, has limitations that should be taken into consideration. 
For example, the model may not always provide accurate or relevant answers, particularly for questions that are complex, ambiguous, or outside of its training data. 
We therefore welcome contributions from individuals and organizations, and encourage collaboration towards creating a more robust and inclusive chatbot.

## Training

**Training Data**

Please refer to [togethercomputer/RedPajama-Data-1T](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)

**Training Procedure**

- **Hardware:** 256 nodes of 6xV100 (IBM Power9), on the OLCF Summit cluster
- **Optimizer:** Apex FusedAdam
- **Parallelism:** Pipeline parallel 6, tensor parallel 2
- **Gradient Accumulations**: 8 (global batch size 4M tokens)
- **Num of Tokens:** 800B Tokens
- **Learning rate:** 0.00016

## Benchmark

Please refer to our [blog post](https://together.xyz) for benchmark results.

## Community

Join us on [Together Discord](https://discord.gg/6ZVDU8tTD4)