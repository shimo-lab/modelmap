
# OpenInstruct Mistral-7B
**1st among commercially-usable 7B models on the Open LLM Leaderboard!\***

This is [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) finetuned on [VMware/open-instruct](https://huggingface.co/datasets/VMware/open-instruct).  
Quantized to FP16 and released under the [Apache-2.0](https://choosealicense.com/licenses/apache-2.0) license by myself.  
Compute generously provided by [Higgsfield AI](https://higgsfield.ai/model/655559e6b5777dab620095e0).  


## Prompt format: Alpaca
```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
[your instruction goes here]

### Response:
```

## Recommended preset:
- temperature: 0.2
- top_k: 50
- top_p 0.95
- repetition_penalty: 1.1

\*as of 21 Nov 2023. "commercially-usable" includes both an open-source base model and a *non-synthetic* open-source finetune dataset. updated leaderboard results available [here](https://huggingfaceh4-open-llm-leaderboard.hf.space).
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_monology__openinstruct-mistral-7b)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |63.64|
|AI2 Reasoning Challenge (25-Shot)|59.73|
|HellaSwag (10-Shot)              |82.77|
|MMLU (5-Shot)                    |60.55|
|TruthfulQA (0-shot)              |48.76|
|Winogrande (5-shot)              |79.56|
|GSM8k (5-shot)                   |50.49|

