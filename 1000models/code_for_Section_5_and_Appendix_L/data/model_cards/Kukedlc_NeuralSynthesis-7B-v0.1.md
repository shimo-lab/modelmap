
# NeuralSynthesis-7B-v0.1


![image/png](https://cdn-uploads.huggingface.co/production/uploads/64d71ab4089bc502ceb44d29/eeH_75Yk5mq29FADx1TJk.png)

 
NeuralSynthesis-7B-v0.1 is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):

## 🧩 Configuration

```yaml
models:
  - model: MiniMoog/Mergerix-7b-v0.3
  - model: automerger/Ognoexperiment27Multi_verse_model-7B
  - model: AurelPx/Percival_01-7b-slerp
  - model: automerger/YamshadowExperiment28-7B
merge_method: model_stock
base_model: automerger/YamshadowExperiment28-7B
dtype: bfloat16

```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "Kukedlc/NeuralSynthesis-7B-v0.1"
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
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Kukedlc__NeuralSynthesis-7B-v0.1)


|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |76.80|
|AI2 Reasoning Challenge (25-Shot)|73.04|
|HellaSwag (10-Shot)              |89.18|
|MMLU (5-Shot)                    |64.37|
|TruthfulQA (0-shot)              |78.15|
|Winogrande (5-shot)              |85.24|
|GSM8k (5-shot)                   |70.81|