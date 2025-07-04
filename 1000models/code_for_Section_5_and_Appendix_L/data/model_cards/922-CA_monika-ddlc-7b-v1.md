
# monika-ddlc-7b-v1:
* LLaMA-2 7b chat fine-tuned for Monika character from DDLC (still somewhat experimental)
* Fine-tuned on a dataset of ~600+ items (dialogue scraped from game, reddit, and Twitter augmented by [l2-7b-monika-v0.3c1](https://huggingface.co/922-CA/llama-2-7b-monika-v0.3c1) to turn each into snippets of multi-turn chat dialogue between Player and Monika; this was then manually edited, with more manually crafted items including info about character added in)
* [GGUFs](https://huggingface.co/922-CA/monika-ddlc-7b-v1-GGUF)
* [QLoras](https://huggingface.co/922-CA/monika-lm-lora-tests/tree/main/monika-ddlc-7b-v1)

### USAGE
This is meant to be mainly a chat model with limited RP ability.

For best results: replace "Human" and "Assistant" with "Player" and "Monika" like so:

\nPlayer: (prompt)\nMonika:

### HYPERPARAMS
* Trained for 3 epochs
* rank: 32
* lora alpha: 64
* lora dropout: 0.5
* lr: 2e-4
* batch size: 2
* warmup ratio: 0.1
* grad steps: 4

### WARNINGS AND DISCLAIMERS
This model is meant to closely reflect the characteristics of Monika. Despite this, there is always the chance that "Monika" will hallucinate and get information about herself wrong or act out of character (for example, in testing she usually knows her own club and its members, her game, and even her height and favorite ice cream flavor, but may still get her eye color wrong or mistake her developer as being a member of her club).

Additionally, being character-focused means that this model may not be the smartest model/not as capable as others for simple tasks (not yet tested).

Finally, this model is not guaranteed to output aligned or safe outputs, use at your own risk.

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_922-CA__monika-ddlc-7b-v1)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |50.49|
|AI2 Reasoning Challenge (25-Shot)|54.95|
|HellaSwag (10-Shot)              |76.78|
|MMLU (5-Shot)                    |45.61|
|TruthfulQA (0-shot)              |43.94|
|Winogrande (5-shot)              |72.85|
|GSM8k (5-shot)                   | 8.79|

