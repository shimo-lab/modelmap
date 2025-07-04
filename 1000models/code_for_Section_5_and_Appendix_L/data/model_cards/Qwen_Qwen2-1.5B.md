
# Qwen2-1.5B

## Introduction

Qwen2 is the new series of Qwen large language models. For Qwen2, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters, including a Mixture-of-Experts model. This repo contains the 1.5B Qwen2 base language model.

Compared with the state-of-the-art opensource language models, including the previous released Qwen1.5, Qwen2 has generally surpassed most opensource models and demonstrated competitiveness against proprietary models across a series of benchmarks targeting for language understanding, language generation, multilingual capability, coding, mathematics, reasoning, etc.

For more details, please refer to our [blog](https://qwenlm.github.io/blog/qwen2/), [GitHub](https://github.com/QwenLM/Qwen2), and [Documentation](https://qwen.readthedocs.io/en/latest/).
<br>


## Model Details
Qwen2 is a language model series including decoder language models of different model sizes. For each size, we release the base language model and the aligned chat model. It is based on the Transformer architecture with SwiGLU activation, attention QKV bias, group query attention, etc. Additionally, we have an improved tokenizer adaptive to multiple natural languages and codes.

## Requirements
The code of Qwen2 has been in the latest Hugging face transformers and we advise you to install `transformers>=4.37.0`, or you might encounter the following error:
```
KeyError: 'qwen2'
```


## Usage

We do not advise you to use base language models for text generation. Instead, you can apply post-training, e.g., SFT, RLHF, continued pretraining, etc., on this model.

## Performance

The evaluation of base models mainly focuses on the model performance of natural language understanding, general question answering, coding, mathematics, scientific knowledge, reasoning, multilingual capability, etc. 

The datasets for evaluation include: 
 
**English Tasks**: MMLU (5-shot), MMLU-Pro (5-shot), GPQA (5shot), Theorem QA (5-shot), BBH (3-shot), HellaSwag (10-shot), Winogrande (5-shot), TruthfulQA (0-shot), ARC-C (25-shot)
 
**Coding Tasks**: EvalPlus (0-shot) (HumanEval, MBPP, HumanEval+, MBPP+), MultiPL-E (0-shot) (Python, C++, JAVA, PHP, TypeScript, C#, Bash, JavaScript)
  
**Math Tasks**: GSM8K (4-shot), MATH (4-shot)
 
**Chinese Tasks**: C-Eval(5-shot), CMMLU (5-shot)
 
**Multilingual Tasks**: Multi-Exam (M3Exam 5-shot, IndoMMLU 3-shot, ruMMLU 5-shot, mMMLU 5-shot), Multi-Understanding (BELEBELE 5-shot, XCOPA 5-shot, XWinograd 5-shot, XStoryCloze 0-shot, PAWS-X 5-shot), Multi-Mathematics (MGSM 8-shot), Multi-Translation (Flores-101 5-shot)
 

#### Qwen2-0.5B & Qwen2-1.5B performances
|  Datasets  |  Phi-2 |   Gemma-2B | MiniCPM |  Qwen1.5-1.8B  |   Qwen2-0.5B  |  Qwen2-1.5B  |
| :--------| :---------: | :------------: | :------------: |:------------: | :------------: | :------------: |
|#Non-Emb Params | 2.5B | 2.0B | 2.4B | 1.3B | 0.35B | 1.3B |
|MMLU | 52.7 | 42.3 | 53.5 | 46.8 | 45.4 | **56.5** |
|MMLU-Pro | - | 15.9 | - | - | 14.7 | 21.8 |
|Theorem QA | - | - | - |- | 8.9 | **15.0** |
|HumanEval | 47.6 |  22.0 |**50.0**| 20.1 | 22.0 | 31.1 |
|MBPP | **55.0** | 29.2 | 47.3 | 18.0 | 22.0 | 37.4  |
|GSM8K | 57.2 |  17.7  | 53.8 | 38.4 | 36.5 | **58.5** |
|MATH  | 3.5 |  11.8  | 10.2 | 10.1 | 10.7 | **21.7** |
|BBH  | **43.4** |  35.2 | 36.9 | 24.2 | 28.4 | 37.2 |
|HellaSwag  | **73.1** |  71.4 | 68.3 | 61.4 |  49.3 | 66.6 |
|Winogrande  | **74.4** |  66.8 | -| 60.3 |  56.8 |  66.2 |
|ARC-C  | **61.1** |  48.5  | -| 37.9 | 31.5 |  43.9 |
|TruthfulQA  | 44.5 |  33.1  | -| 39.4 | 39.7 |  **45.9** |
|C-Eval   | 23.4 |   28.0    | 51.1| 59.7 |  58.2 |  **70.6** |
|CMMLU   | 24.2 |   -    | 51.1 | 57.8 | 55.1 | **70.3** |
  

## Citation

If you find our work helpful, feel free to give us a cite.

```
@article{qwen2,
  title={Qwen2 Technical Report},
  year={2024}
}
```
