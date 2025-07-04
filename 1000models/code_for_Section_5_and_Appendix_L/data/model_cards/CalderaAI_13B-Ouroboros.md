
## 13B-Ouroboros
Ouroboros is an experimental model based on Meta's LLaMA [v1] 13B base model using a custom merging technique, tweaking
each layer's merge % based on internal tests against the PTB dataset, scoring ~26.31 according to internal evaluation
(6 samples, sequence length 1024; this testing is not empirical, it's a quick way to find near-optimum values). Testing,
evaluating, and remixing this model is absolutely permissible and even encouraged (within the bounds of Meta's LLaMAv1
license agreement); the more feedback the better we can tune our process! 😊

## Composition:
Ouroboros is comprised of 40 layers [LLaMAv1 13B standard] mixed at optimized
ratios VS the PTB dataset for lowest perplexity score. Listed below are the
paired models and ratios merged per layer.

Tier One Merge:

13B-airoboros-gpt4-1.4 > 13B-orca_mini_v2

[0.22, 0.85, 0.89, 0.98, 0.3, 0.41, 0.71, 0.83, 0.32, 0.1, 0.44, 0.6, 0.53, 0.15, 0.86, 0.79, 0.93, 0.02, 0.19, 0.82, 0.01, 0.52, 0.07, 0.27, 0.73, 0.86, 0.08, 0.67, 0.42, 0.28, 0.37, 0.08, 0.95, 0.68, 0.45, 0.08, 0.7, 0.93, 0.96, 0.43]

13B-gpt4-x-alpaca > 13B-Vicuna-cocktail

[0.65, 0.94, 0.98, 0.87, 0.28, 0.64, 0.73, 0.7, 0.95, 0.89, 0.84, 0.9, 0.59, 0.92, 0.28, 0.61, 0.88, 0.73, 0.34, 0.85, 0.98, 0.05, 0.74, 0.92, 0.5, 0.78, 0.26, 0.4, 0.27, 0.65, 0.71, 0.7, 0.8, 0.93, 0.36, 0.03, 0.45, 0.39, 0.77, 0.06]

Tier Two Merge:

[13B-airoboros-gpt4-1.4 + 13B-orca_mini_v2] offspring > [13B-gpt4-x-alpaca + 13B-Vicuna-cocktail] offspring

[0.2, 0.83, 0.24, 0.03, 0.37, 0.62, 0.02, 0.82, 0.65, 0.63, 0.45, 0.65, 0.48, 0.45, 0.24, 0.76, 0.06, 0.31, 0.45, 0.86, 0.23, 0.99, 0.93, 0.84, 0.96, 0.53, 0.95, 0.32, 0.19, 0.06, 0.4, 0.08, 0.62, 0.4, 0.26, 0.12, 0.16, 0.91, 0.14, 0.0]

Result:

13B-Ouroboros, a model that seems uncensored and highly competent. So far only Alpaca instruction prompting has been tested and seems to work solidly well.

## Use:

Alpaca's instruct format can be used to do many things, including control of the terms of behavior
between a user and a response from an agent in chat. Below is an example of a command injected into
memory.

```
### Instruction:
Make Narrator function as a text based adventure game that responds with verbose, detailed, and creative descriptions of what happens next after Player's response.
Make Player function as the player input for Narrator's text based adventure game, controlling a character named (insert character name here, their short bio, and
whatever quest or other information to keep consistent in the interaction).

### Response:
{an empty new line here}
```

## Language Models Used Credits:

13B-airoboros-gpt4-1.4 by jondurbin

https://huggingface.co/jondurbin/airoboros-13b-gpt4-1.4

13B-orca_mini_v2 by psmathur

https://huggingface.co/psmathur/orca_mini_v2_13b

13B-gpt4-x-alpaca by chavinlo

https://huggingface.co/chavinlo/gpt4-x-alpaca

13B-Vicuna-cocktail by reeducator

https://huggingface.co/reeducator/vicuna-13b-cocktail

Also thanks to Meta for LLaMA.

Each model was hand picked and considered for what it could contribute to this ensemble.
Thanks to each and every one of you for your incredible work developing some of the best things
to come out of this community.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_CalderaAI__13B-Ouroboros)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 44.66   |
| ARC (25-shot)         | 57.42          |
| HellaSwag (10-shot)   | 82.11    |
| MMLU (5-shot)         | 51.43         |
| TruthfulQA (0-shot)   | 47.99   |
| Winogrande (5-shot)   | 57.85   |
| GSM8K (5-shot)        | 0.45        |
| DROP (3-shot)         | 15.36         |
