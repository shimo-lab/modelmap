
| Model                | MT Bench | EQ Bench | MMLU   | Logic Test |
|----------------------|----------|----------|---------|-------------|
| GPT-4-Turbo         | 9.32     | -        | -       | -           |
| GPT-4               | 8.99     | 62.52    | 86.4    | 0.86        |
| **Kunoichi-DPO-v2-7B** | **8.51**     | **42.18**    | **64.94**| **0.58**        |
| Mixtral-8x7B-Instruct| 8.30     | 44.81    | 70.6    | 0.75        |
| **Kunoichi-DPO-7B** | **8.29**     | **41.60**    | **64.83**    | **0.59**        |
| **Kunoichi-7B**     | **8.14**     | **44.32**    | **64.9**    | **0.58**            |
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

| Model | Average | AGIEval | GPT4All | TruthfulQA | Bigbench |
|---|---:|---:|---:|---:|---:|
| **Kunoichi-DPO-7B**|**58.4**|  45.08 |  74|     66.99|   47.52|
| **Kunoichi-DPO-v2-7B**|**58.31**|  44.85|  75.05|     65.69|   47.65|
| [Kunoichi-7B](https://huggingface.co/SanjiWatsuki/Kunoichi-7B)|57.54|  44.99|  74.86|     63.72|   46.58|
| [OpenPipe/mistral-ft-optimized-1218](https://huggingface.co/OpenPipe/mistral-ft-optimized-1218)| 56.85 | 44.74 | 75.6 | 59.89 | 47.17 |
| [Silicon-Maid-7B](https://huggingface.co/SanjiWatsuki/Silicon-Maid-7B) | 56.45|  44.74|  74.26|      61.5|   45.32|
| [mlabonne/NeuralHermes-2.5-Mistral-7B](https://huggingface.co/mlabonne/NeuralHermes-2.5-Mistral-7B) | 53.51 | 43.67 | 73.24 | 55.37 | 41.76 |
| [teknium/OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B)  | 52.42 | 42.75 | 72.99 | 52.99 | 40.94 |
| [openchat/openchat_3.5](https://huggingface.co/openchat/openchat_3.5) | 51.34 | 42.67 | 72.92 | 47.27 | 42.51 |
| [berkeley-nest/Starling-LM-7B-alpha](https://huggingface.co/berkeley-nest/Starling-LM-7B-alpha) | 51.16 | 42.06 | 72.72 | 47.33 | 42.53 |
| [HuggingFaceH4/zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) | 50.99 | 37.33 | 71.83 | 55.1 | 39.7 |

| Model                       | AlpacaEval2 | Length |
| --------------------------- | ----------- | ------ |
| GPT-4                       | 23.58%      | 1365   |
| GPT-4 0314                  | 22.07%      | 1371   |
| Mistral Medium              | 21.86%      | 1500   |
| Mixtral 8x7B v0.1           | 18.26%      | 1465   |
| **Kunoichi-DPO-v2**         | **17.19%**  | 1785   |
| Claude 2                    | 17.19%      | 1069   |
| Claude                      | 16.99%      | 1082   |
| Gemini Pro                  | 16.85%      | 1315   |
| GPT-4 0613                  | 15.76%      | 1140   |
| Claude 2.1                  | 15.73%      | 1096   |
| Mistral 7B v0.2             | 14.72%      | 1676   |
| GPT 3.5 Turbo 0613          | 14.13%      | 1328   |
| LLaMA2 Chat 70B             | 13.87%      | 1790   |
| LMCocktail-10.7B-v1         | 13.15%      | 1203   |
| WizardLM 13B V1.1           | 11.23%      | 1525   |
| Zephyr 7B Beta              | 10.99%      | 1444   |
| OpenHermes-2.5-Mistral (7B) | 10.34%      | 1107   |
| GPT 3.5 Turbo 0301          | 9.62%       | 827    |
| **Kunoichi-7B**             | **9.38%**   | 1492   |
| GPT 3.5 Turbo 1106          | 9.18%       | 796    |
| GPT-3.5                     | 8.56%       | 1018   |
| Phi-2 DPO                   | 7.76%       | 1687   |
| LLaMA2 Chat 13B             | 7.70%       | 1513   |