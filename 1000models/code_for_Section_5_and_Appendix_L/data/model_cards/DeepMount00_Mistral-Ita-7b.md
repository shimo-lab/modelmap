
# Mistral-7B-v0.1 for Italian Language Text Generation

## Model Architecture
- **Base Model:** [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)
- **Specialization:** Italian Language

## Evaluation

For a detailed comparison of model performance, check out the [Leaderboard for Italian Language Models](https://huggingface.co/spaces/FinancialSupport/open_ita_llm_leaderboard).

Here's a breakdown of the performance metrics:

| Metric                      | hellaswag_it acc_norm | arc_it acc_norm | m_mmlu_it 5-shot acc | Average |
|:----------------------------|:----------------------|:----------------|:---------------------|:--------|
| **Accuracy Normalized**     | 0.6731                | 0.5502          | 0.5364               | 0.5866  |

---


**Quantized 4-Bit Version Available**

A quantized 4-bit version of the model is available for use. This version offers a more efficient processing capability by reducing the precision of the model's computations to 4 bits, which can lead to faster performance and decreased memory usage. This might be particularly useful for deploying the model on devices with limited computational power or memory resources.

For more details and to access the model, visit the following link: [Mistral-Ita-7b-GGUF 4-bit version](https://huggingface.co/DeepMount00/Mistral-Ita-7b-GGUF).

---

## How to Use
How to utilize my Mistral for Italian text generation

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MODEL_NAME = "DeepMount00/Mistral-Ita-7b"

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16).eval()
model.to(device)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def generate_answer(prompt):
    messages = [
        {"role": "user", "content": prompt},
    ]
    model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(device)
    generated_ids = model.generate(model_inputs, max_new_tokens=200, do_sample=True,
                                          temperature=0.001, eos_token_id=tokenizer.eos_token_id)
    decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return decoded[0]

prompt = "Come si apre un file json in python?"
answer = generate_answer(prompt)
print(answer)
```
---
## Developer
[Michele Montebovi]