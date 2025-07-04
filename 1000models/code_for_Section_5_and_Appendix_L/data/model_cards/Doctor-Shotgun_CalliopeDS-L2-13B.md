# Model Card: CalliopeDS-L2-13B

This is a Llama 2-based model consisting of a merge of several models using a weight-adjusted TIES merge ([Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708)):
- [jondurbin/airoboros-l2-13b-2.2](https://huggingface.co/jondurbin/airoboros-l2-13b-2.2)
- [elinas/chronos-13b-v2](https://huggingface.co/elinas/chronos-13b-v2)
- [NousResearch/Nous-Hermes-Llama2-13b](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b)
- [lemonilia/limarp-llama2-v2](https://huggingface.co/lemonilia/limarp-llama2-v2)
- [PygmalionAI/pygmalion-2-13b](https://huggingface.co/PygmalionAI/pygmalion-2-13b)

Charles Goddard's [mergekit](https://github.com/cg123/mergekit) repo was used to perform these operations.

The purpose of this merge was to create a model that excels at creative writing and roleplay while maintaining general intelligence and instruction-following capabilities. In testing, it has shown to be capable at producing descriptive and verbose responses while demonstrating a solid understanding of the context.

## Usage:
Due to this being a merge of multiple models, different prompt formats may work, but you can try the Alpaca instruction format of the LIMARP v2:
```
### Instruction:
Character's Persona: {bot character description}

User's Persona: {user character description}

Scenario: {what happens in the story}

Play the role of Character. You must engage in a roleplaying chat with User below this line. Do not write dialogues and narration for User. Character should respond with messages of medium length.

### Input:
User: {utterance}

### Response:
Character: {utterance}
```
Or the Pygmalion/Metharme format:
```
<|system|>Enter RP mode. Pretend to be {{char}} whose persona follows:
{{persona}}

You shall reply to the user while staying in character, and generate long responses.
<|user|>Hello!<|model|>{model's response goes here}
```
The model was also tested using a system prompt with no instruction sequences:
```
Write Character's next reply in the roleplay between User and Character. Stay in character and write creative responses that move the scenario forward. Narrate in detail, using elaborate descriptions. The following is your persona:
{{persona}}
[Current conversation]
User: {utterance}
Character: {utterance}
```
## Bias, Risks, and Limitations
The model will show biases similar to those observed in niche roleplaying forums on the Internet, besides those exhibited by the base model. It is not intended for supplying factual information or advice in any form. 
## Training Details
This model is a merge. Please refer to the link repositories of the merged models for details.