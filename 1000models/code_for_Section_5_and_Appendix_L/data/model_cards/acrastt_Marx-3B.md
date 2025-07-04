
<a href="https://www.buymeacoffee.com/acrastt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This is [OpenLLaMA 3B V2](https://huggingface.co/openlm-research/open_llama_3b_v2) finetuned on [EverythingLM Data(ShareGPT format more cleaned)](https://huggingface.co/datasets/totally-not-an-llm/everything-sharegptformat-morecleaned) for 1 epochs.

Prompt template:
```
### HUMAN:
{prompt}

### RESPONSE:
<leave a newline for the model to answer>
```
GGML quants available [here](https://huggingface.co/TheBloke/Marx-3b-GGML).</br>
GPTQ quants available [here](https://huggingface.co/TheBloke/Marx-3b-GPTQ).

Note: Don't expect this model to be good, I was just starting out to finetune. So don't roast me please!

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Marx-3B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 41.71   |
| ARC (25-shot)         | 43.17          |
| HellaSwag (10-shot)   | 72.68    |
| MMLU (5-shot)         | 28.46         |
| TruthfulQA (0-shot)   | 39.09   |
| Winogrande (5-shot)   | 65.59   |
| GSM8K (5-shot)        | 1.29        |

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Marx-3B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |41.71|
|AI2 Reasoning Challenge (25-Shot)|43.17|
|HellaSwag (10-Shot)              |72.68|
|MMLU (5-Shot)                    |28.46|
|TruthfulQA (0-shot)              |39.09|
|Winogrande (5-shot)              |65.59|
|GSM8k (5-shot)                   | 1.29|

