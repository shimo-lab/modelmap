
<p align="center">
<img width="1000px" alt="DeepSeek Coder" src="https://github.com/deepseek-ai/DeepSeek-Coder/blob/main/pictures/logo.png?raw=true">
</p>
<p align="center"><a href="https://www.deepseek.com/">[🏠Homepage]</a>  |  <a href="https://coder.deepseek.com/">[🤖 Chat with DeepSeek Coder]</a>  |  <a href="https://discord.gg/Tc7c45Zzu5">[Discord]</a>  |  <a href="https://github.com/guoday/assert/blob/main/QR.png?raw=true">[Wechat(微信)]</a> </p>
<hr>



### 1. Introduction of Deepseek Coder

Deepseek Coder is composed of a series of code language models, each trained from scratch on 2T tokens, with a composition of 87% code and 13% natural language in both English and Chinese. We provide various sizes of the code model, ranging from 1B to 33B versions. Each model is pre-trained on project-level code corpus by employing a window size of 16K and a extra fill-in-the-blank task, to support  project-level code completion and infilling. For coding capabilities, Deepseek Coder achieves state-of-the-art performance among open-source code models on multiple programming languages and various benchmarks. 

- **Massive Training Data**: Trained from scratch on 2T tokens, including 87% code and 13% linguistic data in both English and Chinese languages.
  
- **Highly Flexible & Scalable**: Offered in model sizes of 1.3B, 5.7B, 6.7B, and 33B, enabling users to choose the setup most suitable for their requirements.
  
- **Superior Model Performance**: State-of-the-art performance among publicly available code models on HumanEval, MultiPL-E, MBPP, DS-1000, and APPS benchmarks.
  
- **Advanced Code Completion Capabilities**: A window size of 16K and a fill-in-the-blank task, supporting project-level code completion and infilling tasks.

 
  
### 2. Model Summary
deepseek-coder-1.3b-instruct is a 1.3B parameter model initialized from deepseek-coder-1.3b-base and fine-tuned on 2B tokens of instruction data.
- **Home Page:** [DeepSeek](https://deepseek.com/)
- **Repository:** [deepseek-ai/deepseek-coder](https://github.com/deepseek-ai/deepseek-coder)
- **Chat With DeepSeek Coder:** [DeepSeek-Coder](https://coder.deepseek.com/)


### 3. How to Use
Here give some examples of how to use our model.
#### Chat Model Inference
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct", trust_remote_code=True, torch_dtype=torch.bfloat16).cuda()
messages=[
    { 'role': 'user', 'content': "write a quick sort algorithm in python."}
]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
# tokenizer.eos_token_id is the id of <|EOT|> token
outputs = model.generate(inputs, max_new_tokens=512, do_sample=False, top_k=50, top_p=0.95, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True))
```

### 4. License
This code repository is licensed under the MIT License. The use of DeepSeek Coder models is subject to the Model License. DeepSeek Coder supports commercial use.

See the [LICENSE-MODEL](https://github.com/deepseek-ai/deepseek-coder/blob/main/LICENSE-MODEL) for more details.

### 5. Contact

If you have any questions, please raise an issue or contact us at [agi_code@deepseek.com](mailto:agi_code@deepseek.com).

