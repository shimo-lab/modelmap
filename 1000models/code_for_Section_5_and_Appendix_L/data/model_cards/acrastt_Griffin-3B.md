
<a href="https://www.buymeacoffee.com/acrastt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This is [OpenLLaMA 3B V2](https://huggingface.co/openlm-research/open_llama_3b_v2) finetuned on [Puffin](https://huggingface.co/datasets/LDJnr/Puffin) for 1 epochs.

Prompt template:
```
### HUMAN:
{prompt}

### RESPONSE:
<leave a newline for the model to answer>
```
GGML quants available [here](https://huggingface.co/TheBloke/Griffin-3B-GGML).</br>
GPTQ quants available [here](https://huggingface.co/TheBloke/Griffin-3B-GPTQ).

Note: Don't expect this model to be good, I was just starting out to finetune. So don't roast me please!

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Griffin-3B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 41.13   |
| ARC (25-shot)         | 41.81          |
| HellaSwag (10-shot)   | 72.3    |
| MMLU (5-shot)         | 26.36         |
| TruthfulQA (0-shot)   | 38.33   |
| Winogrande (5-shot)   | 67.01   |
| GSM8K (5-shot)        | 0.99        |

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Griffin-3B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |41.13|
|AI2 Reasoning Challenge (25-Shot)|41.81|
|HellaSwag (10-Shot)              |72.30|
|MMLU (5-Shot)                    |26.36|
|TruthfulQA (0-shot)              |38.33|
|Winogrande (5-shot)              |67.01|
|GSM8k (5-shot)                   | 0.99|

