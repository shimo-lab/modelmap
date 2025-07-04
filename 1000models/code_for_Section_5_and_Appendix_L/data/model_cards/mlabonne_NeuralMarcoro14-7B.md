
![](https://i.imgur.com/CBen22L.jpg)

# NeuralMarcoro14-7B

This is a DPO fine-tuned version of [mlabonne/Marcoro14-7B-slerp](https://huggingface.co/mlabonne/Marcoro14-7B-slerp) using the [chatml_dpo_pairs](https://huggingface.co/datasets/mlabonne/chatml_dpo_pairs) preference dataset. 
It improves the performance of the model on Nous benchmark suite and the Open LLM Benchmark.

It is currently the best-performing 7B LLM on the Open LLM Leaderboard (08/01/24).

You can try it out in this [Space](https://huggingface.co/spaces/mlabonne/NeuralMarcoro14-7B-GGUF-Chat) (GGUF Q4_K_M).

## ⚡ Quantized models

* **GGUF**: https://huggingface.co/mlabonne/NeuralMarcoro14-7B-GGUF

## 🏆 Evaluation

### Open LLM Leaderboard

![](https://i.imgur.com/Int9P07.png)

![](https://i.imgur.com/70NXUKD.png)

### Nous

|          Model          |AGIEval|GPT4ALL|TruthfulQA|Bigbench|Average|
|-------------------------|------:|------:|---------:|-------:|------:|
|[NeuralMarcoro14-7B](https://huggingface.co/mlabonne/NeuralMarcoro14-7B)|  44.59|  76.17|     65.94|    46.9|   58.4|
|[Marcoro14-7B-slerp](https://huggingface.co/mlabonne/Marcoro14-7B-slerp)       |  44.66|  76.24|     64.15|   45.64|  57.67|
|Change                   |  -0.07|  -0.07|    +1.79|   +1.26|   +0.73|

## 🧩 Training hyperparameters

**LoRA**:
* r=16
* lora_alpha=16
* lora_dropout=0.05
* bias="none"
* task_type="CAUSAL_LM"
* target_modules=['k_proj', 'gate_proj', 'v_proj', 'up_proj', 'q_proj', 'o_proj', 'down_proj']

**Training arguments**:
* per_device_train_batch_size=4
* gradient_accumulation_steps=4
* gradient_checkpointing=True
* learning_rate=5e-5
* lr_scheduler_type="cosine"
* max_steps=200
* optim="paged_adamw_32bit"
* warmup_steps=100

**DPOTrainer**:
* beta=0.1
* max_prompt_length=1024
* max_length=1536

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "mlabonne/NeuralMarcoro14-7B"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```