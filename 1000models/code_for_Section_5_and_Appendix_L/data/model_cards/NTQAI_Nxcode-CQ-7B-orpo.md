
<a href="https://ntq.com.vn" target="_blank"><img src="https://cdn-uploads.huggingface.co/production/uploads/5ee1b417636bdb3834e2da19/etbfTJuVdAub2evNP_E4g.png" width="200"/></a>

## Introduction

Nxcode-CQ-7B-orpo is an [Monolithic Preference Optimization without Reference Model](https://arxiv.org/abs/2403.07691) fine-tune of Qwen/CodeQwen1.5-7B on 100k samples of high-quality ranking data.

## [Evalplus](https://github.com/evalplus/evalplus)

| EvalPlus | pass@1 |
| --- | --- |
| HumanEval | 86.6 |
| HumanEval+ | 83.5 |
| MBPP(v0.2.0) | 82.3 |
| MBPP+(v0.2.0) | 70.4 |

We use a simple template to generate the solution for evalplus:

```python
"Complete the following Python function:\n{prompt}"
```

[Evalplus Leaderboard](https://evalplus.github.io/leaderboard.html)
| Models | HumanEval | HumanEval+|
|------ | ------  | ------ |
| GPT-4-Turbo (April 2024)|  90.2| 86.6|
| GPT-4 (May 2023)|  88.4| 81.17|
| GPT-4-Turbo (Nov 2023)|  85.4| 79.3| 
| CodeQwen1.5-7B-Chat|  83.5| 78.7| 
| claude-3-opus (Mar 2024)|  82.9| 76.8|
| DeepSeek-Coder-33B-instruct|  81.1| 75.0|
| WizardCoder-33B-V1.1|  79.9| 73.2|
| OpenCodeInterpreter-DS-33B|  79.3| 73.8|
| speechless-codellama-34B-v2.0|  77.4| 72|
| GPT-3.5-Turbo (Nov 2023)| 76.8| 70.7|
| Llama3-70B-instruct| 76.2| 70.7|

## Bigcode Leaderboard

[Bigcode Leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)

**09/05/2024**

Top 1 average score.

Top 2 winrate.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5ee1b417636bdb3834e2da19/OQonD6a7aNjnN9SsTkFp-.png)


## Quickstart

Here provides a code snippet with `apply_chat_template` to show you how to load the tokenizer and model and how to generate contents. You should upgrade the transformers if you receive an error when loading the tokenizer
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    "NTQAI/Nxcode-CQ-7B-orpo",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("NTQAI/Nxcode-CQ-7B-orpo")

prompt = """Complete the following Python function:
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
"""
messages = [
    {"role": "user", "content": prompt}
]

inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
outputs = model.generate(inputs, max_new_tokens=512, do_sample=False, top_k=50, top_p=0.95, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
res = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)

```

### Contact information
For personal communication related to this project, please contact Nha Nguyen Van (nha.nguyen@ntq-solution.com.vn).