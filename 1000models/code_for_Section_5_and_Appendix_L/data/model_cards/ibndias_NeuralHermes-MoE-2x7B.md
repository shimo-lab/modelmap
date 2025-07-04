
# NeuralHermes-MoE-2x7B

This is a mix between teknium/OpenHermes-2.5-Mistral-7B and Intel/neural-chat-7b-v3-3.
Using mistralai/Mistral-7B-v0.1 as the base model.

This Mixture of Expert was done using `mergekit` method.

# Getting Started

```python
import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="ibndias/NeuralHermes-MoE-2x7B",torch_dtype=torch.bfloat16, device_map="auto")

prompt = """<|system|> You are a helpful assistant.
<|user|>
Write me bash script to scan ip 192.3.1.4 with nmap only port that ends with 9 from 1-100.
<|assistant|>
"""
outputs = pipe(prompt, max_new_tokens=512, do_sample=True, temperature=0.2, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```

Output:
><|system|> You are a helpful assistant.
><|user|>
>Write me bash script to scan ip 192.3.1.4 with nmap only port that ends with 9 from 1-100.
><|assistant|>
>Sure, here's a bash script that scans the specified IP address with nmap for open ports that end with 9 from 1 to 100:
>```
>#!/bin/bash
>IP_ADDRESS="192.3.1.4"
>START_PORT=1
>END_PORT=100
>for ((i=$START_PORT; i<=$END_PORT; i++)); do
>    PORT=$i
>    if [[ $PORT % 10 == 9 ]]; then
>        nmap -p $PORT $IP_ADDRESS
>    fi
>done
>```
>Save the script with a.sh extension (e.g., scan_ports.sh) and make it executable by running `chmod +x scan_ports.sh`. Then, run the script by executing `./scan_ports.sh`.
>...
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ibndias__NeuralHermes-MoE-2x7B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |64.08|
|AI2 Reasoning Challenge (25-Shot)|62.12|
|HellaSwag (10-Shot)              |84.21|
|MMLU (5-Shot)                    |64.56|
|TruthfulQA (0-shot)              |43.61|
|Winogrande (5-shot)              |78.14|
|GSM8k (5-shot)                   |51.86|

