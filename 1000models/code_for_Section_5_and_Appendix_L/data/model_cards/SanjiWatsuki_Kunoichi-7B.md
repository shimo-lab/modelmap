
![image/png](https://huggingface.co/SanjiWatsuki/Kunoichi-7B/resolve/main/assets/kunoichi.png)

<!-- description start -->
## Description

This repository hosts **Kunoichi-7B**, an general purpose model capable of RP. In both my testing and the benchmarks, Kunoichi is an extremely strong model, keeping the advantages of my previous models but gaining more intelligence. Kunoichi scores extremely well on [all benchmarks which correlate closely with ChatBot Arena Elo.](https://www.reddit.com/r/LocalLLaMA/comments/18u0tu3/benchmarking_the_benchmarks_correlation_with/)

| Model                | MT Bench | EQ Bench | MMLU   | Logic Test |
|----------------------|----------|----------|---------|-------------|
| GPT-4-Turbo         | 9.32     | -        | -       | -           |
| GPT-4               | 8.99     | 62.52    | 86.4    | 0.86        |
| **Kunoichi-7B**     | **8.14**     | **44.32**    | **64.9**    | **0.58**        |
| Starling-7B         | 8.09     | -        | 63.9    | 0.51        |
| Claude-2            | 8.06     | 52.14    | 78.5    | -           |
| Silicon-Maid-7B     | 7.96     | 40.44    | 64.7    | 0.54           |
| Loyal-Macaroni-Maid-7B | 7.95     | 38.66    | 64.9   | 0.57        |
| GPT-3.5-Turbo       | 7.94     | 50.28    | 70      | 0.57        |
| Claude-1            | 7.9       | -        | 77      | -           |
| Openchat-3.5        | 7.81     | 37.08    | 64.3    | 0.39        |
| Dolphin-2.6-DPO     | 7.74     | 42.88    | 61.9    | 0.53        |
| Zephyr-7B-beta      | 7.34     | 38.71    | 61.4    | 0.30        |
| Llama-2-70b-chat-hf | 6.86     | 51.56    | 63      | -           |
| Neural-chat-7b-v3-1 | 6.84     | 43.61    | 62.4    | 0.30        |

The model is intended to be used with up to an 8k context window. Using a NTK RoPE alpha of 2.6, the model can be used experimentally up to a 16k context window.

<!-- description end -->
<!-- prompt-template start -->
## Prompt template: Custom format, or Alpaca

### Alpaca:
```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:
```

### SillyTavern format:
I found the best SillyTavern results from using the Noromaid template. 

SillyTavern config files: [Context](https://files.catbox.moe/ifmhai.json), [Instruct](https://files.catbox.moe/ttw1l9.json).

Additionally, here is my highly recommended [Text Completion preset](https://huggingface.co/SanjiWatsuki/Loyal-Macaroni-Maid-7B/blob/main/Characters/MinP.json). You can tweak this by adjusting temperature up or dropping min p to boost creativity or raise min p to increase stability. You shouldn't need to touch anything else!


## WTF is Kunoichi-7B?

Kunoichi-7B is a SLERP merger between my previous RP model, Silicon-Maid-7B, and an unreleased model that I had dubbed "Ninja-7B". This model is the result of me attempting to merge an RP focused model which maintained the strengths of Silicon-Maid-7B but further increased the model's brain power. I sought to increase both MT-Bench and EQ-Bench without losing Silicon Maid's strong ability to follow SillyTavern character cards.

Ninja-7B was born from an attempt to turn [jan-hq/stealth-v1.2](https://huggingface.co/jan-hq/stealth-v1.2) into a viable model through mergers. Although none of the Ninja prototype models developed to a point where I was happy, it turned out to be a strong model to merge. Combined with Silicon-Maid-7B, this appeared to be a strong merger.

## Other Benchmarks


| Model | Average | AGIEval | GPT4All | TruthfulQA | Bigbench |
|---|---:|---:|---:|---:|---:|
| [**Kunoichi-7B**](https://huggingface.co/SanjiWatsuki/Kunoichi-7B)|**57.54**|  **44.99**|  74.86|     **63.72**|   46.58|
| [OpenPipe/mistral-ft-optimized-1218](https://huggingface.co/OpenPipe/mistral-ft-optimized-1218)| 56.85 | 44.74 | **75.6** | 59.89 | **47.17** |
| [Silicon-Maid-7B](https://huggingface.co/SanjiWatsuki/Silicon-Maid-7B) | 56.45|  44.74|  74.26|      61.5|   45.32|
| [mlabonne/NeuralHermes-2.5-Mistral-7B](https://huggingface.co/mlabonne/NeuralHermes-2.5-Mistral-7B) | 53.51 | 43.67 | 73.24 | 55.37 | 41.76 |
| [teknium/OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B)  | 52.42 | 42.75 | 72.99 | 52.99 | 40.94 |
| [openchat/openchat_3.5](https://huggingface.co/openchat/openchat_3.5) | 51.34 | 42.67 | 72.92 | 47.27 | 42.51 |
| [berkeley-nest/Starling-LM-7B-alpha](https://huggingface.co/berkeley-nest/Starling-LM-7B-alpha) | 51.16 | 42.06 | 72.72 | 47.33 | 42.53 |
| [HuggingFaceH4/zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) | 50.99 | 37.33 | 71.83 | 55.1 | 39.7 |