
# Pygmalion 2.7B

## Model description

Pymalion 2.7B is a proof-of-concept dialogue model based on EleutherAI's [gpt-neo-2.7B](https://huggingface.co/EleutherAI/gpt-neo-2.7B).

**Warning:** This model is **NOT** suitable for use by minors. It **will** output X-rated content under certain circumstances.

## Training data

The fine-tuning dataset consisted of 56MB of dialogue data gathered from multiple sources, which includes both real _and_ partially machine-generated conversations.

## Training procedure

Model weights were initialized from the `uft-2.7b` ConvoGPT model made available in [this commit](https://huggingface.co/hakurei/convogpt/tree/07707377dee0aa7d1ee5363ef660b13eb5b73f9d/2.7b-uft).

The model was then further fine-tuned on ~48.5 million tokens for ~5k steps on 4 NVIDIA A40s using DeepSpeed.

## Intended use

### The easy way

We provide a notebook with a Gradio UI for playing around with the model without having to manually format inputs. This notebook can be found [here](https://github.com/PygmalionAI/gradio-ui/blob/master/notebooks/GPU.ipynb).

### The manual way

The model can be used as a regular text generation model, but it'll perform best if the input prompt adheres to the following format:

```
[CHARACTER]'s Persona: [A few sentences about the character you want the model to play]
<START>
[DIALOGUE HISTORY]
You: [Your input message here]
[CHARACTER]:
```

Where `[CHARACTER]` is, as you can probably guess, the name of the character you want the model to portray, `<START>` should be used verbatim as a delimiter token to separate persona and scenario data from the dialogue, and `[DIALOGUE HISTORY]` is chat history so the model can have some conversational context to draw from. Ideally it'll be pairs of messages like:

```
[CHARACTER]: [some dialogue here]
You: [your response to the dialogue above]
```

Apart from chat history, you can also just add example conversations in `[DIALOGUE HISTORY]` to show how the character should speak - ideally at the beginning, so it doesn't get confused as to what's conversation history vs. character definition.

## Known issues

We haven't played around with the model enough to enumerate them. Feel free to give us some feedback!
