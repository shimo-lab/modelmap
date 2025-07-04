
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->
Mistral-7B-v0.2-meditron-turkish is a finetuned Mistral Model version using Freeze technique on Turkish Meditron dataset of [`malhajar/meditron-7b-tr`](https://huggingface.co/datasets/malhajar/meditron-tr) using SFT Training.
This model can answer information about different excplicit ideas in medicine in Turkish and English

### Model Description

- **Finetuned by:** [`Mohamad Alhajar`](https://www.linkedin.com/in/muhammet-alhajar/) 
- **Language(s) (NLP):** Turkish,English
- **Finetuned from model:** [`mistralai/Mistral-7B-Instruct-v0.2`](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)

### Prompt Template For Turkish Generation
```
### Kullancı:
```
### Prompt Template For English Generation
```
### User:
```

## How to Get Started with the Model

Use the code sample provided in the original post to interact with the model.
```python
from transformers import AutoTokenizer,AutoModelForCausalLM
 
model_id = "malhajar/Mistral-7B-v0.2-meditron-turkish"
model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                             device_map="auto",
                                             torch_dtype=torch.float16,
                                             revision="main")

tokenizer = AutoTokenizer.from_pretrained(model_id)

question: "Akciğer kanseri nedir?"
# For generating a response
prompt = '''
### Kullancı:
{question} 
'''
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
output = model.generate(inputs=input_ids,max_new_tokens=512,pad_token_id=tokenizer.eos_token_id,top_k=50, do_sample=True,
        top_p=0.95)
response = tokenizer.decode(output[0])

print(response)
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_malhajar__Mistral-7B-v0.2-meditron-turkish)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |63.34|
|AI2 Reasoning Challenge (25-Shot)|59.56|
|HellaSwag (10-Shot)              |81.79|
|MMLU (5-Shot)                    |60.35|
|TruthfulQA (0-shot)              |66.19|
|Winogrande (5-shot)              |76.24|
|GSM8k (5-shot)                   |35.94|

