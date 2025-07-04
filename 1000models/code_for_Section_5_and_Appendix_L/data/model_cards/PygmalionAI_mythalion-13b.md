<h1 style="text-align: center">Mythalion 13B</h1>
<h2 style="text-align: center">A merge of Pygmalion-2 13B and MythoMax 13B</h2>

## Model Details

The long-awaited release of our new models based on Llama-2 is finally here. This model was created in
collaboration with [Gryphe](https://huggingface.co/Gryphe), a mixture of our [Pygmalion-2 13B](https://huggingface.co/PygmalionAI/pygmalion-2-13b)
and Gryphe's [Mythomax L2 13B](https://huggingface.co/Gryphe/MythoMax-L2-13b).

Finer details of the merge are available in [our blogpost](https://pygmalionai.github.io/blog/posts/introducing_pygmalion_2/#mythalion-13b).
According to our testers, this model seems to outperform MythoMax in RP/Chat. **Please make sure you follow the recommended
generation settings for SillyTavern [here](https://pygmalionai.github.io/blog/posts/introducing_pygmalion_2/#sillytavern) for
the best results!**

This model is freely available for both commercial and non-commercial use, as per the Llama-2 license.


## Prompting

This model can be prompted using both the Alpaca and [Pygmalion formatting](https://huggingface.co/PygmalionAI/pygmalion-2-13b#prompting).

**Alpaca formatting**:
```
### Instruction:
<prompt>

### Response:
<leave a newline blank for model to respond>
```

**Pygmalion/Metharme formatting**:
```
<|system|>Enter RP mode. Pretend to be {{char}} whose persona follows:
{{persona}}

You shall reply to the user while staying in character, and generate long responses.
<|user|>Hello!<|model|>{model's response goes here}

```


The model has been trained on prompts using three different roles, which are denoted by the following tokens: `<|system|>`, `<|user|>` and `<|model|>`.

The `<|system|>` prompt can be used to inject out-of-channel information behind the scenes, while the `<|user|>` prompt should be used to indicate user input.
The `<|model|>` token should then be used to indicate that the model should generate a response. These tokens can happen multiple times and be chained up to
form a conversation history.

## Limitations and biases

The intended use-case for this model is fictional writing for entertainment purposes. Any other sort of usage is out of scope.

As such, it was **not** fine-tuned to be safe and harmless: the base model _and_ this fine-tune have been trained on data known to contain profanity and texts that are lewd or otherwise offensive. It may produce socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. Outputs might often be factually wrong or misleading.

## Acknowledgements
We would like to thank [SpicyChat](https://spicychat.ai/) for sponsoring the training for the [Pygmalion-2 13B](https://huggingface.co/PygmalionAI/pygmalion-2-13b) model.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)