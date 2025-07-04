
# OPT-2.7B-Nerybus-Mix

This is an experimental model containing a ***parameter-wise 50/50 blend (weighted average)*** of the weights of *NerysV2-2.7B* and *ErebusV1-2.7B*
Preliminary testing produces pretty coherent outputs, it appears to retain the NSFWness of Erebus but with a Nerys-esque twist in terms of prose.

# License
The two models used for this blend, *NerysV2-2.7B* and *ErebusV1-2.7B* are made by **Mr. Seeker**.
- https://huggingface.co/KoboldAI/OPT-2.7B-Erebus  
- https://huggingface.co/KoboldAI/OPT-2.7B-Nerys-v2  
The base OPT-2.7B model is licensed under the OPT-175B license, Copyright (c) Meta Platforms, Inc. All Rights Reserved. 

# Evaluation Results
As the original datasets used for the source models are not publically available, I use my own datasets for this evaluation, which may not provide accurate comparison.

Eval parameters: 32000 characters extracted from the middle of the corpus, tested in blocks of 1024 tokens each, same dataset used for each test batch.

```
Literotica Dataset Eval (Randomly selected stories)
{'eval_loss': 2.571258306503296, 'name': 'Concedo_OPT-2.7B-Nerybus-Mix'}
{'eval_loss': 2.5491442680358887, 'name': 'KoboldAI_OPT-2.7B-Erebus'}
{'eval_loss': 2.6158597469329834, 'name': 'KoboldAI_OPT-2.7B-Nerys'}
{'eval_loss': 2.614469051361084, 'name': 'facebook_opt-2.7b'}
{'eval_loss': 2.4960227012634277, 'name': '(Unreleased 2.7B ModronAI Model)'}

ASSTR Dataset Eval (Randomly selected stories)
{'eval_loss': 2.664412498474121, 'name': 'Concedo_OPT-2.7B-Nerybus-Mix'}
{'eval_loss': 2.6451029777526855, 'name': 'KoboldAI_OPT-2.7B-Erebus'}
{'eval_loss': 2.7259647846221924, 'name': 'KoboldAI_OPT-2.7B-Nerys'}
{'eval_loss': 2.6675195693969727, 'name': 'facebook_opt-2.7b'}
{'eval_loss': 2.962111473083496, 'name': '(Unreleased 2.7B ModronAI Model)'}

Sexstories Dataset Eval (Random highly rated stories)
{'eval_loss': 2.2352423667907715, 'name': 'Concedo_OPT-2.7B-Nerybus-Mix'}
{'eval_loss': 2.194378137588501, 'name': 'KoboldAI_OPT-2.7B-Erebus'}
{'eval_loss': 2.307469129562378, 'name': 'KoboldAI_OPT-2.7B-Nerys'}
{'eval_loss': 2.293961763381958, 'name': 'facebook_opt-2.7b'}
{'eval_loss': 2.0103421211242676, 'name': '(Unreleased 2.7B ModronAI Model)'}

Harry Potter Dataset Eval (Canon books)
{'eval_loss': 2.473742961883545, 'name': 'Concedo_OPT-2.7B-Nerybus-Mix'}
{'eval_loss': 2.480600357055664, 'name': 'KoboldAI_OPT-2.7B-Erebus'}
{'eval_loss': 2.506237506866455, 'name': 'KoboldAI_OPT-2.7B-Nerys'}
{'eval_loss': 2.5074169635772705, 'name': 'facebook_opt-2.7b'}
{'eval_loss': 2.273703098297119, 'name': '(Unreleased 2.7B ModronAI Model)'}

Star Wars Dataset Eval (Rogue One Novel)
{'eval_loss': 2.5031676292419434, 'name': 'Concedo_OPT-2.7B-Nerybus-Mix'}
{'eval_loss': 2.5239150524139404, 'name': 'KoboldAI_OPT-2.7B-Erebus'}
{'eval_loss': 2.526801586151123, 'name': 'KoboldAI_OPT-2.7B-Nerys'}
{'eval_loss': 2.473283529281616, 'name': 'facebook_opt-2.7b'}
{'eval_loss': 2.955465793609619, 'name': '(Unreleased 2.7B ModronAI Model)'}

```

It is recommend to use this model with the KoboldAI software. All feedback and comments can be directed to Concedo on the KoboldAI discord.
