
<a href="https://www.buymeacoffee.com/acrastt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This is an experimental merge of models [RedPajama-INCITE-Chat-3B-V1](https://huggingface.co/togethercomputer/RedPajama-INCITE-Chat-3B-v1) and [RedPajama-INCITE-Instruct-3B-V1](https://huggingface.co/togethercomputer/RedPajama-INCITE-Instruct-3B-v1).</br>
This model is adaptive to prompt templates, but this template is recommended:
```
HUMAN: {prompt}
ASSISTANT:
```
Feel free to change HUMAN or ASSISTANT. It will not change much.</br>
GGML versions [here](https://huggingface.co/adadbbb/pajama_ggml) (Note that this is only compatible with [koboldcpp](https://github.com/LostRuins/koboldcpp)).
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__RedPajama-INCITE-Chat-Instruct-3B-V1)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 39.23   |
| ARC (25-shot)         | 42.58          |
| HellaSwag (10-shot)   | 67.48    |
| MMLU (5-shot)         | 25.99         |
| TruthfulQA (0-shot)   | 33.62   |
| Winogrande (5-shot)   | 64.8   |
| GSM8K (5-shot)        | 0.91        |

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__RedPajama-INCITE-Chat-Instruct-3B-V1)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |39.23|
|AI2 Reasoning Challenge (25-Shot)|42.58|
|HellaSwag (10-Shot)              |67.48|
|MMLU (5-Shot)                    |25.99|
|TruthfulQA (0-shot)              |33.62|
|Winogrande (5-shot)              |64.80|
|GSM8k (5-shot)                   | 0.91|

