
# Sample weight
Sample eval in [Open LLM Leaderboard](https://huggingface.co/datasets/open-llm-leaderboard/details_danielpark__gorani-100k-llama2-13b-instruct)

## GORANI 100k
- LFM: [llama2-13b-chat](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf)
- Model: [danielpark/gorani-100k-llama2-13b-instruct](https://huggingface.co/danielpark/gorani-100k-llama2-13b-instruct)
- Dataset: [danielpark/gorani-100k](https://huggingface.co/danielpark/gorani-100k)
- **License**: This model is licensed under the Meta's [LLaMA2 license](https://github.com/facebookresearch/llama/blob/main/LICENSE). You may not use it commercially, and you must adhere to the licenses of the included datasets. Therefore, I currently adopt the strictest and most restrictive license. Please refrain from using it for commercial purposes under any circumstances until an official license is issued. 

<br>

KORANI is derived from GORANI, a project within llama2 that experiments with the distribution of appropriate datasets to transfer or distill knowledge based on English datasets. Officially, it's called Grid Of Ranvier Node In llama2 (GORANI), based on the biological term Ranvier Node, and aims to explore the optimal dataset for transferring knowledge in various languages and specific domains. Due to strict licensing issues with English datasets, GORANI is primarily for research purposes. Therefore, we are refining and training a commercially usable Korean dataset on top of llama2, based on the experimental results of the GORANI project, and this project is named KORANI (Korean GORANI).
- I have conducted preliminary experiments using various techniques such as RoPE scaling, Attention Sinks, and Flash Attention 1 and 2, SWA(Sliding Window Attention), GQA(Grouped Query Attention).
- Please do not use the current model weights as they are not official model weight.
- The most stringent non-commercial use license (CC-BY-NC-4.0) among the licenses of the datasets used for training is also applied to the model weights.
- On 2023-11-12, it was decided that all projects would be kept private. It may be released in a non-public model format on cloud platforms by 2024.

<br>

## Template
Instruction model
```
### System:
{{ System prompt }}

### User:
{{ New user input }}

### Assistant:
{Assistant}
```

Chat model
```
<s>[INST] <<SYS>>
{{ System prompt }}
<</SYS>>

{{ New user message }} [/INST]
```

<details>
  <summary> Templates </summary>


#### Instruct model template
For safety, I used the default system message from Llama-2. But if a system message is specified in any datasets, I use that content.
```python
### System:
{{ System prompt }}

### User:
{{ New user input }}

### Input:
{{ Optional additional user input }}

### Assistant:
{{ New assistant answer }}
```

need to be converted to

```
### System:
{{ System prompt }}

### User:
{{ New user input }}

### Assistant:
{Assistant}
```

## Chat model template

```
# https://github.com/huggingface/blog/blob/main/llama2.md#how-to-prompt-llama-2

<s>[INST] <<SYS>>
{{ System prompt }}
<</SYS>>

{{ New user message }} [/INST]
```

```
<s>[INST] {{ User input }} [/INST] {{ New assistant answer }} </s>[INST] {{ New user input }} [/INST]
```

```
# Llama2 official

default_llama2_system_prompt = "Always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity."


# https://docs.mistral.ai/usage/guardrailing

more_safety_guardrail = """
You're given a list of moderation categories as below:
- illegal: Illegal activity.
- child abuse: child sexual abuse material or any content that exploits or harms children.
- hate violence harassment: Generation of hateful, harassing, or violent content: content that expresses, incites, or promotes hate based on identity, content that intends to harass, threaten, or bully an individual, content that promotes or glorifies violence or celebrates the suffering or humiliation of others.
- malware: Generation of malware: content that attempts to generate code that is designed to disrupt, damage, or gain unauthorized access to a computer system.
- physical harm: activity that has high risk of physical harm, including: weapons development, military and warfare, management or operation of critical infrastructure in energy, transportation, and water, content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.
- economic harm: activity that has high risk of economic harm, including: multi-level marketing, gambling, payday lending, automated determinations of eligibility for credit, employment, educational institutions, or public assistance services.
- fraud: Fraudulent or deceptive activity, including: scams, coordinated inauthentic behavior, plagiarism, academic dishonesty, astroturfing, such as fake grassroots support or fake review generation, disinformation, spam, pseudo-pharmaceuticals.
- adult: Adult content, adult industries, and dating apps, including: content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness), erotic chat, pornography.
- political: Political campaigning or lobbying, by: generating high volumes of campaign materials, generating campaign materials personalized to or targeted at specific demographics, building conversational or interactive systems such as chatbots that provide information about campaigns or engage in political advocacy or lobbying, building products for political campaigning or lobbying purposes.
- privacy: Activity that violates people's privacy, including: tracking or monitoring an individual without their consent, facial recognition of private individuals, classifying individuals based on protected characteristics, using biometrics for identification or assessment, unlawful collection or disclosure of personal identifiable information or educational, financial, or other protected records.
- unqualified law: Engaging in the unauthorized practice of law, or offering tailored legal advice without a qualified person reviewing the information.
- unqualified financial: Offering tailored financial advice without a qualified person reviewing the information.
- unqualified health: Telling someone that they have or do not have a certain health condition, or providing instructions on how to cure or treat a health condition.

Please classify the following text into one of these categories, and answer with that single word only.
If the sentence does not fall within these categories, is safe and does not need to be moderated, please answer "not moderated".
"""
```

The context-dialogue refers to the system prompt I suppose, and in this case we have N samples:

```
[SYSTEM: ](SYSTEM: Act as if you were Napoleon who like playing cricket.
USER: <user_msg_1>
ASSISTANT: <reply_1>
```

```
[SYSTEM: ](SYSTEM: Act as if you were Napoleon who like playing cricket.
USER:
ASSISTANT:
USER:
ASSISTANT:
```

```
[SYSTEM: ](SYSTEM: Act as if you were Napoleon who like playing cricket.
USER: <user_msg_1>
ASSISTANT: <reply_1>
USER: <user_msg_2>
ASSISTANT: <reply_2>
...
USER: <user_msg_N>
ASSISTANT: <reply_N>
```
For each sample S, at training time, we pass the context:

```
[SYSTEM: ](SYSTEM: Act as if you were Napoleon who like playing cricket.
USER: <user_msg_1>
ASSISTANT: <reply_1>
USER: <user_msg_2>
ASSISTANT: <reply_2>
...
USER: <user_msg_S-1>
ASSISTANT: <reply_S-1>
USER: <user_msg_S>
```
And we train the probabilities on ASSISTANT: <reply_S>: the loss is zeroed out for all tokens before, then you compute cross-entropy between ground-truth (the actual <reply_S>) and the predicted tokens P(t>k|t0, ..., tk) where k is the length of the sequence

</details>


## Update
- Since we cannot control resources, we will record the schedule retrospectively.

| Update Schedule | Task Description           | Status |
|-----------------|----------------------------|--------|
| 23-10-05           | Completed training - 19.7k 13b weight (specific data)|  Done       |
| 23-10-06           | Submitted hf model weights (REV 01) |    Done    |
| 23-10-20           | Q.C                         |   Done     |
| 23-11-12           | Changed to a private project.                         |   Kept private     |



## Caution
The model weights and dataset have not been properly curated yet and are strictly prohibited for use under any license. In relation to this, the developers do not assume any responsibility, either implicitly or explicitly.


## Revisions
| Revision       | Commit Hash                                                 | Updated   | Train Process   | Status        |
| ---------------|------------------------------------------------------------|------------|------------------|---------------|
| Revision 01     | [6d30494fa8da84128499d55075eef57094336d03](https://huggingface.co/danielpark/gorani-100k-llama2-13b-instruct/commit/6d30494fa8da84128499d55075eef57094336d03) | 23.10.04  | 19,740/100,000     | On Training   |

