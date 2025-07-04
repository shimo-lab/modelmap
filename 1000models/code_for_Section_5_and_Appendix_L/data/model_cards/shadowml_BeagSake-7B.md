
# BeagSake-7B

BeagSake-7B is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [shadowml/BeagleSempra-7B](https://huggingface.co/shadowml/BeagleSempra-7B)
* [shadowml/WestBeagle-7B](https://huggingface.co/shadowml/WestBeagle-7B)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: shadowml/BeagleSempra-7B
        layer_range: [0, 32]
      - model: shadowml/WestBeagle-7B
        layer_range: [0, 32]
merge_method: slerp
base_model: shadowml/BeagleSempra-7B
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

model = "shadowml/BeagSake-7B"
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
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_shadowml__BeagSake-7B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |75.38|
|AI2 Reasoning Challenge (25-Shot)|72.44|
|HellaSwag (10-Shot)              |88.39|
|MMLU (5-Shot)                    |65.23|
|TruthfulQA (0-shot)              |72.27|
|Winogrande (5-shot)              |82.16|
|GSM8k (5-shot)                   |71.80|

