
Hyperparameters
- 3/8 epoch(3rd epoch checkpoing while 8epoch training)
- 1e-4 -> 1e-5 with cosine lr decay 
- batch size 128
- max sequence length 2048
- AdamW(weigth decay=0.01, b1=0.9, b2=0.99, grad_clip=1.0)
- no warmup
- BF16
- Base Model: [openlm-research/open_llama_3b_v2](https://huggingface.co/openlm-research/open_llama_3b_v2)

```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("heegyu/WizardVicuna-open-llama-3b-v2")
model = AutoModelForCausalLM.from_pretrained("heegyu/WizardVicuna-open-llama-3b-v2")

inputs = tokenizer(["Human: Hi, nice to meet you!\n\nAssistant: "], return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=16)
print(tokenizer.batch_decode(outputs, skip_special_tokens=False))
```

output: `['Human: Hi, nice to meet you!\n\nAssistant: Hello. Great to meet you too. Well, how can I assist you today?<|endoftext|>']`