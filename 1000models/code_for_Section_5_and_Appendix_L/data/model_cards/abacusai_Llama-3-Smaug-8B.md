
# Llama-3-Smaug-8B

### Built with Meta Llama 3


![image/png](https://cdn-uploads.huggingface.co/production/uploads/64c14f95cac5f9ba52bbcd7f/OrcJyTaUtD2HxJOPPwNva.png)

This model was built using the Smaug recipe  for improving performance on real world multi-turn conversations applied to 
[meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct).

### Model Description

- **Developed by:** [Abacus.AI](https://abacus.ai)
- **License:** https://llama.meta.com/llama3/license/
- **Finetuned from model:** [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct).


## Evaluation

### MT-Bench

```
########## First turn ##########
                   score
model             turn
Llama-3-Smaug-8B 1   8.77500
Meta-Llama-3-8B-Instruct 1   8.31250
########## Second turn ##########
                   score
model             turn
Meta-Llama-3-8B-Instruct 2   7.8875 
Llama-3-Smaug-8B 2   7.8875
########## Average ##########
                 score
model
Llama-3-Smaug-8B  8.331250
Meta-Llama-3-8B-Instruct 8.10
```

| Model | First turn | Second Turn | Average |
| :---- | ---------: | ----------: | ------: |
| Llama-3-Smaug-8B | 8.78 | 7.89 | 8.33 |
| Llama-3-8B-Instruct | 8.31 |  7.89 | 8.10 |

This version of Smaug uses new techniques and new data compared to [Smaug-72B](https://huggingface.co/abacusai/Smaug-72B-v0.1), and more information will be released later on. For now, see the previous Smaug paper: https://arxiv.org/abs/2402.13228.