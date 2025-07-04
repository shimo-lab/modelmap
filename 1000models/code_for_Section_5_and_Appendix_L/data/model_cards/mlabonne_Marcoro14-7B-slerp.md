
![](https://i.imgur.com/FSKtmRc.png)

# Marcoro14-7B-slerp

This model is a merge of the following models made with [mergekit](https://github.com/cg123/mergekit):
 * [AIDC-ai-business/Marcoroni-7B-v3](https://huggingface.co/AIDC-ai-business/Marcoroni-7B-v3)
 * [EmbeddedLLM/Mistral-7B-Merge-14-v0.1](https://huggingface.co/EmbeddedLLM/Mistral-7B-Merge-14-v0.1)

## 🏆 Evaluation

Marcoro14-7B-slerp is the best-performing 7B LLM on the Open LLM Leaderboard (rank 1 below is 9B):

![](https://i.imgur.com/5XUuP7g.png)

I also evaluated it using Nous' benchmark suite and obtained the following results:

|          Model          |AGIEval|GPT4ALL|TruthfulQA|Bigbench|Average|
|-------------------------|------:|------:|---------:|-------:|------:|
|Marcoro14-7B-slerp       |  44.66|  76.24|     64.15|   45.64|  57.67|
|OpenHermes-2.5-Mistral-7B|  43.07|  73.12|     53.04|   40.96|  52.57|
|Change                   |  +1.59|  +3.12|    +11.11|   +4.68|   +5.1|

### AGIEval
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |26.38|±  |  2.77|
|                              |       |acc_norm|24.41|±  |  2.70|
|agieval_logiqa_en             |      0|acc     |38.25|±  |  1.91|
|                              |       |acc_norm|39.32|±  |  1.92|
|agieval_lsat_ar               |      0|acc     |24.35|±  |  2.84|
|                              |       |acc_norm|25.22|±  |  2.87|
|agieval_lsat_lr               |      0|acc     |50.00|±  |  2.22|
|                              |       |acc_norm|50.59|±  |  2.22|
|agieval_lsat_rc               |      0|acc     |62.83|±  |  2.95|
|                              |       |acc_norm|62.08|±  |  2.96|
|agieval_sat_en                |      0|acc     |79.61|±  |  2.81|
|                              |       |acc_norm|79.61|±  |  2.81|
|agieval_sat_en_without_passage|      0|acc     |45.15|±  |  3.48|
|                              |       |acc_norm|45.63|±  |  3.48|
|agieval_sat_math              |      0|acc     |33.18|±  |  3.18|
|                              |       |acc_norm|30.45|±  |  3.11|

Average: 44.66%

### GPT4ALL
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |63.91|±  |  1.40|
|             |       |acc_norm|64.93|±  |  1.39|
|arc_easy     |      0|acc     |86.07|±  |  0.71|
|             |       |acc_norm|83.75|±  |  0.76|
|boolq        |      1|acc     |88.56|±  |  0.56|
|hellaswag    |      0|acc     |67.31|±  |  0.47|
|             |       |acc_norm|85.28|±  |  0.35|
|openbookqa   |      0|acc     |36.40|±  |  2.15|
|             |       |acc_norm|48.20|±  |  2.24|
|piqa         |      0|acc     |82.59|±  |  0.88|
|             |       |acc_norm|84.39|±  |  0.85|
|winogrande   |      0|acc     |78.53|±  |  1.15|

Average: 76.24%

### TruthfulQA
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |46.88|±  |  1.75|
|             |       |mc2   |64.15|±  |  1.52|

Average: 64.15%

### Bigbench
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|56.32|±  |  3.61|
|bigbench_date_understanding                     |      0|multiple_choice_grade|66.40|±  |  2.46|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|45.35|±  |  3.11|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|20.33|±  |  2.13|
|                                                |       |exact_str_match      | 4.74|±  |  1.12|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|30.00|±  |  2.05|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|21.43|±  |  1.55|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|52.33|±  |  2.89|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|39.20|±  |  2.19|
|bigbench_navigate                               |      0|multiple_choice_grade|53.90|±  |  1.58|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|72.15|±  |  1.00|
|bigbench_ruin_names                             |      0|multiple_choice_grade|52.46|±  |  2.36|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|25.75|±  |  1.38|
|bigbench_snarks                                 |      0|multiple_choice_grade|72.38|±  |  3.33|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|73.63|±  |  1.40|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|45.70|±  |  1.58|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|23.44|±  |  1.20|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|18.51|±  |  0.93|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|52.33|±  |  2.89|

Average: 45.64%

Average score: 57.67%

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: AIDC-ai-business/Marcoroni-7B-v3
        layer_range: [0, 32]
      - model: EmbeddedLLM/Mistral-7B-Merge-14-v0.1
        layer_range: [0, 32]
merge_method: slerp
base_model: AIDC-ai-business/Marcoroni-7B-v3
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "mlabonne/Marcoro14-7B-slerp"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```

Output:

> A large language model is a type of artificial intelligence (AI) system that has been trained on vast amounts of text data. It's designed to understand and generate human-like language, making predictions on what words or phrases might come next in a sentence or document. These models use complex algorithms and neural network architectures to learn from the data and improve their performance over time. Some well-known large language models include GPT-3 from OpenAI and BERT from Google.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_mlabonne__Marcoro14-7B-slerp)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |73.01|
|AI2 Reasoning Challenge (25-Shot)|69.80|
|HellaSwag (10-Shot)              |87.13|
|MMLU (5-Shot)                    |65.11|
|TruthfulQA (0-shot)              |63.54|
|Winogrande (5-shot)              |81.61|
|GSM8k (5-shot)                   |70.89|

