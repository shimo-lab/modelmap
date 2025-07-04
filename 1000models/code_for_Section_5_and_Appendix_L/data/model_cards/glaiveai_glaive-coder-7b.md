
# Glaive-coder-7b

Glaive-coder-7b is a 7B parameter code model trained on a dataset of ~140k programming related problems and solutions generated from Glaive’s synthetic data generation platform.

The model is fine-tuned on the CodeLlama-7b model.

## Usage:

The model is trained to act as a code assistant, and can do both single instruction following and multi-turn conversations.
It follows the same prompt format as CodeLlama-7b-Instruct-
```
<s>[INST]
<<SYS>>
{{ system_prompt }}
<</SYS>>

{{ user_msg }} [/INST] {{ model_answer }} </s>
<s>[INST] {{ user_msg }} [/INST]
```

You can run the model in the following way-

```python
from transformers import AutoModelForCausalLM , AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("glaiveai/glaive-coder-7b")
model = AutoModelForCausalLM.from_pretrained("glaiveai/glaive-coder-7b").half().cuda()

def fmt_prompt(prompt):
    return f"<s> [INST] {prompt} [/INST]"

inputs = tokenizer(fmt_prompt(prompt),return_tensors="pt").to(model.device)

outputs = model.generate(**inputs,do_sample=True,temperature=0.1,top_p=0.95,max_new_tokens=100)

print(tokenizer.decode(outputs[0],skip_special_tokens=True,clean_up_tokenization_spaces=False))
```

## Benchmarks:

The model achieves a 63.1% pass@1 on HumanEval and a 45.2% pass@1 on MBPP, however it is evident that these benchmarks are not representative of real-world usage of code models so we are launching the [Code Models Arena](https://arena.glaive.ai/) to let users vote on model outputs so we can have a better understanding of user preference on code models and come up with new and better benchmarks. We plan to release the Arena results as soon as we have a sufficient amount of data.

Join the Glaive [discord](https://discord.gg/fjQ4uf3yWD) for improvement suggestions, bug-reports and collaborating on more open-source projects.