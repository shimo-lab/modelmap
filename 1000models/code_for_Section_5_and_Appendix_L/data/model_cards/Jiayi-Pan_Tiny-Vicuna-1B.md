# Tiny Vicuna 1B
This model is a fine-tuned version of [TinyLlama](https://huggingface.co/TinyLlama/TinyLlama-1.1B-intermediate-step-955k-token-2T) on [WizardVicuna Dataset](https://github.com/melodysdreamj/WizardVicunaLM).
It should be fully compatible with Vicuna-v1.5 series.


This model is easy to iterate on for early experiments!
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Jiayi-Pan__Tiny-Vicuna-1B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |34.76|
|AI2 Reasoning Challenge (25-Shot)|33.45|
|HellaSwag (10-Shot)              |55.92|
|MMLU (5-Shot)                    |25.45|
|TruthfulQA (0-shot)              |33.82|
|Winogrande (5-shot)              |58.41|
|GSM8k (5-shot)                   | 1.52|

