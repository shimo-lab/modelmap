
Made for the purpose of comparison with the tinyllama model. 3 epochs, neftune on trilobite. 

Prompt Example:
```
### System:

You are an AI assistant. User will give you a task. Your goal is to complete the task as faithfully as you can. While performing the task think step-by-step and justify your steps.


### Instruction: 

How do you fine tune a large language model? 

### Response:
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_KnutJaegersberg__falcon-1b-t-sft)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |35.02|
|AI2 Reasoning Challenge (25-Shot)|32.94|
|HellaSwag (10-Shot)              |57.24|
|MMLU (5-Shot)                    |25.26|
|TruthfulQA (0-shot)              |38.49|
|Winogrande (5-shot)              |55.88|
|GSM8k (5-shot)                   | 0.30|

