
# CatMarcoro14-7B-slerp

CatMarcoro14-7B-slerp is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [cookinai/CatMacaroni-Slerp](https://huggingface.co/cookinai/CatMacaroni-Slerp)
* [EmbeddedLLM/Mistral-7B-Merge-14-v0.2](https://huggingface.co/EmbeddedLLM/Mistral-7B-Merge-14-v0.2)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: cookinai/CatMacaroni-Slerp
        layer_range: [0, 32]
      - model: EmbeddedLLM/Mistral-7B-Merge-14-v0.2
        layer_range: [0, 32]
merge_method: slerp
base_model: cookinai/CatMacaroni-Slerp
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

model = "occultml/CatMarcoro14-7B-slerp"
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
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_occultml__CatMarcoro14-7B-slerp)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |73.25|
|AI2 Reasoning Challenge (25-Shot)|69.37|
|HellaSwag (10-Shot)              |86.92|
|MMLU (5-Shot)                    |65.27|
|TruthfulQA (0-shot)              |63.24|
|Winogrande (5-shot)              |81.69|
|GSM8k (5-shot)                   |73.01|

