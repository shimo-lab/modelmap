# OpenLLaMA Code Instruct: An Open Reproduction of LLaMA

This is an [OpenLlama model](https://huggingface.co/openlm-research/open_llama_3b) that has been fine-tuned on 1 epoch of the
[AlpacaCode](https://huggingface.co/datasets/mwitiderrick/AlpacaCode) dataset (122K rows).

## Prompt Template
```
### Instruction:

{query}

### Response:
<Leave new line for model to respond> 
```
## Usage 
```python
from transformers import AutoTokenizer, AutoModelForCausalLM,pipeline

tokenizer = AutoTokenizer.from_pretrained("mwitiderrick/open_llama_3b_code_instruct_0.1")
model = AutoModelForCausalLM.from_pretrained("mwitiderrick/open_llama_3b_code_instruct_0.1")
query = "Write a quick sort algorithm in Python"
text_gen = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200)
output = text_gen(f"### Instruction:\n{query}\n### Response:\n")
print(output[0]['generated_text'])
"""
### Instruction:
write a quick sort algorithm in Python
### Response:
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

arr = [5,2,4,3,1]
print(quick_sort(arr))
"""
[1, 2, 3, 4, 5]
"""
```
## Metrics
[Detailed metrics](https://huggingface.co/datasets/open-llm-leaderboard/details_mwitiderrick__open_llama_3b_code_instruct_0.1)
```
|  Tasks   |Version|Filter|n-shot|Metric|Value |   |Stderr|
|----------|-------|------|-----:|------|-----:|---|-----:|
|winogrande|Yaml   |none  |     0|acc   |0.6267|±  |0.0136|
|hellaswag|Yaml   |none  |     0|acc     |0.4962|±  |0.0050|
|         |       |none  |     0|acc_norm|0.6581|±  |0.0047|
|arc_challenge|Yaml   |none  |     0|acc     |0.3481|±  |0.0139|
|             |       |none  |     0|acc_norm|0.3712|±  |0.0141|
|truthfulqa|N/A    |none  |     0|bleu_max   | 24.2580|±  |0.5985|
|          |       |none  |     0|bleu_acc   |  0.2876|±  |0.0003|
|          |       |none  |     0|bleu_diff  | -8.3685|±  |0.6065|
|          |       |none  |     0|rouge1_max | 49.3907|±  |0.7350|
|          |       |none  |     0|rouge1_acc |  0.2558|±  |0.0002|
|          |       |none  |     0|rouge1_diff|-10.6617|±  |0.6450|
|          |       |none  |     0|rouge2_max | 32.4189|±  |0.9587|
|          |       |none  |     0|rouge2_acc |  0.2142|±  |0.0002|
|          |       |none  |     0|rouge2_diff|-12.9903|±  |0.9539|
|          |       |none  |     0|rougeL_max | 46.2337|±  |0.7493|
|          |       |none  |     0|rougeL_acc |  0.2424|±  |0.0002|
|          |       |none  |     0|rougeL_diff|-11.0285|±  |0.6576|
|          |       |none  |     0|acc        |  0.3072|±  |0.0405|
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_mwitiderrick__open_llama_3b_code_instruct_0.1)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |39.72|
|AI2 Reasoning Challenge (25-Shot)|41.21|
|HellaSwag (10-Shot)              |66.96|
|MMLU (5-Shot)                    |27.82|
|TruthfulQA (0-shot)              |35.01|
|Winogrande (5-shot)              |65.43|
|GSM8k (5-shot)                   | 1.90|

