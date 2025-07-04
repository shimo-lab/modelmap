# INSAIT-Institute/BgGPT-7B-Instruct-v0.2

![image/png](https://cdn-uploads.huggingface.co/production/uploads/637e1f8cf7e01589cc17bf7e/p6d0YFHjWCQ3S12jWqO1m.png)

Meet BgGPT-7B, a Bulgarian language model trained from mistralai/Mistral-7B-v0.1. BgGPT is distributed under Apache 2.0 license.

This model was created by [`INSAIT Institute`](https://insait.ai/), part of Sofia University, in Sofia, Bulgaria.

This is an improved version of the model - v0.2.

## Model description

The model is continously pretrained to gain its Bulgarian language and culture capabilities using multiple datasets, including Bulgarian web crawl data, a range of specialized Bulgarian datasets sourced by INSAIT Institute, and machine translations of popular English datasets. 
This Bulgarian data was augmented with English datasets to retain English and logical reasoning skills.

The model's tokenizer has been extended to allow for a more efficient encoding of Bulgarian words written in Cyrillic. 
This not only increases throughput of Cyrillic text but also performance. 

## Instruction format

In order to leverage instruction fine-tuning, your prompt should be surrounded by `[INST]` and `[/INST]` tokens. 
The very first instruction should begin with a begin of sequence token `<s>`. Following instructions should not. 
The assistant generation will be ended by the end-of-sequence token.

E.g.
```
text = "<s>[INST] Кога е основан Софийският университет? [/INST]"
"Софийският университет „Св. Климент Охридски“ е създаден на 1 октомври 1888 г.</s> "
"[INST] Кой го е основал? [/INST]"
```

This format is available as a [chat template](https://huggingface.co/docs/transformers/main/chat_templating) via the `apply_chat_template()` method:

## Benchmarks

The model comes with a set of Benchmarks that are translations of the corresponding English-benchmarks. These are provided at [`https://github.com/insait-institute/lm-evaluation-harness-bg`](https://github.com/insait-institute/lm-evaluation-harness-bg)

As this is an improved version over version 0.1 of the same model and we include benchmark comparisons.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/637e1f8cf7e01589cc17bf7e/aZAEv5qyLcPn5p4KrHpEw.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/637e1f8cf7e01589cc17bf7e/6PafMC6StfUaPY1N8Xrta.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/637e1f8cf7e01589cc17bf7e/L1bKXq4Xiik1ZbTDuCnxj.png)

## Summary
- **Finetuned from:** [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)
- **Model type:** Causal decoder-only transformer language model
- **Language:** Bulgarian and English
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)
- **Contact:** [bggpt@insait.ai](mailto:bggpt@insait.ai)

## Use in 🤗Transformers
First install direct dependencies:
```
pip install transformers torch accelerate
```
If you want faster inference using flash-attention2, you need to install these dependencies:
```bash
pip install packaging ninja
pip install flash-attn
```
Then load the model in transformers:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
model = AutoModelForCausalLM.from_pretrained(
    model="INSAIT-Institute/BgGPT-7B-Instruct-v0.2",
    device_map="auto",
    torch_dtype=torch.bfloat16,
    use_flash_attn_2=True # optional
)
```

## Use with GGML / llama.cpp

The model in GGUF format [INSAIT-Institute/BgGPT-7B-Instruct-v0.2-GGUF](https://huggingface.co/INSAIT-Institute/BgGPT-7B-Instruct-v0.2-GGUF)
