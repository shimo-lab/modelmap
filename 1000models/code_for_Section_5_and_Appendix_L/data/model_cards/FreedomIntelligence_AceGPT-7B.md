# <b>AceGPT</b>
AceGPT is a fully fine-tuned generative text model collection based on LlaMA2, particularly in the  
Arabic language domain. This is the repository for the 7B pretrained model.

---
## Model Details
We have released the AceGPT family of large language models, which is a collection of fully fine-tuned generative text models based on LlaMA2, ranging from 7B to 13B parameters. Our models include two main categories: AceGPT and AceGPT-chat. AceGPT-chat is an optimized version specifically designed for dialogue applications. It is worth mentioning that our models have demonstrated superior performance compared to all currently available open-source Arabic dialogue models in multiple benchmark tests. Furthermore, in our human evaluations, our models have shown comparable satisfaction levels to some closed-source models, such as ChatGPT, in the Arabic language.
## Model Developers 
We are from the School of Data Science, the Chinese University of Hong Kong, Shenzhen (CUHKSZ), the Shenzhen Research Institute of Big Data (SRIBD), and the King Abdullah University of Science and Technology (KAUST).
## Variations
AceGPT families come in a range of parameter sizes —— 7B and 13B, each size of model has a base category and a -chat category.
## Input 
Models input text only.
## Output
Models output text only.

## Model Evaluation Results

Experiments on Arabic MMLU and EXAMs. ' AverageBest ', ' STEM ', ' Humanities ', ' Social Sciences ' and ' Others (Business, Health, Misc)' belong to Arabic MMLU. Best performance is in bold and the second best is underlined.

|   Model         | Average | STEM | Humanities | Social Sciences | Others (Business, Health, Misc) |EXAMs         |
|-----------------|---------|------|------------|-----------------|---------------------------------|--------------|
| Bloomz Muennighoff et al. (2022) | 30.95        | 32.32        | 26.71        | 35.85        | 28.95       | 33.89          |                             
| Llama2-7B                        | 28.81        | 28.48        | 26.68        | 29.88        | 30.18        | 23.48         |                                 
| Llama2-13B                       | 31.25        | 31.06        | 27.11        | 35.5         | 31.35        | 25.45         |                                 
| Jais-13B-base                    | 30.01        | 27.85        | 25.42        | 39.7         | 27.06        | 35.67         |                                 
| AceGPT-7B-base                   | 30.36        | 26.63        | 28.17        | 35.15        | 31.5         | 31.96         |                                 
| AceGPT-13B-base                  | <u>37.26</u> | <u>35.16</u> | <u>30.3</u>  | <u>47.34</u> | <u>36.25</u> | <u>36.63</u>  |                                 
| ChatGPT                          | <b>46.07</b> | <b>44.17</b> | <b>35.33</b> | <b>61.26</b> | <b>43.52</b> | <b>45.63 </b> | 

---
## Samples
#### Arabic MMLU (5-shot)
فيما يلي أسئلة الاختيار من متعدد (مع الإجابات) حول جبر تجريدي  
سؤال: العثور على جميع قيم c في Z_3 بحيث يكون Z_3 [x]/(x^2+c) حقلًا.  
A. 0  
B. 1  
C. 2  
D. 3  
إجابة: B  

  
سؤال: البيان رقم 1 | إذا كان aH عنصرًا في مجموعة العوامل ، فإن | aH | يقسم | a |. البيان رقم 2 | إذا كانت H و K مجموعات فرعية لـ G ، فإن HK مجموعة فرعية لـ G.  
A. صحيح ، صحيح  
B. خطأ ، خطأ  
C. صحيح ، خطأ  
D. خطأ ، صحيح  
إجابة: B  

    
سؤال: العبارة 1 | كل عنصر من مجموعة يولد مجموعة دورية من المجموعة. العبارة 2 | المجموعة المتناظرة S_10 لديها 10 عناصر.  
A. صحيح، صحيح  
B. خطأ، خطأ  
C. صحيح، خطأ  
D. خطأ، صحيح  
إجابة: C  

سؤال: البيان 1| كل وظيفة من مجموعة محدودة على نفسها يجب أن تكون واحدة لكل مجموعة. البيان 2 | كل فرع فرعي لمجموعة أبيلية هو أبيلي.  
A. صحيح, صحيح  
B. خاطئ, خاطئ  
C. صحيح, خاطئ  
D. خاطئ, صحيح\nإجابة: A  

سؤال: اعثر على خاصية الحلقة 2Z.  
A. 0  
B. 3  
C. 12  
D. 30  
إجابة: A  

سؤال: ما هو الدرجة للامتداد الميداني الناتج من Q(sqrt(2), sqrt(3), sqrt(18)) على Q؟  
A. 0  
B. 4  
C. 2  
D. 6  
إجابة:",
# You can get more detail at https://github.com/FreedomIntelligence/AceGPT/tree/main