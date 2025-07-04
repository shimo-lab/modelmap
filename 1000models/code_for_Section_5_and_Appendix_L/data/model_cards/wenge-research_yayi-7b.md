# 雅意大模型

## 介绍
雅意大模型在百万级人工构造的高质量领域数据上进行指令微调得到，训练数据覆盖媒体宣传、舆情分析、公共安全、金融风控、城市治理等五大领域，上百种自然语言指令任务。雅意大模型从预训练初始化权重到领域模型的迭代过程中，我们逐步增强了它的中文基础能力和领域分析能力，并增加了部分插件能力。同时，经过数百名用户内测过程中持续不断的人工反馈优化，我们进一步提升了模型性能和安全性。

通过雅意大模型的开源为促进中文预训练大模型开源社区的发展，贡献自己的一份力量，通过开源，与每一位合作伙伴共建雅意大模型生态。

## 快速开始

以下是一个简单调用 `yayi-7b` 进行下游任务推理的示例代码，可在单张 A100/A800/3090 等GPU运行，使用FP16精度推理时约占用 20GB 显存。若需获取训练数据或基于 `yayi-7b` 进行模型微调，请参考我们的 [💻Github Repo](https://github.com/wenge-research/YaYi)。

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import torch

yayi_7b_path = "wenge-research/yayi-7b"
tokenizer = AutoTokenizer.from_pretrained(yayi_7b_path)
model = AutoModelForCausalLM.from_pretrained(yayi_7b_path, device_map="auto", torch_dtype=torch.bfloat16)

prompt = "你好"
formatted_prompt = f"<|System|>:\nA chat between a human and an AI assistant named YaYi.\nYaYi is a helpful and harmless language model developed by Beijing Wenge Technology Co.,Ltd.\n\n<|Human|>:\n{prompt}\n\n<|YaYi|>:"
inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)

eos_token_id = tokenizer("<|End|>").input_ids[0]
generation_config = GenerationConfig(
    eos_token_id=eos_token_id,
    pad_token_id=eos_token_id,
    do_sample=True,
    max_new_tokens=100,
    temperature=0.3,
    repetition_penalty=1.1,
    no_repeat_ngram_size=0
)
response = model.generate(**inputs, generation_config=generation_config)
print(tokenizer.decode(response[0]))
```

注意，模型训练时添加了 special token `<|End|>` 作为结束符，因此上述代码 `GenerationConfig` 里将 `eos_token_id` 设置为该结束符对应的 token id。

## 相关协议

### 局限性
基于当前数据和基础模型训练得到的SFT模型，在效果上仍存在以下问题：

1. 在涉及事实性的指令上可能会产生违背事实的错误回答。
2. 对于具备危害性的指令无法很好的鉴别，可能会产生危害性言论。
3. 在一些涉及推理、代码、多轮对话等场景下模型的能力仍有待提高。

### 免责声明

基于以上模型局限性，我们要求开发者仅将我们开源的代码、数据、模型及后续用此项目生成的衍生物用于研究目的，不得用于商业用途，以及其他会对社会带来危害的用途。请谨慎鉴别和使用雅意大模型生成的内容，请勿将生成的有害内容传播至互联网。若产生不良后果，由传播者自负。

本项目仅可应用于研究目的，项目开发者不承担任何因使用本项目（包含但不限于数据、模型、代码等）导致的危害或损失。详细请参考[免责声明](https://github.com/wenge-research/YaYi/blob/main/DISCLAIMER)。

### 开源协议

本项目中的代码依照 [Apache-2.0](https://github.com/wenge-research/YaYi/blob/main/LICENSE) 协议开源，数据采用 [CC BY-NC 4.0](https://github.com/wenge-research/YaYi/blob/main/LICENSE_DATA) 协议，YaYi 系列模型权重的使用则需要遵循 [Model License](https://github.com/wenge-research/YaYi/blob/main/LICENSE_MODEL)。

## 致谢
- 本项目使用了 BigScience 的 [bloomz-7b-mt](https://huggingface.co/bigscience/bloomz-7b1-mt) 模型权重作为初始化权重，并基于词表进行扩展；
- 本项目训练代码参考了 Databricks 的 [dolly](https://github.com/databrickslabs/dolly) 项目及 Huggingface [transformers](https://github.com/huggingface/transformers) 库；
- 本项目分布式训练使用了 Microsoft 的 [DeepSpeed](https://github.com/microsoft/deepspeed) 分布式训练工具及 Huggingface transformers 文档中的 [ZeRO stage 2](https://huggingface.co/docs/transformers/main_classes/deepspeed#zero2-config) 配置文件；


---

# YaYi

## Introduction
[YaYi](https://www.wenge.com/yayi/index.html) was fine-tuned on millions of artificially constructed high-quality domain data. This training data covers five key domains: media publicity, public opinion analysis, public safety, financial risk control, and urban governance, encompassing over a hundred natural language instruction tasks. Throughout the iterative development process of the YaYi, starting from pre-training initialization weights and progressing to domain-specific model, we have steadily enhanced its foundational Chinese language capabilities and domain analysis capabilities. We've also introduced multi-turn conversation enhancements and integrated various plug-in capabilities. Furthermore, through continuous manual feedback and optimization from hundreds of users during the internal testing phase, we've meticulously refined the model's performance and security.

By open-sourcing the YaYi model, we will contribute our own efforts to the development of the Chinese pre-trained large language model open-source community. Through this open-source initiative, we seek to collaborate with every partner to build the YaYi model ecosystem together.

## Run

Below is a simple example code for invoking `yayi-7b` for downstream task inference. It can run on a single GPU such as A100/A800/3090 and occupies approximately 20GB of GPU memory when performing inference with FP16 precision. If you need to obtain training data or fine-tune the model based on `yayi-7b`, please refer to our [💻Github Repo](https://github.com/wenge-research/YaYi).

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import torch

yayi_7b_path = "wenge-research/yayi-7b"
tokenizer = AutoTokenizer.from_pretrained(yayi_7b_path)
model = AutoModelForCausalLM.from_pretrained(yayi_7b_path, device_map="auto", torch_dtype=torch.bfloat16)

prompt = "你好"
formatted_prompt = f"<|System|>:\nA chat between a human and an AI assistant named YaYi.\nYaYi is a helpful and harmless language model developed by Beijing Wenge Technology Co.,Ltd.\n\n<|Human|>:\n{prompt}\n\n<|YaYi|>:"
inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)

eos_token_id = tokenizer("<|End|>").input_ids[0]
generation_config = GenerationConfig(
    eos_token_id=eos_token_id,
    pad_token_id=eos_token_id,
    do_sample=True,
    max_new_tokens=100,
    temperature=0.3,
    repetition_penalty=1.1,
    no_repeat_ngram_size=0
)
response = model.generate(**inputs, generation_config=generation_config)
print(tokenizer.decode(response[0]))
```

