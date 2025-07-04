
<img src="./llama-3-merges.webp" alt="Llama-3 DPO Logo" width="500" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


# Llama-3-8B-Instruct-v0.8

This model was developed based on `MaziyarPanahi/Llama-3-8B-Instruct-v0.4` model.

# ⚡ Quantized GGUF

All GGUF models are available here: [MaziyarPanahi/Llama-3-8B-Instruct-v0.8-GGUF](https://huggingface.co/MaziyarPanahi/Llama-3-8B-Instruct-v0.8-GGUF)


# 🏆 [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_MaziyarPanahi__Llama-3-8B-Instruct-v0.8)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |73.20|
|AI2 Reasoning Challenge (25-Shot)|71.67|
|HellaSwag (10-Shot)              |87.77|
|MMLU (5-Shot)                    |68.30|
|TruthfulQA (0-shot)              |63.90|
|Winogrande (5-shot)              |79.08|
|GSM8k (5-shot)                   |68.46|

`MaziyarPanahi/Llama-3-8B-Instruct-v0.8` is the 5th best-performing 8B model on the Open LLM Leaderboard. (03/06/2024).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5fd5e18a90b6dc4633f6d292/ExIVXtyzYIYgilY_MxAPY.png)


**Leaderboard 2.0:**

|      Metric       |Value|
|-------------------|----:|
|Avg.               |26.75|
|IFEval (0-Shot)    |75.12|
|BBH (3-Shot)       |28.27|
|MATH Lvl 5 (4-Shot)| 7.10|
|GPQA (0-shot)      | 7.38|
|MuSR (0-shot)      |10.92|
|MMLU-PRO (5-shot)  |31.68|



# Prompt Template

This model uses `ChatML` prompt template:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
````

# How to use

You can use this model by using `MaziyarPanahi/Llama-3-8B-Instruct-v0.8` as the model name in Hugging Face's
transformers library.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
from transformers import pipeline
import torch

model_id = "MaziyarPanahi/Llama-3-8B-Instruct-v0.8"

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


