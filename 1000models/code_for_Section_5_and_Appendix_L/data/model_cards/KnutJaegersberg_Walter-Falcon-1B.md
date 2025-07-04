

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63732ebbbd81fae2b3aaf3fb/b3PQZKV_xZCGL8W5pjCpu.png)


Walter is an unaligned, free thinking AI assistant that has been given time to think about things.
It's trained on instruction datasets with open source licenses. 
It covers a lot of tasks, 2/3 of the samples are from large datasets like flan, but also other datasets. 
It knows a few tricks, shown by the prompting examples below: 


General Prompt Examples:
```
### System:
You are an AI assistant. You will be given a task. Your goal is to complete the task as faithfully as you can. Let’s work this out in a step by step way to be sure we have the right answer. Always respond without hesitation.  
### Instruction:
Please answer the following question: Process:  - The bat sends out sound waves from their mouth or nose - The sound waves hit an object - Echoes are produced - The echo returns to the bat&#x27;s ears - The bat hears the echo - The bat can figure out where the object is located.  suppose No bats live here happens, how will it affect STRONGER echolocation.  Which of the following is the supposed perturbation?  - directly impacting a step of the process - indirectly impacting a step of the process - not impacting any step of the process Answer: 
### Response:
indirectly impacting a step of the process
```

```
### System:
You are an AI assistant. You will be given a task. Your goal is to complete the task as faithfully as you can. Let’s work this out in a step by step way to be sure we have the right answer. Always respond without hesitation. 
### Instruction:
You will be given a text in Russian language which contain different emotion labels from the list - ['joy', ' sadness', 'surprise', 'fear', 'anger']. You need to output the incorrect emotion label, which is irrelevant to the input text. Your answer (i) should contain only one emotion label (ii) should be unambiguous. 
### Input:
То чувство, когда идешь домой после 3-х часовой тренировки и в подъезде пахнет запеченной курицей - зачем вы меня дразните :( 
### Response:
surprise

```

CoT Prompt Example:
```
### System:
You are an AI assistant. You will be given a task. Your goal is to complete the task as faithfully as you can. Let’s work this out in a step by step way to be sure we have the right answer. Always respond without hesitation. 
### Instruction:
In this task, you are given a sentence with a missing word that can be an object, a person, and/or an action. Fill in the blank with a plausible word. Although each sentence has many correct answers, you only have to write one answer. PersonX puts ___ on PersonY's car 
### Reasoning:
Since PersonX is putting water on PersonY's car, it could be assumed that the car is on fire. 
### Response:
water

```


Summarization Example:
```
### System:
You are an AI assistant. You will be given a task. Your goal is to complete the task as faithfully as you can. Let’s work this out in a step by step way to be sure we have the right answer. Always respond without hesitation. 
### Instruction:
Below is a text. Write a comprehensive, concise and coherent summary. 
### Input:
Embodied bilingual language, also known as L2 embodiment, is the idea that people mentally simulate their actions, perceptions, and emotions when speaking and understanding a second language (L2) as with their first language (L1).  It is closely related to embodied cognition and embodied language processing, both of which only refer to native language thinking and speaking.  An example of embodied bilingual language would be situation in which a L1 English speaker learning Spanish as a second language hears the word rápido ("fast") in Spanish while taking notes and then proceeds to take notes more quickly. ==Overview== Embodied bilingual language refers to the role ......
### Response:
Embodied bilingual language, also known as L2 embodiment, is the idea that people mentally simulate their actions, perceptions, and emotions when speaking and understanding a second language (L2) as with their first language (L1).  It is closely related to embodied cognition and embodied language processing, both of which only refer to native language thinking and speaking.  An example of embodied bilingual language would be situation in which a L1 English speaker learning Spanish as a second language hears the word rápido ("fast") in Spanish while taking notes and then proceeds to take notes more quickly.

```


Essay Example:
```
### System:
You are an AI assistant. You will be given a task. Your goal is to complete the task as faithfully as you can. Let’s work this out in a step by step way to be sure we have the right answer. Always respond without hesitation. 
### Instruction:
Write the original essay for the following summary: A sleeveless dress with a round neck is a great day dress and can be worn for both formal and casual occasions. It has a sweetheart neckline and is made from 100% silk. The dress has a chiffon overlay that covers up the miniskirt and still adds to the class of the dress. 
### Response:
Sleeveless Dress with a Round Neck Essay Casual wear, day dress, more formal dress The garment is a sleeveless dress with a round neck and has a sweetheart neckline. It has sheer detail on the neckline and on the back. These aspects of design make it suitable to be worn for day and evening occasions. Its great detail and chicness make it suitable for more formal events, ....
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_KnutJaegersberg__Walter-Falcon-1B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |34.07|
|AI2 Reasoning Challenge (25-Shot)|31.06|
|HellaSwag (10-Shot)              |54.92|
|MMLU (5-Shot)                    |24.58|
|TruthfulQA (0-shot)              |38.47|
|Winogrande (5-shot)              |55.41|
|GSM8k (5-shot)                   | 0.00|

