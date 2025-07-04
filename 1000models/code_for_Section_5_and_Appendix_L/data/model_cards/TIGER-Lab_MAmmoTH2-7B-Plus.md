# 🦣 MAmmoTH2: Scaling Instructions from the Web

Project Page: [https://tiger-ai-lab.github.io/MAmmoTH2/](https://tiger-ai-lab.github.io/MAmmoTH2/)

Paper: [https://arxiv.org/pdf/2405.03548](https://arxiv.org/pdf/2405.03548)

Code: [https://github.com/TIGER-AI-Lab/MAmmoTH2](https://github.com/TIGER-AI-Lab/MAmmoTH2)


## Introduction
Introducing 🦣 MAmmoTH2, a game-changer in improving the reasoning abilities of large language models (LLMs) through innovative instruction tuning. By efficiently harvesting 10 million instruction-response pairs from the pre-training web corpus, we've developed MAmmoTH2 models that significantly boost performance on reasoning benchmarks. For instance, MAmmoTH2-7B (Mistral) sees its performance soar from 11% to 36.7% on MATH and from 36% to 68.4% on GSM8K, all without training on any domain-specific data. Further training on public instruction tuning datasets yields MAmmoTH2-Plus, setting new standards in reasoning and chatbot benchmarks. Our work presents a cost-effective approach to acquiring large-scale, high-quality instruction data, offering a fresh perspective on enhancing LLM reasoning abilities.

|      | **Base Model** | **MAmmoTH2**                                                 | **MAmmoTH2-Plus**                                                  |
|:-----|:---------------------|:-------------------------------------------------------------------|:------------------------------------------------------------------|
| 7B   | Mistral              | 🦣 [MAmmoTH2-7B](https://huggingface.co/TIGER-Lab/MAmmoTH2-7B)      | 🦣 [MAmmoTH2-7B-Plus](https://huggingface.co/TIGER-Lab/MAmmoTH2-7B-Plus)     |
| 8B   | Llama-3             | 🦣 [MAmmoTH2-8B](https://huggingface.co/TIGER-Lab/MAmmoTH2-8B)      | 🦣 [MAmmoTH2-8B-Plus](https://huggingface.co/TIGER-Lab/MAmmoTH2-8B-Plus)     |
| 8x7B | Mixtral              | 🦣 [MAmmoTH2-8x7B](https://huggingface.co/TIGER-Lab/MAmmoTH2-8x7B)  | 🦣 [MAmmoTH2-8x7B-Plus](https://huggingface.co/TIGER-Lab/MAmmoTH2-8x7B-Plus) |
## Training Data
Please refer to https://huggingface.co/datasets/TIGER-Lab/WebInstructSub for more details.

![Project Framework](webinstruct.png)

## Training Procedure
The models are fine-tuned with the WEBINSTRUCT dataset using the original Llama-3, Mistral and Mistal models as base models. The training procedure varies for different models based on their sizes. Check out our paper for more details.

## Evaluation
The models are evaluated using open-ended and multiple-choice math problems from several datasets. Here are the results:

| **Model**                              | **TheoremQA** | **MATH** | **GSM8K** | **GPQA** | **MMLU-ST** | **BBH** | **ARC-C** | **Avg** |
|:---------------------------------------|:--------------|:---------|:----------|:---------|:------------|:--------|:----------|:--------|
| **MAmmoTH2-7B** (Updated)              | 29.0          | 36.7     | 68.4      | 32.4     | 62.4        | 58.6    | 81.7      | 52.7    |
| **MAmmoTH2-8B** (Updated)              | 30.3          | 35.8     | 70.4      | 35.2     | 64.2        | 62.1    | 82.2      | 54.3    |
| **MAmmoTH2-8x7B**                      | 32.2          | 39.0     | 75.4      | 36.8     | 67.4        | 71.1    | 87.5      | 58.9    |
| **MAmmoTH2-7B-Plus** (Updated)         | 31.2          | 46.0     | 84.6      | 33.8     | 63.8        | 63.3    | 84.4      | 58.1    |
| **MAmmoTH2-8B-Plus** (Updated)         | 31.5          | 43.0     | 85.2      | 35.8     | 66.7        | 69.7    | 84.3      | 59.4    |
| **MAmmoTH2-8x7B-Plus**                 | 34.1          | 47.0     | 86.4      | 37.8     | 72.4        | 74.1    | 88.4      | 62.9    |

To reproduce our results, please refer to https://github.com/TIGER-AI-Lab/MAmmoTH2/tree/main/math_eval.


## Usage
You can use the models through Huggingface's Transformers library. Use the pipeline function to create a text-generation pipeline with the model of your choice, then feed in a math problem to get the solution.
Check our Github repo for more advanced use: https://github.com/TIGER-AI-Lab/MAmmoTH2

## Limitations
We've tried our best to build math generalist models. However, we acknowledge that the models' performance may vary based on the complexity and specifics of the math problem. Still not all mathematical fields can be covered comprehensively.


## Citation
If you use the models, data, or code from this project, please cite the original paper:

```
@article{yue2024mammoth2,
  title={MAmmoTH2: Scaling Instructions from the Web},
  author={Yue, Xiang and Zheng, Tuney and Zhang, Ge and Chen, Wenhu},
  journal={arXiv preprint arXiv:2405.03548},
  year={2024}
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_TIGER-Lab__MAmmoTH2-7B-Plus)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |21.22|
|IFEval (0-Shot)    |55.75|
|BBH (3-Shot)       |18.93|
|MATH Lvl 5 (4-Shot)|16.09|
|GPQA (0-shot)      | 4.03|
|MuSR (0-shot)      |10.11|
|MMLU-PRO (5-shot)  |22.41|

