
# LM-cocktail 10.7B v1


This is a 50%-50% model of the SOLAR model and meow.

https://huggingface.co/upstage/SOLAR-10.7B-Instruct-v1.0

https://huggingface.co/rishiraj/meow


who rank #1 and #2 among models <13B in the https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard by 2023/12/20.

# Alpaca Eval

I am thrilled to announce that ChatGPT has ranked LMCocktail 10.7B as the second best model next to GPT4 on AlpcaEval in my local community run. You can also check the leaderboard at [./alpaca_eval/chatgpt_fn_--SOLAR-10-7B-LMCocktail/](./alpaca_eval/chatgpt_fn_--SOLAR-10-7B-LMCocktail/)

```
                        win_rate  standard_error  n_total  avg_length
gpt4                       73.79            1.54      805        1365
SOLAR-10.7B-LMCocktail(new)73.45            1.56      804        1203
claude                     70.37            1.60      805        1082
chatgpt                    66.09            1.66      805         811
wizardlm-13b               65.16            1.67      805         985
vicuna-13b                 64.10            1.69      805        1037
guanaco-65b                62.36            1.71      805        1249
oasst-rlhf-llama-33b       62.05            1.71      805        1079
alpaca-farm-ppo-human      60.25            1.72      805         803
falcon-40b-instruct        56.52            1.74      805         662
text_davinci_003           50.00            0.00      805         307
alpaca-7b                  45.22            1.74      805         396
text_davinci_001           28.07            1.56      805         296
```


# Code

The LM-cocktail is novel technique for merging multiple models https://arxiv.org/abs/2311.13534

Code is backed up by this repo https://github.com/FlagOpen/FlagEmbedding.git

Merging scripts available under the [./scripts](./scripts) folder


# Result

The SOLAR model is the first model <30B that can answer this question from my test:

```
What will AI be like in the year 1010 A.D?
```

without hullicinating into 1010 A.D is a future time (like other llama2 models)

Models greater than that, like Yi-34B could answer this paradoxic question correctly as well, since it is huge enough.

### SOLAR 10.7B output

![img](./assets/SOLAR.png)

### LMCocktail 10.7B output1

![img](./assets/SOLAR_mixed.png)

### LMCocktail 10.7B output2

![img](./assets/SOLAR_mixed2.png)