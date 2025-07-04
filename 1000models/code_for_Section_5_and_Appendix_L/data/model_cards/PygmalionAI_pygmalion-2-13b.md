<h1 style="text-align: center">Pygmalion-2 13B</h1>
<h2 style="text-align: center">An instruction-tuned Llama-2 biased towards fiction writing and conversation.</h2>

## Model Details

The long-awaited release of our new models based on Llama-2 is finally here. Pygmalion-2 13B (formerly known as Metharme) is based on
[Llama-2 13B](https://huggingface.co/meta-llama/llama-2-13b-hf) released by Meta AI. 

The Metharme models were an experiment to try and get a model that is usable for conversation, roleplaying and storywriting, 
but which can be guided using natural language like other instruct models. After much deliberation, we reached the conclusion
that the Metharme prompting format is superior (and easier to use) compared to the classic Pygmalion. 

This model was trained by doing supervised fine-tuning over a mixture of regular instruction data alongside roleplay, fictional stories
and conversations with synthetically generated instructions attached.

This model is freely available for both commercial and non-commercial use, as per the Llama-2 license.


## Prompting

The model has been trained on prompts using three different roles, which are denoted by the following tokens: `<|system|>`, `<|user|>` and `<|model|>`.

The `<|system|>` prompt can be used to inject out-of-channel information behind the scenes, while the `<|user|>` prompt should be used to indicate user input.
The `<|model|>` token should then be used to indicate that the model should generate a response. These tokens can happen multiple times and be chained up to
form a conversation history.

### Prompting example

The system prompt has been designed to allow the model to "enter" various modes and dictate the reply length. Here's an example:

```
<|system|>Enter RP mode. Pretend to be {{char}} whose persona follows:
{{persona}}

You shall reply to the user while staying in character, and generate long responses.
```

## Dataset
The dataset used to fine-tune this model includes our own [PIPPA](https://huggingface.co/datasets/PygmalionAI/PIPPA), along with several other instruction
datasets, and datasets acquired from various RP forums.

## Limitations and biases

The intended use-case for this model is fictional writing for entertainment purposes. Any other sort of usage is out of scope.

As such, it was **not** fine-tuned to be safe and harmless: the base model _and_ this fine-tune have been trained on data known to contain profanity and texts that are lewd or otherwise offensive. It may produce socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. Outputs might often be factually wrong or misleading.

## Acknowledgements
We would like to thank [SpicyChat](https://spicychat.ai/) for sponsoring the training for this model.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
