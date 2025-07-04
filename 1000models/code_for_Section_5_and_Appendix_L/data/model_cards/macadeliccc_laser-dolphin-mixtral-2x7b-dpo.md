# Laser-Dolphin-Mixtral-2x7b-dpo

![laser_dolphin_image](./dolphin_moe.png)

**New Version out now!**

Credit to Fernando Fernandes and Eric Hartford for their project [laserRMT](https://github.com/cognitivecomputations/laserRMT)

## Overview

This model is a medium-sized MoE implementation based on [cognitivecomputations/dolphin-2.6-mistral-7b-dpo-laser](https://huggingface.co/cognitivecomputations/dolphin-2.6-mistral-7b-dpo-laser)

+ The new version shows ~1 point increase in evaluation performance on average.
  
## Process 

+ The process is outlined in this [notebook](https://github.com/cognitivecomputations/laserRMT/blob/main/examples/laser-dolphin-mixtral-2x7b.ipynb)

+ The mergekit_config is in the files.

+ The models used in the configuration are not lasered, but the final product is. This is an update from the last version.

+ This process is experimental. Your mileage may vary. 

## Future Goals

+ [ ] Function Calling
+ [ ] v2 with new base model to improve performance 

## Quantizations

### ExLlamav2

_These are the recommended quantizations for users that are running the model on GPU_

Thanks to user [bartowski](https://huggingface.co/bartowski) we now have exllamav2 quantizations in 3.5 through 8 bpw. They are available here:

+ [bartowski/laser-dolphin-mixtral-2x7b-dpo-exl2](https://huggingface.co/bartowski/laser-dolphin-mixtral-2x7b-dpo-exl2)

| Branch | Bits | lm_head bits | VRAM (4k) | VRAM (16k) | VRAM (32k) | Description |
| ----- | ---- | ------- | ------ | ------ | ------ | ------------ |
| [8_0](https://huggingface.co/bartowski/laser-dolphin-mixtral-2x7b-dpo-exl2/tree/8_0) | 8.0 | 8.0 | 13.7 GB | 15.1 GB | 17.2 GB | Maximum quality that ExLlamaV2 can produce, near unquantized performance. |
| [6_5](https://huggingface.co/bartowski/laser-dolphin-mixtral-2x7b-dpo-exl2/tree/6_5) | 6.5  | 8.0 | 11.5 GB | 12.9 GB | 15.0 GB | Near unquantized performance at vastly reduced size, **recommended**. |
| [5_0](https://huggingface.co/bartowski/laser-dolphin-mixtral-2x7b-dpo-exl2/tree/5_0) | 5.0  | 6.0 | 9.3 GB | 10.7 GB | 12.8 GB | Slightly lower quality vs 6.5, great for 12gb cards with 16k context. |
| [4_25](https://huggingface.co/bartowski/laser-dolphin-mixtral-2x7b-dpo-exl2/tree/4_25) | 4.25 | 6.0 | 8.2 GB | 9.6 GB | 11.7 GB | GPTQ equivalent bits per weight. |
| [3_5](https://huggingface.co/bartowski/laser-dolphin-mixtral-2x7b-dpo-exl2/tree/3_5) | 3.5  | 6.0 | 7.0 GB | 8.4 GB | 10.5 GB | Lower quality, not recommended. |

His quantizations represent the first ~13B model with GQA support. Check out his repo for more information!

### GGUF

*Current GGUF [Quantizations](https://huggingface.co/macadeliccc/laser-dolphin-mixtral-2x7b-dpo-GGUF)*

### AWQ

*Current AWQ [Quantizations](https://huggingface.co/macadeliccc/laser-dolphin-mixtral-2x7b-dpo-AWQ)

### TheBloke

**These Quants will result in unpredicted behavior. New quants are available as I have updated the model**

Quatizations provided by [TheBloke](https://huggingface.co/TheBloke/laser-dolphin-mixtral-2x7b-dpo-GGUF)

## HF Spaces
+ GGUF chat available [here](https://huggingface.co/spaces/macadeliccc/laser-dolphin-mixtral-chat-GGUF)
+ 4-bit bnb chat available [here](https://huggingface.co/spaces/macadeliccc/laser-dolphin-mixtral-chat)

# Ollama

```bash
ollama run macadeliccc/laser-dolphin-mixtral-2x7b-dpo
```

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6455cc8d679315e4ef16fbec/oVwa7Dwkt00tk8_MtlJdR.png)

## Code Example
Switch the commented model definition to use in 4-bit. Should work with 9GB and still exceed the single 7B model by 5-6 points roughly

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

def generate_response(prompt):
    """
    Generate a response from the model based on the input prompt.

    Args:
    prompt (str): Prompt for the model.

    Returns:
    str: The generated response from the model.
    """
    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate output tokens
    outputs = model.generate(**inputs, max_new_tokens=256, eos_token_id=tokenizer.eos_token_id, pad_token_id=tokenizer.pad_token_id)

    # Decode the generated tokens to a string
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response

# Load the model and tokenizer
model_id = "macadeliccc/laser-dolphin-mixtral-2x7b-dpo"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, load_in_4bit=True)

prompt = "Write a quicksort algorithm in python"

# Generate and print responses for each language
print("Response:")
print(generate_response(prompt), "\n")
```

[colab](https://colab.research.google.com/drive/1cmRhAkDWItV7utHNqNANVZnqDqQNsTUr?usp=sharing) with usage example

## Eval

## EQ Bench

<pre>----Benchmark Complete----
2024-01-31 16:55:37
Time taken: 31.1 mins
Prompt Format: ChatML
Model: macadeliccc/laser-dolphin-mixtral-2x7b-dpo-GGUF
Score (v2): 72.76
Parseable: 171.0
---------------
Batch completed
Time taken: 31.2 mins
---------------
</pre>



evaluation [colab](https://colab.research.google.com/drive/1FpwgsGzCR4tORTxAwUxpN3PcP22En2xk?usp=sharing)
## Summary of previous evaluation
|                                               Model                                               |AGIEval|GPT4All|TruthfulQA|Bigbench|Average|
|---------------------------------------------------------------------------------------------------|------:|------:|---------:|-------:|------:|
|[laser-dolphin-mixtral-2x7b-dpo](https://huggingface.co/macadeliccc/laser-dolphin-mixtral-2x7b-dpo)|  41.31|  73.67|     61.69|   42.79|  54.87|

## Detailed current evaluation
|                                               Model                                               |AGIEval|GPT4All|TruthfulQA|Bigbench|Average|
|---------------------------------------------------------------------------------------------------|------:|------:|---------:|-------:|------:|
|[laser-dolphin-mixtral-2x7b-dpo](https://huggingface.co/macadeliccc/laser-dolphin-mixtral-2x7b-dpo)|  42.25|  73.45|     63.44|   43.96|  55.77|

### AGIEval
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |21.26|±  |  2.57|
|                              |       |acc_norm|21.65|±  |  2.59|
|agieval_logiqa_en             |      0|acc     |34.72|±  |  1.87|
|                              |       |acc_norm|35.64|±  |  1.88|
|agieval_lsat_ar               |      0|acc     |26.96|±  |  2.93|
|                              |       |acc_norm|26.96|±  |  2.93|
|agieval_lsat_lr               |      0|acc     |45.88|±  |  2.21|
|                              |       |acc_norm|46.08|±  |  2.21|
|agieval_lsat_rc               |      0|acc     |59.48|±  |  3.00|
|                              |       |acc_norm|59.48|±  |  3.00|
|agieval_sat_en                |      0|acc     |73.79|±  |  3.07|
|                              |       |acc_norm|73.79|±  |  3.07|
|agieval_sat_en_without_passage|      0|acc     |42.23|±  |  3.45|
|                              |       |acc_norm|41.26|±  |  3.44|
|agieval_sat_math              |      0|acc     |37.27|±  |  3.27|
|                              |       |acc_norm|33.18|±  |  3.18|

Average: 42.25%

### GPT4All
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |58.36|±  |  1.44|
|             |       |acc_norm|58.02|±  |  1.44|
|arc_easy     |      0|acc     |82.20|±  |  0.78|
|             |       |acc_norm|77.40|±  |  0.86|
|boolq        |      1|acc     |87.52|±  |  0.58|
|hellaswag    |      0|acc     |67.50|±  |  0.47|
|             |       |acc_norm|84.43|±  |  0.36|
|openbookqa   |      0|acc     |34.40|±  |  2.13|
|             |       |acc_norm|47.00|±  |  2.23|
|piqa         |      0|acc     |81.61|±  |  0.90|
|             |       |acc_norm|82.59|±  |  0.88|
|winogrande   |      0|acc     |77.19|±  |  1.18|


Average: 73.45%

### GSM8K
|Task |Version|           Metric            |Value|   |Stderr|
|-----|------:|-----------------------------|-----|---|------|
|gsm8k|      2|exact_match,get-answer       | 0.75|   |      |
|     |       |exact_match_stderr,get-answer| 0.01|   |      |
|     |       |alias                        |gsm8k|   |      |

### TruthfulQA
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |45.90|±  |  1.74|
|             |       |mc2   |63.44|±  |  1.56|

Average: 63.44%

### Bigbench
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|58.42|±  |  3.59|
|bigbench_date_understanding                     |      0|multiple_choice_grade|60.70|±  |  2.55|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|38.37|±  |  3.03|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|21.73|±  |  2.18|
|                                                |       |exact_str_match      | 0.00|±  |  0.00|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|35.00|±  |  2.14|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|23.57|±  |  1.61|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|50.33|±  |  2.89|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|45.00|±  |  2.23|
|bigbench_navigate                               |      0|multiple_choice_grade|50.00|±  |  1.58|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|60.35|±  |  1.09|
|bigbench_ruin_names                             |      0|multiple_choice_grade|51.12|±  |  2.36|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|32.26|±  |  1.48|
|bigbench_snarks                                 |      0|multiple_choice_grade|67.96|±  |  3.48|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|70.59|±  |  1.45|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|35.80|±  |  1.52|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|22.56|±  |  1.18|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|17.20|±  |  0.90|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|50.33|±  |  2.89|

Average: 43.96%

Average score: 55.77%

Elapsed time: 02:43:45
## Citations

Fernando Fernandes Neto and Eric Hartford. "Optimizing Large Language Models Using Layer-Selective Rank Reduction and Random Matrix Theory." 2024.

```bibtex
@article{sharma2023truth,
title={The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction},
author={Sharma, Pratyusha and Ash, Jordan T and Misra, Dipendra},
journal={arXiv preprint arXiv:2312.13558},
year={2023} }
```

```bibtex
@article{gao2021framework,
  title={A framework for few-shot language model evaluation},
  author={Gao, Leo and Tow, Jonathan and Biderman, Stella and Black, Sid and DiPofi, Anthony and Foster, Charles and Golding, Laurence and Hsu, Jeffrey and McDonell, Kyle and Muennighoff, Niklas and others},
  journal={Version v0. 0.1. Sept},
  year={2021}
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_macadeliccc__laser-dolphin-mixtral-2x7b-dpo)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |67.16|
|AI2 Reasoning Challenge (25-Shot)|65.96|
|HellaSwag (10-Shot)              |85.80|
|MMLU (5-Shot)                    |63.17|
|TruthfulQA (0-shot)              |60.76|
|Winogrande (5-shot)              |79.01|
|GSM8k (5-shot)                   |48.29|

