

## 💻 For English
Defne_llama3_2x8B is a Mixure of Experts (MoE) (two llama3 models).
(Change the system prompt for Turkish as shown below)


```python
!pip install -qU transformers bitsandbytes accelerate

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "Eurdem/Defne_llama3_2x8B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto", load_in_8bit= True)

messages = [{"role": "system", "content": "You are a helpful chatbot, named Defne, who always responds friendly."},
            {"role": "user", "content": "Answer the questions: 1) Who are you? 2) f(x)=3x^2+4x+12 so what is f(3)?"},
]

input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
outputs = model.generate(input_ids, max_new_tokens=1024, do_sample=True, temperature=0.7, top_p=0.7, top_k=500,)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))
```
### Output
```
Hello there! I'm Defne, a friendly chatbot here to help with any questions you may have.

Now, let's get to the math problem!

The function is f(x) = 3x^2 + 4x + 12, and we want to find f(3). To do that, we can plug in 3 for x in the function:

f(3) = 3(3)^2 + 4(3) + 12
f(3) = 3(9) + 12 + 12
f(3) = 27 + 24
f(3) = 51

So, f(3) is equal to 51!
```

## 💻 Türkçe İçin
Defne_llama3_2x8B, iki llama3 8B modelinin birleşmesi ile oluşturulan MoE yapısında bir modeldir.  

```python
!pip install -qU transformers bitsandbytes accelerate

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "Eurdem/Defne_llama3_2x8B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto", load_in_8bit= True)

messages = [{"role": "system", "content": "Sen, Defne isimli Türkçe konuşan bir chatbotsun."},
            {"role": "user", "content": "Soruları numaralandırarak cevapla. 1) Sen kimsin?  2)f(x)=3x^2+4x+12 ise f(3) kaçtır?"}
]

input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
outputs = model.generate(input_ids, max_new_tokens=1024, do_sample=True, temperature=0.7, top_p=0.7, top_k=500,)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))
```
### Çıktı
```
Merhaba!

1. Ben Defne, Türkçe konuşan bir chatbot.

2. f(x) = 3x^2 + 4x + 12 formülüne göre, f(3)'ü hesaplamak isterseniz, x'in değeri 3 olarak girelim:

f(3) = 3(3)^2 + 4(3) + 12
= 3(9) + 12 + 12
= 27 + 24
= 51

Bu nedenle, f(3) 51'dir.
```
