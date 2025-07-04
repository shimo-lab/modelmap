
# **Synatra-10.7B-v0.4🐧**  
![Synatra-10.7B-v0.4](./Synatra.png)

# Join our discord

[Server Link](https://discord.gg/MrBt3PXdXc)

# **License**

The "Model" is completely free (ie. base model, derivates, merges/mixes) to use for non-commercial purposes as long as the the included **cc-by-sa-4.0** license in any parent repository, and the non-commercial use statute remains, regardless of other models' licences. 
# **Model Details**

**Base Model**  
[upstage/SOLAR-10.7B-v1.0](https://huggingface.co/upstage/SOLAR-10.7B-v1.0)  

**Trained On**  
A100 80GB * 1

**Instruction format**

It follows **Alpaca** format.

# **Model Benchmark**


## Ko-LLM-Leaderboard

On Benchmarking...

# **Implementation Code**

Since, chat_template already contains insturction format above.
You can use the code below.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("maywell/Synatra-10.7B-v0.4")
tokenizer = AutoTokenizer.from_pretrained("maywell/Synatra-10.7B-v0.4")

messages = [
    {"role": "user", "content": "바나나는 원래 하얀색이야?"},
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
```