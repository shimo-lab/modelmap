
# Uploaded  model

- **Developed by:** walid-iguider
- **License:** cc-by-nc-sa-4.0
- **Finetuned from model :** unsloth/Phi-3-mini-4k-instruct-bnb-4bit


## Evaluation

For a detailed comparison of model performance, check out the [Leaderboard for Italian Language Models](https://huggingface.co/spaces/FinancialSupport/open_ita_llm_leaderboard).

Here's a breakdown of the performance metrics:
| Metric                      | hellaswag_it acc_norm | arc_it acc_norm | m_mmlu_it 5-shot acc | Average |
|:----------------------------|:----------------------|:----------------|:---------------------|:--------|
| **Accuracy Normalized**     | 0.5841                | 0.4414        | 0.5389              | 0.5214  |

---

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("FairMind/Phi-3-mini-4k-instruct-bnb-4bit-Ita")
model = AutoModelForCausalLM.from_pretrained("FairMind/Phi-3-mini-4k-instruct-bnb-4bit-Ita")
model.to(device)


generation_config = GenerationConfig(
      penalty_alpha=0.6, # The values balance the model confidence and the degeneration penalty in contrastive search decoding.
      do_sample = True, # Whether or not to use sampling ; use greedy decoding otherwise.
      top_k=5, #  The number of highest probability vocabulary tokens to keep for top-k-filtering.
      temperature=0.001, #  The value used to modulate the next token probabilities.
      repetition_penalty=1.7, # The parameter for repetition penalty. 1.0 means no penalty.
      max_new_tokens = 64, # The maximum numbers of tokens to generate, ignoring the number of tokens in the prompt.
      eos_token_id=tokenizer.eos_token_id, # The id of the *end-of-sequence* token.
      pad_token_id=tokenizer.eos_token_id, # The id of the *padding* token.
  )


def generate_answer(question):
    messages = [
        {"role": "user", "content": question},
    ]
    model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(device)
    outputs = model.generate(model_inputs, generation_config=generation_config)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    return result


question = """Quale è la torre più famosa di Parigi?"""
answer = generate_answer(question)
print(answer)
```
---

This model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)