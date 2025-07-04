
![Juanako.AI & SauerkrautLM Productions](https://vago-solutions.de/wp-content/uploads/2023/12/sauerkrautlm-solar.png "LUNA-SOLARkrautLM-Instruct")
## VAGO solutions LUNA-SOLARkrautLM-Instruct
Introducing **LUNA-SOLARkrautLM-Instruct** – a UNA-Sauerkraut version of the powerful [upstage/SOLAR-10.7B-Instruct-v1.0](https://huggingface.co/upstage/SOLAR-10.7B-Instruct-v1.0) ! 
Aligned with **DPO** and tamed with **UNA**.

# Table of Contents
1. [Overview of all LUNA-SOLARkrautLM-Instruct models](#all-sauerkrautlm-solar-instruct-models)
2. [Model Details](#model-details)
   - [Prompt template](#prompt-template)
   - [Training Dataset](#training-dataset)
   - [Data Contamination Test](#data-contamination-test-results)
3. [Evaluation](#evaluation)
5. [Disclaimer](#disclaimer)
6. [Contact](#contact)
7. [Collaborations](#collaborations)
8. [Acknowledgement](#acknowledgement)


## Model Details
**LUNA-SOLARkrautLM-Instruct**
- **Model Type:** LUNA-SOLARkrautLM-Instruct is a UNA  Model based on [fblgit/UNA-SOLAR-10.7B-Instruct-v1.0](https://huggingface.co/fblgit/UNA-SOLAR-10.7B-Instruct-v1.0) and the powerful set of [SauerkrautLM-SOLAR-Instruct](https://huggingface.co/VAGOsolutions/SauerkrautLM-SOLAR-Instruct/)
- **Language(s):** English, German
- **License:** cc-by-nc-4.0
- **Contact:** [Website](https://vago-solutions.de/#Kontakt) [David Golchinfar](mailto:golchinfar@vago-solutions.de) [Juanako.AI - UNA](mailto:info@juanako.ai)

### Training Dataset:

LUNA-SOLARkrautLM-Instruct was trained with mix of German data augmentation and translated data. 
Aligned through **DPO** with our **new German SauerkrautLM-DPO dataset** based on parts of the SFT SauerkrautLM dataset 
as chosen answers and [Sauerkraut-7b-HerO](https://huggingface.co/VAGOsolutions/SauerkrautLM-7b-HerO) as rejected answers. Added with additional **translated Parts of the [HuggingFaceH4/ultrafeedback_binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized)** (Our dataset do not contain any TruthfulQA prompts - check Data Contamination Test Results) and **[argilla/distilabel-math-preference-dpo](https://huggingface.co/datasets/argilla/distilabel-math-preference-dpo).**  
We found, that only a simple translation of training data can lead to unnatural German phrasings. 
Data augmentation techniques were used to grant grammatical, syntactical correctness and a more natural German wording in our training data. 

We improved the German language skills on this model. Nevertheless, certain formulations may occur that are not entirely correct.


### Data Contamination Test Results

Some models on the HuggingFace leaderboard had problems with wrong data getting mixed in.
We checked our SauerkrautLM-DPO dataset with a special test [1] on this model as target model and upstage/SOLAR-10.7B-Instruct-v1.0 as reference model. 
The HuggingFace team used the same methods [2, 3].

Our results, with `result < 0.1, %:` being well below 0.9, indicate that our dataset is free from contamination.

*The data contamination test results of HellaSwag and Winograde will be added once [1] supports them.*

| Dataset                        | ARC   | MMLU | TruthfulQA | GSM8K |
|------------------------------|-------|-------|-------|-------|
| **SauerkrautLM-DPO**| result < 0.1, %: 0.0 |result < 0.1, %: 0.09 | result < 0.1, %: 0.13 | result < 0.1, %: 0.16 |

[1] https://github.com/swj0419/detect-pretrain-code-contamination

[2] https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard/discussions/474#657f2245365456e362412a06

[3] https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard/discussions/265#657b6debf81f6b44b8966230

### Prompt Template:
```
<|im_start|>system
Du bist LUNA-SOLARkrautLM, ein großes Sprachmodell, das höflich und kompetent antwortet.<|im_end|>
<|im_start|>user
Wie geht es dir?<|im_end|>
<|im_start|>assistant

```

```
### User:
Hello, how are you?

### Assistant:
Hi there! I am an AI language model, so I don't have personal feelings or emotions in the traditional sense. However, I can assure you that my systems and processes are functioning well at this moment, allowing me to provide helpful responses for your queries.
How may I assist you today?

```

## Evaluation
```

hf (pretrained=fblgit/LUNA-SOLARkrautLM-Instruct), gen_kwargs: (), limit: None, num_fewshot: 5, batch_size: auto
|Tasks|Version|  Filter  |n-shot|  Metric   |Value |   |Stderr|
|-----|-------|----------|-----:|-----------|-----:|---|-----:|
|gsm8k|Yaml   |get-answer|     5|exact_match|0.6467|±  |0.0132|

hf (pretrained=fblgit/LUNA-SOLARkrautLM-Instruct), gen_kwargs: (), limit: None, num_fewshot: 0, batch_size: auto (64)
|    Tasks     |Version|Filter|n-shot|Metric|Value |   |Stderr|
|--------------|-------|------|-----:|------|-----:|---|-----:|
|truthfulqa_mc2|Yaml   |none  |     0|acc   |0.7368|±  |0.0149|

hf (pretrained=fblgit/LUNA-SOLARkrautLM-Instruct), gen_kwargs: (), limit: None, num_fewshot: 25, batch_size: auto (32)
|    Tasks    |Version|Filter|n-shot| Metric |Value|   |Stderr|
|-------------|-------|------|-----:|--------|----:|---|-----:|
|arc_challenge|Yaml   |none  |    25|acc     |0.692|±  |0.0135|
|             |       |none  |    25|acc_norm|0.715|±  |0.0132|

hf (pretrained=fblgit/LUNA-SOLARkrautLM-Instruct), gen_kwargs: (), limit: None, num_fewshot: 0, batch_size: auto (64)
|   Tasks   |Version|Filter|n-shot|Metric| Value |   |Stderr|
|-----------|-------|------|-----:|------|------:|---|-----:|
|paws_de    |Yaml   |none  |     0|acc   | 0.3965|±  |0.0109|
|wmt16-en-de|Yaml   |none  |     0|bleu  | 3.5784|±  |0.1325|
|           |       |none  |     0|ter   |64.5707|±  |0.4514|
|           |       |none  |     0|chrf  |45.7068|±  |0.3861|
|xnli_de    |Yaml   |none  |     0|acc   | 0.4129|±  |0.0099|

hf (pretrained=fblgit/LUNA-SOLARkrautLM-Instruct), gen_kwargs: (), limit: None, num_fewshot: 10, batch_size: auto (32)
|  Tasks  |Version|Filter|n-shot| Metric |Value |   |Stderr|
|---------|-------|------|-----:|--------|-----:|---|-----:|
|hellaswag|Yaml   |none  |    10|acc     |0.7131|±  |0.0045|
|         |       |none  |    10|acc_norm|0.8815|±  |0.0032|

hf (pretrained=fblgit/LUNA-SOLARkrautLM-Instruct), gen_kwargs: (), limit: None, num_fewshot: 5, batch_size: auto (64)
|   Tasks   |Version|Filter|n-shot|Metric| Value |   |Stderr|
|-----------|-------|------|-----:|------|------:|---|-----:|
|wmt16-de-en|Yaml   |none  |     5|bleu  |14.9310|±  |0.8014|
|           |       |none  |     5|ter   |46.3206|±  |0.4087|
|           |       |none  |     5|chrf  |60.8637|±  |0.4436|
|wmt16-en-de|Yaml   |none  |     5|bleu  | 6.2016|±  |0.2918|
|           |       |none  |     5|ter   |63.9997|±  |0.4591|
|           |       |none  |     5|chrf  |51.1399|±  |0.3978|
|xnli_de    |Yaml   |none  |     5|acc   | 0.4703|±  |0.0100|

hf (pretrained=fblgit/LUNA-SOLARkrautLM-Instruct,dtype=float16), gen_kwargs: (), limit: None, num_fewshot: 5, batch_size: auto (16)
|                 Tasks                 |Version|Filter|n-shot|Metric|Value |   |Stderr|
|---------------------------------------|-------|------|-----:|------|-----:|---|-----:|
|mmlu                                   |N/A    |none  |     0|acc   |0.6461|±  |0.1215|
| - humanities                          |N/A    |none  |     5|acc   |0.5960|±  |0.1200|
|  - formal_logic                       |Yaml   |none  |     5|acc   |0.4683|±  |0.0446|
|  - high_school_european_history       |Yaml   |none  |     5|acc   |0.8121|±  |0.0305|
|  - high_school_us_history             |Yaml   |none  |     5|acc   |0.8480|±  |0.0252|
|  - high_school_world_history          |Yaml   |none  |     5|acc   |0.8312|±  |0.0244|
|  - international_law                  |Yaml   |none  |     5|acc   |0.7851|±  |0.0375|
|  - jurisprudence                      |Yaml   |none  |     5|acc   |0.7685|±  |0.0408|
|  - logical_fallacies                  |Yaml   |none  |     5|acc   |0.7423|±  |0.0344|
|  - moral_disputes                     |Yaml   |none  |     5|acc   |0.7283|±  |0.0239|
|  - moral_scenarios                    |Yaml   |none  |     5|acc   |0.3899|±  |0.0163|
|  - philosophy                         |Yaml   |none  |     5|acc   |0.7074|±  |0.0258|
|  - prehistory                         |Yaml   |none  |     5|acc   |0.7716|±  |0.0234|
|  - professional_law                   |Yaml   |none  |     5|acc   |0.4824|±  |0.0128|
|  - world_religions                    |Yaml   |none  |     5|acc   |0.7661|±  |0.0325|
| - other                               |N/A    |none  |     5|acc   |0.7097|±  |0.0900|
|  - business_ethics                    |Yaml   |none  |     5|acc   |0.7700|±  |0.0423|
|  - clinical_knowledge                 |Yaml   |none  |     5|acc   |0.6792|±  |0.0287|
|  - college_medicine                   |Yaml   |none  |     5|acc   |0.6647|±  |0.0360|
|  - global_facts                       |Yaml   |none  |     5|acc   |0.3600|±  |0.0482|
|  - human_aging                        |Yaml   |none  |     5|acc   |0.6861|±  |0.0311|
|  - management                         |Yaml   |none  |     5|acc   |0.8350|±  |0.0368|
|  - marketing                          |Yaml   |none  |     5|acc   |0.8504|±  |0.0234|
|  - medical_genetics                   |Yaml   |none  |     5|acc   |0.6700|±  |0.0473|
|  - miscellaneous                      |Yaml   |none  |     5|acc   |0.7893|±  |0.0146|
|  - nutrition                          |Yaml   |none  |     5|acc   |0.7549|±  |0.0246|
|  - professional_accounting            |Yaml   |none  |     5|acc   |0.5213|±  |0.0298|
|  - professional_medicine              |Yaml   |none  |     5|acc   |0.7353|±  |0.0268|
|  - virology                           |Yaml   |none  |     5|acc   |0.5783|±  |0.0384|
| - social_sciences                     |N/A    |none  |     5|acc   |0.7501|±  |0.0684|
|  - econometrics                       |Yaml   |none  |     5|acc   |0.5175|±  |0.0470|
|  - high_school_geography              |Yaml   |none  |     5|acc   |0.8485|±  |0.0255|
|  - high_school_government_and_politics|Yaml   |none  |     5|acc   |0.8912|±  |0.0225|
|  - high_school_macroeconomics         |Yaml   |none  |     5|acc   |0.6615|±  |0.0240|
|  - high_school_microeconomics         |Yaml   |none  |     5|acc   |0.7311|±  |0.0288|
|  - high_school_psychology             |Yaml   |none  |     5|acc   |0.8385|±  |0.0158|
|  - human_sexuality                    |Yaml   |none  |     5|acc   |0.7023|±  |0.0401|
|  - professional_psychology            |Yaml   |none  |     5|acc   |0.6683|±  |0.0190|
|  - public_relations                   |Yaml   |none  |     5|acc   |0.6909|±  |0.0443|
|  - security_studies                   |Yaml   |none  |     5|acc   |0.7633|±  |0.0272|
|  - sociology                          |Yaml   |none  |     5|acc   |0.8358|±  |0.0262|
|  - us_foreign_policy                  |Yaml   |none  |     5|acc   |0.8800|±  |0.0327|
| - stem                                |N/A    |none  |     5|acc   |0.5569|±  |0.1360|
|  - abstract_algebra                   |Yaml   |none  |     5|acc   |0.3800|±  |0.0488|
|  - anatomy                            |Yaml   |none  |     5|acc   |0.6148|±  |0.0420|
|  - astronomy                          |Yaml   |none  |     5|acc   |0.7237|±  |0.0364|
|  - college_biology                    |Yaml   |none  |     5|acc   |0.7708|±  |0.0351|
|  - college_chemistry                  |Yaml   |none  |     5|acc   |0.4600|±  |0.0501|
|  - college_computer_science           |Yaml   |none  |     5|acc   |0.5400|±  |0.0501|
|  - college_mathematics                |Yaml   |none  |     5|acc   |0.2700|±  |0.0446|
|  - college_physics                    |Yaml   |none  |     5|acc   |0.3333|±  |0.0469|
|  - computer_security                  |Yaml   |none  |     5|acc   |0.7300|±  |0.0446|
|  - conceptual_physics                 |Yaml   |none  |     5|acc   |0.6213|±  |0.0317|
|  - electrical_engineering             |Yaml   |none  |     5|acc   |0.6276|±  |0.0403|
|  - elementary_mathematics             |Yaml   |none  |     5|acc   |0.4788|±  |0.0257|
|  - high_school_biology                |Yaml   |none  |     5|acc   |0.8065|±  |0.0225|
|  - high_school_chemistry              |Yaml   |none  |     5|acc   |0.5123|±  |0.0352|
|  - high_school_computer_science       |Yaml   |none  |     5|acc   |0.7000|±  |0.0461|
|  - high_school_mathematics            |Yaml   |none  |     5|acc   |0.3889|±  |0.0297|
|  - high_school_physics                |Yaml   |none  |     5|acc   |0.3576|±  |0.0391|
|  - high_school_statistics             |Yaml   |none  |     5|acc   |0.5926|±  |0.0335|
|  - machine_learning                   |Yaml   |none  |     5|acc   |0.4554|±  |0.0473|

|      Groups      |Version|Filter|n-shot|Metric|Value |   |Stderr|
|------------------|-------|------|-----:|------|-----:|---|-----:|
|mmlu              |N/A    |none  |     0|acc   |0.6461|±  |0.1215|
| - humanities     |N/A    |none  |     5|acc   |0.5960|±  |0.1200|
| - other          |N/A    |none  |     5|acc   |0.7097|±  |0.0900|
| - social_sciences|N/A    |none  |     5|acc   |0.7501|±  |0.0684|
| - stem           |N/A    |none  |     5|acc   |0.5569|±  |0.1360|
```
### MT-Bench
```
########## Average ##########
                                  score
model
gpt-4                          8.990625
gpt-3.5-turbo                  7.943750
claude-instant-v1              7.905660
claude-v1                      7.900000
UNA-SOLAR-10.7B-Instruct-v1.0  7.521875
LUNA-SOLARkrautLM-Instruct     7.462500
vicuna-33b-v1.3                7.121875
wizardlm-30b                   7.009375
Llama-2-70b-chat               6.856250
Llama-2-13b-chat               6.650000
guanaco-33b                    6.528125
tulu-30b                       6.434375
guanaco-65b                    6.409375
oasst-sft-7-llama-30b          6.409375
palm-2-chat-bison-001          6.400000
mpt-30b-chat                   6.393750
vicuna-13b-v1.3                6.387500
wizardlm-13b                   6.353125
Llama-2-7b-chat                6.268750
vicuna-7b-v1.3                 5.996875
baize-v2-13b                   5.750000
nous-hermes-13b                5.553459
mpt-7b-chat                    5.459119
gpt4all-13b-snoozy             5.452830
koala-13b                      5.350000
mpt-30b-instruct               5.218750
falcon-40b-instruct            5.168750
h2ogpt-oasst-open-llama-13b    4.625000
alpaca-13b                     4.531250
chatglm-6b                     4.500000
oasst-sft-4-pythia-12b         4.318750
rwkv-4-raven-14b               3.984375
dolly-v2-12b                   3.275000
fastchat-t5-3b                 3.040625
stablelm-tuned-alpha-7b        2.753125
llama-13b                      2.606250
```

## Disclaimer
We must inform users that despite our best efforts in data cleansing, the possibility of uncensored content slipping through cannot be entirely ruled out.
However, we cannot guarantee consistently appropriate behavior. Therefore, if you encounter any issues or come across inappropriate content, we kindly request that you inform us through the contact information provided.
Additionally, it is essential to understand that the licensing of these models does not constitute legal advice. We are not held responsible for the actions of third parties who utilize our models.
 
## Contact
If you are interested in customized LLMs for business applications, please get in contact with us via our website or contact us at [Dr. Daryoush Vaziri](mailto:vaziri@vago-solutions.de). We are also grateful for your feedback and suggestions.
 
## Collaborations
We are also keenly seeking support and investment for our startup, [VAGO Solutions](https://huggingface.co/VAGOsolutions), where we continuously advance the development of robust language models designed to address a diverse range of purposes and requirements. If the prospect of collaboratively navigating future challenges excites you, we warmly invite you to reach out to us.

[Juanako.AI](https://huggingface.co/fblgit) is also seeking support and investment for our startup, we also are open for collaborating with other labs to make awesome models like this one.

## Acknowledgement
Big Hug to [VAGO Solutions](https://huggingface.co/VAGOsolutions), we merely used our UNA transformers library on their code and dataset, nothing else. This won't be possible without them, thanks!

Many thanks to [argilla](https://huggingface.co/datasets/argilla) and [Huggingface](https://huggingface.co) for providing such valuable datasets to the Open-Source community. And of course a big thanks to [upstage](https://huggingface.co/upstage) for providing the open source community with their latest technology!

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_fblgit__LUNA-SOLARkrautLM-Instruct)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |73.79|
|AI2 Reasoning Challenge (25-Shot)|71.16|
|HellaSwag (10-Shot)              |88.28|
|MMLU (5-Shot)                    |66.11|
|TruthfulQA (0-shot)              |73.37|
|Winogrande (5-shot)              |82.95|
|GSM8k (5-shot)                   |60.88|

