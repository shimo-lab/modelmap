
# Model Card for mncai/agiin-13.6B-v0.1

### Introduction of MindsAndCompany

https://mnc.ai/

We create various AI models and develop solutions that can be applied to businesses. And as for generative AI, we are developing products like Code Assistant, TOD Chatbot, LLMOps, and are in the process of developing Enterprise AGI (Artificial General Intelligence).

### Model Summary
This model was built based on the Mistral architecture. It was inspired by neural connection technology and rehabilitation therapy.
I have created a new model architecture that does not require pretraining, and training the model is sufficient with just one H100 for 7 hours.

### Data
Intel/orca_dpo_pairs (DPO) 

### Surgery and Training

stack mistral 62 layers and DPO.

### How to Use 

```python
message = [
    {"role": "system", "content": "You are a helpful assistant chatbot."},
    {"role": "user", "content": "두 개의 구가 각각 지름이 1, 2일때 두 구의 부피는 몇배지? 설명도 같이 해줘."}
]
tokenizer = AutoTokenizer.from_pretrained(hf_model)
prompt = tokenizer.apply_chat_template(message, add_generation_prompt=True, tokenize=False)

pipeline = transformers.pipeline(
    "text-generation",
    model=hf_model,
    tokenizer=tokenizer
)


sequences = pipeline(
    prompt,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    num_return_sequences=1,
    max_length=512,
)
print(sequences[0]['generated_text'])
```

### Contact 
If you have any questions, please raise an issue or contact us at dwmyoung@mnc.ai