Please note that a special token `<|End|>` was added as an end-of-sequence marker during model training. Therefore, in the `GenerationConfig` provided above, you should set `eos_token_id` to the token id corresponding to this end-of-sequence marker. 

## Related agreements

### Limitations
The SFT model trained based on the current data and base model still exhibits the following issues in terms of performance:

1. It may generate factually incorrect responses for factual instructions.
2. It struggles to effectively identify harmful instructions, potentially leading to harmful content generation.
3. Its capabilities in scenarios involving logical reasoning, code generation, scientific computation, and similar tasks still require improvement.

### Disclaimer

Due to the limitations of the model mentioned above, we request that developers use the code, data, models, and any derivatives generated from this project solely for research purposes and refrain from using them for commercial or any other potentially harmful purposes to society. Please exercise caution in evaluating and utilizing content generated by the YaYi model, and do not propagate harmful content on the internet. Any adverse consequences resulting from such actions are the responsibility of the disseminator.

This project is intended for research purposes only, and the project developers bear no responsibility for any harm or losses incurred due to the use of this project, including but not limited to data, models, code, etc. For more details, please refer to the [Disclaimer](DISCLAIMER).

### License

The code in this project is open-source under the [Apache-2.0](LICENSE) license, the data follows the [CC BY-NC 4.0](LICENSE_DATA) license, and the usage of YaYi series model weights must adhere to the [Model License](LICENSE_MODEL).

## Acknowledgements
- In this project, we used model weights from BigScience's [bloomz-7b1-mt](https://huggingface.co/bigscience/bloomz-7b1-mt) and Meta's [Llama 2](https://huggingface.co/meta-llama) series as initialization weights, along with vocabulary expansion.
- The training code in this project was inspired by Databricks' [dolly](https://github.com/databrickslabs/dolly) project and Huggingface's [transformers](https://github.com/huggingface/transformers) library.
- Distributed training in this project utilized Microsoft's [DeepSpeed](https://github.com/microsoft/deepspeed) distributed training tool and configuration files from Huggingface transformers' [ZeRO stage 2](https://huggingface.co/docs/transformers/main_classes/deepspeed#zero2-config).