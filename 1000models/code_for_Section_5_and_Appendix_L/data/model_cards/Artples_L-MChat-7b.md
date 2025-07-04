
# L-MChat-7b

<div style="text-align:center;width:250px;height:250px;">
    <img src="https://priority.cdn.leunos.com/logo-l-mchat-rs.png" alt="L-MChat-Series-Logo"">
</div>

L-MChat-7b is a merge of the following models:
* [Nexusflow/Starling-LM-7B-beta](https://huggingface.co/Nexusflow/Starling-LM-7B-beta)
* [FuseAI/FuseChat-7B-VaRM](https://huggingface.co/FuseAI/FuseChat-7B-VaRM)

## Configuration

```yaml
slices:
  - sources:
      - model: Nexusflow/Starling-LM-7B-beta
        layer_range: [0, 32]
      - model: FuseAI/FuseChat-7B-VaRM
        layer_range: [0, 32]
merge_method: slerp
base_model: FuseAI/FuseChat-7B-VaRM
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
```

## Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "Artples/M-LChat-7b"
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

## License

Apache 2.0 but you cannot use this model to directly compete with OpenAI.

## How?

Usage of [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing).

## [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Artples__L-MChat-7b)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |69.57|
|AI2 Reasoning Challenge (25-Shot)|65.61|
|HellaSwag (10-Shot)              |84.59|
|MMLU (5-Shot)                    |65.44|
|TruthfulQA (0-shot)              |50.94|
|Winogrande (5-shot)              |81.37|
|GSM8k (5-shot)                   |69.45|


# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Artples__L-MChat-7b)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |21.02|
|IFEval (0-Shot)    |52.97|
|BBH (3-Shot)       |24.20|
|MATH Lvl 5 (4-Shot)| 7.93|
|GPQA (0-shot)      | 7.38|
|MuSR (0-shot)      | 8.12|
|MMLU-PRO (5-shot)  |25.54|

