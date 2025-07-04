
![image/webp](https://cdn-uploads.huggingface.co/production/uploads/62cd3a3691d27e60db0698b0/s21sMRxRT56c5t4M15GBP.webp)

**The Faro chat model focuses on practicality and long-context modeling. It handles various downstream tasks with higher quality, delivering stable and reliable results even when inputs contain lengthy documents or complex instructions. Faro seamlessly works in both English and Chinese.**

# Faro-Yi-9B
Faro-Yi-9B is an improved [Yi-9B-200K](https://huggingface.co/01-ai/Yi-9B-200K) with extensive instruction tuning on [Fusang-V1](https://huggingface.co/datasets/wenbopan/Fusang-v1). Compared to Yi-9B-200K, Faro-Yi-9B has gained greater capability in various downstream tasks and long-context modeling thanks to the large-scale synthetic data in Fusang-V1.

Just like Yi-9B-200K, Faro-Yi-9B supports up to 200K context length. 

## How to Use

Faro-Yi-9B uses the chatml template and performs well in both short and long contexts. For longer inputs under **24GB of VRAM**, I recommend to use vLLM to have a max prompt of 32K. Setting `kv_cache_dtype="fp8_e5m2"` allows for 48K input length. 4bit-AWQ quantization on top of that can boost input length to 160K, albeit with some performance impact. Adjust `max_model_len` arg in vLLM or `config.json` to avoid OOM.


```python
import io
import requests
from PyPDF2 import PdfReader
from vllm import LLM, SamplingParams

llm = LLM(model="wenbopan/Faro-Yi-9B", kv_cache_dtype="fp8_e5m2", max_model_len=100000)

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

model = AutoModelForCausalLM.from_pretrained('wenbopan/Faro-Yi-9B', device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained('wenbopan/Faro-Yi-9B')
messages = [
    {"role": "system", "content": "You are a helpful assistant. Always answer with a short response."},
    {"role": "user", "content": "Tell me what is Pythagorean theorem like you are a pirate."}
]

input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt").to(model.device)
generated_ids = model.generate(input_ids, max_new_tokens=512, temperature=0.5)
response = tokenizer.decode(generated_ids[0], skip_special_tokens=True) # Aye, matey! The Pythagorean theorem is a nautical rule that helps us find the length of the third side of a triangle. ...
```

</details>

## Performance

Faro-Yi-9B enhances its ability compared to Yi-9B-200K in most dimensions, especially in long-range modeling and bilingual (English, Chinese) understanding. Faro is competitive among all open-sourced models at around 9B parameters.

<details> <summary>Benchmark Results</summary>

### Fact-based Evaluation (Open LLM Leaderboard)

| **Metric**     | **MMLU**  | **GSM8K** | **HellaSwag** | **TruthfulQA** | **Arc** | **Winogrande** |
| -------------- | --------- | --------- | ------------- | -------------- | ----------- | -------------- |
| **Yi-9B-200K** | 65.73     | 50.49     | 56.72         | 33.80          | 69.25       | 71.67          |
| **Faro-Yi-9B** | **68.80** | **63.08** | **57.28**     | **40.86**      | **72.58**   | 71.11          |

### Long-context Modeling ([LongBench](https://github.com/THUDM/LongBench))

| **Name**       | **Average_zh** | **Average_en** | **Code Completion** |
|----------------|----------------|----------------|---------------------|
| **Yi-9B-200K** | 30.288         | 36.7071        | 72.2                |
| **Faro-Yi-9B** | **41.092**     | **40.9536**    | 46.0                |

<details>
<summary>Score breakdown</summary>

| **Name**       | **Few-shot Learning_en** | **Synthetic Tasks_en** | **Single-Doc QA_en** | **Multi-Doc QA_en** | **Summarization_en** | **Few-shot Learning_zh** | **Synthetic Tasks_zh** | **Single-Doc QA_zh** | **Multi-Doc QA_zh** | **Summarization_zh** |
|----------------|--------------------------|------------------------|----------------------|---------------------|----------------------|--------------------------|------------------------|----------------------|---------------------|----------------------|
| **Yi-9B-200K** | 60.6                     | 22.8                   | 30.9                 | 38.9                | 25.8                 | 46.5                     | 28.0                   | 49.6                 | 17.7                | 9.7                  |
| **Faro-Yi-9B** | **63.8**                 | **40.2**               | **36.2**             | 38.0                | **26.3**             | 30.0                     | **75.1**               | **55.6**             | **30.7**            | **14.1**             |

</details>

### Performance on Preference (MT-Bench)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/62cd3a3691d27e60db0698b0/M0Kc64sIsbNyCCvrRk1Lv.png)

### Bilingual Ability (CMMLU & MMLU)

| **Name**       | MMLU      | **CMMLU** |
| -------------- | --------- | --------- |
| **Yi-9B-200K** | 65.73     | 71.97     |
| **Faro-Yi-9B** | **68.80** | **73.28** |

</details>