
<a href="https://www.buymeacoffee.com/acrastt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This is [OpenLLaMA 3B V2](https://huggingface.co/openlm-research/open_llama_3b_v2) finetuned on [LIMA(ShareGPT format)](https://huggingface.co/datasets/64bits/lima_vicuna_format) for 2 epochs.

Prompt template:
```
### HUMAN:
{prompt}

### RESPONSE:
<leave a newline for the model to answer>
```
GGUF quantizations available [here](https://huggingface.co/maddes8cht/acrastt-Bean-3B-gguf).

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Bean-3B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 40.18   |
| ARC (25-shot)         | 40.36          |
| HellaSwag (10-shot)   | 72.0    |
| MMLU (5-shot)         | 26.43         |
| TruthfulQA (0-shot)   | 36.11   |
| Winogrande (5-shot)   | 65.67   |
| GSM8K (5-shot)        | 0.53        |

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Bean-3B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |40.18|
|AI2 Reasoning Challenge (25-Shot)|40.36|
|HellaSwag (10-Shot)              |72.00|
|MMLU (5-Shot)                    |26.43|
|TruthfulQA (0-shot)              |36.11|
|Winogrande (5-shot)              |65.67|
|GSM8k (5-shot)                   | 0.53|

