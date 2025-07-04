
# llama3-8B-slerp-biomed-chat-chinese

llama3-8B-slerp-biomed-chat-chinese is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [shanchen/llama3-8B-slerp-med-chinese](https://huggingface.co/shanchen/llama3-8B-slerp-med-chinese)
* [shenzhi-wang/Llama3-8B-Chinese-Chat](https://huggingface.co/shenzhi-wang/Llama3-8B-Chinese-Chat)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: shanchen/llama3-8B-slerp-med-chinese
        layer_range: [0,32]
      - model: shenzhi-wang/Llama3-8B-Chinese-Chat
        layer_range: [0,32]
merge_method: slerp
base_model: shenzhi-wang/Llama3-8B-Chinese-Chat
parameters:
  t:
    - filter: self_attn
      value: [0.3, 0.5, 0.5, 0.7, 1]
    - filter: mlp
      value: [1, 0.7, 0.5, 0.5, 0.3]
    - value: 0.5
dtype: bfloat16
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "shanchen/llama3-8B-slerp-biomed-chat-chinese"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype="auto", device_map="auto"
)

messages = [
    {"role": "user", "content": "Can you speak Japanese?"},
]

input_ids = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

outputs = model.generate(
    input_ids,
    max_new_tokens=192 max#8192,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))

```