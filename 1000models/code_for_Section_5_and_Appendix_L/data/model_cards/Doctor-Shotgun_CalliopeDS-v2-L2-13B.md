# CalliopeDS-v2-L2-13B

[EXL2 Quants](https://huggingface.co/Doctor-Shotgun/CalliopeDS-v2-L2-13B-exl2)

[GGUF Quants](https://huggingface.co/Doctor-Shotgun/Misc-Models)

This is a Llama 2-based model consisting of a merge of several models using PEFT adapters and SLERP merging:
- [PygmalionAI/pygmalion-2-13b](https://huggingface.co/PygmalionAI/pygmalion-2-13b)
- [NousResearch/Nous-Hermes-Llama2-13b](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b)
- [Doctor-Shotgun/llama-2-supercot-lora](https://huggingface.co/Doctor-Shotgun/llama-2-supercot-lora)
- [lemonilia/LimaRP-Llama2-13B-v3-EXPERIMENT](https://huggingface.co/lemonilia/LimaRP-Llama2-13B-v3-EXPERIMENT)
- [Undi95/Storytelling-v2-13B-lora](https://huggingface.co/Undi95/Storytelling-v2-13B-lora)

Charles Goddard's [mergekit](https://github.com/cg123/mergekit) repo was used to perform these operations.

The purpose of this merge was to create a model that excels at creative writing and roleplay while maintaining general intelligence and instruction-following capabilities. In testing, it has shown to be capable at producing descriptive and verbose responses while demonstrating a solid understanding of the context.

## Usage:
Due to this being a merge of multiple models, different prompt formats may work, but you can try the Alpaca instruction format of LIMARP v3:
```
### Instruction:
Character's Persona: {bot character description}

User's Persona: {user character description}

Scenario: {what happens in the story}

Play the role of Character. You must engage in a roleplaying chat with User below this line. Do not write dialogues and narration for User.

### Input:
User: {utterance}

### Response:
Character: {utterance}

### Input
User: {utterance}

### Response:
Character: {utterance}

(etc.)
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
## Message length control
Due to the inclusion of LimaRP v3, it is possible to append a length modifier to the response instruction sequence, like this:
```
### Input
User: {utterance}

### Response: (length = medium)
Character: {utterance}
```
This has an immediately noticeable effect on bot responses. The available lengths are: tiny, short, medium, long, huge, humongous, extreme, unlimited. The recommended starting length is medium. Keep in mind that the AI may ramble or impersonate the user with very long messages.
## Bias, Risks, and Limitations
The model will show biases similar to those observed in niche roleplaying forums on the Internet, besides those exhibited by the base model. It is not intended for supplying factual information or advice in any form. 
## Training Details
This model is a merge. Please refer to the link repositories of the merged models for details.