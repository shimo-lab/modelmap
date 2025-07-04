<h1 style="text-align: center">Metharme 7B</h1>
<h2 style="text-align: center">An instruction-tuned LLaMA biased towards fiction writing and conversation.</h2>

## Model Details

Converted from the XORs weights from PygmalionAI's release https://huggingface.co/PygmalionAI/metharme-7b

Metharme 7B is an instruct model based on Meta's LLaMA-7B.

This is an experiment to try and get a model that is usable for conversation, roleplaying and storywriting, but which can be guided using natural language like other instruct models. See the [prompting](#prompting) section below for examples.

It was trained by doing supervised fine-tuning over a mixture of regular instruction data alongside roleplay, fictional stories and conversations with synthetically generated instructions attached.

## Prompting

The current model version has been trained on prompts using three different roles, which are denoted by the following tokens: `<|system|>`, `<|user|>` and `<|model|>`.

The `<|system|>` prompt can be used to inject out-of-channel information behind the scenes, while the `<|user|>` prompt should be used to indicate user input. The `<|model|>` token should then be used to indicate that the model should generate a response. These tokens can happen multiple times and be chained up to form a conversation history.

### Prompting example

Here's a concrete example. Let's say you have the following system prompt:

> This is a text adventure game. Describe the scenario to the user and give him three options to pick from on each turn.

And the user has typed in the following message:

> Start!

To perform inference against the model, the prompt should be formatted like this:

```
<|system|>This is a text adventure game. Describe the scenario to the user and give him three options to pick from on each turn.<|user|>Start!<|model|>
```

The model might generate something like:

> You are standing in front of an old, abandoned house. The windows are boarded up, and there's no sign of life around it. As you approach, you notice a strange feeling emanating from within. Suddenly, you hear a voice calling out to you... 'Come inside!'
>
> - Go inside the house.
> - Ignore the call and move away.
> - Run as fast as you can.

It will automatically emit an end-of-text token (`</s>`) when it judges that the response is complete.

Pretend then that the user has replied with `go inside`. The next prompt should then be:

```
<|system|>This is a text adventure game. Describe the scenario to the user and give him three options to pick from on each turn.<|user|>Start!<|model|>You are standing in front of an old, abandoned house. The windows are boarded up, and there's no sign of life around it. As you approach, you notice a strange feeling emanating from within. Suddenly, you hear a voice calling out to you... 'Come inside!'

- Go inside the house.
- Ignore the call and move away.
- Run as fast as you can.<|user|>go inside<|model|>
```

Which might generate something like:

> You enter the house, and immediately, a wave of unsettling energy washes over you. Your senses seem heightened, but your mind feels foggy. A figure appears before you - a tall man with piercing eyes. He speaks to you in a language you don't understand.
>
> - Ask him what he wants.
> - Attack him.
> - Run away.

Same process applies. Usually, it is best to do a sliding window over the user and model turns, but keep the system prompt fixed at the start of the context window.

## Limitations and biases

The intended use-case for this model is fictional writing for entertainment purposes. Any other sort of usage is out of scope.

As such, it was **not** fine-tuned to be safe and harmless: the base model _and_ this fine-tune have been trained on data known to contain profanity and texts that are lewd or otherwise offensive. It may produce socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. Outputs might often be factually wrong or misleading.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Neko-Institute-of-Science__metharme-7b)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 41.5   |
| ARC (25-shot)         | 53.67          |
| HellaSwag (10-shot)   | 78.62    |
| MMLU (5-shot)         | 35.91         |
| TruthfulQA (0-shot)   | 39.16   |
| Winogrande (5-shot)   | 72.53   |
| GSM8K (5-shot)        | 5.0        |
| DROP (3-shot)         | 5.62         |
