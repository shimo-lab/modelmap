The LLaMA based Pygmalion-7b model:

https://huggingface.co/PygmalionAI/pygmalion-7b

Merged alongside lmsys's Vicuna v1.1 deltas: 

https://huggingface.co/lmsys/vicuna-13b-delta-v1.1

This merge was done using an weighted average merge strategy, and the end result is a model composed of:

Pygmalion-7b [60%] + LLaMA Vicuna v1.1 [40%] 


This was done under request, but the end result is intended to lean heavily towards Pygmalion's chatting + RP tendencies, and to inherit some of Vicuna's Assistant / Instruct / Helpful properties.

Due to the influence  of Pygmalion, this model will very likely generate content that is considered NSFW.

The specific prompting is unknown, but try Pygmalion's prompt styles first, 
then a mix of the two to see what brings most interesting results.

Treat this as a normal HF Transformers model.