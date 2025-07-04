# 雅意大模型

## 介绍

[雅意大模型](https://www.wenge.com/yayi/index.html)在百万级人工构造的高质量领域数据上进行指令微调得到，训练数据覆盖媒体宣传、舆情分析、公共安全、金融风控、城市治理等五大领域，上百种自然语言指令任务。雅意大模型从预训练初始化权重到领域模型的迭代过程中，我们逐步增强了它的中文基础能力和领域分析能力，并增加了多轮对话和部分插件能力。同时，经过数百名用户内测过程中持续不断的人工反馈优化，我们进一步提升了模型性能和安全性。

通过雅意大模型的开源为促进中文预训练大模型开源社区的发展，贡献自己的一份力量，通过开源，与每一位合作伙伴共建雅意大模型生态。

*News: 🔥 雅意大模型已开源基于 LLaMA 2 的中文优化模型版本，探索适用于中文多领域任务的最新实践。*


## 模型地址

|  模型名称  | 🤗HF模型标识 |  下载地址  |
| --------- | ---------    | --------- |
|  YaYi-7B  | wenge-research/yayi-7b  | [模型下载](https://huggingface.co/wenge-research/yayi-7b)  |
| YaYi-7B-Llama2 | wenge-research/yayi-7b-llama2 | [模型下载](https://huggingface.co/wenge-research/yayi-7b-llama2) |
| YaYi-13B-Llama2 | wenge-research/yayi-13b-llama2 | [模型下载](https://huggingface.co/wenge-research/yayi-13b-llama2) |
| YaYi-70B-Llama2 | wenge-research/yayi-70b-llama2 | [模型下载](https://huggingface.co/wenge-research/yayi-70b-llama2) |

详情请参考我们的 [💻Github Repo](https://github.com/wenge-research/YaYi)。


## 运行方式

```python
import torch 
from transformers import LlamaForCausalLM, LlamaTokenizer, GenerationConfig
from transformers import StoppingCriteria, StoppingCriteriaList

pretrained_model_name_or_path = "wenge-research/yayi-7b-llama2"
tokenizer = LlamaTokenizer.from_pretrained(pretrained_model_name_or_path)
model = LlamaForCausalLM.from_pretrained(pretrained_model_name_or_path, device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=False)

# Define the stopping criteria
class KeywordsStoppingCriteria(StoppingCriteria):
    def __init__(self, keywords_ids:list):
        self.keywords = keywords_ids

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        if input_ids[0][-1] in self.keywords:
            return True
        return False

stop_words = ["<|End|>", "<|YaYi|>", "<|Human|>", "</s>"]
stop_ids = [tokenizer.encode(w)[-1] for w in stop_words]
stop_criteria = KeywordsStoppingCriteria(stop_ids)

# inference
prompt = "你是谁？"
formatted_prompt = f"""<|System|>:
You are a helpful, respectful and honest assistant named YaYi developed by Beijing Wenge Technology Co.,Ltd. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.

<|Human|>:
{prompt}

<|YaYi|>:
"""

inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)
eos_token_id = tokenizer("<|End|>").input_ids[0]
generation_config = GenerationConfig(
    eos_token_id=eos_token_id,
    pad_token_id=eos_token_id,
    do_sample=True,
    max_new_tokens=256,
    temperature=0.3,
    repetition_penalty=1.1,
    no_repeat_ngram_size=0
)
response = model.generate(**inputs, generation_config=generation_config, stopping_criteria=StoppingCriteriaList([stop_criteria]))
response = [response[0][len(inputs.input_ids[0]):]]
response_str = tokenizer.batch_decode(response, skip_special_tokens=False, clean_up_tokenization_spaces=False)[0]
print(response_str)
```


---
# YaYi

## Introduction

[YaYi](https://www.wenge.com/yayi/index.html) was fine-tuned on millions of artificially constructed high-quality domain data. This training data covers five key domains: media publicity, public opinion analysis, public safety, financial risk control, and urban governance, encompassing over a hundred natural language instruction tasks. Throughout the iterative development process of the YaYi, starting from pre-training initialization weights and progressing to domain-specific model, we have steadily enhanced its foundational Chinese language capabilities and domain analysis capabilities. We've also introduced multi-turn conversation enhancements and integrated various plug-in capabilities. Furthermore, through continuous manual feedback and optimization from hundreds of users during the internal testing phase, we've meticulously refined the model's performance and security.

By open-sourcing the YaYi model, we will contribute our own efforts to the development of the Chinese pre-trained large language model open-source community. Through this open-source initiative, we seek to collaborate with every partner to build the YaYi model ecosystem together.

*News: 🔥 YaYi has open sourced the Chinese optimization model version based on LLaMA 2 to explore the latest practices suitable for Chinese multi-domain tasks.*


## Model download

|  Model  | 🤗HF Model Name |  Download Links  |
| --------- | ---------    | --------- |
|  YaYi-7B  | wenge-research/yayi-7b  | [Download](https://huggingface.co/wenge-research/yayi-7b)  |
| YaYi-7B-Llama2 | wenge-research/yayi-7b-llama2 | [Download](https://huggingface.co/wenge-research/yayi-7b-llama2) |
| YaYi-13B-Llama2 | wenge-research/yayi-13b-llama2 | [Download](https://huggingface.co/wenge-research/yayi-13b-llama2) |
| YaYi-70B-Llama2 | wenge-research/yayi-70b-llama2 | [Download](https://huggingface.co/wenge-research/yayi-70b-llama2) |

For more details, please refer to our [💻Github Repo](https://github.com/wenge-research/YaYi)。



## Run

```python
import torch 
from transformers import LlamaForCausalLM, LlamaTokenizer, GenerationConfig
from transformers import StoppingCriteria, StoppingCriteriaList

pretrained_model_name_or_path = "wenge-research/yayi-7b-llama2"
tokenizer = LlamaTokenizer.from_pretrained(pretrained_model_name_or_path)
model = LlamaForCausalLM.from_pretrained(pretrained_model_name_or_path, device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=False)

# Define the stopping criteria
class KeywordsStoppingCriteria(StoppingCriteria):
    def __init__(self, keywords_ids:list):
        self.keywords = keywords_ids

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        if input_ids[0][-1] in self.keywords:
            return True
        return False

stop_words = ["<|End|>", "<|YaYi|>", "<|Human|>", "</s>"]
stop_ids = [tokenizer.encode(w)[-1] for w in stop_words]
stop_criteria = KeywordsStoppingCriteria(stop_ids)

# inference
prompt = "你是谁？"
formatted_prompt = f"""<|System|>:
You are a helpful, respectful and honest assistant named YaYi developed by Beijing Wenge Technology Co.,Ltd. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.

<|Human|>:
{prompt}

<|YaYi|>:
"""

inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)
eos_token_id = tokenizer("<|End|>").input_ids[0]
generation_config = GenerationConfig(
    eos_token_id=eos_token_id,
    pad_token_id=eos_token_id,
    do_sample=True,
    max_new_tokens=256,
    temperature=0.3,
    repetition_penalty=1.1,
    no_repeat_ngram_size=0
)
response = model.generate(**inputs, generation_config=generation_config, stopping_criteria=StoppingCriteriaList([stop_criteria]))
response = [response[0][len(inputs.input_ids[0]):]]
response_str = tokenizer.batch_decode(response, skip_special_tokens=False, clean_up_tokenization_spaces=False)[0]
print(response_str)
```

