
# llama 13b mega merge v2

The following were merged with DARE using [https://github.com/martyn/safetensors-merge-supermario](https://github.com/martyn/safetensors-merge-supermario)

## Mergelist

```
meta-llama/Llama-2-13b-hf
ajibawa-2023/Code-13B
ajibawa-2023/Python-Code-13B
meta-math/MetaMath-13B-V1.0
rombodawg/LosslessMegaCoder-llama2-13b-mini
NousResearch/Nous-Hermes-Llama2-13b
allenai/digital-socrates-13b
migtissera/Synthia-13B
Gryphe/MythoLogic-L2-13b
allenai/tulu-2-dpo-13b
FPHam/Free_Sydney_13b_HF
FPHam/Free_Sydney_V2_13b_HF
FPHam/Sydney_Overthinker_13b_HF
KoboldAI/LLaMA2-13B-Psyfighter2
Undi95/Unholy-v1-12L-13B
athirdpath/Eileithyia-13B
athirdpath/Orca-2-13b-Alpaca-Uncensored
```

## Merge command

```
python hf_merge.py mergelist.txt 13b-merge-v2 -p 0.11 -lambda 2.1
```

## Notes

* seems to generalize instruct styles
* `p` and `lambda` are still a guess