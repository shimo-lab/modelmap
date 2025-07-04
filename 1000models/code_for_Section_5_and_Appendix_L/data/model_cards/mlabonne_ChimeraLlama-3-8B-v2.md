
# ChimeraLlama-3-8B-v2

ChimeraLlama-3-8B-v2 is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [NousResearch/Meta-Llama-3-8B-Instruct](https://huggingface.co/NousResearch/Meta-Llama-3-8B-Instruct)
* [mlabonne/OrpoLlama-3-8B](https://huggingface.co/mlabonne/OrpoLlama-3-8B)
* [cognitivecomputations/dolphin-2.9-llama3-8b](https://huggingface.co/cognitivecomputations/dolphin-2.9-llama3-8b)
* [Locutusque/llama-3-neural-chat-v1-8b](https://huggingface.co/Locutusque/llama-3-neural-chat-v1-8b)
* [cloudyu/Meta-Llama-3-8B-Instruct-DPO](https://huggingface.co/cloudyu/Meta-Llama-3-8B-Instruct-DPO)
* [vicgalle/Configurable-Llama-3-8B-v0.3](https://huggingface.co/vicgalle/Configurable-Llama-3-8B-v0.3)

## 🧩 Configuration

```yaml
models:
  - model: NousResearch/Meta-Llama-3-8B
    # No parameters necessary for base model
  - model: NousResearch/Meta-Llama-3-8B-Instruct
    parameters:
      density: 0.6
      weight: 0.55
  - model: mlabonne/OrpoLlama-3-8B
    parameters:
      density: 0.55
      weight: 0.05
  - model: cognitivecomputations/dolphin-2.9-llama3-8b
    parameters:
      density: 0.55
      weight: 0.1
  - model: Locutusque/llama-3-neural-chat-v1-8b
    parameters:
      density: 0.55
      weight: 0.05
  - model: cloudyu/Meta-Llama-3-8B-Instruct-DPO
    parameters:
      density: 0.55
      weight: 0.15
  - model: vicgalle/Configurable-Llama-3-8B-v0.3
    parameters:
      density: 0.55
      weight: 0.1
merge_method: dare_ties
base_model: NousResearch/Meta-Llama-3-8B
parameters:
  int8_mask: true
dtype: float16
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "mlabonne/ChimeraLlama-3-8B-v2"
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
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_mlabonne__ChimeraLlama-3-8B-v2)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |19.99|
|IFEval (0-Shot)    |44.69|
|BBH (3-Shot)       |28.48|
|MATH Lvl 5 (4-Shot)| 8.31|
|GPQA (0-shot)      | 4.70|
|MuSR (0-shot)      | 5.25|
|MMLU-PRO (5-shot)  |28.54|

