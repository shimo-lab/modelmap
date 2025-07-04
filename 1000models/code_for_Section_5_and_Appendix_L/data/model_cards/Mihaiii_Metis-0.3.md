
[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

An instruct based fine tune of [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2).

It works well with long system prompts.

It isn't generic in a sense that it shouldn't be used for story telling, for example, but only for reasoning and text comprehension.

This model is trained on a private dataset. The high GSM8K score is **NOT** because of the MetaMath dataset. 

# Prompt Format ([see the guidelines from the base model](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2#instruction-format)):

```
<s>[INST] {system_message} . Say "Acknowledged!" if you understood. [/INST] Acknowledged! </s> [INST] {prompt} [/INST]

```