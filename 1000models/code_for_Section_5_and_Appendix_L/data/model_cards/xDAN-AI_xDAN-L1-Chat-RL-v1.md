
<div style="display: flex; justify-content: center; align-items: center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/643197ac288c9775673a01e9/tVAcwKkIH5vkfzqgqHeHi.png" style="width: 45%;">
</div
>


<p align="center">
  <big><b>Top 1 Performer on MT-bench🏆</b
></big>
</p>

<p align="center">
  <strong>**The first top model which is performance at Humanalities, Coding and Writing with 7b. **</strong>
</p>

<p
 align="center"
  <a href="The TOP1 MT-Bench Model">xDAN-AI</a> •
>
  <a href="https://discord.gg/7NrMX5AK">Discord</a> •
  <a href="https://twitter.com/shootime007">Twitter</a> •
  <a href="https://huggingface.co/xDAN-AI">Huggingface</a>
</p>

<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/643197ac288c9775673a01e9/QANDZApzpTHM6sBsjmdew.png" alt="Image" width="50%">
</p>



## Outperformer GPT3.5turbo & Claude-v1

![image/png
](https://cdn-uploads.huggingface.co/production/uploads/643197ac288c9775673a01e9/c9btBdopOpM06VuBsvRxq.png)

## Touch nearby GPT4 on MT-Bench

![image/png](https://cdn-uploads.huggingface.co/production/uploads/643197ac288c9775673a01e9/QhcLDoOGZznkvy0v4FsUY.png)


**########## First turn ##########**
| model              | turn | score    | size
|--------------------|------|----------|--------
| gpt-4              | 1    | 8.95625  |  -
| **xDAN-L1-Chat-RL-v1** | 1    | **8.87500**  |  **7b**
| xDAN-L2-Chat-RL-v2 | 1    | 8.78750  |  30b
| claude-v1          | 1    | 8.15000  |  -
| gpt-3.5-turbo      | 1    | 8.07500  |  20b
| vicuna-33b-v1.3    | 1    | 7.45625  |  33b
| wizardlm-30b       | 1    | 7.13125  |  30b
| oasst-sft-7-llama-30b | 1 | 7.10625  |  30b
| Llama-2-70b-chat   | 1    | 6.98750  |  70b


########## Second turn ##########
| model              | turn | score     | size
|--------------------|------|-----------|--------
| gpt-4              | 2    | 9.025000  |  -
| xDAN-L2-Chat-RL-v2 | 2    | 8.087500  |  30b
| **xDAN-L1-Chat-RL-v1** | 2   | **7.825000**  |   **7b**
| gpt-3.5-turbo      | 2    | 7.812500  |  20b
| claude-v1          | 2    | 7.650000  |  -
| wizardlm-30b       | 2    | 6.887500  |  30b
| vicuna-33b-v1.3    | 2    | 6.787500  |  33b
| Llama-2-70b-chat   | 2    | 6.725000  |  70b

########## Average turn##########
| model              | score     | size
|--------------------|-----------|--------
| gpt-4              | 8.990625  |  -
| xDAN-L2-Chat-RL-v2 | 8.437500  |  30b
| **xDAN-L1-Chat-RL-v1** | **8.350000**  |  **7b**
| gpt-3.5-turbo      | 7.943750  |  20b
| claude-v1          | 7.900000  |  -
| vicuna-33b-v1.3    | 7.121875  |  33b
| wizardlm-30b       | 7.009375  |  30b
| Llama-2-70b-chat   | 6.856250  |  70b


## LM-Evaluation-Harness

| Task         | Score  |
|--------------|--------|
| Average | 68.38  |
| ARC     | 66.3  |
| HellaSwag        | 85.81  |
| MMLU    | 63.21  |
| TruthfulQA   | 56.7   |
| Winogrande         | 78.85  |
| GSM8K   | 59.44  |




### Prompt Template(Alpaca)
You are a helpful assistant named DAN. You are an expert in worldly knowledge, skilled in employing a probing questioning strategy, 
and you carefully consider each step before providing answers. 
\n\n### Instruction:\n{instruction}\n\n### Response:


### Dataset:
1. Selected from OpenOrca
2. Intel Orca-DPO-Pairs
3. Privately Crafted Dataset

### Training:
1. SFT with Mixed dataset from OpenOrca & Intel
2. The DPO-v2 dataset  
3. The DPO-v2 Trainer

## Created By xDAN-AI at 2023-12-15
## Eval by FastChat: https://github.com/lm-sys/FastChat.git

 
## Disclaimer
We employ rigorous data compliance validation algorithms throughout the training of our language model to ensure the highest level of compliance. However, due to the intricate nature of data and the wide range of potential usage scenarios for the model, we cannot guarantee that it will consistently produce accurate and sensible outputs. Users should be aware of the possibility of the model generating problematic results. Our organization disclaims any responsibility for risks or issues arising from misuse, improper guidance, unlawful usage, misinformation, or subsequent concerns regarding data security.

## About xDAN-AI
xDAN-AI represents the forefront of Silicon-Based Life Factory technology. For comprehensive information and deeper insights into our cutting-edge technology and offerings, please visit our website: https://www.xdan.ai.