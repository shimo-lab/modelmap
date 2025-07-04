
# SJ-Donald/SJ-SOLAR-10.7b-DPO

SJ-Donald/SJ-SOLAR-10.7b-DPO is fine-tuned using DPO method.

## Environment

Using **Google CoLab A100**

## Base model

* [SJ-Donald/SOLAR-10.7B-slerp](https://huggingface.co/SJ-Donald/SOLAR-10.7B-slerp)

## Datasets

* [SJ-Donald/orca-dpo-pairs-ko](https://huggingface.co/datasets/SJ-Donald/orca-dpo-pairs-ko)

## Benchmark

### Open-LLM-Leaderboard(https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

| Average |   ARC  |   HellaSwag  |   MMLU  |  TruthfulQA  | Winogrande |  GSM8K  |
| ------: | -----: | -----------: | ------: | -----------: | ---------: | ------: | 
|   72.67 |  68.26 |        86.95 |   66.73 |        67.74 |      84.21 |   62.03 |

### open-ko-llm-leaderboard(https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard)

| Average | Ko-ARC | Ko-HellaSwag | Ko-MMLU | Ko-TruthfulQA | Ko-CommonGen V2 |
| ------: | -----: | -----------: | ------: | ------------: | --------------: |
|   56.93 |  53.67 |        61.99 |   53.36 |          57.2 |           58.44 |

## How to use

```Python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = 'SJ-Donald/SJ-SOLAR-10.7b-DPO'

tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(
    repo,
    return_dict=True,
    torch_dtype=torch.float16,
    device_map='auto'
)
```

## Chat Template

```Python
template = """### System:
{{system_content}}

### User:
{{question}}

### Assistant:
"""
```

## GGUF Version

You can use gguf model file here! -> [SJ-Donald/SJ-SOLAR-10.7b-DPO-GGUF](https://huggingface.co/SJ-Donald/SJ-SOLAR-10.7b-DPO-GGUF)
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_SJ-Donald__SJ-SOLAR-10.7b-DPO)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |72.67|
|AI2 Reasoning Challenge (25-Shot)|68.26|
|HellaSwag (10-Shot)              |86.95|
|MMLU (5-Shot)                    |66.73|
|TruthfulQA (0-shot)              |67.74|
|Winogrande (5-shot)              |84.21|
|GSM8k (5-shot)                   |62.09|

