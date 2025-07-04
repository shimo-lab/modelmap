
# MultiverseEx26-7B-slerp

MultiverseEx26-7B-slerp is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [yam-peleg/Experiment26-7B](https://huggingface.co/yam-peleg/Experiment26-7B)
* [MTSAIR/multi_verse_model](https://huggingface.co/MTSAIR/multi_verse_model)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: yam-peleg/Experiment26-7B
        layer_range: [0, 32]
      - model: MTSAIR/multi_verse_model
        layer_range: [0, 32]
merge_method: slerp
base_model: yam-peleg/Experiment26-7B
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "allknowingroger/MultiverseEx26-7B-slerp"
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