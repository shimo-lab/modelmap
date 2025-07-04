**Please Check out EM German, our new german-speaking LLM model family with significantly improved capabilites. EM German is available in Llama2 7b,13b and 70b and Mistral- and LeoLM-based versions! All information and download links can be found [here](https://github.com/jphme/EM_German/blob/main/README.md).**


# Llama 2 13b Chat German

Llama-2-13b-chat-german is a variant of [Meta](https://huggingface.co/meta-llama)´s [Llama 2 13b Chat](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) model, finetuned on an additional dataset in German language.

This model is optimized for German text, providing proficiency in understanding, generating, and interacting with German language content. However the model is not yet fully optimized for German language, as it has been trained on a small, experimental dataset and has limited capabilities due to the small parameter count.
Some of the fineunting data is also targeted towards factual retrieval (only answer questions from information in the context and refuse to hallucinate) and the model should perform better for these tasks than original Llama 2 Chat.

I am working on improving the model´s capabilities and will update the model if there is sufficient interest.

A quantized GGML version for use with llama.cpp, kobold.cpp and other GUIs for CPU inference can be found [here](https://huggingface.co/jphme/Llama-2-13b-chat-german-GGML).

Please note the license of the base model, which is contained in the repo under LICENSE.TXT and see the original model card below for more information.

## Data

* Prorietary German Conversation Dataset 
* German SQuAD and German legal SQuAD data (see datasets), augmented with "wrong" contexts, to improve factual RAG

## Prompt Template

Llama2 Chat uses a new prompt format:

```
<s>[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information. Please answer in the same language as the user.
<</SYS>>

This is a test question[/INST] This is a answer </s><s>
```

See also the original implementation [here](https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L213). 

There is also a (so far non-documented?) method right in transformers to generate the correct tokenization: [LLamaTokenizer._build_conversation_input_ids](https://github.com/huggingface/transformers/blob/b257c46a075419c09e5ce5c5aa39bc346ecdb9a5/src/transformers/models/llama/tokenization_llama.py#L334).

## Results

I did only evaluate the output on a small, handcrafted sample on test prompts in German, confirming that the model's ability to understand and generate German text is above the base model in many situations. More detailed evaluations and examples will be posted soon.

## Examples

*These examples were not in the training set. They have been generated with a quantized version (Q4_0 for the German finetuned version, Q4_1 for the original Llama2 Chat version), so FP16 results should be better.*

### Example 1 (General Knowledge)

**Question**: 
> Wie heißt die Hauptstadt von Nordrhein-Westfalen?

**Answer Original Llama 2 13b Chat**: 
> Hello! As your helpful and respectful assistant, I'm here to help you with any questions you may have. The main city of North Rhine-Westphalia is called Düsseldorf. Is there anything else you would like to know about this topic or the region in general? Please let me know if there's anything else I can assist you with!

**Answer Llama 2 13b Chat German**: 
> Die Hauptstadt von Nordrhein-Westfalen ist Düsseldorf.

### Example 2 (RAG/Factual Retrieval):

**Question**:
> Warum ist die Mongolische Volksrepublik nicht dem Warschauer Pakt beigetreten?
> 
> Kontext zur Beantwortung der Frage: Warschauer_Pakt
> 
> === Bilaterale Verträge über Freundschaft, Zusammenarbeit und gegenseitigen Beistand === Mit den bilateralen Bündnisverträgen wurde die Verpflichtung zur gegenseitigen Hilfeleistung unterzeichnet, um alle gewaltsamen militärischen Handlungen, die sich gegen die territoriale Integrität und Souveränität einer Vertragspartei richteten, zu verhindern. Den ersten dieser Freundschaftsverträge hatte die Sowjetunion schon während des Krieges am 12. Dezember 1943 mit der tschechoslowakischen Exilregierung abgeschlossen, der am 27. November 1963 für die Tschechoslowakei verlängert wurde. Von 1943 bis 1949 gab es bereits 23 bilaterale Verträge über Freundschaft, Zusammenarbeit und gegenseitigen Beistand (VFZ) der ersten Generation in Osteuropa. Neben diesem Vertragssystem bestanden ab 1956/57 auch weitere Abkommen: * Truppenstationierungsabkommen der Sowjetunion mit der DDR (12. März 1957), * Truppenstationierungsabkommen der Sowjetunion mit der Volksrepublik Polen (17. Dezember 1956), * Truppenstationierungsabkommen der Sowjetunion mit Rumänien (15. April 1957) und * Truppenstationierungsabkommen der Sowjetunion mit Ungarn (27. Mai 1957) jeweils mit einer Laufzeit von 20 Jahren. Aber bereits der Vertrag über die Beziehungen zwischen der DDR und der Sowjetunion vom 20. September 1950 zur Grenzregelung enthielt eine Vereinbarung zur Stationierung von sowjetischen Truppen auf dem Gebiet der DDR. Im Juli 1963 bat auch die Mongolische Volksrepublik, dem Warschauer Pakt nach Artikel 9 des Warschauer Vertrages beizutreten. Dazu hätte ein Sonderprotokoll gefasst werden müssen, da der Vertragstext nach Artikel 4 sich nur auf Europa bezog. Aufgrund des aufkommenden Chinesisch-sowjetischen Zerwürfnisses gab es keinen Beitritt, sondern es blieb bei einem Beobachterstatus. Stattdessen wurden ab 1966 sowjetische Truppenstationierungen vereinbart. Nachdem die Sowjetunion mit der DDR am 12. Juni 1964 einen Vertrag über Freundschaft, Zusammenarbeit und gegenseitigen Beistand schloss, der die volle Einbeziehung der DDR in das bilaterale Bündnissystem vorsah, wurden in der Zeit von 1964 bis 1972 insgesamt 20 Bündnisverträge der zweiten Generation unterzeichnet: Die Hegemonie der Sowjetunion wurde durch die bilateralen Bündnisverträge noch verstärkt, da diese eine unmittelbare Beistandsverpflichtung bei einem bewaffneten Angriff vorsahen, die auch in den meisten Verträgen sich nicht nur auf Europa beschränkte. In der dritten Generation der Verträge über Freundschaft, Zusammenarbeit und gegenseitigen Beistand erfolgte nach der Unterzeichnung der Schlussakte von Helsinki der Konferenz über Sicherheit und Zusammenarbeit in Europa (KSZE) im August 1975 die Einbeziehung der Breschnew-Doktrin und der ökonomischen Integration. Zudem wurde die Laufzeit der Verträge auf 25 Jahre festgelegt. Die DDR unterzeichnete am 7. Oktober 1975 mit der Sowjetunion diesen neuen Vertrag sowie später weitere mit Ungarn (24. März 1977), Polen (29. Mai 1977), Bulgarien (14. September 1977) und der Tschechoslowakei (3. Oktober 1977).
> 
> Bitte beantworte die Frage mit einem kurzen, wörtlichen Zitat aus dem Kontext. Sollte der Kontext keine Antwort auf die Frage enthalten, bitte antworte dass die Frage mit den gegebenen Informationen nicht zu beantworten ist.

**Answer Original Llama 2 13b Chat**: 
> Die Mongolische Volksrepublik hat nicht dem Warschauer Pakt beigetreten, weil es keinen Beitritt gab, sondern nur einen Beobachterstatus. (Quelle: Der Kontext)
> 
**Answer Llama 2 13b Chat German**: 
> Aufgrund des aufkommenden Chinesisch-sowjetischen Zerwürfnisses gab es keinen Beitritt, sondern es blieb bei einem Beobachterstatus

### Example 3 (RAG / Factual Retrieval negative):

**Question**:
> Nach was benannte Spielberg seine Produktionsfirma Anfang der 1980er?
> 
> Kontext zur Beantwortung der Frage: Webbrowser
> 
> == Marktanteile und deren Messung == Bild zeigt die lt. Statistik von StatCounter meistverwendeten Browser nach Ländern 9/2019. Die Statistik für März 2020 ist über folgenden Weblink abrufbar: Die tatsächliche Verbreitung eines Webbrowsers ist nicht zweifelsfrei feststellbar. Verschiedene Anbieter veröffentlichen Statistiken über die Verbreitung von Webbrowsern aufgrund unterschiedlicher häufig recht begrenzter Datenbasen. Da die generelle Verbreitungsrate eines Browsers von verschiedensten Faktoren beeinflusst wird, sind diese Statistiken unterschiedlich aussagekräftig und kommen zu teilweise stark unterschiedlichen, scheinbar widersprüchlichen Ergebnissen. So schwankt die Verbreitung eines Browsers je nach Themengebiet einer aufgerufenen Webseite, Herkunftsregion der aufrufenden Person und dem Zeitpunkt der Messung. Beispielsweise können Benutzer an ihrem Arbeitsplatz an die Verwendung eines vorgegebenen Webbrowsers gebunden sein, privat jedoch einen anderen Browser bevorzugen und verwenden. Auch verschiedene Ereignisse führen zu starken Schwankungen. So steigt der Marktanteil bei der Veröffentlichung einer neuen Hauptversion oder sinkt beim Bekanntwerden einer Sicherheitslücke. Insgesamt geben Browserstatistiken nur die grobe Verteilung und ggf. Trends an, da jede Statistik nur auf der Auswertung der Logdateien ausgewählter Websites beruht und es keine unbestritten repräsentative Auswahl dafür zu verwendender Websites gibt. Die Messungen werden in der Regel anhand des sogenannten ''User-Agent''-Headers durchgeführt, mit der sich der verwendete Browser identifizieren lässt und die dieser bei jeder Anfrage an den Server übermittelt. Bei praktisch allen Browsern kann diese Kennung vom Benutzer verändert werden. Die weltweiten Marktanteile von Desktop-Browsern sehen laut Netmarketshare Stand Juli 2018 und September 2019 prozentual wie folgt aus: Bei Berücksichtigung auch der Browser in den inzwischen sehr häufig verwendeten mobilen Geräten wie Smartphone, Tablet etc. ergibt sich laut den veröffentlichten Statistiken von Netmarketshare, für September 2019 folgendes Bild: Chrome 66 %, Safari 19 %, Firefox 4 %, IE 2,6 %, Edge 2,5 %, QQ 1,4 % etc. Die Verbreitung laut Statistik von StatCounter der verschiedenen Browser auf mobilen Geräten ist hier abrufbar. Die Auswahl der Anzeige ist editierbar.
>
> Bitte beantworte die Frage mit einem kurzen, wörtlichen Zitat aus dem Kontext. Sollte der Kontext keine Antwort auf die Frage enthalten, bitte antworte dass die Frage mit den gegebenen Informationen nicht zu beantworten ist.

**Answer Original Llama 2 13b Chat**: 
> Sure! Here's the answer to your question with a direct quote from the context: "According to Netmarketshare, in July 2018 and September 2019, the worldwide market share of desktop browsers looked like this: Chrome 66%, Safari 19%, Firefox 4%, IE 2.6%, Edge 2.5%, QQ 1.4% etc." So, according to Netmarketshare's statistics, in July 2018 and September 2019, Google Chrome had a market share of 66%.
> 
**Answer Llama 2 13b Chat German**: 
> Mit den gegebenen Informationen ist diese Frage nicht zu beantworten.

----------------------------
----------------------------


# Original **Llama 2** model card
Llama 2 is a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. This is the repository for the 13B fine-tuned model, optimized for dialogue use cases and converted for the Hugging Face Transformers format. Links to other models can be found in the index at the bottom.

## Model Details
*Note: Use of this model is governed by the Meta license. In order to download the model weights and tokenizer, please visit the [website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and accept our License before requesting access here.*

Meta developed and publicly released the Llama 2 family of large language models (LLMs), a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama-2-Chat, are optimized for dialogue use cases. Llama-2-Chat models outperform open-source chat models on most benchmarks we tested, and in our human evaluations for helpfulness and safety, are on par with some popular closed-source models like ChatGPT and PaLM.

**Model Developers** Meta

**Variations** Llama 2 comes in a range of parameter sizes — 7B, 13B, and 70B — as well as pretrained and fine-tuned variations.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture** Llama 2 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align to human preferences for helpfulness and safety.


||Training Data|Params|Content Length|GQA|Tokens|LR|
|---|---|---|---|---|---|---|
|Llama 2|*A new mix of publicly available online data*|7B|4k|&#10007;|2.0T|3.0 x 10<sup>-4</sup>|
|Llama 2|*A new mix of publicly available online data*|13B|4k|&#10007;|2.0T|3.0 x 10<sup>-4</sup>|
|Llama 2|*A new mix of publicly available online data*|70B|4k|&#10004;|2.0T|1.5 x 10<sup>-4</sup>|

*Llama 2 family of models.* Token counts refer to pretraining data only. All models are trained with a global batch-size of 4M tokens. Bigger models -  70B -- use Grouped-Query Attention (GQA) for improved inference scalability.

**Model Dates** Llama 2 was trained between January 2023 and July 2023.

**Status** This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we improve model safety with community feedback.

**License** A custom commercial license is available at: [https://ai.meta.com/resources/models-and-libraries/llama-downloads/](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)

**Research Paper** ["Llama-2: Open Foundation and Fine-tuned Chat Models"](arxiv.org/abs/2307.09288)

## Intended Use
**Intended Use Cases** Llama 2 is intended for commercial and research use in English. Tuned models are intended for assistant-like chat, whereas pretrained models can be adapted for a variety of natural language generation tasks.

To get the expected features and performance for the chat versions, a specific formatting needs to be followed, including the `INST` and `<<SYS>>` tags, `BOS` and `EOS` tokens, and the whitespaces and breaklines in between (we recommend calling `strip()` on inputs to avoid double-spaces). See our reference code in github for details: [`chat_completion`](https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L212).

**Out-of-scope Uses** Use in any manner that violates applicable laws or regulations (including trade compliance laws).Use in languages other than English. Use in any other way that is prohibited by the Acceptable Use Policy and Licensing Agreement for Llama 2.

## Hardware and Software
**Training Factors** We used custom training libraries, Meta's Research Super Cluster, and production clusters for pretraining. Fine-tuning, annotation, and evaluation were also performed on third-party cloud compute.

**Carbon Footprint** Pretraining utilized a cumulative 3.3M GPU hours of computation on hardware of type A100-80GB (TDP of 350-400W). Estimated total emissions were 539 tCO2eq, 100% of which were offset by Meta’s sustainability program.

||Time (GPU hours)|Power Consumption (W)|Carbon Emitted(tCO<sub>2</sub>eq)|
|---|---|---|---|
|Llama 2 7B|184320|400|31.22|
|Llama 2 13B|368640|400|62.44|
|Llama 2 70B|1720320|400|291.42|
|Total|3311616||539.00|

**CO<sub>2</sub> emissions during pretraining.** Time: total GPU time required for training each model. Power Consumption: peak power capacity per GPU device for the GPUs used adjusted for power usage efficiency. 100% of the emissions are directly offset by Meta's sustainability program, and because we are openly releasing these models, the pretraining costs do not need to be incurred by others.

## Training Data
**Overview** Llama 2 was pretrained on 2 trillion tokens of data from publicly available sources. The fine-tuning data includes publicly available instruction datasets, as well as over one million new human-annotated examples. Neither the pretraining nor the fine-tuning datasets include Meta user data.

**Data Freshness** The pretraining data has a cutoff of September 2022, but some tuning data is more recent, up to July 2023.

## Evaluation Results

In this section, we report the results for the Llama 1 and Llama 2 models on standard academic benchmarks.For all the evaluations, we use our internal evaluations library.

|Model|Size|Code|Commonsense Reasoning|World Knowledge|Reading Comprehension|Math|MMLU|BBH|AGI Eval|
|---|---|---|---|---|---|---|---|---|---|
|Llama 1|7B|14.1|60.8|46.2|58.5|6.95|35.1|30.3|23.9|
|Llama 1|13B|18.9|66.1|52.6|62.3|10.9|46.9|37.0|33.9|
|Llama 1|33B|26.0|70.0|58.4|67.6|21.4|57.8|39.8|41.7|
|Llama 1|65B|30.7|70.7|60.5|68.6|30.8|63.4|43.5|47.6|
|Llama 2|7B|16.8|63.9|48.9|61.3|14.6|45.3|32.6|29.3|
|Llama 2|13B|24.5|66.9|55.4|65.8|28.7|54.8|39.4|39.1|
|Llama 2|70B|**37.5**|**71.9**|**63.6**|**69.4**|**35.2**|**68.9**|**51.2**|**54.2**|

**Overall performance on grouped academic benchmarks.** *Code:* We report the average pass@1 scores of our models on HumanEval and MBPP. *Commonsense Reasoning:* We report the average of PIQA, SIQA, HellaSwag, WinoGrande, ARC easy and challenge, OpenBookQA, and CommonsenseQA. We report 7-shot results for CommonSenseQA and 0-shot results for all other benchmarks. *World Knowledge:* We evaluate the 5-shot performance on NaturalQuestions and TriviaQA and report the average. *Reading Comprehension:* For reading comprehension, we report the 0-shot average on SQuAD, QuAC, and BoolQ. *MATH:* We report the average of the GSM8K (8 shot) and MATH (4 shot) benchmarks at top 1.

|||TruthfulQA|Toxigen|
|---|---|---|---|
|Llama 1|7B|27.42|23.00|
|Llama 1|13B|41.74|23.08|
|Llama 1|33B|44.19|22.57|
|Llama 1|65B|48.71|21.77|
|Llama 2|7B|33.29|**21.25**|
|Llama 2|13B|41.86|26.10|
|Llama 2|70B|**50.18**|24.60|

**Evaluation of pretrained LLMs on automatic safety benchmarks.** For TruthfulQA, we present the percentage of generations that are both truthful and informative (the higher the better). For ToxiGen, we present the percentage of toxic generations (the smaller the better).


|||TruthfulQA|Toxigen|
|---|---|---|---|
|Llama-2-Chat|7B|57.04|**0.00**|
|Llama-2-Chat|13B|62.18|**0.00**|
|Llama-2-Chat|70B|**64.14**|0.01|

**Evaluation of fine-tuned LLMs on different safety datasets.** Same metric definitions as above.

## Ethical Considerations and Limitations
Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their specific applications of the model.

Please see the Responsible Use Guide available at [https://ai.meta.com/llama/responsible-use-guide/](https://ai.meta.com/llama/responsible-use-guide)

## Reporting Issues
Please report any software “bug,” or other problems with the models through one of the following means:
- Reporting issues with the model: [github.com/facebookresearch/llama](http://github.com/facebookresearch/llama)
- Reporting problematic content generated by the model: [developers.facebook.com/llama_output_feedback](http://developers.facebook.com/llama_output_feedback)
- Reporting bugs and security concerns: [facebook.com/whitehat/info](http://facebook.com/whitehat/info)

## Llama Model Index
|Model|Llama2|Llama2-hf|Llama2-chat|Llama2-chat-hf|
|---|---|---|---|---|
|7B| [Link](https://huggingface.co/llamaste/Llama-2-7b) | [Link](https://huggingface.co/llamaste/Llama-2-7b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-7b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-7b-chat-hf)|
|13B| [Link](https://huggingface.co/llamaste/Llama-2-13b) | [Link](https://huggingface.co/llamaste/Llama-2-13b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-13b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-13b-hf)|
|70B| [Link](https://huggingface.co/llamaste/Llama-2-70b) | [Link](https://huggingface.co/llamaste/Llama-2-70b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-70b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-70b-hf)|