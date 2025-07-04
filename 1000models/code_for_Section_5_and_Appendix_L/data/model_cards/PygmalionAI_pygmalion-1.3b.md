
# Pygmalion 1.3B

## Model description

Pymalion 1.3B is a proof-of-concept dialogue model based on EleutherAI's [pythia-1.3b-deduped](https://huggingface.co/EleutherAI/pythia-1.3b-deduped).

**Warning:** This model is **NOT** suitable for use by minors. It **will** output X-rated content under certain circumstances.

## Training data

The fine-tuning dataset consisted of 56MB of dialogue data gathered from multiple sources, which includes both real _and_ partially machine-generated conversations.

## Training procedure

Fine-tuning was done using [ColossalAI](https://github.com/hpcaitech/ColossalAI) (specifically, with a slightly modified version of their [OPT fine-tune example](https://github.com/hpcaitech/ColossalAI/blob/78509124d32b63b7fc36f6508e0576a326d51422/examples/language/opt/run_clm.py)) for around 11.4 million tokens over 5440 steps on a single 24GB GPU. The run took just under 21 hours.

## Intended use

### The easy way

We provide a notebook with a Gradio UI for playing around with the model without having to manually format inputs. This notebook can be found [here](https://github.com/PygmalionAI/gradio-ui/blob/master/notebooks/GPU.ipynb).

### The manual way

The model can be used as a regular text generation model, but it'll perform best if the input prompt adheres to the following format:

```
[CHARACTER]'s Persona: [A few sentences about the character you want the model to play]

[DIALOGUE HISTORY]
You: [Your input message here]
[CHARACTER]:
```

Where `[CHARACTER] `is, as you can probably guess, the name of the character you want the model to portray, and `[DIALOGUE HISTORY]` is chat history so the model can have some conversational context to draw from. Ideally it'll be pairs of messages like:

```
[CHARACTER]: [some dialogue here]
You: [your response to the dialogue above]
```

Apart from chat history, you can also just add example conversations in `[DIALOGUE HISTORY]` to show how the character should speak - ideally at the beginning, so it doesn't get confused as to what's conversation history vs. character definition.

## Known issues

- The model can get stuck repeating certain phrases, or sometimes even entire sentences.
  - We believe this is due to that behavior being present in the training data itself, and plan to investigate and adjust accordingly for future versions.
