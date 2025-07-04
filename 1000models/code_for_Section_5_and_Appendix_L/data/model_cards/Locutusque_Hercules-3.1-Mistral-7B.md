# Model Card: Hercules-3.1-Mistral-7B

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6437292ecd93f4c9a34b0d47/Ip9wEG2Ne4vihNStHSDvX.png)

## Model Description

Hercules-3.1-Mistral-7B is a fine-tuned language model derived from Mistralai/Mistral-7B-v0.1. It is specifically designed to excel in instruction following, function calls, and conversational interactions across various scientific and technical domains. The dataset used for fine-tuning, also named Hercules-v3.0, expands upon the diverse capabilities of OpenHermes-2.5 with contributions from numerous curated datasets. This fine-tuning has hercules-v3.0 with enhanced abilities in:

- Complex Instruction Following: Understanding and accurately executing multi-step instructions, even those involving specialized terminology.
- Function Calling: Seamlessly interpreting and executing function calls, providing appropriate input and output values.
- Domain-Specific Knowledge: Engaging in informative and educational conversations about Biology, Chemistry, Physics, Mathematics, Medicine, Computer Science, and more.

## Intended Uses & Potential Bias

Hercules-3.1-Mistral-7B is well-suited to the following applications:

- Specialized Chatbots: Creating knowledgeable chatbots and conversational agents in scientific and technical fields.
- Instructional Assistants: Supporting users with educational and step-by-step guidance in various disciplines.
- Code Generation and Execution: Facilitating code execution through function calls, aiding in software development and prototyping.

**Important Note: Although Hercules-v3.0 is carefully constructed, it's important to be aware that the underlying data sources may contain biases or reflect harmful stereotypes. Use this model with caution and consider additional measures to mitigate potential biases in its responses.**

## Limitations and Risks

- Toxicity: The dataset contains toxic or harmful examples.
- Hallucinations and Factual Errors: Like other language models, Hercules-3.1-Mistral-7B may generate incorrect or misleading information, especially in specialized domains where it lacks sufficient expertise.
- Potential for Misuse: The ability to engage in technical conversations and execute function calls could be misused for malicious purposes.

## Training Data

Hercules-3.1-Mistral-7B is fine-tuned from the following sources:

- `cognitivecomputations/dolphin`
- `Evol Instruct 70K & 140K`
- `teknium/GPT4-LLM-Cleaned`
- `jondurbin/airoboros-3.2`
- `AlekseyKorshuk/camel-chatml`
- `CollectiveCognition/chats-data-2023-09-22`
- `Nebulous/lmsys-chat-1m-smortmodelsonly`
- `glaiveai/glaive-code-assistant-v2`
- `glaiveai/glaive-code-assistant`
- `glaiveai/glaive-function-calling-v2`
- `garage-bAInd/Open-Platypus`
- `meta-math/MetaMathQA`
- `teknium/GPTeacher-General-Instruct`
- `GPTeacher roleplay datasets`
- `BI55/MedText`
- `pubmed_qa labeled subset`
- `Unnatural Instructions`
- `M4-ai/LDJnr_combined_inout_format`
- `CollectiveCognition/chats-data-2023-09-27`
- `CollectiveCognition/chats-data-2023-10-16`
- `NobodyExistsOnTheInternet/sharegptPIPPA`
- `yuekai/openchat_sharegpt_v3_vicuna_format`
- `ise-uiuc/Magicoder-Evol-Instruct-110K`
- `sablo/oasst2_curated`

The bluemoon dataset was filtered from the training data as it showed to cause performance degradation.

## Training Procedure

- This model was trained on 8 kaggle TPUs, using torch xla SPMD for high MXU efficiency. There was no expense on my end (meaning you can reproduce this too!)
- A learning rate of 2e-06 with the Adam optimizer. A linear scheduler was used, with an end factor of 0.3. A low learning rate was used to prevent exploding gradients.
- No mixed precision was used, with the default dtype being bfloat16.
- Trained on 700,000 examples of Hercules-v3.0
- No model parameters were frozen.
- This model was trained on OpenAI's ChatML prompt format. Because this model has function calling capabilities, the prompt format is slightly different, here's what it would look like: ```<|im_start|>system\n{message}<|im_end|>\n<|im_start|>user\n{user message}<|im_end|>\n<|im_start|>call\n{function call message}<|im_end|>\n<|im_start|>function\n{function response message}<|im_end|>\n<|im_start|>assistant\n{assistant message}</s>```

This model was fine-tuned using the TPU-Alignment repository. https://github.com/Locutusque/TPU-Alignment

# Quants

ExLlamaV2 by bartowski https://huggingface.co/bartowski/Hercules-3.1-Mistral-7B-exl2
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Locutusque__Hercules-3.1-Mistral-7B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |62.09|
|AI2 Reasoning Challenge (25-Shot)|61.18|
|HellaSwag (10-Shot)              |83.55|
|MMLU (5-Shot)                    |63.65|
|TruthfulQA (0-shot)              |42.83|
|Winogrande (5-shot)              |79.01|
|GSM8k (5-shot)                   |42.30|

