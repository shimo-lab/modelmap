
# NeuralSynthesis-7b-v0.4-slerp

NeuralSynthesis-7b-v0.4-slerp is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [allknowingroger/MultiverseEx26-7B-slerp](https://huggingface.co/allknowingroger/MultiverseEx26-7B-slerp)
* [Kukedlc/NeuralSynthesis-7B-v0.1](https://huggingface.co/Kukedlc/NeuralSynthesis-7B-v0.1)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: allknowingroger/MultiverseEx26-7B-slerp
        layer_range: [0, 32]
      - model: Kukedlc/NeuralSynthesis-7B-v0.1
        layer_range: [0, 32]
merge_method: slerp
base_model: Kukedlc/NeuralSynthesis-7B-v0.1
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

model = "Kukedlc/NeuralSynthesis-7b-v0.4-slerp"
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