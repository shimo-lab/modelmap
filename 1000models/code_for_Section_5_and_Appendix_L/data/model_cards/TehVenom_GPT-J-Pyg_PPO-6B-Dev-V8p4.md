GPT-J-Pyg_PPO-6B [GPT-J Pygmalion Dev V8p4 + GPT-J PPO_HH]

GPT-J-Pyg_PPO-6B is an experimental model containing a parameter-wise 40/60 blend (weighted average PPO_HH:Pygmalion) of the weights of ppo_hh_gpt-j and Pygmalion-6b Dev V8p4.

-Intended Merge Value-

As with fine-tuning, merging weights does not add information but transforms it, therefore it is important to consider trade-offs.
Pyg_PPO combines ppo_hh_gpt-j and Pygmalion-6b; both technical
achievements are blended with the intent to elevate the strengths of
both. Datasets of both are linked below to assist in exploratory speculation on which datasets in what quantity and configuration have
the largest impact on the usefulness of a model without the expense of
fine-tuning. Blend was done in FP32 and output in FP16.

-Intended Use-

Research purposes only, intended for responsible use.
Express a conversation in natural language, and Pyg_PPO will do the thing.
Try starting a two line prompt such as:
```
Bot: "Hello, how are you?"
You: "I am doing just fine, thank you."
```
Or any other
topic, and the model will carry on in this back and forth format.

Can also be used as a base to merge with other creative,
technical, or adventure themed models of the same class
(GPT-J & 6b NeoX) and parameter size (6b) to experiment with
the morphology of model weights based on the value added
by instruct.

Merge tested using KoboldAI with Nucleus Sampling Top-P set to 0.9, Temperature at 0.6, and Repetition Penalty at 1.1; extra samplers
disabled.

-Credits To-

Core Model:
https://huggingface.co/EleutherAI/gpt-j-6B
Author:
https://www.eleuther.ai/

Model1; 50% ppo_hh_gpt-j:
https://huggingface.co/reciprocate/ppo_hh_gpt-j

Author Repo:
https://huggingface.co/reciprocate

Related; CarperAI:
https://huggingface.co/CarperAI

Dataset is a variant of the Helpful Harmless assistant themed
dataset and Proximal Policy Optimization, specific datasets
used are unknown; listed repo datasets include:
https://huggingface.co/datasets/reciprocate/summarize_eval_ilql
https://huggingface.co/datasets/reciprocate/hh_eval_ilql

PPO explained:
https://paperswithcode.com/method/ppo
Potential HH-type datasets utilized:
https://huggingface.co/HuggingFaceH4
https://huggingface.co/datasets/Anthropic/hh-rlhf

Model2; 50% Pygmalion-6b:
https://huggingface.co/PygmalionAI/pygmalion-6b

Author Repo:
https://huggingface.co/PygmalionAI

Weight merge Script credit to Concedo:
https://huggingface.co/concedo

Model's card template credit to Digitous:
https://huggingface.co/digitous/GPT-R