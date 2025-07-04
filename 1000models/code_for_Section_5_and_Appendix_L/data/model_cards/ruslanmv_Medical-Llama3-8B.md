
# Medical-Llama3-8B-16bit: Fine-Tuned Llama3 for Medical Q&A
[![](future.jpg)](https://ruslanmv.com/)
This repository provides a fine-tuned version of the powerful Llama3 8B model, specifically designed to answer medical questions in an informative way. It leverages the rich knowledge contained in the AI Medical Chatbot dataset ([ruslanmv/ai-medical-chatbot](https://huggingface.co/datasets/ruslanmv/ai-medical-chatbot)).

**Model & Development**

- **Developed by:** ruslanmv
- **License:** Apache-2.0
- **Finetuned from model:** meta-llama/Meta-Llama-3-8B

**Key Features**

- **Medical Focus:** Optimized to address health-related inquiries.
- **Knowledge Base:** Trained on a comprehensive medical chatbot dataset.
- **Text Generation:** Generates informative and potentially helpful responses.

**Installation**

This model is accessible through the Hugging Face Transformers library. Install it using pip:

```bash
pip install transformers   bitsandbytes  accelerate
```

**Usage Example**

Here's a Python code snippet demonstrating how to interact with the `Medical-Llama3-8B-16bit` model and generate answers to your medical questions:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch
model_name = "ruslanmv/Medical-Llama3-8B"
device_map = 'auto'
bnb_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",bnb_4bit_compute_dtype=torch.float16,)
model = AutoModelForCausalLM.from_pretrained( model_name,quantization_config=bnb_config, trust_remote_code=True,use_cache=False,device_map=device_map)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

def askme(question):
    sys_message = ''' 
    You are an AI Medical Assistant trained on a vast dataset of health information. Please be thorough and
    provide an informative answer. If you don't know the answer to a specific medical inquiry, advise seeking professional help.
    '''   
    # Create messages structured for the chat template
    messages = [{"role": "system", "content": sys_message}, {"role": "user", "content": question}]
    
    # Applying chat template
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=100, use_cache=True)
    
    # Extract and return the generated text, removing the prompt
    response_text = tokenizer.batch_decode(outputs)[0].strip()
    answer = response_text.split('<|im_start|>assistant')[-1].strip()
    return answer
# Example usage
# - Context: First describe your problem.
# - Question: Then make the question.

question = '''I'm a 35-year-old male and for the past few months, I've been experiencing fatigue, 
increased sensitivity to cold, and dry, itchy skin. 
Could these symptoms be related to hypothyroidism? 
If so, what steps should I take to get a proper diagnosis and discuss treatment options?'''

print(askme(question))

```
the type of answer is :
```
Based on your description, it sounds like you may be experiencing symptoms of hypothyroidism. 
Hypothyroidism is a condition where the thyroid gland doesn't produce enough hormones, leading to a variety of symptoms. 
Some common symptoms include fatigue, weight gain, constipation, and dry skin. 
If you're experiencing any of these symptoms, it's important to see a doctor for a proper diagnosis and treatment plan. 
Your doctor may order blood tests to check your thyroid hormone levels
```
**Important Note**

This model is intended for informational purposes only and should not be used as a substitute for professional medical advice. Always consult with a qualified healthcare provider for any medical concerns.

**License**

This model is distributed under the Apache License 2.0 (see LICENSE file for details).

**Contributing**

We welcome contributions to this repository! If you have improvements or suggestions, feel free to create a pull request.

**Disclaimer**

While we strive to provide informative responses, the accuracy of the model's outputs cannot be guaranteed. It is crucial to consult a doctor or other healthcare professional for definitive medical advice.
```