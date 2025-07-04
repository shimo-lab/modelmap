
# Faro-Yi-9B-DPO

This is the DPO version of [wenbopan/Faro-Yi-9B](https://huggingface.co/wenbopan/Faro-Yi-9B). Compared to Faro-Yi-9B and [Yi-9B-200K](https://huggingface.co/01-ai/Yi-9B-200K), the DPO model excels at many tasks, surpassing the original Yi-9B-200K by a large margin. On the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard), it ranks **#2** among all 9B models, **#1** among all Yi-9B variants.

| **Metric**              | **MMLU**  | **GSM8K** | **hellaswag** | **truthfulqa** | **ai2_arc** | **winogrande** | **CMMLU** |
| ----------------------- | --------- | --------- | ------------- | -------------- | ----------- | -------------- | --------- |
| **Yi-9B-200K**          | 65.73     | 50.49     | 56.72         | 33.80          | 69.25       | 71.67          | 71.97     |
| **Faro-Yi-9B**          | 68.80     | 63.08     | 57.28         | 40.86          | 72.58       | 71.11          | 73.28     |
| **Faro-Yi-9B-DPO**      | **69.98** | **66.11** | **59.04**     | **48.01**      | **75.68**   | **73.40**      | **75.23** |

Faro-Yi-9B-DPO's responses are also favored by GPT-4 Judge in MT-Bench

![image/png](https://cdn-uploads.huggingface.co/production/uploads/62cd3a3691d27e60db0698b0/ArlnloL4aPfiiD6kUqaSH.png)

## How to Use

Faro-Yi-9B-DPO uses the chatml template and performs well in both short and long contexts. For longer inputs under **24GB of VRAM**, I recommend to use vLLM to have a max prompt of 32K. Setting `kv_cache_dtype="fp8_e5m2"` allows for 48K input length. 4bit-AWQ quantization on top of that can boost input length to 160K, albeit with some performance impact. Adjust `max_model_len` arg in vLLM or `config.json` to avoid OOM.


```python
import io
import requests
from PyPDF2 import PdfReader
from vllm import LLM, SamplingParams

llm = LLM(model="wenbopan/Faro-Yi-9B-DPO", kv_cache_dtype="fp8_e5m2", max_model_len=100000)

pdf_data = io.BytesIO(requests.get("https://arxiv.org/pdf/2303.08774.pdf").content)
document = "".join(page.extract_text() for page in PdfReader(pdf_data).pages) # 100 pages

question = f"{document}\n\nAccording to the paper, what is the parameter count of GPT-4?"
messages = [ {"role": "user", "content": question} ] # 83K tokens
prompt = llm.get_tokenizer().apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
output = llm.generate(prompt, SamplingParams(temperature=0.8, max_tokens=500))
print(output[0].outputs[0].text)
# Yi-9B-200K:      175B. GPT-4 has 175B \nparameters. How many models were combined to create GPT-4? Answer: 6. ...
# Faro-Yi-9B: GPT-4 does not have a publicly disclosed parameter count due to the competitive landscape and safety implications of large-scale models like GPT-4. ...
```


<details> <summary>Or With Transformers</summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained('wenbopan/Faro-Yi-9B-DPO', device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained('wenbopan/Faro-Yi-9B-DPO')
messages = [
    {"role": "system", "content": "You are a helpful assistant. Always answer with a short response."},
    {"role": "user", "content": "Tell me what is Pythagorean theorem like you are a pirate."}
]

input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt").to(model.device)
generated_ids = model.generate(input_ids, max_new_tokens=512, temperature=0.5)
response = tokenizer.decode(generated_ids[0], skip_special_tokens=True) # Aye, matey! The Pythagorean theorem is a nautical rule that helps us find the length of the third side of a triangle. ...
```

</details>
