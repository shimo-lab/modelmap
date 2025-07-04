
# Model Card: Nous-Hermes-13b

## Model Description

Nous-Hermes-13b is a state-of-the-art language model fine-tuned on over 300,000 instructions. This model was fine-tuned by Nous Research, with Teknium and Karan4D leading the fine tuning process and dataset curation, Redmond AI sponsoring the compute, and several other contributors. The result is an enhanced Llama 13b model that rivals GPT-3.5-turbo in performance across a variety of tasks.

This model stands out for its long responses, low hallucination rate, and absence of OpenAI censorship mechanisms. The fine-tuning process was performed with a 2000 sequence length on an 8x a100 80GB DGX machine for over 50 hours. 

## Model Training

The model was trained almost entirely on synthetic GPT-4 outputs. This includes data from diverse sources such as GPTeacher, the general, roleplay v1&2, code instruct datasets, Nous Instruct & PDACTL (unpublished), CodeAlpaca, Evol_Instruct Uncensored, GPT4-LLM, and Unnatural Instructions. 

Additional data inputs came from Camel-AI's Biology/Physics/Chemistry and Math Datasets, Airoboros' GPT-4 Dataset, and more from CodeAlpaca. The total volume of data encompassed over 300,000 instructions.

## Collaborators
The model fine-tuning and the datasets were a collaboration of efforts and resources between Teknium, Karan4D, Nous Research, Huemin Art, and Redmond AI. 
  
Huge shoutout and acknowledgement is deserved for all the dataset creators who generously share their datasets openly. 

Special mention goes to @winglian, @erhartford, and @main_horse for assisting in some of the training issues.

Among the contributors of datasets, GPTeacher was made available by Teknium, Wizard LM by nlpxucan, and the Nous Research Instruct Dataset was provided by Karan4D and HueminArt.  
The GPT4-LLM and Unnatural Instructions were provided by Microsoft, Airoboros dataset by jondurbin, Camel-AI datasets are from Camel-AI, and CodeAlpaca dataset by Sahil 2801.
If anyone was left out, please open a thread in the community tab.

## Prompt Format

The model follows the Alpaca prompt format:
```
### Instruction:

### Response:
```

or 

```
### Instruction:

### Input:

### Response:
```  

## Resources for Applied Use Cases:
For an example of a back and forth chatbot using huggingface transformers and discord, check out: https://github.com/teknium1/alpaca-discord  
For an example of a roleplaying discord bot, check out this: https://github.com/teknium1/alpaca-roleplay-discordbot  

## Future Plans
The model is currently being uploaded in FP16 format, and there are plans to convert the model to GGML and GPTQ 4bit quantizations. The team is also working on a full benchmark, similar to what was done for GPT4-x-Vicuna. We will try to get in discussions to get the model included in the GPT4All.

## Benchmark Results
```
|    Task     |Version| Metric |Value |   |Stderr|
|-------------|------:|--------|-----:|---|-----:|
|arc_challenge|      0|acc     |0.4915|±  |0.0146|
|             |       |acc_norm|0.5085|±  |0.0146|
|arc_easy     |      0|acc     |0.7769|±  |0.0085|
|             |       |acc_norm|0.7424|±  |0.0090|
|boolq        |      1|acc     |0.7948|±  |0.0071|
|hellaswag    |      0|acc     |0.6143|±  |0.0049|
|             |       |acc_norm|0.8000|±  |0.0040|
|openbookqa   |      0|acc     |0.3560|±  |0.0214|
|             |       |acc_norm|0.4640|±  |0.0223|
|piqa         |      0|acc     |0.7965|±  |0.0094|
|             |       |acc_norm|0.7889|±  |0.0095|
|winogrande   |      0|acc     |0.7190|±  |0.0126|
```

These benchmarks currently have us at #1 on ARC-c, ARC-e, Hellaswag, and OpenBookQA, and 2nd place on Winogrande, comparing to GPT4all's benchmarking list. 

## Model Usage
The model is available for download on Hugging Face. It is suitable for a wide range of language tasks, from generating creative text to understanding and following complex instructions.
  
Compute provided by our project sponsor Redmond AI, thank you!!