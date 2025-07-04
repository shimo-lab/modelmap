
![SauerkrautLM](https://vago-solutions.ai/wp-content/uploads/2023/11/PHOTO-2023-11-24-17-36-05.jpg "SauerkrautLM-7b-HerO")
## VAGO solutions SauerkrautLM-7b-HerO
Introducing **SauerkrautLM-7b-HerO** – the pinnacle of German language model technology! 
Crafted through the **merging** of **[Teknium's OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B)** and **[Open-Orca's Mistral-7B-OpenOrca](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca)** and **uniquely fine-tuned with the Sauerkraut dataset.** 
SauerkrautLM-7b-HerO represents a breakthrough in language modeling, achieving an optimal balance between extensive German data and essential international sources. 
This ensures the model not only excels in understanding the nuances of the German language but also retains its global capabilities.
Harnessing the innovative power of the **gradient SLERP method from MergeKit**, we've achieved a groundbreaking fusion of two of the most best performing 7B models based on the Mistral framework.
This merge  has allowed us to combine the best features of both models, creating an unparalleled synergy. 
Coupled with the German Sauerkraut dataset, which consists of a mix of augmented and translated data, we have successfully taught the English-speaking merged model the intricacies of the German language.
This was achieved *without the typical loss of core competencies often associated with fine-tuning in another language of models previously trained mainly in English.*
Our approach ensures that the model retains its original strengths while acquiring a profound understanding of German, **setting a new benchmark in bilingual language model proficiency.**

# Table of Contents
1. [Overview of all Her0 models](#all-hero-models)
2. [Model Details](#model-details)
   - [Prompt template](#prompt-template)
   - [Training Dataset](#training-dataset)
   - [Merge Procedure](#merge-procedure) 
3. [Evaluation](#evaluation)
    - [GPT4ALL](#gpt4all)
    - [Language Model evaluation Harness](#language-model-evaluation-harness)
    - [BigBench](#big-bench)
    - [MMLU](#mmlu)
    - [TruthfulQA](#truthfulqa)
    - [MT-Bench (German)](#mt-bench-german)
    - [MT-Bench (English)](#mt-bench-english)
    - [Additional German Benchmark results](#additional-german-benchmark-results)
5. [Disclaimer](#disclaimer)
6. [Contact](#contact)
7. [Collaborations](#collaborations)
8. [Acknowledgement](#acknowledgement)


## All HerO Models

| Model | HF    | GPTQ  | GGUF  | AWQ  |
|-------|-------|-------|-------|-------|
| SauerkrautLM-7b-HerO   | [Link](https://huggingface.co/VAGOsolutions/SauerkrautLM-7b-HerO) | [Link](https://huggingface.co/TheBloke/SauerkrautLM-7B-HerO-GPTQ) | [Link](https://huggingface.co/TheBloke/SauerkrautLM-7B-HerO-GGUF) |[Link](https://huggingface.co/TheBloke/SauerkrautLM-7B-HerO-AWQ) |

## Model Details
**SauerkrautLM-7b-HerO**
- **Model Type:** SauerkrautLM-7b-HerO is an auto-regressive language model based on the transformer architecture 
- **Language(s):** English, German
- **License:** APACHE 2.0
- **Contact:** [Website](https://vago-solutions.de/#Kontakt) [David Golchinfar](mailto:golchinfar@vago-solutions.de)

### Training Dataset:

SauerkrautLM-7b-HerO was trained with mix of German data augmentation and translated data. 
We found, that only a simple translation of training data can lead to unnatural German phrasings. 
Data augmentation techniques were used to grant grammatical, syntactical correctness and a more natural German wording in our training data. 

### Merge Procedure:

SauerkrautLM-7b-HerO was merged on 1 A100 with [mergekit](https://github.com/cg123/mergekit).
The merged model contains [OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B) and [Open-Orca/Mistral-7B-OpenOrca](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca).
We applied the gradient SLERP method.



### Prompt Template:
```
<|im_start|>system
Du bist Sauerkraut-HerO, ein großes Sprachmodell, das höflich und kompetent antwortet. Schreibe deine Gedanken Schritt für Schritt auf, um Probleme sinnvoll zu lösen.<|im_end|>
<|im_start|>user
Wie geht es dir?<|im_end|>
<|im_start|>assistant
Mir geht es gut!<|im_end|>
<|im_start|>user
Bitte erkläre mir, wie die Zusammenführung von Modellen durch bestehende Spitzenmodelle profitieren kann.<|im_end|>
<|im_start|>assistant
```
## Evaluation

### GPT4ALL:
*Compared to relevant German Closed and Open Source models*
![GPT4ALL diagram](https://vago-solutions.de/wp-content/uploads/2023/11/GPT4All.png "SauerkrautLM-7b-HerO GPT4ALL Diagram")

![GPT4ALL table](https://vago-solutions.de/wp-content/uploads/2023/11/GPT4All-Tabelle.png "SauerkrautLM-7b-HerO GPT4ALL Table")

### Language Model evaluation Harness:
*Compared to Aleph Alpha Luminous Models*
![Harness](https://vago-solutions.de/wp-content/uploads/2023/11/Luminous-comparison.png "SauerkrautLM-7b-HerO Harness")

**performed with newest Language Model Evaluation Harness*
### Big Bench:
![BBH](https://vago-solutions.de/wp-content/uploads/2023/11/BigBench.png "SauerkrautLM-7b-HerO BBH")
**performed with newest Language Model Evaluation Harness*

### MMLU:
*Compared to Big Boy LLMs (Grok0,Grok1,GPT3.5,GPT4)*
![MMLU](https://vago-solutions.de/wp-content/uploads/2023/11/MMLU-Benchmark.png "SauerkrautLM-7b-HerO MMLU")
### TruthfulQA:
*Compared to OpenAI Models (GPT3.5,GPT4)*
![TruthfulQA](https://vago-solutions.de/wp-content/uploads/2023/11/Truthfulqa-Benchmark.png "SauerkrautLM-7b-HerO TruthfulQA")

### MT-Bench (German):
![MT-Bench German Diagram](https://vago-solutions.de/wp-content/uploads/2023/11/MT-Bench-German.png "SauerkrautLM-7b-HerO MT-Bench German Diagram")
```
########## First turn ########## 
                                                           score 
model                                              turn          
SauerkrautLM-70b-v1                                1     7.25000 
SauerkrautLM-7b-HerO  <---                         1     6.96875 
SauerkrautLM-7b-v1-mistral                         1     6.30625 
leo-hessianai-13b-chat                             1     6.18750 
SauerkrautLM-13b-v1                                1     6.16250 
leo-mistral-hessianai-7b-chat                      1     6.15625 
Llama-2-70b-chat-hf                                1     6.03750 
vicuna-13b-v1.5                                    1     5.80000 
SauerkrautLM-7b-v1                                 1     5.65000 
leo-hessianai-7b-chat                              1     5.52500 
vicuna-7b-v1.5                                     1     5.42500 
Mistral-7B-v0.1                                    1     5.37500 
SauerkrautLM-3b-v1                                 1     3.17500 
Llama-2-7b                                         1     1.28750 
open_llama_3b_v2                                   1     1.68750 

########## Second turn ########## 
                                                           score 
model                                              turn          
SauerkrautLM-70b-v1                                2     6.83125 
SauerkrautLM-7b-HerO  <---                         2     6.30625 
vicuna-13b-v1.5                                    2     5.63125 
SauerkrautLM-13b-v1                                2     5.34375 
SauerkrautLM-7b-v1-mistral                         2     5.26250 
leo-mistral-hessianai-7b-chat                      2     4.99375 
SauerkrautLM-7b-v1                                 2     4.73750 
leo-hessianai-13b-chat                             2     4.71250 
vicuna-7b-v1.5                                     2     4.67500 
Llama-2-70b-chat-hf                                2     4.66250 
Mistral-7B-v0.1                                    2     4.53750 
leo-hessianai-7b-chat                              2     2.65000 
SauerkrautLM-3b-v1                                 2     1.98750 
open_llama_3b_v2                                   2     1.22500 
Llama-2-7b                                         2     1.07500 

########## Average ########## 
                                                       score 
model                                                        
SauerkrautLM-70b-v1                                 7.040625 
SauerkrautLM-7b-HerO   <---                         6.637500
SauerkrautLM-7b-v1-mistral                          5.784375 
SauerkrautLM-13b-v1                                 5.753125 
vicuna-13b-v1.5                                     5.715625 
leo-mistral-hessianai-7b-chat                       5.575000 
leo-hessianai-13b-chat                              5.450000 
Llama-2-70b-chat-hf                                 5.350000 
SauerkrautLM-v1-7b                                  5.193750 
vicuna-7b-v1.5                                      5.050000 
Mistral-7B-v0.1                                     4.956250 
leo-hessianai-7b-chat                               4.087500 
SauerkrautLM-3b-v1                                  2.581250 
open_llama_3b_v2                                    1.456250 
Llama-2-7b                                          1.181250 
```
**performed with the newest FastChat Version*
### MT-Bench (English):
![MT-Bench English Diagram](https://vago-solutions.de/wp-content/uploads/2023/11/MT-Bench-English.png "SauerkrautLM-7b-HerO MT-Bench English Diagram")
```
########## First turn ########## 
                                                           score 
model                                              turn          
OpenHermes-2.5-Mistral-7B                          1     8.21875 
SauerkrautLM-7b-HerO    <---                       1     8.03125 
Mistral-7B-OpenOrca                                1     7.65625 
neural-chat-7b-v3-1                                1     7.22500 

########## Second turn ########## 
                                                          score 
model                                              turn          
OpenHermes-2.5-Mistral-7B                          2     7.1000 
SauerkrautLM-7b-HerO  <---                         2     6.7875 
neural-chat-7b-v3-1                                2     6.4000 
Mistral-7B-OpenOrca                                2     6.1750 
 
########## Average ########## 
                                                       score 
model                                                         
OpenHermes-2.5-Mistral-7B                           7.659375 
SauerkrautLM-7b-HerO  <---                          7.409375 
Mistral-7B-OpenOrca                                 6.915625 
neural-chat-7b-v3-1                                 6.812500 
```
**performed with the newest FastChat Version*

### Additional German Benchmark results:
![GermanBenchmarks](https://vago-solutions.de/wp-content/uploads/2023/11/German-benchmarks.png "SauerkrautLM-7b-HerO German Benchmarks")
*performed with newest Language Model Evaluation Harness
## Disclaimer
We must inform users that despite our best efforts in data cleansing, the possibility of uncensored content slipping through cannot be entirely ruled out.
However, we cannot guarantee consistently appropriate behavior. Therefore, if you encounter any issues or come across inappropriate content, we kindly request that you inform us through the contact information provided.
Additionally, it is essential to understand that the licensing of these models does not constitute legal advice. We are not held responsible for the actions of third parties who utilize our models. These models may be employed for commercial purposes, and the Apache 2.0 remains applicable and is included with the model files.
 
## Contact
If you are interested in customized LLMs for business applications, please get in contact with us via our website or contact us at [Dr. Daryoush Vaziri](mailto:vaziri@vago-solutions.de). We are also grateful for your feedback and suggestions.
 
## Collaborations
We are also keenly seeking support and investment for our startup, VAGO solutions, where we continuously advance the development of robust language models designed to address a diverse range of purposes and requirements. If the prospect of collaboratively navigating future challenges excites you, we warmly invite you to reach out to us.

## Acknowledgement
Many thanks to [OpenOrca](https://huggingface.co/Open-Orca) and [teknium](https://huggingface.co/teknium) for providing such valuable models to the Open-Source community.
Many thanks to [TheBloke](https://huggingface.co/TheBloke) for super fast quantifying all of our models. 

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)