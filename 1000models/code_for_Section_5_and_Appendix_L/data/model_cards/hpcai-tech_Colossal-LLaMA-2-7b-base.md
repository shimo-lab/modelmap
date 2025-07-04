
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->
<div align="center">
<h1>
  Colossal-LLaMA-2-7B
</h1>
</div>

<div align="center">
  🎉 We released Colossal-LLaMA-2-7B-base based on LLaMA-2 !!
</div>

<div align="center">
  ｜<a href="https://github.com/hpcaitech/ColossalAI/tree/main/applications/Colossal-LLaMA-2" target="_blank">🔥 GitHub </a> | 
  <a href="https://modelscope.cn/models/colossalai/Colossal-LLaMA-2-7b-base/summary" target="_blank">👾 Modelscope</a>｜
  <a href="https://github.com/hpcaitech/public_assets/tree/main/colossalai/contact/slack" target="_blank">😊 Slack</a>｜
  <a href="https://raw.githubusercontent.com/hpcaitech/public_assets/main/colossalai/img/WeChat.png" target="_blank">💬 WeChat</a>｜
</div>

<div align="center">
<h1>
<img src="https://github.com/hpcaitech/public_assets/blob/main/applications/colossal-llama-2/colossalllam2.jpg?raw=true" width=800/>
</h1>
</div>

