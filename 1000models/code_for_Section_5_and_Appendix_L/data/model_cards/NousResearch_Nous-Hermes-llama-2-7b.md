
# Model Card: Nous-Hermes-Llama2-7b

Compute provided by our project sponsor Redmond AI, thank you! Follow RedmondAI on Twitter @RedmondAI.

## Model Description

Nous-Hermes-Llama2-7b is a state-of-the-art language model fine-tuned on over 300,000 instructions. This model was fine-tuned by Nous Research, with Teknium leading the fine tuning process and dataset curation, Redmond AI sponsoring the compute, and several other contributors.

This Hermes model uses the exact same dataset as Hermes on Llama-1. This is to ensure consistency between the old Hermes and new, for anyone who wanted to keep Hermes as similar to the old one, just more capable.

This model stands out for its long responses, lower hallucination rate, and absence of OpenAI censorship mechanisms. The fine-tuning process was performed with a 4096 sequence length on an 8x a100 80GB DGX machine.


## Model Training

The model was trained almost entirely on synthetic GPT-4 outputs. Curating high quality GPT-4 datasets enables incredibly high quality in knowledge, task completion, and style.

This includes data from diverse sources such as GPTeacher, the general, roleplay v1&2, code instruct datasets, Nous Instruct & PDACTL (unpublished), and several others, detailed further below

## Collaborators
The model fine-tuning and the datasets were a collaboration of efforts and resources between Teknium, Karan4D, Emozilla, Huemin Art and Redmond AI. 
  
Special mention goes to @winglian for assisting in some of the training issues.

Huge shoutout and acknowledgement is deserved for all the dataset creators who generously share their datasets openly. 

Among the contributors of datasets:
- GPTeacher was made available by Teknium
- Wizard LM by nlpxucan
- Nous Research Instruct Dataset was provided by Karan4D and HueminArt.  
- GPT4-LLM and Unnatural Instructions were provided by Microsoft
- Airoboros dataset by jondurbin
- Camel-AI's domain expert datasets are from Camel-AI
- CodeAlpaca dataset by Sahil 2801.

If anyone was left out, please open a thread in the community tab.

## Prompt Format

The model follows the Alpaca prompt format:
```
### Instruction:
<prompt>

### Response:
<leave a newline blank for model to respond>

```

or 

```
### Instruction:
<prompt>

### Input:
<additional context>

### Response:
<leave a newline blank for model to respond>
```

GPT4All:
```|    Task     |Version| Metric |Value |   |Stderr|
|-------------|------:|--------|-----:|---|-----:|
|arc_challenge|      0|acc     |0.4735|±  |0.0146|
|             |       |acc_norm|0.5017|±  |0.0146|
|arc_easy     |      0|acc     |0.7946|±  |0.0083|
|             |       |acc_norm|0.7605|±  |0.0088|
|boolq        |      1|acc     |0.8000|±  |0.0070|
|hellaswag    |      0|acc     |0.5924|±  |0.0049|
|             |       |acc_norm|0.7774|±  |0.0042|
|openbookqa   |      0|acc     |0.3600|±  |0.0215|
|             |       |acc_norm|0.4660|±  |0.0223|
|piqa         |      0|acc     |0.7889|±  |0.0095|
|             |       |acc_norm|0.7976|±  |0.0094|
|winogrande   |      0|acc     |0.6993|±  |0.0129|
Average: 0.686
```  

BigBench:
```
|                      Task                      |Version|       Metric        |Value |   |Stderr|
|------------------------------------------------|------:|---------------------|-----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|0.5579|±  |0.0361|
|bigbench_date_understanding                     |      0|multiple_choice_grade|0.6233|±  |0.0253|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|0.3062|±  |0.0288|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|0.2006|±  |0.0212|
|                                                |       |exact_str_match      |0.0000|±  |0.0000|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|0.2540|±  |0.0195|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|0.1657|±  |0.0141|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|0.4067|±  |0.0284|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|0.2780|±  |0.0201|
|bigbench_navigate                               |      0|multiple_choice_grade|0.5000|±  |0.0158|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|0.4405|±  |0.0111|
|bigbench_ruin_names                             |      0|multiple_choice_grade|0.2701|±  |0.0210|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|0.2034|±  |0.0127|
|bigbench_snarks                                 |      0|multiple_choice_grade|0.5028|±  |0.0373|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|0.6136|±  |0.0155|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|0.2720|±  |0.0141|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|0.1944|±  |0.0112|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|0.1497|±  |0.0085|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|0.4067|±  |0.0284|
Average: 0.3525
```  

AGIEval
```  
|             Task             |Version| Metric |Value |   |Stderr|
|------------------------------|------:|--------|-----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |0.2520|±  |0.0273|
|                              |       |acc_norm|0.2402|±  |0.0269|
|agieval_logiqa_en             |      0|acc     |0.2796|±  |0.0176|
|                              |       |acc_norm|0.3241|±  |0.0184|
|agieval_lsat_ar               |      0|acc     |0.2478|±  |0.0285|
|                              |       |acc_norm|0.2348|±  |0.0280|
|agieval_lsat_lr               |      0|acc     |0.2843|±  |0.0200|
|                              |       |acc_norm|0.2765|±  |0.0198|
|agieval_lsat_rc               |      0|acc     |0.3271|±  |0.0287|
|                              |       |acc_norm|0.3011|±  |0.0280|
|agieval_sat_en                |      0|acc     |0.4660|±  |0.0348|
|                              |       |acc_norm|0.4223|±  |0.0345|
|agieval_sat_en_without_passage|      0|acc     |0.3738|±  |0.0338|
|                              |       |acc_norm|0.3447|±  |0.0332|
|agieval_sat_math              |      0|acc     |0.2500|±  |0.0293|
|                              |       |acc_norm|0.2364|±  |0.0287|
Average: 0.2975
```  

## Benchmark Results




## Resources for Applied Use Cases:
For an example of a back and forth chatbot using huggingface transformers and discord, check out: https://github.com/teknium1/alpaca-discord  
For an example of a roleplaying discord chatbot, check out this: https://github.com/teknium1/alpaca-roleplay-discordbot  

LM Studio is a good choice for a chat interface that supports GGML versions (to come)

## Future Plans
We plan to continue to iterate on both more high quality data, and new data filtering techniques to eliminate lower quality data going forward. 

## Model Usage
The model is available for download on Hugging Face. It is suitable for a wide range of language tasks, from generating creative text to understanding and following complex instructions.