
# OpenHermes-13B

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6317aade83d8d2fd903192d9/ovkrkIIUwJ9azhPtW6dAb.png)

## Model description

OpenHermes 13B is the first fine tune of the Hermes dataset that has a fully open source dataset!

OpenHermes was trained on 242,000 entries of primarily GPT-4 generated data, from open datasets across the AI landscape, including:

- GPTeacher - General Instruct, Roleplay v1, Roleplay v2, and Code Instruct Datasets, by Teknium
- WizardLM (v1, evol_instruct 70k), by WizardLM Team/nlpxucan
- Airoboros GPT-4 (v1.0), by JonDurbin
- Camel-AI's domain expert datasets, by the Camel-AI Team
- CodeAlpaca, by Sahil2801
- GPT4-LLM and Unnatural Instructions, by Microsoft

Filtering included removal of OpenAI refusals, disclaimers, and "As an AI" type examples and more

The base dataset mix the model was trained on is identical to Nous-Hermes', minus the Nous-Instruct and PDACTL datasets which were private datasets.

The WANDB Project is public and can be examined at this link: https://wandb.ai/teknium1/openhermes/runs/openhermes-v2-fullft-13b

Huge thank you to [main_horse](https://twitter.com/main_horse) for compute access and a16z for sponsoring my work, and all the dataset creators and other people who's work has contributed to this project!

## Example Outputs

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6317aade83d8d2fd903192d9/wMSeFqUSBwCNefm7s6G1-.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6317aade83d8d2fd903192d9/00iVenvEOMWIO9X6EY2EZ.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6317aade83d8d2fd903192d9/o7hHbCbtwMLitDy-FWDAg.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6317aade83d8d2fd903192d9/-9ZT1FBSE2BJhDowoh6Gj.png)

## Benchmark Information

## Benchmark Results

GPT-4All Benchmark Set
```
|    Task     |Version| Metric |Value |   |Stderr|
|-------------|------:|--------|-----:|---|-----:|
|arc_challenge|      0|acc     |0.5009|±  |0.0146|
|             |       |acc_norm|0.5247|±  |0.0146|
|arc_easy     |      0|acc     |0.8127|±  |0.0080|
|             |       |acc_norm|0.7854|±  |0.0084|
|boolq        |      1|acc     |0.8153|±  |0.0068|
|hellaswag    |      0|acc     |0.6126|±  |0.0049|
|             |       |acc_norm|0.7995|±  |0.0040|
|openbookqa   |      0|acc     |0.3660|±  |0.0216|
|             |       |acc_norm|0.4600|±  |0.0223|
|piqa         |      0|acc     |0.7922|±  |0.0095|
|             |       |acc_norm|0.8112|±  |0.0091|
|winogrande   |      0|acc     |0.7293|±  |0.0125|
Average: 0.7036
```  

AGI-Eval
```
|             Task             |Version| Metric |Value |   |Stderr|
|------------------------------|------:|--------|-----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |0.2008|±  |0.0252|
|                              |       |acc_norm|0.2126|±  |0.0257|
|agieval_logiqa_en             |      0|acc     |0.3410|±  |0.0186|
|                              |       |acc_norm|0.3564|±  |0.0188|
|agieval_lsat_ar               |      0|acc     |0.2261|±  |0.0276|
|                              |       |acc_norm|0.2174|±  |0.0273|
|agieval_lsat_lr               |      0|acc     |0.3725|±  |0.0214|
|                              |       |acc_norm|0.3373|±  |0.0210|
|agieval_lsat_rc               |      0|acc     |0.4684|±  |0.0305|
|                              |       |acc_norm|0.4572|±  |0.0304|
|agieval_sat_en                |      0|acc     |0.6553|±  |0.0332|
|                              |       |acc_norm|0.5971|±  |0.0343|
|agieval_sat_en_without_passage|      0|acc     |0.4515|±  |0.0348|
|                              |       |acc_norm|0.4029|±  |0.0343|
|agieval_sat_math              |      0|acc     |0.3273|±  |0.0317|
|                              |       |acc_norm|0.2636|±  |0.0298|
Average: 0.3556
```
BigBench Reasoning Test
```
|                      Task                      |Version|       Metric        |Value |   |Stderr|
|------------------------------------------------|------:|---------------------|-----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|0.5368|±  |0.0363|
|bigbench_date_understanding                     |      0|multiple_choice_grade|0.7127|±  |0.0236|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|0.3023|±  |0.0286|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|0.1003|±  |0.0159|
|                                                |       |exact_str_match      |0.0000|±  |0.0000|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|0.2720|±  |0.0199|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|0.1986|±  |0.0151|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|0.4500|±  |0.0288|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|0.2880|±  |0.0203|
|bigbench_navigate                               |      0|multiple_choice_grade|0.5000|±  |0.0158|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|0.5390|±  |0.0111|
|bigbench_ruin_names                             |      0|multiple_choice_grade|0.3906|±  |0.0231|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|0.1844|±  |0.0123|
|bigbench_snarks                                 |      0|multiple_choice_grade|0.5249|±  |0.0372|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|0.5335|±  |0.0159|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|0.2980|±  |0.0145|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|0.2048|±  |0.0114|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|0.1297|±  |0.0080|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|0.4500|±  |0.0288|
Average: 36.75
```  

This is a slight improvement on GPT4ALL Suite and BigBench Suite, with a degredation in AGIEval compared to the original hermes.

Average Score Comparison between Nous-Hermes Llama-2 and OpenHermes Llama-2:
```
|             Bench            | Nous-Hermes | OpenHermes | Change |
|------------------------------|------------:|------------|--------|
|GPT4All                       |        70.00|       70.36|   +0.36|
|------------------------------------------------------------------|
|BigBench                      |        36.57|       36.75|   +0.18|
|------------------------------------------------------------------|
|AGI Eval                      |        37.20|       35.56|   -1.64|
```

## Training procedure


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6317aade83d8d2fd903192d9/pqQ6MrMVy80hHEKSfqIX2.png)

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 300
- num_epochs: 3