
It was trained for like 3 epochs on a merger dataset of several instruction datasets, with partially longer instructions. 

Alpaca Prompt Format:
```
### Instruction:
blablabla
### Input: 
(optional)
### Response:
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_KnutJaegersberg__MistralInstructLongish)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 48.99   |
| ARC (25-shot)         | 60.75          |
| HellaSwag (10-shot)   | 81.86    |
| MMLU (5-shot)         | 60.49         |
| TruthfulQA (0-shot)   | 40.55   |
| Winogrande (5-shot)   | 76.56   |
| GSM8K (5-shot)        | 1.52        |
| DROP (3-shot)         | 21.22         |
