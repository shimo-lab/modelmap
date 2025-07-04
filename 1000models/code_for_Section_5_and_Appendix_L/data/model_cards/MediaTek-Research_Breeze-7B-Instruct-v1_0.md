
# Model Card for MediaTek Research Breeze-7B-Instruct-v1_0

MediaTek Research Breeze-7B (hereinafter referred to as Breeze-7B) is a language model family that builds on top of [Mistral-7B](https://huggingface.co/mistralai/Mistral-7B-v0.1), specifically intended for Traditional Chinese use.

[Breeze-7B-Base](https://huggingface.co/MediaTek-Research/Breeze-7B-Base-v1_0) is the base model for the Breeze-7B series. 
It is suitable for use if you have substantial fine-tuning data to tune it for your specific use case.

[Breeze-7B-Instruct](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v1_0) derives from the base model Breeze-7B-Base, making the resulting model amenable to be used as-is for commonly seen tasks.

The current release version of Breeze-7B is v1.0, which has undergone a more refined training process compared to Breeze-7B-v0_1, resulting in significantly improved performance in both English and Traditional Chinese.

For details of this model please read our [paper](https://arxiv.org/abs/2403.02712).

Practicality-wise:
- Breeze-7B-Base expands the original vocabulary with an additional 30,000 Traditional Chinese tokens. With the expanded vocabulary, and everything else being equal, Breeze-7B operates at twice the inference speed for Traditional Chinese to Mistral-7B and Llama 7B. [See [Inference Performance](#inference-performance).]
- Breeze-7B-Instruct can be used as is for common tasks such as Q&A, RAG, multi-round chat, and summarization.


Performance-wise:
- Breeze-7B-Instruct demonstrates impressive performance in benchmarks for Traditional Chinese and English when compared to similar-sized open-source contemporaries such as Taiwan-LLM-7B/13B-chat, QWen(1.5)-7B-Chat, and Yi-6B-Chat. [See [Chat Model Performance](#chat-model-performance).]


*A project by the members (in alphabetical order): Chan-Jan Hsu 許湛然, Chang-Le Liu 劉昶樂, Feng-Ting Liao 廖峰挺, Po-Chun Hsu 許博竣, [Yi-Chang Chen 陳宜昌](https://ycc.idv.tw/about-me), and the supervisor Da-Shan Shiu 許大山.*

## Demo

<a href="https://huggingface.co/spaces/MediaTek-Research/Demo-MR-Breeze-7B" style="color:red;font-weight:bold;">Try Demo Here 👩‍💻🧑🏻‍💻</a>


## Features

- Breeze-7B-Base-v1_0
  - Expanding the vocabulary dictionary size from 32k to 62k to better support Traditional Chinese
  - 8k-token context length
- Breeze-7B-Instruct-v1_0
  - Expanding the vocabulary dictionary size from 32k to 62k to better support Traditional Chinese 
  - 8k-token context length
  - Multi-turn dialogue (without special handling for harmfulness)


## Model Details

- Breeze-7B-Base-v1_0
  - Finetuned from: [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)
  - Model type: Causal decoder-only transformer language model
  - Language: English and Traditional Chinese (zh-tw)
- Breeze-7B-Instruct-v1_0
  - Finetuned from: [MediaTek-Research/Breeze-7B-Base-v1_0](https://huggingface.co/MediaTek-Research/Breeze-7B-Base-v1_0)
  - Model type: Causal decoder-only transformer language model
  - Language: English and Traditional Chinese (zh-tw)

## Base Model Performance

Here we compare Breeze-7B-Base-v1_0 with other open-source base language models of similar parameter size that are widely recognized for their good performance in Chinese.
**TMMLU+**, **DRCD**, and **Table** source from [MediaTek-Research/TCEval-v2](https://huggingface.co/datasets/MediaTek-Research/TCEval-v2).
[MediaTek-Research/TCEval-v2](https://huggingface.co/datasets/MediaTek-Research/TCEval-v2) derives from [TCEval-v1](https://github.com/mtkresearch/MR-Models/tree/main/TC-Eval)
 and [ikala/tmmluplus](https://huggingface.co/datasets/ikala/tmmluplus). **MMLU** sources from [hails/mmlu_no_train](https://huggingface.co/datasets/hails/mmlu_no_train).
 We use the code revised from [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) to evaluate **TMMLU+**, **DRCD**, **Table**, and **MMLU**. All choice problems adapt the selection by the log-likelihood.


| Models                                                                                    | #Parameters | ↑ TMMLU+ (ACC) | DRCD (EM)   | Table (ACC) | MMLU (ACC) |
|----------------------------------------------                                             |--------|--------------|-------------|-------------|------------|
|                                                                                           |        |TC, Knowledge |TC, Reasoning|TC, Reasoning|EN, Knowledge|
|                                                                                           |        | 5 shot       | 3 shot      | 5 shot      | 5 shot      |
| [Yi-6B](https://huggingface.co/01-ai/Yi-6B)                                               | 6B     |   49.63      | 76.61       |   34.72     | 65.35       |
| [Qwen1.5-7B](https://huggingface.co/Qwen/Qwen1.5-7B)                                      | 7B     |   46.59      | 74.41       |   30.56     | 63.07       |
| [**Breeze-7B-Base-v1_0**](https://huggingface.co/MediaTek-Research/Breeze-7B-Base-v1_0)   | 7B     |   42.67      | 80.61       |   31.99     | 61.24       |
| [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)                       | 7B     |   36.93      | 79.27       |   27.78     | 64.89       |

## Instruction-tuned Model Performance

Here we compare Breeze-7B-Instruct-v1_0 with other open-source instruction-tuned language models of similar parameter size that are widely recognized for their good performance in Chinese.
Also, we listed the benchmark scores of GPT-3.5 Turbo (1106), which represents one of the most widely used high-quality cloud language model API services, for reference.
**TMMLU+**, **DRCD**, **Table**, and **MT-Bench-tw** source from [MediaTek-Research/TCEval-v2](https://huggingface.co/datasets/MediaTek-Research/TCEval-v2).
[MediaTek-Research/TCEval-v2](https://huggingface.co/datasets/MediaTek-Research/TCEval-v2) derives from [TCEval-v1](https://github.com/mtkresearch/MR-Models/tree/main/TC-Eval)
 and [ikala/tmmluplus](https://huggingface.co/datasets/ikala/tmmluplus). **MMLU** sources from [hails/mmlu_no_train](https://huggingface.co/datasets/hails/mmlu_no_train).
 **MT-Bench** source from [lmsys/mt_bench_human_judgments](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments).
 We use the code revised from [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) to evaluate **TMMLU+**, **DRCD**, **Table**, and **MMLU**. All choice problems adapt the selection by the log-likelihood.
 We use the code revised from [fastchat llm_judge](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) (GPT4 as judge) to evaluate **MT-Bench-tw** and **MT-Bench**.


| Models                                                                                             | #Parameters | ↑ MT-Bench-tw (Score)| TMMLU+ (ACC) | Table (ACC) | MT-Bench (Score) | MMLU (ACC)  | 
|---------------------------------------------------------------------------------------------------------|--------|--------------------|--------------|-------------|------------------|-------------|
|                                                                                                         |        |TC, Chat            |TC, Knowledge |TC, Reasoning|EN, Chat          |EN, Knowledge|
|                                                                                                         |        |0 shot              | 0 shot       | 0 shot      |0 shot            |  0 shot     | 
| [GPT-3.5-Turbo](https://openai.com)                                                                     |        |7.1                 | 43.56        | 45.14       |7.9               |  67.09      |    
| [Qwen1.5-7B-Chat](https://huggingface.co/Qwen/Qwen1.5-7B-Chat)                                          | 7B     |6.4                 | 45.65        | 34.72       |7.6               |  61.85      |    
| [**Breeze-7B-Instruct-v1_0**](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v1_0)         | 7B     |6.0                 | 42.67        | 39.58       |7.4               |  61.73     |    
| [Mistral-7B-v0.2-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)                   | 7B     |5.6                 | 34.95        | 33.33       |7.6               |    59.97    |                                                  
| [Yi-6B-Chat](https://huggingface.co/01-ai/Yi-6B-Chat)                                                   | 6B     |5.0                 | 44.79        | 25.69       |6.0               |    59.45    |    
| [Taiwan-LLM-13B-v2.0-chat](https://huggingface.co/yentinglin/Taiwan-LLM-13B-v2.0-chat)                  | 13B    |5.0                 | 29.47        | 23.61       |N/A*                |    50.50    |     
| [Taiwan-LLM-7B-v2.1-chat](https://huggingface.co/yentinglin/Taiwan-LLM-7B-v2.1-chat)                    | 7B     |4.2                 | 28.08        | 31.25       |N/A*               |    42.72    |    

\* Taiwan-LLM models respond to multi-turn questions (English) in Traditional Chinese.    


| Details on MT-Bench-tw (0 shot):<br/>Models         | STEM    |Extraction|Reasoning| Math   | Coding  | Roleplay| Writing |Humanities|       AVG    | 
|-----------------------------------------------------|---------|---------|---------|---------|---------|---------|---------|----------|  ---------   | 
| GPT-3.5-Turbo                                       |  7.8    |  6.1    |   5.1   |   6.4   |  6.2    |   8.7   |   7.4   |   9.3    |        7.1   |
| Qwen1.5-7B-Chat                                     |  9      |  5.6    |   4.7   |   2.8   |  3.7    |   8.0   |   8.0   |   9.4    |        6.4   |
| **Breeze-7B-Instruct-v1_0**                         |  7.8    |  5.2    |   4.2   |   4.2   |  4.1    |   7.6   |   5.9   |   9.1    |        6.0   |
| Mistral-7B-v0.2-Instruct                            |  6.9    |  4.6    |   4.3   |   3.3   |  4.4    |   7.2   |   6.2   |   7.8    |        5.6   |                                          
| Yi-6B-Chat                                          |  7.3    |  2.7    |   3.1   |   3.3   |  2.3    |   7.2   |   5.2   |   8.8    |        5.0   |
| Taiwan-LLM-13B-v2.0-chat                            |  6.1    |  3.4    |   4.1   |   2.3   |  3.1    |   7.4   |   6.6   |   6.8    |        5.0   |
| Taiwan-LLM-7B-v2.1-chat                             |  5.2    |  2.6    |   2.3   |   1.2   |  3.4    |   6.6   |   5.7   |   6.8    |        4.2   |



| Details on TMMLU+ (0 shot):<br/>Model               | STEM         | Social Science | Humanities | Other      |   AVG   |
|-----------------------------------------------------|--------------|----------------|------------|------------|---------|
| GPT-3.5-Turbo                                       | 41.58        | 48.52          | 40.96      | 43.18      | 43.56   |
| Qwen1.5-7B-Chat                                     | 41.48        | 51.66          | 44.05      | 45.40      | 45.65   |
| **Breeze-7B-Instruct-v1_0**                         | 36.46        | 48.38          | 45.11      | 40.75      | 42.67   |
| Mistral-7B-v0.2-Instruct                            | 32.79        | 38.05          | 34.89      | 34.04      | 34.94   |
| Yi-6B-Chat                                          | 37.80        | 51.74          | 45.36      | 44.25      | 44.79   |
| Taiwan-LLM-13B-v2.0-chat                            | 27.74        | 33.69          | 27.03      | 29.43      | 29.47   |
| Taiwan-LLM-7B-v2.1-chat                             | 25.58        | 31.76          | 27.36      | 27.61      | 28.08   |



## Inference Performance
In this test, we use the first 700 characters of the [web article](https://health.udn.com/health/story/5976/7699252?from=udn_ch1005_main_index) as the input and ask the model to write the same article again.
All inferences run on 2 RTX A6000 GPUs (using `vllm`, with a tensor-parallel size of 2).

| Models                                                             | ↓ Inference Time (sec)|Estimated Max Input Length (Char)|
|--------------------------------------------------------------------|-------------------|--------------------------|
| Qwen1.5-7B-Chat                                                    |  9.35             |    38.9k                  |
| Yi-6B-Chat                                                         |   10.62           |   5.2k                |
| **Breeze-7B-Instruct-v1_0**                                        |  10.74            |    11.1k                 |
| Mistral-7B-Instruct-v0.2                                           |  20.48           |    5.1k                 |
| Taiwan-LLM-7B-v2.1-chat                                            |   26.26          |    2.2k                  |
<!---| Taiwan-LLM-13B-v2.0-chat                                           |   36.80          |    2.2k                  |--->


<!---## Long-context Performance
TBD--->

## Use in Transformers

First install direct dependencies:
```
pip install transformers torch accelerate
```
If you want faster inference using flash-attention2, you need to install these dependencies:
```bash
pip install packaging ninja
pip install flash-attn
```
Then load the model in transformers:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Instruction Model
model = AutoModelForCausalLM.from_pretrained(
    "MediaTek-Research/Breeze-7B-Instruct-v1_0",
    device_map="auto",
    torch_dtype=torch.bfloat16,
    # attn_implementation="flash_attention_2" # optional
)

# Basemodel
model = AutoModelForCausalLM.from_pretrained(
    "MediaTek-Research/Breeze-7B-Base-v1_0",
    device_map="auto",
    torch_dtype=torch.bfloat16,
    # attn_implementation="flash_attention_2" # optional
)
```

**For Breeze-7B-Instruct**, the structure of the query is 
```txt
<s>SYS_PROMPT  [INST] QUERY1 [/INST] RESPONSE1 [INST] QUERY2 [/INST] 
```
where `SYS_PROMPT`, `QUERY1`, `RESPONSE1`, and `QUERY2` can be provided by the user.

The suggested default `SYS_PROMPT` is 
```txt
You are a helpful AI assistant built by MediaTek Research. The user you are helping speaks Traditional Chinese and comes from Taiwan.
```

We also integrate `chat_template` into [tokenizer_config.json](tokenizer_config.json), so you can `apply_chat_template` to get the prompt.

```python
>>> from transformers import AutoTokenizer
>>> tokenizer = AutoTokenizer.from_pretrained("MediaTek-Research/Breeze-7B-Instruct-v1_0")
>>> chat = [
...   {"role": "user", "content": "你好，請問你可以完成什麼任務？"},
...   {"role": "assistant", "content": "你好，我可以幫助您解決各種問題、提供資訊和協助您完成許多不同的任務。例如：回答技術問題、提供建議、翻譯文字、尋找資料或協助您安排行程等。請告訴我如何能幫助您。"},
...   {"role": "user", "content": "太棒了！"},
... ]
>>> tokenizer.apply_chat_template(chat, tokenize=False)
"<s>You are a helpful AI assistant built by MediaTek Research. The user you are helping speaks Traditional Chinese and comes from Taiwan.  [INST] 你好，請問你可以完成什麼任務？ [/INST] 你好，我可以幫助您解決各種問題、提供資訊和協助您完成許多不同的任務。例如：回答技術問題、提供建議、翻譯文字、尋找資料或協助您安排行程等。請告訴我如何能幫助您。 [INST] 太棒了！ [/INST] "
# Tokenized results
# ['▁', '你好', '，', '請問', '你', '可以', '完成', '什麼', '任務', '？']
# ['▁', '你好', '，', '我', '可以', '幫助', '您', '解決', '各種', '問題', '、', '提供', '資訊', '和', '協助', '您', '完成', '許多', '不同', '的', '任務', '。', '例如', '：', '回答', '技術', '問題', '、', '提供', '建議', '、', '翻譯', '文字', '、', '尋找', '資料', '或', '協助', '您', '安排', '行程', '等', '。', '請', '告訴', '我', '如何', '能', '幫助', '您', '。']
# ['▁', '太', '棒', '了', '！']
```

Text generation can be done by `generate` and `apply_chat_template` functions:
```python
>>> outputs = model.generate(tokenizer.apply_chat_template(chat, return_tensors="pt"),
>>>                          # adjust below parameters if necessary 
>>>                          max_new_tokens=128,
>>>                          top_p=0.01,
>>>                          top_k=85,
>>>                          repetition_penalty=1.1,
>>>                          temperature=0.01)
>>>                          
>>> print(tokenizer.decode(outputs[0]))
```

## Citation

```
@article{MediaTek-Research2024breeze7b,
      title={Breeze-7B Technical Report}, 
      author={Chan-Jan Hsu and Chang-Le Liu and Feng-Ting Liao and Po-Chun Hsu and Yi-Chang Chen and Da-Shan Shiu},
      year={2024},
      eprint={2403.02712},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```