
# **SOLAR-tail-10.7B-Merge-v1.0**  

## Model Details

**Model Developers** Kyujin Han (kyujinpy)

**Method**  
Using [Mergekit](https://github.com/cg123/mergekit).  
- [upstage/SOLAR-10.7B-v1.0](https://huggingface.co/upstage/SOLAR-10.7B-v1.0)  
- [Yhyu13/LMCocktail-10.7B-v1](Yhyu13/LMCocktail-10.7B-v1)  

**Merge config**
```
slices:
  - sources:
      - model: upstage/SOLAR-10.7B-v1.0
        layer_range: [0, 48]
      - model: Yhyu13/LMCocktail-10.7B-v1
        layer_range: [0, 48]
        
merge_method: slerp
base_model: upstage/SOLAR-10.7B-v1.0

parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
tokenizer_source: union
    
dtype: float16
```
  
# **Model Benchmark**  

## Open Ko leaderboard
- Follow up as [Ko-link](https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard).  

| Model | Average | ARC | HellaSwag | MMLU | TruthfulQA | Ko-CommonGenV2 |
| --- | --- | --- | --- | --- | --- | --- | 
| PracticeLLM/SOLAR-tail-10.7B-Merge-v1.0 | 48.32 | 45.73 | 56.97 | 38.77 | 38.75 | 61.16 |
| jjourney1125/M-SOLAR-10.7B-v1.0 | 55.15 | 49.57 | 60.12 | 54.60 | 49.23 | 62.22 |

- Follow up as [En-link](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard).  
| Model | Average | ARC | HellaSwag | MMLU | TruthfulQA | Winogrande | GSM8K |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| PracticeLLM/SOLAR-tail-10.7B-Merge-v1.0 | 71.68 | 66.13 | 86.54 | **66.52** | 60.57 | **84.77** | **65.58** |
| kyujinpy/Sakura-SOLAR-Instruct | **74.40** | **70.99** | **88.42** | 66.33 | **71.79** | 83.66 | 65.20 |


## lm-evaluation-harness
```
gpt2 (pretrained=PracticeLLM/SOLAR-tail-10.7B-Merge-v1.0), limit: None, provide_description: False, num_fewshot: 0, batch_size: None
|      Task      |Version| Metric |Value |   |Stderr|
|----------------|------:|--------|-----:|---|-----:|
|kobest_boolq    |      0|acc     |0.5021|±  |0.0133|
|                |       |macro_f1|0.3343|±  |0.0059|
|kobest_copa     |      0|acc     |0.6220|±  |0.0153|
|                |       |macro_f1|0.6217|±  |0.0154|
|kobest_hellaswag|      0|acc     |0.4380|±  |0.0222|
|                |       |acc_norm|0.5380|±  |0.0223|
|                |       |macro_f1|0.4366|±  |0.0222|
|kobest_sentineg |      0|acc     |0.4962|±  |0.0251|
|                |       |macro_f1|0.3316|±  |0.0113|
```
   
    
# Implementation Code
```python
### KO-Platypus
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

repo = "PracticeLLM/SOLAR-tail-10.7B-Merge-v1.0"
OpenOrca = AutoModelForCausalLM.from_pretrained(
        repo,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map='auto'
)
OpenOrca_tokenizer = AutoTokenizer.from_pretrained(repo)
```

---
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_PracticeLLM__SOLAR-tail-10.7B-Merge-v1.0)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |71.68|
|AI2 Reasoning Challenge (25-Shot)|66.13|
|HellaSwag (10-Shot)              |86.54|
|MMLU (5-Shot)                    |66.52|
|TruthfulQA (0-shot)              |60.57|
|Winogrande (5-shot)              |84.77|
|GSM8k (5-shot)                   |65.58|

