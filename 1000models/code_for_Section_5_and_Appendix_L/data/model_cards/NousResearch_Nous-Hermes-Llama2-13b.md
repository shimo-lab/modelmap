
# Model Card: Nous-Hermes-Llama2-13b

Compute provided by our project sponsor Redmond AI, thank you! Follow RedmondAI on Twitter @RedmondAI.

## Model Description

Nous-Hermes-Llama2-13b is a state-of-the-art language model fine-tuned on over 300,000 instructions. This model was fine-tuned by Nous Research, with Teknium and Emozilla leading the fine tuning process and dataset curation, Redmond AI sponsoring the compute, and several other contributors.

This Hermes model uses the exact same dataset as Hermes on Llama-1. This is to ensure consistency between the old Hermes and new, for anyone who wanted to keep Hermes as similar to the old one, just more capable.

This model stands out for its long responses, lower hallucination rate, and absence of OpenAI censorship mechanisms. The fine-tuning process was performed with a 4096 sequence length on an 8x a100 80GB DGX machine.

## Example Outputs:
![Example4](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b/resolve/main/example5.png "Example 4")
![Example1](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b/resolve/main/Example1.png "Example 1")
![Example2](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b/resolve/main/example2.png "Example 2")
![Example3](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b/resolve/main/example3.png "Example 3")

## Model Training

The model was trained almost entirely on synthetic GPT-4 outputs. Curating high quality GPT-4 datasets enables incredibly high quality in knowledge, task completion, and style.

This includes data from diverse sources such as GPTeacher, the general, roleplay v1&2, code instruct datasets, Nous Instruct & PDACTL (unpublished), and several others, detailed further below

## Collaborators
The model fine-tuning and the datasets were a collaboration of efforts and resources between Teknium, Karan4D, Emozilla, Huemin Art, and Redmond AI. 
  
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

## Benchmark Results
AGI-Eval
```
|             Task             |Version| Metric |Value |   |Stderr|
|agieval_aqua_rat              |      0|acc     |0.2362|±  |0.0267|
|                              |       |acc_norm|0.2480|±  |0.0272|
|agieval_logiqa_en             |      0|acc     |0.3425|±  |0.0186|
|                              |       |acc_norm|0.3472|±  |0.0187|
|agieval_lsat_ar               |      0|acc     |0.2522|±  |0.0287|
|                              |       |acc_norm|0.2087|±  |0.0269|
|agieval_lsat_lr               |      0|acc     |0.3510|±  |0.0212|
|                              |       |acc_norm|0.3627|±  |0.0213|
|agieval_lsat_rc               |      0|acc     |0.4647|±  |0.0305|
|                              |       |acc_norm|0.4424|±  |0.0303|
|agieval_sat_en                |      0|acc     |0.6602|±  |0.0331|
|                              |       |acc_norm|0.6165|±  |0.0340|
|agieval_sat_en_without_passage|      0|acc     |0.4320|±  |0.0346|
|                              |       |acc_norm|0.4272|±  |0.0345|
|agieval_sat_math              |      0|acc     |0.2909|±  |0.0307|
|                              |       |acc_norm|0.2727|±  |0.0301|
```
GPT-4All Benchmark Set
```
|    Task     |Version| Metric |Value |   |Stderr|
|arc_challenge|      0|acc     |0.5102|±  |0.0146|
|             |       |acc_norm|0.5213|±  |0.0146|
|arc_easy     |      0|acc     |0.7959|±  |0.0083|
|             |       |acc_norm|0.7567|±  |0.0088|
|boolq        |      1|acc     |0.8394|±  |0.0064|
|hellaswag    |      0|acc     |0.6164|±  |0.0049|
|             |       |acc_norm|0.8009|±  |0.0040|
|openbookqa   |      0|acc     |0.3580|±  |0.0215|
|             |       |acc_norm|0.4620|±  |0.0223|
|piqa         |      0|acc     |0.7992|±  |0.0093|
|             |       |acc_norm|0.8069|±  |0.0092|
|winogrande   |      0|acc     |0.7127|±  |0.0127|
```
BigBench Reasoning Test
```
|                      Task                      |Version|       Metric        |Value |   |Stderr|

|bigbench_causal_judgement                       |      0|multiple_choice_grade|0.5526|±  |0.0362|
|bigbench_date_understanding                     |      0|multiple_choice_grade|0.7344|±  |0.0230|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|0.2636|±  |0.0275|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|0.0195|±  |0.0073|
|                                                |       |exact_str_match      |0.0000|±  |0.0000|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|0.2760|±  |0.0200|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|0.2100|±  |0.0154|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|0.4400|±  |0.0287|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|0.2440|±  |0.0192|
|bigbench_navigate                               |      0|multiple_choice_grade|0.4950|±  |0.0158|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|0.5570|±  |0.0111|
|bigbench_ruin_names                             |      0|multiple_choice_grade|0.3728|±  |0.0229|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|0.1854|±  |0.0123|
|bigbench_snarks                                 |      0|multiple_choice_grade|0.6298|±  |0.0360|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|0.6156|±  |0.0155|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|0.3140|±  |0.0147|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|0.2032|±  |0.0114|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|0.1406|±  |0.0083|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|0.4400|±  |0.0287|
```

These are the highest benchmarks Hermes has seen on every metric, achieving the following average scores:
- GPT4All benchmark average is now 70.0 - from 68.8 in Hermes-Llama1
- 0.3657 on BigBench, up from 0.328 on hermes-llama1
- 0.372 on AGIEval, up from 0.354 on Hermes-llama1

These benchmarks currently have us at #1 on ARC-c, ARC-e, Hellaswag, and OpenBookQA, and 2nd place on Winogrande, comparing to GPT4all's benchmarking list, supplanting Hermes 1 for the new top position. 

## Resources for Applied Use Cases:
Check out LM Studio for a nice chatgpt style interface here: https://lmstudio.ai/
For an example of a back and forth chatbot using huggingface transformers and discord, check out: https://github.com/teknium1/alpaca-discord  
For an example of a roleplaying discord chatbot, check out this: https://github.com/teknium1/alpaca-roleplay-discordbot  

## Future Plans
We plan to continue to iterate on both more high quality data, and new data filtering techniques to eliminate lower quality data going forward. 

## Model Usage
The model is available for download on Hugging Face. It is suitable for a wide range of language tasks, from generating creative text to understanding and following complex instructions.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
