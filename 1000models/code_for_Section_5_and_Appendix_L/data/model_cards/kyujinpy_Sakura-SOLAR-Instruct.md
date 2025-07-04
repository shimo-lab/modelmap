
# **Sakura-SOLAR-Instruct**  
<img src='./sakura.png' width=512>
  
**(주)미디어그룹사람과숲과 (주)마커의 LLM 연구 컨소시엄에서 개발된 모델입니다**

## Model Details

**Model Developers** Kyujin Han (kyujinpy)

**Method**  
Using [Mergekit](https://github.com/cg123/mergekit).  
I shared the information about my model. (training and code)  
**Please see: [⭐Sakura-SOLAR](https://github.com/KyujinHan/Sakura-SOLAR-DPO).**  

**Blog**
- [Sakura-SOLAR 모델 제작 과정 및 후기](https://kyujinpy.tistory.com/122).   

# **Model Benchmark**  

## Open leaderboard
- Follow up as [link](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard).  

| Model | Average | ARC | HellaSwag | MMLU | TruthfulQA | Winogrande | GSM8K |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sakura-SOLRCA-Instruct-DPO | 74.05 | 71.16 | 88.49 | 66.17 | 72.10 | 82.95 | 63.46 |
| Sakura-SOLAR-Instruct-DPO-v2 | 74.14 | 70.90 | 88.41 | 66.48 | 71.86 | 83.43 | 63.76 |
| [kyujinpy/Sakura-SOLAR-Instruct](https://huggingface.co/kyujinpy/Sakura-SOLAR-Instruct) | 74.40 | 70.99 | 88.42 | 66.33 | 71.79 | 83.66 | 65.20
> Rank1 2023.12.27 PM 11:50

   
# Implementation Code
```python
### KO-Platypus
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

repo = "kyujinpy/Sakura-SOLAR-Instruct"
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
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_kyujinpy__Sakura-SOLAR-Instruct)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |74.40|
|AI2 Reasoning Challenge (25-Shot)|70.99|
|HellaSwag (10-Shot)              |88.42|
|MMLU (5-Shot)                    |66.33|
|TruthfulQA (0-shot)              |71.79|
|Winogrande (5-shot)              |83.66|
|GSM8k (5-shot)                   |65.20|

 