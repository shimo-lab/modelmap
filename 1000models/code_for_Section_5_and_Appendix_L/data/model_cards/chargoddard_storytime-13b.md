
Chat model with a storytelling bent. 

Recipe:
* [Chronorctypus-Limarobormes](https://huggingface.co/chargoddard/Chronorctypus-Limarobormes-13b) base
* a healthy SLERPing of [ReMM-v2.2-L2-13B](https://huggingface.co/Undi95/ReMM-v2.2-L2-13B)
* [Llama-2-13B-Storywriter](https://huggingface.co/Blackroot/Llama-2-13B-Storywriter-LORA) x 0.5
* WIP storytelling LORA


Responds well to the Alpaca prompt format.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_chargoddard__storytime-13b)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 50.55   |
| ARC (25-shot)         | 62.03          |
| HellaSwag (10-shot)   | 83.96    |
| MMLU (5-shot)         | 57.48         |
| TruthfulQA (0-shot)   | 52.5   |
| Winogrande (5-shot)   | 75.53   |
| GSM8K (5-shot)        | 8.34        |
| DROP (3-shot)         | 14.0         |
