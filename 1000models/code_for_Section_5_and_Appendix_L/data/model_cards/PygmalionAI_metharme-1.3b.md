<h1 style="text-align: center">Metharme 1.3B</h1>
<h2 style="text-align: center">An instruction-tuned Pythia biased towards fiction writing and conversation.</h2>

## Model Details

Metharme 1.3B is an instruct model based on EleutherAI's [Pythia 1.4B Deduped](https://huggingface.co/EleutherAI/pythia-1.4b-deduped).

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

It will automatically emit an end-of-text token (`<|endoftext|>`) when it judges that the response is complete.

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

## Evaluation Metrics
The model was evaluated using EleutherAI's [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) test suite. It was evaluated on the following tasks:


|    Task     |Version| Metric |Value |   |Stderr|
|-------------|------:|--------|-----:|---|-----:|
|anli_r1      |      0|acc     |0.3430|±  |0.0150|
|anli_r2      |      0|acc     |0.3330|±  |0.0149|
|anli_r3      |      0|acc     |0.3350|±  |0.0136|
|arc_challenge|      0|acc     |0.2747|±  |0.0130|
|             |       |acc_norm|0.3114|±  |0.0135|
|arc_easy     |      0|acc     |0.6237|±  |0.0099|
|             |       |acc_norm|0.5631|±  |0.0102|
|boolq        |      1|acc     |0.6214|±  |0.0085|
|cb           |      1|acc     |0.1964|±  |0.0536|
|             |       |f1      |0.1712|   |      |
|hellaswag    |      0|acc     |0.4295|±  |0.0049|
|             |       |acc_norm|0.5496|±  |0.0050|
|openbookqa   |      0|acc     |0.2360|±  |0.0190|
|             |       |acc_norm|0.3360|±  |0.0211|
|piqa         |      0|acc     |0.7285|±  |0.0104|
|             |       |acc_norm|0.7318|±  |0.0103|
|rte          |      0|acc     |0.5235|±  |0.0301|
|truthfulqa_mc|      1|mc1     |0.2436|±  |0.0150|
|             |       |mc2     |0.3791|±  |0.0142|
|wic          |      0|acc     |0.5000|±  |0.0198|
|winogrande   |      0|acc     |0.5675|±  |0.0139|
|wsc          |      0|acc     |0.3654|±  |0.0474|


Illustrated comparison of Metharme-1.3B's performance on benchmarks to Pygmalion-6B, Metharme-7B, and [RedPajama-INCITE-Chat-3B-v1](https://huggingface.co/togethercomputer/RedPajama-INCITE-Chat-3B-v1):
![Eval](https://i.imgur.com/hW8Owbc.png)

## Limitations and biases

Due to being a smaller model than Metharme 7B and 13B, the coherency will very likely suffer.

The intended use-case for this model is fictional writing for entertainment purposes. Any other sort of usage is out of scope.

As such, it was **not** fine-tuned to be safe and harmless: the base model _and_ this fine-tune have been trained on data known to contain profanity and texts that are lewd or otherwise offensive. It may produce socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. Outputs might often be factually wrong or misleading.