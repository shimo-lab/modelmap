

# Instruct_Yi-6B_Dolly15K
Fine-tuned from Yi-6B， used Dolly15k for the dataset. 90% for training, 10% validation.  Trained for 2.0 epochs using Lora.  Trained with 2048 context window. Compared with https://huggingface.co/HenryJJ/Instruct_Yi-6B_Dolly15K, I add additional CodeAlpaca_20K dataset that good at coding.

# Model Details
* **Trained by**: trained by HenryJJ.
* **Model type:**  **Instruct_Yi-6B_Dolly15K** is an auto-regressive language model based on the Llama 2 transformer architecture.
* **Language(s)**: English
* **License for Instruct_Yi-6B_Dolly15K**: apache-2.0 license


# Prompting

## Prompt Template With Context
<|startoftext|>[INST]{instruction} {context}[/INST]{response}<|endoftext|>

```
<|startoftext|>[INST]
Write a 10-line poem about a given topic
The topic is about racecars
[/INST]
```
## Prompt Template Without Context
```
<|startoftext|>[INST]
Who was the was the second president of the United States?
[/INST]
```

# Training script:
Fully opensourced at: https://github.com/hengjiUSTC/learn-llm/blob/main/trl_finetune.py. Run on aws g4dn.12xlarge instance for 10 hours.

```
python3 trl_finetune.py --config configs/yi_6b-large.yml
```