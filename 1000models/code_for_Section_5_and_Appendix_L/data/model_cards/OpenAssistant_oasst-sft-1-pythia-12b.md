
# Open-Assistant SFT-1 12B Model


This is the first iteration English supervised-fine-tuning (SFT) model of 
the [Open-Assistant](https://github.com/LAION-AI/Open-Assistant) project. 
It is based on a Pythia 12B that was fine-tuned on ~22k human demonstrations 
of assistant conversations collected through the 
[https://open-assistant.io/](https://open-assistant.io/) human feedback web 
app before March 7, 2023. 

## Model Details

- **Developed by:** [Open-Assistant Contributors](https://open-assistant.io/)
- **Model type:** Transformer-based Language Model
- **Language:** English
- **Finetuned from:** [EleutherAI / pythia-12b-deduped](https://huggingface.co/EleutherAI/pythia-12b-deduped)
- **Code:** [Open-Assistant/model/model_training](https://github.com/LAION-AI/Open-Assistant/tree/main/model/model_training)
- **Demo:** [Continuations for 250 random prompts](https://open-assistant.github.io/oasst-model-eval/?f=https%3A%2F%2Fraw.githubusercontent.com%2FOpen-Assistant%2Foasst-model-eval%2Fmain%2Fsampling_reports%2Foasst-sft%2F2023-03-09_andreaskoepf_oasst-1_12b_7000_sampling_noprefix_lottery.json) ([sampling code](https://github.com/Open-Assistant/oasst-model-eval/blob/3d71f3be100c05cd8ddb568365e036a29fbff8c7/model_eval/manual/sampling_report.py)).
- **License:** Apache 2.0
- **Contact:** [Open-Assistant Discord](https://ykilcher.com/open-assistant-discord)

## Prompting

Two special tokens are used to mark the beginning of user and assistant turns:
`<|prompter|>` and `<|assistant|>`. Each turn ends with a `<|endoftext|>` token.

Input prompt example:
```
<|prompter|>What is a meme, and what's the history behind this word?<|endoftext|><|assistant|>
```
The input ends with the `<|assistant|>` token to signal that the model should 
start generating the assistant reply.


Example of generated continuation (typical sampling 0.2):
```
A visual joke often accompanied by text that spreads rapidly from individual
to individual. The exact origin of the term "meme" is unclear, but it was
first used in the 1990s by Richard Dawkins in his book "The Selfish Gene."
He defined a meme as an idea, behavior, or style that is transmitted from
one person to another within a culture.

Dawkins' use of the term caught on among scholars and journalists, who began
to apply the concept to other types of cultural items such as advertisements,
fashion trends, and jokes. Over time, the term "meme" has come to be used
more generally to describe any social behavior that can be repeated and
altered by individuals. Today, the term is widely recognized and applied in
fields ranging from anthropology to psychology to marketing.<|endoftext|>
```

## Limitations

See limitations of Pythia 12B base model [here](https://huggingface.co/EleutherAI/pythia-12b-deduped#limitations-and-biases).

The model is known to fail horribly at answering math and coding questions.

Beware of hallucinations: Outputs are often factually wrong or misleading. 
Replies might look convincing (at first glance) while containing completely 
made up false statements.

This model is usable only for English conversations.