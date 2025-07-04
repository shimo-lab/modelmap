
<p align="center">
<img width="500px" alt="DeepSeek Chat" src="https://github.com/deepseek-ai/DeepSeek-LLM/blob/main/images/logo.png?raw=true">
</p>
<p align="center"><a href="https://www.deepseek.com/">[🏠Homepage]</a>  |  <a href="https://chat.deepseek.com/">[🤖 Chat with DeepSeek LLM]</a>  |  <a href="https://discord.gg/Tc7c45Zzu5">[Discord]</a>  |  <a href="https://github.com/deepseek-ai/DeepSeek-LLM/blob/main/images/qr.jpeg">[Wechat(微信)]</a> </p>
<hr>




### 1. Introduction of Deepseek LLM

Introducing DeepSeek LLM, an advanced language model comprising 7 billion parameters. It has been trained from scratch on a vast dataset of 2 trillion tokens in both English and Chinese. In order to foster research, we have made DeepSeek LLM 7B/67B Base and DeepSeek LLM 7B/67B Chat open source for the research community.

  
### 2. Model Summary
`deepseek-llm-7b-chat` is a 7B parameter model initialized from `deepseek-llm-7b-base` and fine-tuned on extra instruction data.

- **Home Page:** [DeepSeek](https://deepseek.com/)
- **Repository:** [deepseek-ai/deepseek-LLM](https://github.com/deepseek-ai/deepseek-LLM)
- **Chat With DeepSeek LLM:** [DeepSeek-LLM](https://chat.deepseek.com/)


### 3. How to Use
Here give some examples of how to use our model.
#### Chat Completion
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig

model_name = "deepseek-ai/deepseek-llm-7b-chat"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="auto")
model.generation_config = GenerationConfig.from_pretrained(model_name)
model.generation_config.pad_token_id = model.generation_config.eos_token_id

messages = [
    {"role": "user", "content": "Who are you?"}
]
input_tensor = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
outputs = model.generate(input_tensor.to(model.device), max_new_tokens=100)

result = tokenizer.decode(outputs[0][input_tensor.shape[1]:], skip_special_tokens=True)
print(result)
```

Avoiding the use of the provided function `apply_chat_template`, you can also interact with our model following the sample template. Note that `messages` should be replaced by your input.

```
User: {messages[0]['content']}

Assistant: {messages[1]['content']}<｜end▁of▁sentence｜>User: {messages[2]['content']}

Assistant:
```

**Note:** By default (`add_special_tokens=True`), our tokenizer automatically adds a `bos_token` (`<｜begin▁of▁sentence｜>`) before the input text. Additionally, since the system prompt is not compatible with this version of our models, we DO NOT RECOMMEND including the system prompt in your input.

### 4. License
This code repository is licensed under the MIT License. The use of DeepSeek LLM models is subject to the Model License. DeepSeek LLM supports commercial use.

See the [LICENSE-MODEL](https://github.com/deepseek-ai/deepseek-LLM/blob/main/LICENSE-MODEL) for more details.

### 5. Contact

If you have any questions, please raise an issue or contact us at [service@deepseek.com](mailto:service@deepseek.com).

