
<div style="text-align:center;width:250px;height:250px;">
    <img src="https://huggingface.co/mrm8488/llama-2-coder-7b/resolve/main/llama2-coder-logo-removebg-preview.png" alt="llama-2 coder logo"">
</div>


# LlaMa 2 Coder 🦙👩‍💻
**LlaMa-2 7b** fine-tuned on the **CodeAlpaca 20k instructions dataset** by using the method **QLoRA** with [PEFT](https://github.com/huggingface/peft) library.

## Model description 🧠

[Llama-2](https://huggingface.co/meta-llama/Llama-2-7b)

Llama 2 is a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters.
Meta developed and publicly released the Llama 2 family of large language models (LLMs), a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama-2-Chat, are optimized for dialogue use cases. Llama-2-Chat models outperform open-source chat models on most benchmarks we tested, and in our human evaluations for helpfulness and safety, are on par with some popular closed-source models like ChatGPT and PaLM.


## Training and evaluation data 📚

[CodeAlpaca_20K](https://huggingface.co/datasets/HuggingFaceH4/CodeAlpaca_20K): contains 20K instruction-following data used for fine-tuning the Code Alpaca model.


### Training hyperparameters ⚙

```py
    optim="paged_adamw_32bit",
    num_train_epochs = 2,
    eval_steps=50,
    save_steps=50,
    evaluation_strategy="steps",
    save_strategy="steps",
    save_total_limit=2,
    seed=66,
    load_best_model_at_end=True,
    logging_steps=1,
    learning_rate=2e-4,
    fp16=True,
    bf16=False,
    max_grad_norm=0.3,
    warmup_ratio=0.03,
    group_by_length=True,
    lr_scheduler_type="constant"
```

### Training results 🗒️


| Step | Training Loss | Validation Loss |
|------|----------|----------|
| 50   | 0.624400 | 0.600070 |
| 100  | 0.634100 | 0.592757 |
| 150  | 0.545800 | 0.586652 |
| 200  | 0.572500 | 0.577525 |
| 250  | 0.528000 | 0.590118 |


### Eval results 📊

WIP


### Example of usage 👩‍💻
```py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

model_id = "mrm8488/llama-2-coder-7b"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id).to("cuda")

def create_prompt(instruction):
  system = "You are a coding assistant that will help the user to resolve the following instruction:"
  instruction = "### Instruction: " + instruction
  return system + "\n" + instruction + "\n\n" + "### Solution:" + "\n"

def generate(
        instruction,
        max_new_tokens=128,
        temperature=0.1,
        top_p=0.75,
        top_k=40,
        num_beams=4,
        **kwargs,
):
    prompt = create_prompt(instruction)
    print(prompt)
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].to("cuda")
    attention_mask = inputs["attention_mask"].to("cuda")
    generation_config = GenerationConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        num_beams=num_beams,
        **kwargs,
    )
    with torch.no_grad():
        generation_output = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            generation_config=generation_config,
            return_dict_in_generate=True,
            output_scores=True,
            max_new_tokens=max_new_tokens,
            early_stopping=True
        )
    s = generation_output.sequences[0]
    output = tokenizer.decode(s)
    return output.split("### Solution:")[1].lstrip("\n")

instruction = """
Edit the following XML code to add a navigation bar to the top of a web page
<html>
<head>
  <title>CliBrAIn</title>
</head>
"""
print(generate(instruction))
```

### Citation

```
@misc {manuel_romero_2023,
	author       = { {Manuel Romero} },
	title        = { llama-2-coder-7b (Revision d30d193) },
	year         = 2023,
	url          = { https://huggingface.co/mrm8488/llama-2-coder-7b },
	doi          = { 10.57967/hf/0931 },
	publisher    = { Hugging Face }
}
```