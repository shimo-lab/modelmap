
# llama3-8B-slerp-med-262k

llama3-8B-slerp-med-262k is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [gradientai/Llama-3-8B-Instruct-262k](https://huggingface.co/gradientai/Llama-3-8B-Instruct-262k)
* [johnsnowlabs/JSL-MedLlama-3-8B-v1.0](https://huggingface.co/johnsnowlabs/JSL-MedLlama-3-8B-v1.0)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: gradientai/Llama-3-8B-Instruct-262k
        layer_range: [0,32]
      - model: johnsnowlabs/JSL-MedLlama-3-8B-v1.0
        layer_range: [0,32]
merge_method: slerp
base_model: gradientai/Llama-3-8B-Instruct-262k
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

from transformers import AutoTokenizer
import transformers
import torch

model = "shanchen/llama3-8B-slerp-med-262k"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```