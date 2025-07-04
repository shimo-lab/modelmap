![EM Logo](em_model_logo_web.jpeg)

LeoLM Mistral is the showcase-model of the EM German model family and as of its release in our opinion the best open German LLM.

**Many thanks to the [LeoLM](https://huggingface.co/LeoLM) team for the publication of a base model that has received continued pretraining with German texts, greatly improving generation capabilities.**

*Please note that the Mistral architecture is very recent and still not supported by all libraries (e.g. AutoGPTQ). In case of any problems, please try a different format/base model.*

# Table of Contents

1. [Introduction](#introduction)
2. [Links & Demos](#links--demos)
   - [Model Links](#model-links)
   - [Demos](#demos)
3. [Prompt Format](#prompt-format)
4. [Example Output](#example-output)
5. [Acknowledgements](#acknowledgements)
6. [Contact](#contact)
7. [Disclaimer](#disclaimer)

# Introduction

**EM German** is a Llama2/Mistral/LeoLM-based model family, finetuned on a large dataset of various instructions in German language. The models are optimized for German text, providing proficiency in understanding, generating, and interacting with German language content.

We offer versions based on 7b, 13b and 70b Llama-2, Mistral and LeoLM (Llama-2/Mistral with continued pretraining on German texts) models.

Please find all Informations, Example Outputs, the special RAG prompt format, output examples and eval results for the EM German Model family in [our Github Repository](https://github.com/jphme/EM_German).  ([Deutsche Version](https://github.com/jphme/EM_German/blob/main/README_DE.md)). You will also find instructions on how to run the models with a GUI (GPT4All/LM Studio).


# Links & Demos

## Model Links

Should you only try one model version, I strongly recommend the **[LeoLM Mistral](https://huggingface.co/jphme/em_german_leo_mistral)** model which offers by far the best combination of performance and computing requirements!

| Base Model | HF    | GPTQ  | GGUF  | AWQ   |
|-------|-------|-------|-------|-------|
| Llama2 7b   | [Link](https://huggingface.co/jphme/em_german_7b_v01) | [Link](https://huggingface.co/TheBloke/em_german_7b_v01-GPTQ) | [Link](https://huggingface.co/TheBloke/em_german_7b_v01-GGUF) | [Link](https://huggingface.co/TheBloke/em_german_7b_v01-AWQ) |
| Llama2 13b  | [Link](https://huggingface.co/jphme/em_german_13b_v01) | [Link](https://huggingface.co/TheBloke/em_german_13b_v01-GPTQ) | [Link](https://huggingface.co/TheBloke/em_german_13b_v01-GGUF) | [Link](https://huggingface.co/TheBloke/em_german_13b_v01-AWQ) |
| Llama2 70b   | [Link](https://huggingface.co/jphme/em_german_70b_v01) | [Link](https://huggingface.co/TheBloke/em_german_70b_v01-GPTQ) | [Link](https://huggingface.co/TheBloke/em_german_70b_v01-GGUF) | [Link](https://huggingface.co/TheBloke/em_german_70b_v01-AWQ) |
| [Mistral 7b](https://huggingface.co/mistralai/Mistral-7B-v0.1) | [Link](https://huggingface.co/jphme/em_german_mistral_v01) | [Link](https://huggingface.co/TheBloke/em_german_mistral_v01-GPTQ) | [Link](https://huggingface.co/TheBloke/em_german_mistral_v01-GGUF) | [Link](https://huggingface.co/TheBloke/em_german_mistral_v01-AWQ) |
| [LeoLM 7b](https://huggingface.co/LeoLM/leo-hessianai-7b) | [Link](https://huggingface.co/jphme/em_german_7b_leo) | [Link](https://huggingface.co/jphme/em_german_7b_leo_gptq) | [Link](hhttps://huggingface.co/jphme/em_german_7b_leo_gguf) | tbc |
| [LeoLM 13b](https://huggingface.co/LeoLM/leo-hessianai-13b) | soon | soon | [Link](https://huggingface.co/jphme/em_german_13b_leo_gguf) | tbc |
| [LeoLM Mistral](https://huggingface.co/LeoLM/leo-mistral-hessianai-7b) | [Link](https://huggingface.co/jphme/em_german_leo_mistral) | [Link](https://huggingface.co/TheBloke/em_german_leo_mistral-GPTQ) | [Link](https://huggingface.co/TheBloke/em_german_leo_mistral-GGUF) | [Link](https://huggingface.co/TheBloke/em_german_leo_mistral-AWQ) |

### Notes about the different versions:
See also the [comparison of example outputs](https://github.com/jphme/EM_German/blob/main/example_output_comparison.md) for a comparison of (7b) model capabilities.

If you get unsatisfying results with one or another EM German version, please try a different (and/or larger) model or version for your usecase.


## Demos:

You can use some of the models with **free** google Colab instances (e.g. the 7bn model in 8bit or the 13b model with GPTQ):

* [Example Colab Notebook for 13b with GPTQ](https://colab.research.google.com/drive/1IJfJdVwGkfe5MYOqHptystR3FBeEUdGn?usp=sharing)
* [Example Colab Notebook for 7b with 8bit-Loading](https://colab.research.google.com/drive/1bsv6vkLM4AlCpSyXA6ol9P32zxZmf7Zu?usp=sharing)
* [Example Colab Notebook for 7b Mistral GGUF with Grammar-based structured output](https://colab.research.google.com/drive/17O-a3D4BnVc_V9Of3dFfed18v1ULu1Sv?usp=sharing)


# Prompt Format

This model follows the Vicuna format without linebreaks (but should work with linebreaks as well). The format is as follows:

```
Du bist ein hilfreicher Assistent. USER: <instruction> ASSISTANT:
```

You can swap the standard system prompt for a better suited one (see below for RAG-tasks).

# Example Output

Please find a selection of various example outputs for all 7b versions of EM German [here](https://github.com/jphme/EM_German/blob/main/example_output_comparison.md).

**Prompt:**
> Erkläre die Bedeutung von drei wesentlichen Elementen der Bilanzierung und des Accountings nach IFRS für Unternehmen, die auf internationaler Ebene tätig sind.

**Antwort EM German Leo Mistral 7b:**
```
Die International Financial Reporting Standards (IFRS) sind eine Reihe von internationalen Rechnungslegungsstandards, die von der International Accounting Standards Board (IASB) entwickelt wurden. Sie sollen dazu beitragen, dass Finanzberichte vergleichbar, zuverlässig und relevant sind.

1. Fair Value: Dieses Konzept ist ein zentraler Bestandteil der IFRS. Es besagt, dass Vermögenswerte und Schulden zum fairen Wert bilanziert werden sollten, was dem Preis entspricht, zu dem sie zwischen Marktteilnehmern gehandelt werden könnten. Dadurch wird sichergestellt, dass das Unternehmen eine genaue Darstellung seiner finanziellen Lage liefert.

2. Konsolidierung: Die IFRS verlangen von Unternehmen, ihre Finanzergebnisse auf konsolidierter Basis darzustellen. Das bedeutet, dass alle Tochtergesellschaften und verbundenen Unternehmen in die Bilanz des Mutterunternehmens aufgenommen werden. Dadurch wird ein klareres Bild von der finanziellen Situation des Konzerns geschaffen.

3. Vollständigkeitsprinzip: Die IFRS verlangen von Unternehmen, alle relevanten Informationen offenzulegen. Dies umfasst sowohl positive als auch negative Faktoren, wie zum Beispiel Gewinne und Verluste, Einnahmen und Ausgaben sowie Risiken und Unsicherheiten. Durch dieses Prinzip wird sichergestellt, dass Investoren, Kreditgeber und andere Stakeholder eine umfassende Einschätzung der finanziellen Lage des Unternehmens vornehmen können.
```

**Prompt:**
> Ein Mensch atmet durchschnittlich 16 Mal pro Minute. Wie oft atmet er an einem Tag?

**Antwort EM German Leo Mistral 7b:**
```
 Zuerst berechnen wir, wie oft eine Person in einer Stunde atmet. Wir wissen, dass eine Stunde 60 Minuten hat, also:

Atemzüge pro Stunde = Atemfrequenz * Minuten pro Stunde
= 16 Atemzüge pro Minute * 60 Minuten
= 960 Atemzüge

Um herauszufinden, wie viele Atemzüge eine Person an einem Tag macht, müssen wir diese stündliche Rate mit der Anzahl der Stunden an einem Tag multiplizieren, also 24:

Atemzüge pro Tag = Atemzüge pro Stunde * Stunden pro Tag
= 960 Atemzüge * 24 Stunden
= 23.040 Atemzüge

Also macht ein durchschnittlicher Mensch etwa 23.040 Atemzüge an einem Tag.
```
(For more examples,  please visit [our Github Repository](https://github.com/jphme/EM_German).)

# Acknowledgements:

Many thanks to [winglian/caseus](https://huggingface.co/winglian) for his great work on Axolotl which I used to train the EM mdoels. I am also grateful to [Jon Durbin](https://huggingface.co/jondurbin) and his [Airoboros](https://huggingface.co/jondurbin/airoboros-l2-70b-2.2.1) models and code from which I borrowed many ideas and code snippets.
Additionally many thanks to [Björn Plüster](https://huggingface.co/bjoernp) and the LeoLM team for the outstanding pretraining work on LeoLM and last but not least many many thanks to [TheBloke](https://huggingface.co/TheBloke) for the preparation of quantized versions in all formats under the sun.
The 70b model was trained with support of the [OVH Cloud Startup Program](https://startup.ovhcloud.com/en/).

# Contact

For detailed feedback & feature requests, please open an issue or get in contact with me via [my website](https://www.jph.me).

*PS: We are also always interested in support for our startup [ellamind](https://ellamind.com), which will offer customized models for business applications in the future (we are currently still in stealth mode). If you use our models for business applications and have advanced needs for specialized capabilities, please get in touch.*

# Disclaimer:

I am not responsible for the actions of third parties who use this model or the outputs of the model. This model should only be used for research purposes. The original base model license applies and is distributed with the model files.