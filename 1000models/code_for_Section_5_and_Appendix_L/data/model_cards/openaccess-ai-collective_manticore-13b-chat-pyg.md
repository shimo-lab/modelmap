
# Manticore 13B Chat

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

Manticore 13B Chat builds on Manticore with new datasets, including a de-duped subset of the Pygmalion dataset. It also removes all Alpaca style prompts using `###` in favor of 
chat only style prompts using `USER:`,`ASSISTANT:` as well as [pygmalion/metharme prompting](https://huggingface.co/PygmalionAI/metharme-7b#prompting) using `<|system|>, <|user|> and <|model|>` tokens.

Questions, comments, feedback, looking to donate, or want to help? Reach out on our [Discord](https://discord.gg/PugNNHAF5r) or email [wing@openaccessaicollective.org](mailto:wing@openaccessaicollective.org)

# Training Datasets

Manticore 13B Chat is a Llama 13B model fine-tuned on the following datasets along with the datasets from the original Manticore 13B. 

**Manticore 13B Chat was trained on 25% of the datasets below. The datasets were merged, shuffled, and then sharded into 4 parts.**

- de-duped pygmalion dataset, filtered down to RP data
- [riddle_sense](https://huggingface.co/datasets/riddle_sense) - instruct augmented 
- hellaswag, updated for detailed explanations w 30K+ rows
- [gsm8k](https://huggingface.co/datasets/gsm8k) - instruct augmented 
- [ewof/code-alpaca-instruct-unfiltered](https://huggingface.co/datasets/ewof/code-alpaca-instruct-unfiltered)

Manticore 13B
- [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered) - based on a cleaned and de-suped subset
- [WizardLM](https://huggingface.co/datasets/ehartford/WizardLM_alpaca_evol_instruct_70k_unfiltered)
- [Wizard-Vicuna](https://huggingface.co/datasets/ehartford/wizard_vicuna_70k_unfiltered)
- [subset of QingyiSi/Alpaca-CoT for roleplay and CoT](https://huggingface.co/QingyiSi/Alpaca-CoT)
- [GPT4-LLM-Cleaned](https://huggingface.co/datasets/teknium/GPT4-LLM-Cleaned)
- [GPTeacher-General-Instruct](https://huggingface.co/datasets/teknium/GPTeacher-General-Instruct)
- ARC-Easy & ARC-Challenge - instruct augmented for detailed responses, derived from the `train` split
- [hellaswag](https://huggingface.co/datasets/hellaswag) - 5K row subset of instruct augmented for concise responses, derived from the `train` split
- [metaeval/ScienceQA_text_only](https://huggingface.co/datasets/metaeval/ScienceQA_text_only) - instruct for concise responses
- [openai/summarize_from_feedback](https://huggingface.co/datasets/openai/summarize_from_feedback) - instruct augmented tl;dr summarization

Not added from Manticore 13B:
- mmlu - mmlu datasets were not added to this model as the `test` split is used for benchmarks

# Shoutouts

Special thanks to Nanobit for helping with Axolotl, TheBloke for quantizing these models are more accessible to all, ehartford for cleaned datasets, and 0x000011b for the RP dataset.
# Demo

Try out the model in HF Spaces. The demo uses a quantized GGML version of the model to quickly return predictions on smaller GPUs (and even CPUs). Quantized GGML may have some minimal loss of model quality.
- https://huggingface.co/spaces/openaccess-ai-collective/manticore-13b-chat-pyg

## Release Notes

- https://wandb.ai/wing-lian/manticore-13b-v2/runs/hxr3aiiw

## Build

Manticore was built with [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) on 8xA100 80GB 
 - 3 epochs taking approximately 8 hours. No further epochs will be released. 
 - The configuration to duplicate this build is provided in this repo's [/config folder](https://huggingface.co/openaccess-ai-collective/manticore-13b/tree/main/configs).

## Bias, Risks, and Limitations
Manticore has not been aligned to human preferences with techniques like RLHF or deployed with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so).
Manticore was fine-tuned from the base model LlaMa 13B, please refer to its model card's Limitations Section for relevant information.

## Examples

```
USER: make up a sonnet in the style of shakespeare about a skier skiing in the glades on a bluebird day.
ASSISTANT: A skier doth glide 'neath sun’s glow, His edges sharp to cut the snow, Bluebird sky above, While he doth revel on the slopes below, The cold air biting his nose, But not his spirits, For he is filled with a sense of joy, As he carves through the powdery drifts. His body moves in graceful rhythm, And each turn he makes with ease, He feels like he could ski forever, With no care for the world outside these glades.
```

```
USER: tell me a joke about alpacas
ASSISTANT: Did you hear about the famous alpaca ballet dancer? She was a prima llama.
USER: okay, that is actually pretty good
ASSISTANT: What do you call an alpaca in a bowtie? A llama-cholla!
USER: why is that funny?
ASSISTANT: Because it’s a play on words. “Llama-cholla” sounds like “lame chola,” which is Spanish slang for someone who acts cool or pretentious. So, the joke is implying that alpacas are vain and act cool with their bowties.
```

```
USER: What is 44 + 77?
ASSISTANT: 121
USER: What is the sum of 33 and 77?
ASSISTANT: 110
USER: tell me 5 words that start with “ex” and the sum of 33 and 77.
ASSISTANT: exotic, expressive, explicit, experimental, and extravagant. The sum of 33 and 77 is 110.
USER: tell me 3 words that start with “egr” and end in “s”
ASSISTANT: egret, eggplant, and egrets.
```
- oof


```
USER: Sally has 3 brothers. Each brother has 2 sisters. How many sisters does Sally have?
ASSISTANT: Sally has a total of 6 siblings, so she has a total of 6 - 2 = 4 sisters.
USER: Sally has 3 brothers. Each brother has 2 sisters. How many sisters does Sally have? Use multi-step reasoning to explain your answer.
ASSISTANT: Sally has a total of three brothers, so she has a total of three * 2 = six siblings. Her family consists of three boys and six girls in total. This means that Sally has three sisters since there are six female relatives and only three male ones.
USER: But when brothers have sisters, aren’t they shared or the same?
ASSISTANT: No, not every sibling shares their mother. For example, I have two brothers who share one mother but my third brother has a different mother from both of them.
USER: Let’s assume they all share the same mother and father. Now explain with multi-step reasoning.
ASSISTANT: If Sally has three brothers then that means she has six siblings altogether. Each brother has two sisters, which means that there are twelve female relatives in her family - one for each of her brothers and herself. Since there are only six females in the entire family, that means that Sally’s mother has no other children than her own three sons - so she can’t be the mother of any of the sisters. So all those sisters have to belong to one of the brothers, and since they are shared by two brothers, then each brother has a single sister. Therefore, there is only one sister for Sally, making the final answer 1.
```
- pretty sure that reasoning isn't correct, and the final answer of having 1 sister is a lucky guess