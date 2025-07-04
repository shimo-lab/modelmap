# MedAlpaca 7b


## Table of Contents

[Model Description](#model-description)  
- [Architecture](#architecture)    
- [Training Data](#trainig-data)  
[Model Usage](#model-usage)  
[Limitations](#limitations)  

## Model Description
### Architecture
`medalpaca-7b` is a large language model specifically fine-tuned for medical domain tasks. 
It is based on LLaMA (Large Language Model Meta AI) and contains 7 billion parameters. 
The primary goal of this model is to improve question-answering and medical dialogue tasks.
Architecture


### Training Data
The training data for this project was sourced from various resources. 
Firstly, we used Anki flashcards to automatically generate questions, 
from the front of the cards and anwers from the back of the card. 
Secondly, we generated medical question-answer pairs from [Wikidoc](https://www.wikidoc.org/index.php/Main_Page). 
We extracted paragraphs with relevant headings, and used Chat-GPT 3.5 
to generate questions from the headings and using the corresponding paragraphs 
as answers. This dataset is still under development and we believe 
that approximately 70% of these question answer pairs are factual correct. 
Thirdly, we used StackExchange to extract question-answer pairs, taking the 
top-rated question from five categories: Academia, Bioinformatics, Biology, 
Fitness, and Health. Additionally, we used a dataset from [ChatDoctor](https://arxiv.org/abs/2303.14070) 
consisting of 200,000 question-answer pairs, available at https://github.com/Kent0n-Li/ChatDoctor.

| Source                      | n items |
|------------------------------|--------|
| ChatDoc large                | 200000 |
| wikidoc                      | 67704  |
| Stackexchange academia       | 40865  |
| Anki flashcards              | 33955  |
| Stackexchange biology        | 27887  |
| Stackexchange fitness        | 9833   |
| Stackexchange health         | 7721   |
| Wikidoc patient information  | 5942   |
| Stackexchange bioinformatics | 5407   |

## Model Usage
To evaluate the performance of the model on a specific dataset, you can use the Hugging Face Transformers library's built-in evaluation scripts. Please refer to the evaluation guide for more information.
Inference

You can use the model for inference tasks like question-answering and medical dialogues using the Hugging Face Transformers library. Here's an example of how to use the model for a question-answering task:

```python

from transformers import pipeline

pl = pipeline("text-generation", model="medalpaca/medalpaca-7b", tokenizer="medalpaca/medalpaca-7b")
question = "What are the symptoms of diabetes?"
context = "Diabetes is a metabolic disease that causes high blood sugar. The symptoms include increased thirst, frequent urination, and unexplained weight loss."
answer = pl(f"Context: {context}\n\nQuestion: {question}\n\nAnswer: ")
print(answer)
```

## Limitations
The model may not perform effectively outside the scope of the medical domain.
The training data primarily targets the knowledge level of medical students, 
which may result in limitations when addressing the needs of board-certified physicians.
The model has not been tested in real-world applications, so its efficacy and accuracy are currently unknown. 
It should never be used as a substitute for a doctor's opinion and must be treated as a research tool only.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_medalpaca__medalpaca-7b)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 44.98   |
| ARC (25-shot)         | 54.1          |
| HellaSwag (10-shot)   | 80.42    |
| MMLU (5-shot)         | 41.47         |
| TruthfulQA (0-shot)   | 40.46   |
| Winogrande (5-shot)   | 71.19   |
| GSM8K (5-shot)        | 3.03        |
| DROP (3-shot)         | 24.21         |