# Table of Contents
- [Model Introduction](#model-introducation)
- [Usage](#usage)
- [Performance Evaluation](#performance-evaluation)
- [Technical Insights](#technical-insights)
  - [Data](#data)
  - [Tokenizer](#tokenizer)
  - [Training Logs](#training-logs)
  - [Training Strategy](#training-strategy)
    - [Multi-stage Training](#multi-stage-training)
    - [Bucket-based Training](#bucket-based-training)
- [Limitations](#limitations)
- [Citations](#citations)


# Model Introduction
The [Colossal-AI](https://github.com/hpcaitech/ColossalAI) team has introduced the **open-source** model **Colossal-LLaMA-2-7B-base**. This model, a derivation of LLaMA-2, has undergone continual pre-training involving approximately 8.5 billion tokens over a duration of 15 hours with 64 A800 GPUs. At a cost of **less than $1,000**, you can achieve results **similar to those that cost millions of dollars to pretrain from scratch**. It is licensed under the LLaMA-2 license and [Apache 2.0 License](https://github.com/hpcaitech/ColossalAI/blob/main/LICENSE) **without any additional commercial use restrictions**. This solution can also be used to build models of specific domain knowledge or tasks.

Colossal-LLaMA-2-7B-base is designed to accommodate both the Chinese and English languages, featuring an expansive context window spanning 4096 tokens. Remarkably, it has exhibited exceptional performance when benchmarked against models of equivalent scale in standard Chinese and English evaluation metrics, including C-Eval and MMLU, among others. 


# Usage
To load Colossal-LLaMA-2-7B-base model using Transformers, use the following code:
```Python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("hpcai-tech/Colossal-LLaMA-2-7b-base", device_map="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("hpcai-tech/Colossal-LLaMA-2-7b-base", trust_remote_code=True)
input = "明月松间照，\n\n->\n\n"
inputs = tokenizer(input, return_tensors='pt')
inputs = inputs.to('cuda:0')
pred = model.generate(**inputs,
                        max_new_tokens=512,
                        do_sample=True,
                        temperature=0.3,
                        top_k=50,
                        top_p=0.95,
                        num_return_sequences=1)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True)[len(input):])
```


# Performance Evaluation
### Performance Evaluation
We conducted comprehensive evaluation on 4 datasets and compare our Colossal-Llama-2-7b-base model with various models.

- We use 5-shot for MMLU and calculate scores based on the logits of first predicted token.
- We use 5-shot for CMMLU and calculate scores based on the logits of first predicted token.
- We use 5-shot for AGIEval and only calculate scores for 4-choice questions using a combination metric of exact match and the logits of first predicted token. If any of the exact match or logits of first predicted token is correct, the model will get the score.
- We use 0-shot for GAOKAO-Bench and only calculate scores for 4-choice questions based on the logits of first predicted token.
- The generation config for all dataset is greedy search.
- We also provided CEval scores from its latest leaderboard or the official repository of the model.

More details about metrics can be found in [Metrics](https://github.com/hpcaitech/ColossalAI/tree/main/applications/ColossalEval#metrics).

|                                |  Backbone  | Tokens Consumed |  |         MMLU         |     CMMLU     | AGIEval | GAOKAO | CEval  |
| :----------------------------: | :--------: | :-------------: | :------------------: | :-----------: | :-----: | :----: | :----: | :----------------------------: |
|                                |     -      |        -        |                |        5-shot        |    5-shot     | 5-shot  | 0-shot | 5-shot |
|          Baichuan-7B           |     -      |      1.2T       |             |    42.32 (42.30)     | 44.53 (44.02) |  38.72  | 36.74  | 42.80  |
|       Baichuan2-7B-Base        |     -      |      2.6T       |             |    46.97 (54.16)     | 57.67 (57.07) |  45.76  | 52.60  | 54.00  |
|           ChatGLM-6B           |     -      |      1.0T       |             |    39.67 (40.63)     |   41.17 (-)   |  40.10  | 36.53  | 38.90  |
|          ChatGLM2-6B           |     -      |      1.4T       |             |    44.74 (45.46)     |   49.40 (-)   |  46.36  | 45.49  | 51.70  |
|          InternLM-7B           |     -      |        -        |                |    46.70 (51.00)     |   52.00 (-)   |  44.77  | 61.64  | 52.80  |
|            Qwen-7B (original)             |     -      |      2.2T       |             | 54.29 (56.70) | 56.03 (58.80) |  52.47  | 56.42  | 59.60  |
|            Qwen-7B             |     -      |      2.4T       |             | 58.33 (58.20) | 62.54 (62.20) |  64.34  | 74.05 | 63.50 |
|                                |            |                 |                 |                      |               |         |        |        |
|           Llama-2-7B           |     -      |      2.0T       |             |    44.47 (45.30)     |   32.97 (-)   |  32.60  | 25.46  |   -    |
| Linly-AI/Chinese-LLaMA-2-7B-hf | Llama-2-7B |      1.0T       |             |        37.43         |     29.92     |  32.00  | 27.57  |   -    |
| wenge-research/yayi-7b-llama2  | Llama-2-7B |        -        |                |        38.56         |     31.52     |  30.99  | 25.95  |   -    |
| ziqingyang/chinese-llama-2-7b  | Llama-2-7B |        -        |                |        33.86         |     34.69     |  34.52  | 25.18  |  34.2  |
| TigerResearch/tigerbot-7b-base | Llama-2-7B |      0.3T       |             |        43.73         |     42.04     |  37.64  | 30.61  |   -    |
|  LinkSoul/Chinese-Llama-2-7b   | Llama-2-7B |        -        |                |        48.41         |     38.31     |  38.45  | 27.72  |   -    |
|       FlagAlpha/Atom-7B        | Llama-2-7B |      0.1T       |             |        49.96         |     41.10     |  39.83  | 33.00  |   -    |
|  |  |  |  |  |  |  |  |  |
|    **Colossal-LLaMA-2-7b-base**    | Llama-2-7B |      **0.0085T**      |            |        53.06         |     49.89     |  51.48  | 58.82  |  50.20  |

> The score in parentheses corresponds to the scores in the official repository of the model.
>
> We use zero-shot for ChatGLM models.
>
> To evaluate Qwen-7B on dataset MMLU, the prompt would be "xxx Answer:"(remove the space after ":") and we calculate the logits over " A", " B", " C" and " D" for Qwen-7B. Both the original and updated versions of Qwen-7B tend to be much more deterministic than other models. For example, the logits over " A" can be `-inf` and softmax would be exact `0`.
>
> For other models and other dataset, we calculate logits over "A", "B", "C" and "D".

❗️ More details of the evaluation methods and reproduction of the results, please refer to [ColossalEval](https://github.com/hpcaitech/ColossalAI/tree/main/applications/ColossalEval).


# Technical Insights
In order to enhance LLaMA-2's capabilities for understanding and generating Chinese content, The [Colossal-AI](https://github.com/hpcaitech/ColossalAI) team proposes the continuation of pre-training the LLaMA-2 model using both Chinese and English corpora.

## Data
Large language models such as LLaMA-2 have undergone training using a heterogeneous blend of high-quality datasets, yielding promising outcomes. Enhancing LLaMA-2's performance for the Chinese corpus, while preserving its proficiency in English, critically hinges on two pivotal factors: the composition of the dataset, which encompasses both English and Chinese content, and the quality of each constituent dataset.

The following figure shows the data processing pipeline conducted for Colossal-LLaMA-2.
<p id="Colossal-LLaMA-2-data-processing-pipeline" align="center">
<img src="https://github.com/hpcaitech/public_assets/blob/main/applications/colossal-llama-2/data_processing_pipeline.jpeg?raw=true" width=800/>
</p>

❗️**Important**: We will open-source our data-processing toolkit soon, stay tuned!

## Tokenizer
The original LLaMA-2 vacabulary comprises fewer than a thousand Chinese characters, thus proves inadequate for encoding comprehensive Chinese texts effectively. Secondly, the utilization of byte tokens presents a challenge for transformer encoders to capture the semantic nuances of Chinese characters.

To address the above issues, we extend LLaMA-2 vocabulary from 32,000 to 69,104. To adapt the LLaMA-2 model for use with the Colossal-LLaMA-2 tokenizer, we initialize the new word embeddings by calculating the mean values from the original LLaMA-2 embeddings and subsequently append these new rows to the end of the original embedding matrices.

Advantages of extending vocabulary size:
* Improve the compression rate of string sequence encoding.
* Enhance the integrity of information.
* Enable encoded sequences to contain more valuable information, thereby theoretically enhancing the ability for chapter-level encoding.

Advantages of large vocabulary size under low-resource settings:
* The presence of numerous unused tokens can be attributed to the limited training dataset, where an excessive number of tokens might not have been effectively learned.
* Excessive vocabulary expansion leads to an increase in embedding-related parameters, resulting in higher memory usage, which, in turn, affects the efficiency of the training process.

To balance both sides, we finally construct our vocabulary with size 69,104. The following table below presents a comparison of various models at the 7B level.

| Model | Vocabulary Size | Compression Rate | Average Length of Samples (token-level) |
| :-----------: | :---------: | :----: | :----: |
| **Colossal-LLaMA-2** | **69104** | **0.659** | **73.682** |
| LLaMA-2-7B | 32000 | 1.205 | 134.689 |
| Atom-7B | 65000 | 0.634 | 70.915 |
| Baichuan-7B | 64000 | 0.678 | 75.857 |
| Baichuan2-7B-base | 125696 | 0.570 | 63.761 |
| Chatglm2-6B | 64789 | 0.645 | 72.178 |
| InternLM-7B | 103168 | 0.566 | 63.349 |
| Qwen-7B | 151643 | 0.578 | 64.703 |
| Tigerbot-7B-base | 60515 | 0.630 | 70.515 |
| Yayi-7B-llama2 | 32005 | 1.214 | 135.689 |
| Chinese-llama-2-7b | 55296 | 0.668 | 74.690 |
| Chinese-Falcon-7B | 90046 | 0.669 | 74.858 |
| LinkSoul-Chinese-Llama-2-7b | 40076 | 0.958 | 107.089 |
| Ziya-LLaMA-13B-v1.1 | 39410 | 0.958 | 107.074 |

## Training Logs
Here are the training logs for the our experiment:
<p id="Colossal-LLaMA-2-Multi-stage-training" align="center">
<img src="https://github.com/hpcaitech/public_assets/blob/main/applications/colossal-llama-2/trainingLossBySteps.jpeg?raw=true" width=600/>
</p>
<p id="Colossal-LLaMA-2-Multi-stage-training" align="center">
<img src="https://github.com/hpcaitech/public_assets/blob/main/applications/colossal-llama-2/trainingLossByTokens.jpeg?raw=true" width=600/>
</p>


## Training Strategy
### Multi-stage Training
In order to enhance the model's performance and harness the full potential of the original LLaMA-2, we have developed a multi-stage training strategy. This strategy is designed to systematically unlock the model's capabilities over a series of stages. 

Therefore, we have divided the training process into three stages:
* Large-scale pre-training stage (Conducted by LLaMA-2): This initial stage is aimed at establishing the model's foundational capabilities from the ground up. It necessitates the use of a substantial dataset comprising no less than 1 trillion tokens.
* Chinese knowledge injection stage: In this stage, we introduce Chinese knowledge into the model. It requires access to a high-quality dataset rich in comprehensive knowledge relevant to the Chinese language.
* Knowledge replay stage: Knowledge is replayed through a question-answering (QA) mechanism, encompassing both the Chinese and English domains.

Following the completion of this multi-stage training process, the model exhibits notable improvements in performance across both English and Chinese benchmarks.

The following figure illustrates the three stages for training Colossal-LLaMA-2. 

<p id="Colossal-LLaMA-2-Multi-stage-training" align="center">
<img src="https://github.com/hpcaitech/public_assets/blob/main/applications/colossal-llama-2/multi-stage-training.png?raw=true" width=600/>
</p>

### Bucket-based Training
Our experiments have revealed that the distributions within the training dataset, as well as the arrangement of various topic-related data points, significantly impact the overall performance of the model, particularly in the context of continual pre-training of LLaMA-2.

In an effort to achieve a more balanced distribution and exert control over the dataset's ordering, we have adopted a method where we divide each sub-dataset into discrete bins. These bins are then combined to construct individual data buckets, with one bin contributed by each sub-dataset.

For more details, please refer to our [Github](https://github.com/hpcaitech/ColossalAI/tree/main/applications/Colossal-LLaMA-2).


# Limitations
Colossal-LLaMA-2-7B is a derivation of LLaMA-2 that carries risks with use. Testing conducted to date has been exclusively performed in English and Chinese languages, and it is important to acknowledge that it could not encompass all possible scenarios. Same as other LLMs, it is impossible to predict the potential outcomes of Colossal-LLaMA-2-7B-base in advance. In certain situations, Colossal-LLaMA-2-7B-base may generate responses that are inaccurate, biased, or otherwise poisonous. Consequently, prior to deploying any applications powered by Colossal-LLaMA-2-7B-base, it is imperative for developers to engage in safety testing and tuning tailored the model to meet the specific requirements of their applications.

# Citations
```bibtex
@article{bian2021colossal,
    title={Colossal-AI: A Unified Deep Learning System For Large-Scale Parallel Training},
    author={Bian, Zhengda and Liu, Hongxin and Wang, Boxiang and Huang, Haichen and Li, Yongbin and Wang, Chuanrui and Cui, Fan and You, Yang},
    journal={arXiv preprint arXiv:2110.14883},
    year={2021}
}
```
```bibtex
@misc{touvron2023llama,
    title={Llama 2: Open Foundation and Fine-Tuned Chat Models}, 
    author={Hugo Touvron and Louis Martin and Kevin Stone and Peter Albert and Amjad Almahairi and Yasmine Babaei and Nikolay Bashlykov and Soumya Batra and Prajjwal Bhargava and Shruti Bhosale and Dan Bikel and Lukas Blecher and Cristian Canton Ferrer and Moya Chen and Guillem Cucurull and David Esiobu and Jude Fernandes and Jeremy Fu and Wenyin Fu and Brian Fuller and Cynthia Gao and Vedanuj Goswami and Naman Goyal and Anthony Hartshorn and Saghar Hosseini and Rui Hou and Hakan Inan and Marcin Kardas and Viktor Kerkez and Madian Khabsa and Isabel Kloumann and Artem Korenev and Punit Singh Koura and Marie-Anne Lachaux and Thibaut Lavril and Jenya Lee and Diana Liskovich and Yinghai Lu and Yuning Mao and Xavier Martinet and Todor Mihaylov and Pushkar Mishra and Igor Molybog and Yixin Nie and Andrew Poulton and Jeremy Reizenstein and Rashi Rungta and Kalyan Saladi and Alan Schelten and Ruan Silva and Eric Michael Smith and Ranjan Subramanian and Xiaoqing Ellen Tan and Binh Tang and Ross Taylor and Adina Williams and Jian Xiang Kuan and Puxin Xu and Zheng Yan and Iliyan Zarov and Yuchen Zhang and Angela Fan and Melanie Kambadur and Sharan Narang and Aurelien Rodriguez and Robert Stojnic and Sergey Edunov and Thomas Scialom},
    year={2023},
    eprint={2307.09288},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
```bibtex
@article{dao2023flashattention2,
    title={Flash{A}ttention-2: Faster Attention with Better Parallelism and Work Partitioning},
    author={Dao, Tri},
    year={2023}
}
```