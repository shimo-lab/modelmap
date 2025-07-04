
### Medichat-Llama3-8B

Built upon the powerful LLaMa-3 architecture and fine-tuned on an extensive dataset of health information, this model leverages its vast medical knowledge to offer clear, comprehensive answers.

This model is generally better for accurate and informative responses, particularly for users seeking in-depth medical advice.


The following YAML configuration was used to produce this model:

```yaml

models:
  - model: Undi95/Llama-3-Unholy-8B
    parameters:
      weight: [0.25, 0.35, 0.45, 0.35, 0.25]
      density: [0.1, 0.25, 0.5, 0.25, 0.1]
  - model: Locutusque/llama-3-neural-chat-v1-8b
  - model: ruslanmv/Medical-Llama3-8B-16bit
    parameters:
      weight: [0.55, 0.45, 0.35, 0.45, 0.55]
      density: [0.1, 0.25, 0.5, 0.25, 0.1]
merge_method: dare_ties
base_model: Locutusque/llama-3-neural-chat-v1-8b
parameters:
  int8_mask: true
dtype: bfloat16

```

# Comparision Against Dr.Samantha 7B

| Subject                 | Medichat-Llama3-8B Accuracy (%) | Dr. Samantha Accuracy (%) |
|-------------------------|---------------------------------|---------------------------|
| Clinical Knowledge      | 71.70                           | 52.83                     |
| Medical Genetics        | 78.00                           | 49.00                     |
| Human Aging             | 70.40                           | 58.29                     |
| Human Sexuality         | 73.28                           | 55.73                     |
| College Medicine        | 62.43                           | 38.73                     |
| Anatomy                 | 64.44                           | 41.48                     |
| College Biology         | 72.22                           | 52.08                     |
| High School Biology     | 77.10                           | 53.23                     |
| Professional Medicine   | 63.97                           | 38.73                     |
| Nutrition               | 73.86                           | 50.33                     |
| Professional Psychology | 68.95                           | 46.57                     |
| Virology                | 54.22                           | 41.57                     |
| High School Psychology  | 83.67                           | 66.60                     |
| **Average**             | **70.33**                       | **48.85**                 |


The current model demonstrates a substantial improvement over the previous [Dr. Samantha](sethuiyer/Dr_Samantha-7b) model in terms of subject-specific knowledge and accuracy.

### Usage:
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class MedicalAssistant:
    def __init__(self, model_name="sethuiyer/Medichat-Llama3-8B", device="cuda"):
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
        self.sys_message = ''' 
        You are an AI Medical Assistant trained on a vast dataset of health information. Please be thorough and
        provide an informative answer. If you don't know the answer to a specific medical inquiry, advise seeking professional help.
        '''

    def format_prompt(self, question):
        messages = [
            {"role": "system", "content": self.sys_message},
            {"role": "user", "content": question}
        ]
        prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        return prompt

    def generate_response(self, question, max_new_tokens=512):
        prompt = self.format_prompt(question)
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_new_tokens=max_new_tokens, use_cache=True)
        answer = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0].strip()
        return answer

if __name__ == "__main__":
    assistant = MedicalAssistant()
    question = '''
    Symptoms:
    Dizziness, headache, and nausea.

    What is the differential diagnosis?
    '''
    response = assistant.generate_response(question)
    print(response)

```

## Quants
Thanks to [Quant Factory](https://huggingface.co/QuantFactory), the quantized version of this model is available at [QuantFactory/Medichat-Llama3-8B-GGUF](https://huggingface.co/QuantFactory/Medichat-Llama3-8B-GGUF),


## Ollama
This model is now also available on Ollama. You can use it by running the command ```ollama run monotykamary/medichat-llama3``` in your 
terminal. If you have limited computing resources, check out this [video](https://www.youtube.com/watch?v=Qa1h7ygwQq8) to learn how to run it on 
a Google Colab backend.