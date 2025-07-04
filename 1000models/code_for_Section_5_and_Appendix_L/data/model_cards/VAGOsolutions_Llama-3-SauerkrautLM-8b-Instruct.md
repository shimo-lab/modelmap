

![SauerkrautLM](https://vago-solutions.ai/wp-content/uploads/2024/04/Llama3-Pic.png "Llama-3-SauerkrautLM-8b-Instruct")
## VAGO solutions Llama-3-SauerkrautLM-8b-Instruct
Introducing **Llama-3-SauerkrautLM-8b-Instruct** – our Sauerkraut version of the powerful [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)!

The model **Llama-3-SauerkrautLM-8b-Instruct** is a **joint effort** between **VAGO Solutions** and **Hyperspace.ai.** 

- Aligned with **DPO**

# Table of Contents
1. [Overview of all Llama-3-SauerkrautLM-8b-Instruct](#all-Llama-3-SauerkrautLM-8b-Instruct)
2. [Model Details](#model-details)
   - [Prompt template](#prompt-template)
   - [Training procedure](#proceed-of-the-training)
3. [Evaluation](#evaluation)
5. [Disclaimer](#disclaimer)
6. [Contact](#contact)
7. [Collaborations](#collaborations)
8. [Acknowledgement](#acknowledgement)


## All SauerkrautLM-llama-3-8B-Instruct

| Model | HF    | EXL2  | GGUF  | AWQ  |
|-------|-------|-------|-------|-------|
| Llama-3-SauerkrautLM-8b-Instruct | [Link](https://huggingface.co/VAGOsolutions/Llama-3-SauerkrautLM-8b-Instruct) | [Link](https://huggingface.co/bartowski/Llama-3-SauerkrautLM-8b-Instruct-exl2) | [Link](https://huggingface.co/bartowski/Llama-3-SauerkrautLM-8b-Instruct-GGUF) | coming soon |

## Model Details
**SauerkrautLM-llama-3-8B-Instruct**
- **Model Type:** Llama-3-SauerkrautLM-8b-Instruct is a finetuned Model based on [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
- **Language(s):** German, English
- **License:** [meta-llama](https://llama.meta.com/llama3/license)
- **Contact:** [VAGO solutions](https://vago-solutions.ai), [Hyperspace.ai](https://hyperspace.computer/)

### Training procedure:
- We trained this model in a two staged DPO Fine-Tuning for 1 epoch with 70k data and another epoch with 20k data.
- LaserRMT version coming soon

**We improved the model's capabilities noticably by feeding it with curated German data.**


### Prompt Template:

**English:**
```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are a helpful AI assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>

Input<|eot_id|><|start_header_id|>assistant<|end_header_id|>

```

**German:**
```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Du bist ein freundlicher und hilfreicher deutscher KI-Assistent.<|eot_id|><|start_header_id|>user<|end_header_id|>

Input<|eot_id|><|start_header_id|>assistant<|end_header_id|>

```
### Example output of german language:

```

Prompt: Erkläre mir die Vorteile für das Fine-Tuning von Meta's LLama Modellen.

Antwort:
Sehr gern!

Fine-tuning von Meta's LLaMA-Modellen ist eine sehr effektive Möglichkeit, um Ihre Anwendung oder Ihr Projekt mit einer hochentwickelten Sprachverarbeitung auszustatten.

Die Vorteile des Fine-Tunings von LLaMA-Modellen sind:

Adaptation an spezielle Aufgaben: Durch das Fine-Tuning können Sie die Modelle auf Ihre speziellen Bedürfnisse und Anforderungen anpassen.
Dies ermöglicht es Ihnen, die Leistung der Modelle in Ihren Anwendungen zu verbessern.

Verbesserte Genauigkeit: Die fine-tuned Modelle lernen, sich an die spezifischen Merkmale Ihres Datenbestands anzupassen, was zu einer besseren Genauigkeit bei der Textklassifizierung, -generierung, -summarisierung usw. führt.

Anpassung an Branche oder Domain: Wenn Sie beispielsweise ein Medizinprojekt haben, können Sie die Modelle auf medizinische Fachterminologie und -konzepte trainieren, um eine höhere Präzision bei der Analyse medizinischer Texte zu erzielen.

Kosten-Effektivität: Im Vergleich zum Training neuer Modelle von Grund auf kann das Fine-Tuning viel kosteneffektiver sein, da Sie nur einen kleinen Teil des Trainingsdatums benötigen, um die Modelle an Ihre spezifischen Anforderungen anzupassen.

Schnellere Entwicklung: Das Fine-Tuning ermöglicht es Entwicklern, schnell neue Funktionen und Features in ihre Anwendungen einzufügen, ohne dass sie lange warten müssen, bis neue Modelle trainiert werden.

Bessere Interpretierbarkeit: Da die fine-tuned Modelle auf Ihre spezifischen Daten bestimmt wurden, können Sie leichter verstehen, warum bestimmte Entscheidungen getroffen werden, was wichtig ist, wenn es um Transparenz und Verantwortlichkeit geht.

Insgesamt bietet das Fine-Tuning von LLaMA-Modellen eine flexible und effektive Möglichkeit, um Ihre Anwendungen und Projekte durch die Integration von fortschrittlichen Sprachmodellen zu verbessern.
```

## Evaluation

**Open LLM Leaderboard:**

evaluated with lm-evaluation-benchmark-harness 0.4.2
| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | **74.57**  |
| ARC (25-shot)         | 74.66          |
| HellaSwag (10-shot)   | 89.60   |
| MMLU (5-shot)         | 66.55 |
| TruthfulQA (0-shot)   | 66.32 |
| Winogrande (5-shot)   | 80.98  |
| GSM8K (5-shot)        | 69.29        |


**MT-Bench English**

```
########## First turn ########## 
                                         score 
model                            turn 
Llama-3-SauerkrautLM-8b-Instruct 1     8.15625 
  
########## Second turn ########## 
                                       score 
model                            turn 
Llama-3-SauerkrautLM-8b-Instruct 2      7.65 
  
########## Average ########## 
                                     score 
model 
Llama-3-SauerkrautLM-8b-Instruct  7.903125 *

```
* due to specific instruction training the english MT-Bench score is slightly lower than the original LLama-3-8B-Instruct


**MT-Bench German**

```
########## First turn ##########
                                       score
model                            turn
Llama-3-SauerkrautLM-8b-Instruct 1     7.675

########## Second turn ##########
                                        score
model                            turn
Llama-3-SauerkrautLM-8b-Instruct 2     7.6375

########## Average ##########
                                    score
model
Llama-3-SauerkrautLM-8b-Instruct  7.65625
```

**German RAG LLM Evaluation**
corrected result after FIX: https://github.com/huggingface/lighteval/pull/171
```
|                         Task                         |Version|Metric|Value|   |Stderr|
|------------------------------------------------------|------:|------|----:|---|-----:|
|all                                                   |       |acc   |0.910|±  |0.0084|
|community:german_rag_eval:_average:0                  |       |acc   |0.910|±  |0.0084|
|community:german_rag_eval:choose_context_by_question:0|      0|acc   |0.928|±  |0.0082|
|community:german_rag_eval:choose_question_by_context:0|      0|acc   |0.824|±  |0.0120|
|community:german_rag_eval:context_question_match:0    |      0|acc   |0.982|±  |0.0042|
|community:german_rag_eval:question_answer_match:0     |      0|acc   |0.906|±  |0.0092|
```

## Disclaimer
We must inform users that despite our best efforts in data cleansing, the possibility of uncensored content slipping through cannot be entirely ruled out.
However, we cannot guarantee consistently appropriate behavior. Therefore, if you encounter any issues or come across inappropriate content, we kindly request that you inform us through the contact information provided.
Additionally, it is essential to understand that the licensing of these models does not constitute legal advice. We are not held responsible for the actions of third parties who utilize our models.
 
## Contact
If you are interested in customized LLMs for business applications, please get in contact with us via our websites. We are also grateful for your feedback and suggestions.
 
## Collaborations
We are also keenly seeking support and investment for our startups, VAGO solutions and Hyperspace where we continuously advance the development of robust language models designed to address a diverse range of purposes and requirements. If the prospect of collaboratively navigating future challenges excites you, we warmly invite you to reach out to us at [VAGO solutions](https://vago-solutions.de/#Kontakt), [Hyperspace.computer](https://hyperspace.computer/)

## Acknowledgement
Many thanks to [Meta](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) for providing such valuable model to the Open-Source community.
Also many thanks to [bartowski](https://huggingface.co/bartowski) for super fast quantification of our Model in GGUF and EXL format.
