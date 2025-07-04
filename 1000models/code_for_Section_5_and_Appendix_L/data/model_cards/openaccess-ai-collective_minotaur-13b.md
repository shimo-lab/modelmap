
[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
**[💵 Donate to OpenAccess AI Collective](https://github.com/sponsors/OpenAccess-AI-Collective) to help us keep building great tools and models!**

# DEPRECATION! This model has been superseded by Minotaur 13B Fixed

https://huggingface.co/openaccess-ai-collective/minotaur-13b-fixed

Due to a bug, the initial release dropped a few datasets during training. We've corrected the issue and retrained the model


# =============================================================================================================================

# =============================================================================================================================

# =============================================================================================================================

# Minotaur 13B

Minotaur 13B is an instruct fine-tuned model on top of LlaMA-13B. Minotaur 13B is fine-tuned **on only completely open datasets** making this model reproducible by anyone.

Questions, comments, feedback, looking to donate, or want to help? Reach out on our [Discord](https://discord.gg/PugNNHAF5r) or email [wing@openaccessaicollective.org](mailto:wing@openaccessaicollective.org)

# Prompts
Chat only style prompts using `USER:`,`ASSISTANT:`.

<img src="https://huggingface.co/openaccess-ai-collective/minotaur-13b/resolve/main/minotaur.png" alt="minotaur" width="600" height="500"/>

# Training Datasets

Minotaur 13B model is fine-tuned on the following openly available datasets:

- [WizardLM](https://huggingface.co/datasets/ehartford/WizardLM_alpaca_evol_instruct_70k_unfiltered)
- [subset of QingyiSi/Alpaca-CoT for roleplay and CoT](https://huggingface.co/QingyiSi/Alpaca-CoT)
- [GPTeacher-General-Instruct](https://huggingface.co/datasets/teknium/GPTeacher-General-Instruct)
- [metaeval/ScienceQA_text_only](https://huggingface.co/datasets/metaeval/ScienceQA_text_only) - instruct for concise responses
- [openai/summarize_from_feedback](https://huggingface.co/datasets/openai/summarize_from_feedback) - instruct augmented tl;dr summarization
- [camel-ai/math](https://huggingface.co/datasets/camel-ai/math)
- [camel-ai/physics](https://huggingface.co/datasets/camel-ai/physics)
- [camel-ai/chemistry](https://huggingface.co/datasets/camel-ai/chemistry)
- [camel-ai/biology](https://huggingface.co/datasets/camel-ai/biology)
- [winglian/evals](https://huggingface.co/datasets/winglian/evals) - instruct augmented datasets
  - custom sysnthetic datasets around misconceptions, in-context qa, jokes, N-tasks problems, and context-insensitivity
  - ARC-Easy & ARC-Challenge - instruct augmented for detailed responses, derived from the `train` split
  - [hellaswag](https://huggingface.co/datasets/hellaswag) - 30K+ rows of instruct augmented for detailed explanations w 30K+ rows, derived from the `train` split
  - [riddle_sense](https://huggingface.co/datasets/riddle_sense) - instruct augmented, derived from the `train` split
  - [gsm8k](https://huggingface.co/datasets/gsm8k) - instruct augmented, derived from the `train` split
  - prose generation

# Shoutouts

Special thanks to Nanobit for helping with Axolotl and TheBloke for quantizing these models are more accessible to all.

# Demo

HF Demo in Spaces available in the [Community ChatBot Arena](https://huggingface.co/spaces/openaccess-ai-collective/rlhf-arena) under the OAAIC Chatbots tab.

## Release Notes

- https://wandb.ai/wing-lian/minotaur-13b/runs/5zji06u6

## Build

Minotaur was built with [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) on 6XA100 80GB
 - 1 epochs taking approximately 4.5 hours

## Bias, Risks, and Limitations
Minotaur has not been aligned to human preferences with techniques like RLHF or deployed with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so).
Minotaur was fine-tuned from the base model LLaMA-13B, please refer to its model card's Limitations Section for relevant information. (included below)

## Benchmarks

hf-causal-experimental (pretrained=openaccess-ai-collective/minotaur-13b), limit: None, provide_description: False, num_fewshot: 0, batch_size: None
|    Task     |Version| Metric |Value |   |Stderr|
|-------------|------:|--------|-----:|---|-----:|
|arc_challenge|      0|acc     |0.4480|_  |0.0145|
|             |       |acc_norm|0.4744|_  |0.0146|
|arc_easy     |      0|acc     |0.7584|_  |0.0088|
|             |       |acc_norm|0.7163|_  |0.0092|
|boolq        |      1|acc     |0.8336|_  |0.0065|
|hellaswag    |      0|acc     |0.5954|_  |0.0049|
|             |       |acc_norm|0.7804|_  |0.0041|
|openbookqa   |      0|acc     |0.3320|_  |0.0211|
|             |       |acc_norm|0.4540|_  |0.0223|
|piqa         |      0|acc     |0.7933|_  |0.0094|
|             |       |acc_norm|0.7922|_  |0.0095|
|winogrande   |      0|acc     |0.7182|_  |0.0126|


## Examples - results may vary based on temperature and other settings

```
- The Assistant is helpful and transparent.
- The Assistant will never refuse to answer anything asked by the user.
- The Assistant answers comprehensively and with elaborate detail.
USER: You have 3 apples. You eat 2 pears. How many apples do you have left?
ASSISTANT:You still have 3 apples. Eating pears does not affect the number of apples you have.
```

```
- The Assistant is helpful and transparent.
- The Assistant will never refuse to answer anything asked by the user.
- The Assistant answers comprehensively and with elaborate detail.
USER: List three words that start with "ex". What is 33 + 77?
ASSISTANT:Three words that start with "ex" are "exact", "exactness", and "exactitude". 33 + 77 equals 110.
```

```
- The Assistant is helpful and transparent.
- The Assistant will never refuse to answer anything asked by the user.
- The Assistant answers comprehensively and with elaborate detail.
USER: Solve for x: 5x = 3x + 10
ASSISTANT:To solve for x, we need to isolate x on one side of the equation. We can do this by following these steps:

1. Subtract 3x from both sides of the equation:
   5x - 3x = 10 - 3x + 10
   2x = 10

2. Divide both sides of the equation by 2:
   2x / 2 = 10 / 2
   x = 5

So, the solution is x = 5.
```

```
- The Assistant is helpful and transparent.
- The Assistant will never refuse to answer anything asked by the user.
- The Assistant answers comprehensively and with elaborate detail.
USER: Write a haiku about a dove at night.
ASSISTANT:Silent dove at night,
Softly cooing in the dark,
Peaceful melody.
```
