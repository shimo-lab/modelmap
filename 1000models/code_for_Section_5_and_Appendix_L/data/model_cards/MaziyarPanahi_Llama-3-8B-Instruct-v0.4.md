
<img src="./llama-3-merges.webp" alt="Llama-3 DPO Logo" width="500" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


# Llama-3-8B-Instruct-v0.4

This model was developed based on `meta-llama/Meta-Llama-3-8B-Instruct` model.

# Quantized GGUF

All GGUF models are available here: [MaziyarPanahi/Llama-3-8B-Instruct-v0.4-GGUF](https://huggingface.co/MaziyarPanahi/Llama-3-8B-Instruct-v0.4-GGUF)


# Prompt Template

This model uses `ChatML` prompt template:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
````

# How to use

You can use this model by using `MaziyarPanahi/Llama-3-8B-Instruct-v0.4` as the model name in Hugging Face's
transformers library.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
from transformers import pipeline
import torch

model_id = "MaziyarPanahi/Llama-3-8B-Instruct-v0.4"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
    # attn_implementation="flash_attention_2"
)

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True
)

streamer = TextStreamer(tokenizer)

pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    model_kwargs={"torch_dtype": torch.bfloat16},
    streamer=streamer
)

# Then you can use the pipeline to generate text.

messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": "Who are you?"},
]

prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

terminators = [
    tokenizer.eos_token_id,    
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = pipeline(
    prompt,
    max_new_tokens=512,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.95,
)
print(outputs[0]["generated_text"][len(prompt):])
```