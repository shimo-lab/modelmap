
### Mistral-7B-Forest-DPO
Introducing Mistral-7B-Forest-DPO, a LLM fine-tuned with base model mistralai/Mistral-7B-v0.1, using direct preference optimization.
This model showcases exceptional prowess across a spectrum of natural language processing (NLP) tasks. 

A mixture of the following datasets was used for fine-tuning.

1. Intel/orca_dpo_pairs
2. nvidia/HelpSteer
3. jondurbin/truthy-dpo-v0.1



💻 Usage

```python
!pip install -qU transformers bitsandbytes accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "abhishekchohan/mistral-7B-forest-dpo"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    model_kwargs={"torch_dtype": torch.float16, "load_in_4bit": True},
)

messages = [{"role": "user", "content": "Explain what a Mixture of Experts is in less than 100 words."}]
prompt = pipeline.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

```