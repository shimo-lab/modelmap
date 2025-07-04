**Update**
- 01.03.2024 - Reuploaded the model in bfloat16 dtype.
- 02.03.2024 - **strongest Gemma finetune model so far: added AGIEval,GPT4ALL and Bigbench scoring with AVG of 54.13 and H6 Open LLM Leaderboard with AVG of 67.83**

![SauerkrautLM](https://vago-solutions.ai/wp-content/uploads/2024/03/sauerkrautgemma.png "SauerkrautLM-Gemma-7b")
## VAGO solutions SauerkrautLM-Gemma-7b (alpha)
Introducing **SauerkrautLM-Gemma-7b** – our Sauerkraut version of the powerful [google/gemma-7b](https://huggingface.co/google/gemma-7b)  !
**It is an early stage finetuned model and should be used with caution!**

The model **SauerkrautLM-Gemma-7b** is a **joint effort** between **VAGO solutions** and **Hyperspace.ai.** 
Much appreciation goes to the tremendous research effort of **Fernando Fernandes Neto, David Golchinfar and Eric Hartford on their laserRMT approach.** 
Without their independent research collaboration this model release would not have been possible. 

- Fintuned with **SFT**
- Aligned with **DPO**
- **Using a novel training technique: laser-QLoRA**  -  we partially freeze the model according to a laser-like analysis (Official Paper soon). It allows to evaluate the no free lunch theorem and supports better decision making when optimizing the theorem - created by the [LaserRMT research group](https://github.com/cognitivecomputations/laserRMT)
- Optimized with **LaserRMT**

# Table of Contents
1. [Overview of all SauerkrautLM-Gemma-7b models](#all-sauerkrautlm-gemma-7b-models)
2. [Model Details](#model-details)
   - [Prompt template](#prompt-template)
   - [Training procedure](#proceed-of-the-training)
3. [Evaluation](#evaluation)
5. [Disclaimer](#disclaimer)
6. [Contact](#contact)
7. [Collaborations](#collaborations)
8. [Acknowledgement](#acknowledgement)


## All SauerkrautLM-Gemma-7b Models

| Model | HF    | GPTQ  | GGUF  | AWQ  |
|-------|-------|-------|-------|-------|
| SauerkrautLM-Gemma-7b  | [Link](https://huggingface.co/VAGOsolutions/SauerkrautLM-Gemma-7b) | coming soon | coming soon | coming soon |

## Model Details
**SauerkrautLM-Gemma-7b**
- **Model Type:** SauerkrautLM-Gemma-7b is a finetuned Model based on [google/gemma-7b](https://huggingface.co/google/gemma-7b) 
- **Language(s):** German, English
- **License:** [gemma-terms-of-use](https://ai.google.dev/gemma/terms)
- **Contact:** [VAGO solutions](https://vago-solutions.ai), [Hyperspace.ai](https://hyperspace.computer/)

### Training procedure:

**Warning**: **This finetuned model is in an early stage and we sometimes observed strange behavior. It is still work in progress!**

Anyone who has attempted or succeeded in fine-tuning a model is aware of the difficulty in nudging it towards a specific skill, such as mastering new languages, as well as the challenges associated with achieving significant improvements in performance.
Experimenting with a novel training strategy and Spherical Linear Interpolation alongside a lasered version of the model itself has proven to be both fascinating and revealing.

Furthermore, we developed one iteration of the model using our entire SFT -Sauerkraut dataset and two additional iterations using subsets of the full dataset—one focused on enhancing MMLU and TQA capabilities, and the other on boosting GSM8K and Winogrande skills.

After optimizing our primary SFT model, we applied a similar strategy to our new DPO Dataset, dividing it into further subsets. We trained one model on the entire dataset again and two more on these specialized subsets.

We actively monitor and assesed the results of each training. Whenever we found a decrease in perplexity on the gsm8k benchmark we intervined. By following this procedure we were able to improve the overall performance, especially in math abilities, without detracting from performance on other benchmarks—a task that is, in general, quite difficult.

This process not only helps in understanding the effectiveness of Spherical Linear Interpolation but also introduces a new method for refining models with enhanced skills through a cycle of targeted data selection (Laser data(x)) + SLERP, followed by a subsequent focus on different data (Laser again on data(y)).

Additionally, we integrated a novel training strategy on the SFT and DPO training process, where we partially freeze the model according to a laser-like analysis aiming to navigate and optimize the trade-offs highlighted by the no free lunch theorem. This innovative training method effectively prevents the significant problem of language models forgetting previously acquired knowledge. 
This aspect is particularly crucial when attempting to teach the model specific skills, such as a new language, where in general, the model might lose a considerable amount of its prior knowledge and exhibit a decline in overall intelligence. 

Detailed information on how the new training strategy works and the advantages it offers over conventional training methods will soon be published in a detailed paper by the LaserRMT research group.


**We teached German language skills on this model.** As far as we know, it is the first Gemma model with bilingual skills in German and English. Nevertheless, formulations may occur that are not entirely correct (still work in progress).


### Prompt Template:
We trained on vicuna prompt template. Please add the following stopping string to your client: ``` "</s>","</p>" ``` (we did not add the special tokens to the training config)
```
You are a helpful AI Assistant.

USER: Hello, how are you?
ASSISTANT:
```


## Evaluation

**Open LLM Leaderboard:**


| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | **67.83**  |
| ARC (25-shot)         | 59.98         |
| HellaSwag (10-shot)   | 81.91  |
| MMLU (5-shot)         | 63.76|
| TruthfulQA (0-shot)   | 61 |
| Winogrande (5-shot)   | 76.64  |
| GSM8K (5-shot)        | 63.68        |

**Performance**

|                                 Model                                 |AGIEval|GPT4All|TruthfulQA|BigBench|Average ⬇️|
|-----------------------------------------------------------------------|------:|------:|---------:|-------:|------:|
|[VAGOsolutions/SauerkrautLM-Gemma-7b](https://huggingface.co/VAGOsolutions/SauerkrautLM-Gemma-7b)  |  37.5|  72.46|     61.24|   45.33|  54.13|
|[zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)  |  37.52|  71.77|     55.26|   39.77|  51.08|
|[zephyr-7b-gemma-v0.1](https://huggingface.co/HuggingFaceH4/zephyr-7b-gemma-v0.1)|  34.22|  66.37|     52.19|   37.10|  47.47|
|[google/gemma-7b-it](https://huggingface.co/google/gemma-7b-it)        |  21.33|  40.84|     41.70|   30.25|  33.53|


<details><summary>Details of AGIEval, GPT4All, TruthfulQA, BigBench </summary>

**AGIEval** 
|            Tasks             |Version|Filter|n-shot| Metric |Value |   |Stderr|
|------------------------------|------:|------|------|--------|-----:|---|-----:|
|agieval_sat_math              |      1|none  |None  |acc     |0.3682|±  |0.0326|
|                              |       |none  |None  |acc_norm|0.3364|±  |0.0319|
|agieval_sat_en_without_passage|      1|none  |None  |acc     |0.4272|±  |0.0345|
|                              |       |none  |None  |acc_norm|0.3738|±  |0.0338|
|agieval_sat_en                |      1|none  |None  |acc     |0.7427|±  |0.0305|
|                              |       |none  |None  |acc_norm|0.6893|±  |0.0323|
|agieval_lsat_rc               |      1|none  |None  |acc     |0.5539|±  |0.0304|
|                              |       |none  |None  |acc_norm|0.5167|±  |0.0305|
|agieval_lsat_lr               |      1|none  |None  |acc     |0.3431|±  |0.0210|
|                              |       |none  |None  |acc_norm|0.3471|±  |0.0211|
|agieval_lsat_ar               |      1|none  |None  |acc     |0.1913|±  |0.0260|
|                              |       |none  |None  |acc_norm|0.1739|±  |0.0250|
|agieval_logiqa_en             |      1|none  |None  |acc     |0.3303|±  |0.0184|
|                              |       |none  |None  |acc_norm|0.3303|±  |0.0184|
|agieval_aqua_rat              |      1|none  |None  |acc     |0.2480|±  |0.0272|
|                              |       |none  |None  |acc_norm|0.2323|±  |0.0265|

Average: 37.5%

**GPT4All**
|  Tasks  |Version|Filter|n-shot| Metric |Value |   |Stderr|
|---------|------:|------|------|--------|-----:|---|-----:|
|arc_challenge|      1|none  |None  |acc     |0.5358|±  |0.0146|
|             |       |none  |None  |acc_norm|0.5597|±  |0.0145|
|arc_easy     |      1|none  |None  |acc     |0.8249|±  |0.0078|
|             |       |none  |None  |acc_norm|0.7955|±  |0.0083|
|boolq        |      2|none  |None  |acc     |0.8651|±  |0.006 |
|hellaswag    |      1|none  |None  |acc     |0.6162|±  |0.0049|
|             |       |none  |None  |acc_norm|0.8117|±  |0.0039|
|openbookqa   |      1|none  |None  |acc     |0.336|±   |0.0211|
|             |       |none  |None  |acc_norm|0.470|±   |0.0223|
|piqa         |      1|none  |None  |acc     |0.7900|±  |0.0095|
|             |       |none  |None  |acc_norm|0.8096|±  |0.00  |
|winogrande   |      1|none  |None  |acc     |0.7609|±  |0.012 |

Average: 72.46%

**TruthfulQA**
|    Tasks     |Version|Filter|n-shot|Metric|Value |   |Stderr|
|--------------|------:|------|-----:|------|-----:|---|-----:|
|truthfulqa_mc2|      2|none  |     0|acc   |0.6124|±  |0.0148|


Average: 61.24%

**Bigbench**
|                       Tasks                        |Version|     Filter     |n-shot|  Metric   |Value |   |Stderr|
|----------------------------------------------------|------:|----------------|-----:|-----------|-----:|---|-----:|
|bbh_zeroshot_tracking_shuffled_objects_three_objects|      2|flexible-extract|     0|exact_match|0.2760|±  |0.0283|
|bbh_zeroshot_tracking_shuffled_objects_seven_objects|      2|flexible-extract|     0|exact_match|0.1280|± |0.0212|
|bbh_zeroshot_tracking_shuffled_objects_five_objects |      2|flexible-extract|     0|exact_match|0.1240|±  |0.0209|
|bbh_zeroshot_temporal_sequences                     |      2|flexible-extract|     0|exact_match|0.4520|±  |0.0315|
|bbh_zeroshot_sports_understanding                   |      2|flexible-extract|     0|exact_match|0.7120|± |0.0287|
|bbh_zeroshot_snarks                                 |      2|flexible-extract|     0|exact_match|0.5056|±  |0.0376|
|bbh_zeroshot_salient_translation_error_detection    |      2|flexible-extract|     0|exact_match|0.4480|±  |0.0315|
|bbh_zeroshot_ruin_names                             |      2|flexible-extract|     0|exact_match|0.4520|±  |0.0315|
|bbh_zeroshot_reasoning_about_colored_objects        |      2|flexible-extract|     0|exact_match|0.4800|±  |0.0317|
|bbh_zeroshot_navigate                               |      2|flexible-extract|     0|exact_match|0.5480|±  |0.0315|
|bbh_zeroshot_movie_recommendation                   |      2|flexible-extract|     0|exact_match|0.7000|±  |0.0290|
|bbh_zeroshot_logical_deduction_three_objects        |      2|flexible-extract|     0|exact_match|0.5200|±  |0.0317|
|bbh_zeroshot_logical_deduction_seven_objects        |      2|flexible-extract|     0|exact_match|0.4120|±  |0.0312|
|bbh_zeroshot_logical_deduction_five_objects         |      2|flexible-extract|     0|exact_match|0.3840|±  |0.0308|
|bbh_zeroshot_geometric_shapes                       |      2|flexible-extract|     0|exact_match|0.2920|±  |0.0288|
|bbh_zeroshot_disambiguation_qa                      |      2|flexible-extract|     0|exact_match|0.6480|±  |0.0303|
|bbh_zeroshot_date_understanding                     |      2|flexible-extract|     0|exact_match|0.5000|±  |0.0317|
|bbh_zeroshot_causal_judgement                       |      2|flexible-extract|     0|exact_match|0.5775|±  |0.0362|

Average: 45.33%

</details>


Despite the fact that we archived great results on the Open LLM leaderboard benchmarks the model subjectively does not feel as smart as comparable mistral finetunes. Most of its answers are coherent but we observed that the model sometimes answers realy lazy or odd.

## Disclaimer
We must inform users that despite our best efforts in data cleansing, the possibility of uncensored content slipping through cannot be entirely ruled out.
However, we cannot guarantee consistently appropriate behavior. Therefore, if you encounter any issues or come across inappropriate content, we kindly request that you inform us through the contact information provided.
Additionally, it is essential to understand that the licensing of these models does not constitute legal advice. We are not held responsible for the actions of third parties who utilize our models.
 
## Contact
If you are interested in customized LLMs for business applications, please get in contact with us via our websites. We are also grateful for your feedback and suggestions.
 
## Collaborations
We are also keenly seeking support and investment for our startups, VAGO solutions and Hyperspace where we continuously advance the development of robust language models designed to address a diverse range of purposes and requirements. If the prospect of collaboratively navigating future challenges excites you, we warmly invite you to reach out to us at [VAGO solutions](https://vago-solutions.de/#Kontakt), [Hyperspace.computer](https://hyperspace.computer/)

## Acknowledgement
Many thanks to [google](https://huggingface.co/google) for providing such valuable model to the Open-Source community