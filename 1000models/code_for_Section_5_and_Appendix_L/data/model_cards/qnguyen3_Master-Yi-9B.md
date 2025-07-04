
## Model Description

Master is a collection of LLMs trained using human-collected seed questions and regenerate the answers with a mixture of high performance Open-source LLMs.

**Master-Yi-9B** is trained using the ORPO technique. The model shows strong abilities in reasoning on coding and math questions.

**Quantized Version**: [Here](https://huggingface.co/qnguyen3/Master-Yi-9B-GGUF)

**Communitiy Quantization** (Thanks to [@LoneStriker](https://huggingface.co/LoneStriker))
- exl2: [Master-Yi-9B-8.0bpw-h8-exl2](https://huggingface.co/LoneStriker/Master-Yi-9B-8.0bpw-h8-exl2), [Master-Yi-9B-6.0bpw-h6-exl2](https://huggingface.co/LoneStriker/Master-Yi-9B-6.0bpw-h6-exl2), [Master-Yi-9B-5.0bpw-h6-exl2](https://huggingface.co/LoneStriker/Master-Yi-9B-5.0bpw-h6-exl2), [Master-Yi-9B-4.0bpw-h6-exl2](https://huggingface.co/LoneStriker/Master-Yi-9B-4.0bpw-h6-exl2)
- GGUFs: [Master-Yi-9B-GGUF](https://huggingface.co/LoneStriker/Master-Yi-9B-GGUF)

**Master-Yi-9B-Vision**: **Coming Soon**


![img](https://huggingface.co/qnguyen3/Master-Yi-9B/resolve/main/Master-Yi-9B.webp)

## Prompt Template

```
<|im_start|>system
You are a helpful AI assistant.<|im_end|>
<|im_start|>user
What is the meaning of life?<|im_end|>
<|im_start|>assistant
```

## Examples

![image/png](https://cdn-uploads.huggingface.co/production/uploads/630430583926de1f7ec62c6b/E27JmdRAMrHQacM50-lBk.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/630430583926de1f7ec62c6b/z0HS4bxHFQzPe0gZlvCzZ.png)

## Inference Code

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    "qnguyen3/Master-Yi-9B",
    torch_dtype='auto',
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("qnguyen3/Master-Yi-9B")

prompt = "What is the mearning of life?"
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=1024,
    eos_token_id=tokenizer.eos_token_id,
    temperature=0.25,
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids)[0]
print(response)
```

## Benchmarks 

### Nous Benchmark:

|                       Model                       |AGIEval|GPT4All|TruthfulQA|Bigbench|Average|
|---------------------------------------------------|------:|------:|---------:|-------:|------:|
|[Master-Yi-9B](https://huggingface.co/qnguyen3/Master-Yi-9B)|  43.55|  71.48|     48.54|   41.43|  51.25|


### AGIEval
```
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |35.83|±  |  3.01|
|                              |       |acc_norm|31.89|±  |  2.93|
|agieval_logiqa_en             |      0|acc     |38.25|±  |  1.91|
|                              |       |acc_norm|37.79|±  |  1.90|
|agieval_lsat_ar               |      0|acc     |23.04|±  |  2.78|
|                              |       |acc_norm|20.43|±  |  2.66|
|agieval_lsat_lr               |      0|acc     |48.04|±  |  2.21|
|                              |       |acc_norm|42.75|±  |  2.19|
|agieval_lsat_rc               |      0|acc     |61.34|±  |  2.97|
|                              |       |acc_norm|52.79|±  |  3.05|
|agieval_sat_en                |      0|acc     |79.13|±  |  2.84|
|                              |       |acc_norm|72.33|±  |  3.12|
|agieval_sat_en_without_passage|      0|acc     |44.17|±  |  3.47|
|                              |       |acc_norm|42.72|±  |  3.45|
|agieval_sat_math              |      0|acc     |52.27|±  |  3.38|
|                              |       |acc_norm|47.73|±  |  3.38|

Average: 43.55%
```

### GPT4All
```
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |54.95|±  |  1.45|
|             |       |acc_norm|58.70|±  |  1.44|
|arc_easy     |      0|acc     |82.28|±  |  0.78|
|             |       |acc_norm|81.10|±  |  0.80|
|boolq        |      1|acc     |86.15|±  |  0.60|
|hellaswag    |      0|acc     |59.16|±  |  0.49|
|             |       |acc_norm|77.53|±  |  0.42|
|openbookqa   |      0|acc     |37.40|±  |  2.17|
|             |       |acc_norm|44.00|±  |  2.22|
|piqa         |      0|acc     |79.00|±  |  0.95|
|             |       |acc_norm|80.25|±  |  0.93|
|winogrande   |      0|acc     |72.61|±  |  1.25|

Average: 71.48%
```

### TruthfulQA
```
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |33.05|±  |  1.65|
|             |       |mc2   |48.54|±  |  1.54|

Average: 48.54%
```

### Bigbench
```
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|54.74|±  |  3.62|
|bigbench_date_understanding                     |      0|multiple_choice_grade|68.02|±  |  2.43|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|40.31|±  |  3.06|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|30.36|±  |  2.43|
|                                                |       |exact_str_match      | 2.23|±  |  0.78|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|26.00|±  |  1.96|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|20.71|±  |  1.53|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|44.00|±  |  2.87|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|35.00|±  |  2.14|
|bigbench_navigate                               |      0|multiple_choice_grade|58.40|±  |  1.56|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|61.80|±  |  1.09|
|bigbench_ruin_names                             |      0|multiple_choice_grade|42.41|±  |  2.34|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|31.56|±  |  1.47|
|bigbench_snarks                                 |      0|multiple_choice_grade|55.25|±  |  3.71|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|69.37|±  |  1.47|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|27.70|±  |  1.42|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|21.36|±  |  1.16|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|14.69|±  |  0.85|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|44.00|±  |  2.87|

Average: 41.43%
```

**Average score**: 51.25%


### OpenLLM Benchmark:

|                       Model                       |ARC |HellaSwag|MMLU |TruthfulQA|Winogrande|GSM8K|Average|
|---------------------------------------------------|---:|--------:|----:|---------:|---------:|----:|------:|
|[Master-Yi-9B](https://huggingface.co/qnguyen3/Master-Yi-9B)|61.6|    79.89|69.95|     48.59|     77.35|67.48|  67.48|

### ARC
```
|    Task     |Version|       Metric       |    Value    |   |Stderr|
|-------------|------:|--------------------|-------------|---|------|
|arc_challenge|      1|acc,none            |         0.59|   |      |
|             |       |acc_stderr,none     |         0.01|   |      |
|             |       |acc_norm,none       |         0.62|   |      |
|             |       |acc_norm_stderr,none|         0.01|   |      |
|             |       |alias               |arc_challenge|   |      |

Average: 61.6%
```

### HellaSwag
```
|  Task   |Version|       Metric       |  Value  |   |Stderr|
|---------|------:|--------------------|---------|---|------|
|hellaswag|      1|acc,none            |     0.61|   |      |
|         |       |acc_stderr,none     |        0|   |      |
|         |       |acc_norm,none       |     0.80|   |      |
|         |       |acc_norm_stderr,none|        0|   |      |
|         |       |alias               |hellaswag|   |      |

Average: 79.89%
```

### MMLU
```
|                  Task                  |Version|    Metric     |                 Value                 |   |Stderr|
|----------------------------------------|-------|---------------|---------------------------------------|---|------|
|mmlu                                    |N/A    |acc,none       |                                    0.7|   |      |
|                                        |       |acc_stderr,none|                                      0|   |      |
|                                        |       |alias          |mmlu                                   |   |      |
|mmlu_abstract_algebra                   |      0|alias          |  - abstract_algebra                   |   |      |
|                                        |       |acc,none       |0.46                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_anatomy                            |      0|alias          |  - anatomy                            |   |      |
|                                        |       |acc,none       |0.64                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_astronomy                          |      0|alias          |  - astronomy                          |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_business_ethics                    |      0|alias          |  - business_ethics                    |   |      |
|                                        |       |acc,none       |0.76                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_clinical_knowledge                 |      0|alias          |  - clinical_knowledge                 |   |      |
|                                        |       |acc,none       |0.71                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_college_biology                    |      0|alias          |  - college_biology                    |   |      |
|                                        |       |acc,none       |0.82                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_college_chemistry                  |      0|alias          |  - college_chemistry                  |   |      |
|                                        |       |acc,none       |0.52                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_computer_science           |      0|alias          |  - college_computer_science           |   |      |
|                                        |       |acc,none       |0.56                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_mathematics                |      0|alias          |  - college_mathematics                |   |      |
|                                        |       |acc,none       |0.44                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_college_medicine                   |      0|alias          |  - college_medicine                   |   |      |
|                                        |       |acc,none       |0.72                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_college_physics                    |      0|alias          |  - college_physics                    |   |      |
|                                        |       |acc,none       |0.45                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_computer_security                  |      0|alias          |  - computer_security                  |   |      |
|                                        |       |acc,none       |0.81                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_conceptual_physics                 |      0|alias          |  - conceptual_physics                 |   |      |
|                                        |       |acc,none       |0.74                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_econometrics                       |      0|alias          |  - econometrics                       |   |      |
|                                        |       |acc,none       |0.65                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_electrical_engineering             |      0|alias          |  - electrical_engineering             |   |      |
|                                        |       |acc,none       |0.72                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_elementary_mathematics             |      0|alias          |  - elementary_mathematics             |   |      |
|                                        |       |acc,none       |0.62                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_formal_logic                       |      0|alias          |  - formal_logic                       |   |      |
|                                        |       |acc,none       |0.57                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_global_facts                       |      0|alias          |  - global_facts                       |   |      |
|                                        |       |acc,none       |0.46                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_high_school_biology                |      0|alias          |  - high_school_biology                |   |      |
|                                        |       |acc,none       |0.86                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_chemistry              |      0|alias          |  - high_school_chemistry              |   |      |
|                                        |       |acc,none       |0.67                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_computer_science       |      0|alias          |  - high_school_computer_science       |   |      |
|                                        |       |acc,none       |0.84                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_european_history       |      0|alias          |  - high_school_european_history       |   |      |
|                                        |       |acc,none       |0.82                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_geography              |      0|alias          |  - high_school_geography              |   |      |
|                                        |       |acc,none       |0.86                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_government_and_politics|      0|alias          |  - high_school_government_and_politics|   |      |
|                                        |       |acc,none       |0.90                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_macroeconomics         |      0|alias          |  - high_school_macroeconomics         |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_mathematics            |      0|alias          |  - high_school_mathematics            |   |      |
|                                        |       |acc,none       |0.43                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_microeconomics         |      0|alias          |  - high_school_microeconomics         |   |      |
|                                        |       |acc,none       |0.86                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_physics                |      0|alias          |  - high_school_physics                |   |      |
|                                        |       |acc,none       |0.45                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_high_school_psychology             |      0|alias          |  - high_school_psychology             |   |      |
|                                        |       |acc,none       |0.87                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_high_school_statistics             |      0|alias          |  - high_school_statistics             |   |      |
|                                        |       |acc,none       |0.68                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_high_school_us_history             |      0|alias          |  - high_school_us_history             |   |      |
|                                        |       |acc,none       |0.85                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_high_school_world_history          |      0|alias          |  - high_school_world_history          |   |      |
|                                        |       |acc,none       |0.85                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_human_aging                        |      0|alias          |  - human_aging                        |   |      |
|                                        |       |acc,none       |0.76                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_human_sexuality                    |      0|alias          |  - human_sexuality                    |   |      |
|                                        |       |acc,none       |0.78                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_humanities                         |N/A    |alias          | - humanities                          |   |      |
|                                        |       |acc,none       |0.63                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_international_law                  |      0|alias          |  - international_law                  |   |      |
|                                        |       |acc,none       |0.79                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_jurisprudence                      |      0|alias          |  - jurisprudence                      |   |      |
|                                        |       |acc,none       |0.79                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_logical_fallacies                  |      0|alias          |  - logical_fallacies                  |   |      |
|                                        |       |acc,none       |0.80                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_machine_learning                   |      0|alias          |  - machine_learning                   |   |      |
|                                        |       |acc,none       |0.52                                   |   |      |
|                                        |       |acc_stderr,none|0.05                                   |   |      |
|mmlu_management                         |      0|alias          |  - management                         |   |      |
|                                        |       |acc,none       |0.83                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_marketing                          |      0|alias          |  - marketing                          |   |      |
|                                        |       |acc,none       |0.89                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_medical_genetics                   |      0|alias          |  - medical_genetics                   |   |      |
|                                        |       |acc,none       |0.78                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_miscellaneous                      |      0|alias          |  - miscellaneous                      |   |      |
|                                        |       |acc,none       |0.85                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_moral_disputes                     |      0|alias          |  - moral_disputes                     |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_moral_scenarios                    |      0|alias          |  - moral_scenarios                    |   |      |
|                                        |       |acc,none       |0.48                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_nutrition                          |      0|alias          |  - nutrition                          |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_other                              |N/A    |alias          | - other                               |   |      |
|                                        |       |acc,none       |0.75                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_philosophy                         |      0|alias          |  - philosophy                         |   |      |
|                                        |       |acc,none       |0.78                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_prehistory                         |      0|alias          |  - prehistory                         |   |      |
|                                        |       |acc,none       |0.77                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_professional_accounting            |      0|alias          |  - professional_accounting            |   |      |
|                                        |       |acc,none       |0.57                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_law                   |      0|alias          |  - professional_law                   |   |      |
|                                        |       |acc,none       |0.50                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_professional_medicine              |      0|alias          |  - professional_medicine              |   |      |
|                                        |       |acc,none       |0.71                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_professional_psychology            |      0|alias          |  - professional_psychology            |   |      |
|                                        |       |acc,none       |0.73                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_public_relations                   |      0|alias          |  - public_relations                   |   |      |
|                                        |       |acc,none       |0.76                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_security_studies                   |      0|alias          |  - security_studies                   |   |      |
|                                        |       |acc,none       |0.78                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_social_sciences                    |N/A    |alias          | - social_sciences                     |   |      |
|                                        |       |acc,none       |0.81                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_sociology                          |      0|alias          |  - sociology                          |   |      |
|                                        |       |acc,none       |0.86                                   |   |      |
|                                        |       |acc_stderr,none|0.02                                   |   |      |
|mmlu_stem                               |N/A    |alias          | - stem                                |   |      |
|                                        |       |acc,none       |0.65                                   |   |      |
|                                        |       |acc_stderr,none|0.01                                   |   |      |
|mmlu_us_foreign_policy                  |      0|alias          |  - us_foreign_policy                  |   |      |
|                                        |       |acc,none       |0.92                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |
|mmlu_virology                           |      0|alias          |  - virology                           |   |      |
|                                        |       |acc,none       |0.58                                   |   |      |
|                                        |       |acc_stderr,none|0.04                                   |   |      |
|mmlu_world_religions                    |      0|alias          |  - world_religions                    |   |      |
|                                        |       |acc,none       |0.82                                   |   |      |
|                                        |       |acc_stderr,none|0.03                                   |   |      |

Average: 69.95%
```

### TruthfulQA
```
|     Task     |Version|        Metric         |      Value      |   |Stderr|
|--------------|-------|-----------------------|-----------------|---|------|
|truthfulqa    |N/A    |bleu_acc,none          |             0.45|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |rouge1_acc,none        |             0.45|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |rouge2_diff,none       |             0.92|   |      |
|              |       |rouge2_diff_stderr,none|             1.07|   |      |
|              |       |bleu_max,none          |            23.77|   |      |
|              |       |bleu_max_stderr,none   |             0.81|   |      |
|              |       |rouge2_acc,none        |             0.38|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |acc,none               |             0.41|   |      |
|              |       |acc_stderr,none        |             0.01|   |      |
|              |       |rougeL_diff,none       |             1.57|   |      |
|              |       |rougeL_diff_stderr,none|             0.93|   |      |
|              |       |rougeL_acc,none        |             0.46|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |bleu_diff,none         |             1.38|   |      |
|              |       |bleu_diff_stderr,none  |             0.75|   |      |
|              |       |rouge2_max,none        |            33.01|   |      |
|              |       |rouge2_max_stderr,none |             1.05|   |      |
|              |       |rouge1_diff,none       |             1.72|   |      |
|              |       |rouge1_diff_stderr,none|             0.92|   |      |
|              |       |rougeL_max,none        |            45.25|   |      |
|              |       |rougeL_max_stderr,none |             0.92|   |      |
|              |       |rouge1_max,none        |            48.29|   |      |
|              |       |rouge1_max_stderr,none |             0.90|   |      |
|              |       |alias                  |truthfulqa       |   |      |
|truthfulqa_gen|      3|bleu_max,none          |            23.77|   |      |
|              |       |bleu_max_stderr,none   |             0.81|   |      |
|              |       |bleu_acc,none          |             0.45|   |      |
|              |       |bleu_acc_stderr,none   |             0.02|   |      |
|              |       |bleu_diff,none         |             1.38|   |      |
|              |       |bleu_diff_stderr,none  |             0.75|   |      |
|              |       |rouge1_max,none        |            48.29|   |      |
|              |       |rouge1_max_stderr,none |             0.90|   |      |
|              |       |rouge1_acc,none        |             0.45|   |      |
|              |       |rouge1_acc_stderr,none |             0.02|   |      |
|              |       |rouge1_diff,none       |             1.72|   |      |
|              |       |rouge1_diff_stderr,none|             0.92|   |      |
|              |       |rouge2_max,none        |            33.01|   |      |
|              |       |rouge2_max_stderr,none |             1.05|   |      |
|              |       |rouge2_acc,none        |             0.38|   |      |
|              |       |rouge2_acc_stderr,none |             0.02|   |      |
|              |       |rouge2_diff,none       |             0.92|   |      |
|              |       |rouge2_diff_stderr,none|             1.07|   |      |
|              |       |rougeL_max,none        |            45.25|   |      |
|              |       |rougeL_max_stderr,none |             0.92|   |      |
|              |       |rougeL_acc,none        |             0.46|   |      |
|              |       |rougeL_acc_stderr,none |             0.02|   |      |
|              |       |rougeL_diff,none       |             1.57|   |      |
|              |       |rougeL_diff_stderr,none|             0.93|   |      |
|              |       |alias                  | - truthfulqa_gen|   |      |
|truthfulqa_mc1|      2|acc,none               |             0.33|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc1|   |      |
|truthfulqa_mc2|      2|acc,none               |             0.49|   |      |
|              |       |acc_stderr,none        |             0.02|   |      |
|              |       |alias                  | - truthfulqa_mc2|   |      |

Average: 48.59%
```

### Winogrande
```
|   Task   |Version|    Metric     |  Value   |   |Stderr|
|----------|------:|---------------|----------|---|------|
|winogrande|      1|acc,none       |      0.77|   |      |
|          |       |acc_stderr,none|      0.01|   |      |
|          |       |alias          |winogrande|   |      |

Average: 77.35%
```

### GSM8K
```
|Task |Version|              Metric               |Value|   |Stderr|
|-----|------:|-----------------------------------|-----|---|------|
|gsm8k|      3|exact_match,strict-match           | 0.67|   |      |
|     |       |exact_match_stderr,strict-match    | 0.01|   |      |
|     |       |exact_match,flexible-extract       | 0.68|   |      |
|     |       |exact_match_stderr,flexible-extract| 0.01|   |      |
|     |       |alias                              |gsm8k|   |      |

Average: 67.48%
```

**Average score**: 67.48%
