# **Mistral-ORPO-Capybara-7k (7B)**

**Mistral-ORPO** is a fine-tuned version of [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) using the *[odds ratio preference optimization (ORPO)](https://arxiv.org/abs/2403.07691)*. With ORPO, the model directly learns the preference without the supervised fine-tuning warmup phase. 

**Mistral-ORPO-ORPO-Capybara-7k** is fine-tuned for **2.5 hours on four A100s** exclusively on the **7k** instances of the distilled Capybara paired multi-turn conversation dataset, [argilla/distilabel-capybara-dpo-7k-binarized](https://huggingface.co/datasets/argilla/distilabel-capybara-dpo-7k-binarized), by [Argilla](https://huggingface.co/argilla).

- **Github Repository**: https://github.com/xfactlab/orpo

## 👍 **Model Performance**

### 1) AlpacaEval & MT-Bench

|Model Name|Size|Align|MT-Bench|AlpacaEval 2.0 (LC)|
|:--------|:--------------:|:-------------------:|:------------:|:------------:|
|**Mistral-<tt>ORPO</tt>-Capybara-7k**|7B|<tt>ORPO</tt>|7.44|15.9|
|**Mistral-<tt>ORPO</tt>-β**|7B|<tt>ORPO</tt>|7.32|14.7|
|Zephyr β |7B|DPO|7.34|13.2|
|TULU-2-DPO |13B|DPO|7.00|11.6|
|Llama-2-Chat |7B|RLHF|6.27|5.4|
|Llama-2-Chat |13B|RLHF|6.65|8.4|

### 2) IFEval

| **Model Type**     | **Prompt-Strict** | **Prompt-Loose** | **Inst-Strict** | **Inst-Loose** |
|--------------------|:-----------------:|:----------------:|:---------------:|:--------------:|
| **Mistral-ORPO-Capybara-7k** |       0.5083      |      0.5083      |      0.5827     |     0.6127     |
| **Mistral-ORPO-⍺** |       0.5009      |      0.5083      |      0.5995     |     0.6163     |
| **Mistral-ORPO-β** |       0.5287      |      0.5564      |      0.6355     |     0.6619     |

## 🗺️ **MT-Bench by Category**

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6415c043486c7c9a5d151583/pmR91-0dpERqVvPqZ_IQg.png)

## 🖥️ **Inference**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("kaist-ai/mistral-orpo-capybara-7k")
tokenizer = AutoTokenizer.from_pretrained("kaist-ai/mistral-orpo-capybara-7k")
# Apply chat template
query = [{'role': 'user', 'content': 'Hi! How are you doing?'}]
prompt = tokenizer.apply_chat_template(query, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors='pt')
# Generation with specific configurations
output = model.generate(
  **inputs,
  max_new_tokens=128,
  do_sample=True,
  temperature=0.7
)
response = tokenizer.batch_decode(output)
#<|user|>
#Hi! How are you doing?</s>
#<|assistant|>
#I'm doing well, thank you! How are you?</s>
```

## 📎 **Citation**

```
@misc{hong2024orpo,
      title={ORPO: Monolithic Preference Optimization without Reference Model}, 
      author={Jiwoo Hong and Noah Lee and James Thorne},
      year={2024},
      eprint={2403.07691},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```