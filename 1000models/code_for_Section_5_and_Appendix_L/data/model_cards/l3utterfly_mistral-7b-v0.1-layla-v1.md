
# Model Card

### Model Description

Mistral 7B fine-tuned using ShareGPT datasets for multi-turn conversations.

- **Developed by:** l3utterfly
- **Funded by:** Layla Network
- **Model type:** Mistral
- **Language(s) (NLP):** English
- **License:** Apache-2.0
- **Finetuned from model:** Mistral 7B

## Uses

Base model used by Layla - the offline personal assistant: https://www.layla-network.ai

Help & support: https://discord.gg/x546YJ6nYC

Prompt:
```
User:
Assistant:
```

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_l3utterfly__mistral-7b-v0.1-layla-v1)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 55.05   |
| ARC (25-shot)         | 60.15          |
| HellaSwag (10-shot)   | 83.25    |
| MMLU (5-shot)         | 60.31         |
| TruthfulQA (0-shot)   | 48.9   |
| Winogrande (5-shot)   | 75.93   |
| GSM8K (5-shot)        | 16.83        |
| DROP (3-shot)         | 40.01         |

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)