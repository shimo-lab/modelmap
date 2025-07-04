<a href="https://www.buymeacoffee.com/acrastt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This is [OpenLLaMA 3B V2](https://huggingface.co/openlm-research/open_llama_3b_v2) finetuned on [EverythingLM Data V2(ShareGPT format)](https://huggingface.co/datasets/totally-not-an-llm/EverythingLM-data-V2-sharegpt) for 2 epochs.

Prompt template:
```
### HUMAN:
{prompt}

### RESPONSE:
<leave a newline for the model to answer>
```
q4_1 GGML quant available [here](https://huggingface.co/NikolayKozloff/Marx-3B-V2/).</br>
q4_1 GGUF quant available [here]( https://huggingface.co/NikolayKozloff/Marx-3B-V2-GGUF/).

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_acrastt__Marx-3B-V2)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |42.08|
|AI2 Reasoning Challenge (25-Shot)|44.03|
|HellaSwag (10-Shot)              |72.92|
|MMLU (5-Shot)                    |27.84|
|TruthfulQA (0-shot)              |39.92|
|Winogrande (5-shot)              |66.54|
|GSM8k (5-shot)                   | 1.21|

