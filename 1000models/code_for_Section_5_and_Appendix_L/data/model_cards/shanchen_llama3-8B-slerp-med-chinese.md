
# llama3-8B-slerp-med-chinese

llama3-8B-slerp-med-chinese is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [winninghealth/WiNGPT2-Llama-3-8B-Base](https://huggingface.co/winninghealth/WiNGPT2-Llama-3-8B-Base)
* [johnsnowlabs/JSL-MedLlama-3-8B-v1.0](https://huggingface.co/johnsnowlabs/JSL-MedLlama-3-8B-v1.0)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: winninghealth/WiNGPT2-Llama-3-8B-Base
        layer_range: [0,32]
      - model: johnsnowlabs/JSL-MedLlama-3-8B-v1.0
        layer_range: [0,32]
merge_method: slerp
base_model: winninghealth/WiNGPT2-Llama-3-8B-Base
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.5, 0.5, 1]
    - filter: mlp
      value: [1, 0.5, 0.5, 0.5, 0]
    - value: 0.5
dtype: bfloat16
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "shanchen/llama3-8B-slerp-med-chinese"
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