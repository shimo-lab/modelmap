
# Chinese Alpaca Plus 7B Model

**发布中文LLaMA, Alpaca Plus版（7B）模型**


推出中文LLaMA, Alpaca Plus版（7B），相比基础版本的改进点如下：

- 进一步扩充了训练数据，其中LLaMA扩充至120G文本（通用领域），Alpaca扩充至4M指令数据（重点增加了STEM相关数据）
- Alpaca训练时采用了更大的rank，相比原版具有更低的验证集损失
- 评测结果显示，Alpaca-Plus-7B相比基础版Alpaca-7B效果更优，部分任务接近或超过13B版本
- 这一轮比拼：7B获得65.3分，13B获得70.9分，Plus-7B效果75.3分，具体评测结果请参考[效果评测](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/main/examples/README.md)

本模型是`原生LLaMA-7B`合并`中文LLaMA LoRA`和`中文Alpaca LoRA`后的模型权重`chinese-alpaca-plus-7b-hf`，并转化为HuggingFace版本权重（.bin文件），可以直接使用或者继续训练。

13b-hf权重链接：https://huggingface.co/shibing624/chinese-alpaca-plus-13b-hf

test case:

|input_text|predict|
|:-- |:--- |
|为什么天空是蓝色的？|天空是蓝色的，是因为大气层中的气体分子会散射太阳光中的蓝色光，使得我们看到的天空是蓝色的。|


## release model weight

- chinese-llama-plus-7b 模型权重链接：https://huggingface.co/minlik/chinese-llama-plus-7b-merged
- chinese-alpaca-plus-7b 模型权重链接：https://huggingface.co/shibing624/chinese-alpaca-plus-7b-hf
- chinese-llama-plus-13b 模型权重链接：https://huggingface.co/shibing624/chinese-llama-plus-13b-hf
- chinese-aplaca-plus-13b 模型权重链接：https://huggingface.co/shibing624/chinese-alpaca-plus-13b-hf

## Usage

本项目开源在textgen项目：[textgen](https://github.com/shibing624/textgen)，可支持llama模型，通过如下命令调用：

Install package:
```shell
pip install -U textgen
```

```python
from textgen import GptModel
model = GptModel("llama", "shibing624/chinese-alpaca-plus-7b-hf")
r = model.predict(["用一句话描述地球为什么是独一无二的。"])
print(r) # ['地球是独一无二的，因为它拥有独特的大气层、水循环、生物多样性以及其他自然资源，这些都使它成为一个独特的生命支持系统。']
```

## Usage (HuggingFace Transformers)
Without [textgen](https://github.com/shibing624/textgen), you can use the model like this: 

First, you pass your input through the transformer model, then you get the generated sentence.

Install package:
```
pip install sentencepiece
pip install transformers>=4.28.0
```

```python
import torch
import transformers
from transformers import LlamaTokenizer, LlamaForCausalLM

def generate_prompt(text):
    return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{text}

### Response:"""


tokenizer = LlamaTokenizer.from_pretrained('shibing624/chinese-alpaca-plus-7b-hf')
model = LlamaForCausalLM.from_pretrained('shibing624/chinese-alpaca-plus-7b-hf').half().cuda()
model.eval()

text = '为什么天空是蓝色的？'
prompt = generate_prompt(text)
input_ids = tokenizer.encode(prompt, return_tensors='pt').to('cuda')


with torch.no_grad():
    output_ids = model.generate(
        input_ids=input_ids,
        max_new_tokens=128,
        temperature=1,
        top_k=40,
        top_p=0.9,
        repetition_penalty=1.15
    ).cuda()
output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(output.replace(text, '').strip())
```


output:
```shell
为什么天空是蓝色的？
天空是蓝色的，是因为大气层中的气体分子会散射太阳光中的蓝色光，使得我们看到的天空是蓝色的。
```

## 模型来源
release合并后的模型权重，一步到位直接使用，省电、减少碳排放。

基于 [多LoRA权重合并（适用于Chinese-Alpaca-Plus ）](https://github.com/ymcui/Chinese-LLaMA-Alpaca/wiki/%E6%89%8B%E5%8A%A8%E6%A8%A1%E5%9E%8B%E5%90%88%E5%B9%B6%E4%B8%8E%E8%BD%AC%E6%8D%A2#%E5%A4%9Alora%E6%9D%83%E9%87%8D%E5%90%88%E5%B9%B6%E9%80%82%E7%94%A8%E4%BA%8Echinese-alpaca-plus-)方法手动合并而成，具体是使用 [decapoda-research/llama-7b-hf](https://huggingface.co/decapoda-research/llama-7b-hf) 
底座模型 合并 Chinese-LLaMA-Plus-LoRA和Chinese-Alpaca-Plus-LoRA 两个LoRA权重 得到，并转化为HuggingFace版本权重（.bin文件）。


HuggingFace版本权重（.bin文件）可用于：
- 使用Transformers进行训练和推理
- 使用text-generation-webui搭建界面

PyTorch版本权重（.pth文件）可用于：
- 使用llama.cpp工具进行量化和部署

PyTorch版本权重（.pth文件）链接，8-bit量化版的Alpaca-Plus-7B：[Billsfriend/chinese-Alpaca-7b-plus-ggml-q8_0](https://huggingface.co/Billsfriend/chinese-Alpaca-7b-plus-ggml-q8_0/tree/main)


模型文件组成：
```
chinese-alpaca-plus-7b-hf
    config.json
    generation_config.json
    pytorch_model-00001-of-00002.bin
    pytorch_model-00002-of-00002.bin
    pytorch_model.bin.index.json
    special_tokens_map.json
    tokenizer.json
    tokenizer.model
    tokenizer_config.json
```

硬件要求：14G显存

### 微调数据集
我整理部分公开微调数据集：

1. 50万条中文ChatGPT指令Belle数据集：[BelleGroup/train_0.5M_CN](https://huggingface.co/datasets/BelleGroup/train_0.5M_CN)
2. 100万条中文ChatGPT指令Belle数据集：[BelleGroup/train_1M_CN](https://huggingface.co/datasets/BelleGroup/train_1M_CN)
3. 5万条英文ChatGPT指令Alpaca数据集：[50k English Stanford Alpaca dataset](https://github.com/tatsu-lab/stanford_alpaca#data-release)
4. 5万条中文GPT4指令Alpaca数据集：[shibing624/alpaca-zh](https://huggingface.co/datasets/shibing624/alpaca-zh)
5. 69万条中文指令Guanaco数据集(Belle50万条+Guanaco19万条)：[Chinese-Vicuna/guanaco_belle_merge_v1.0](https://huggingface.co/datasets/Chinese-Vicuna/guanaco_belle_merge_v1.0)


如果需要训练LLaMA模型，请参考[https://github.com/shibing624/textgen](https://github.com/shibing624/textgen)


## Citation

```latex
@software{textgen,
  author = {Xu Ming},
  title = {textgen: Implementation of language model finetune},
  year = {2023},
  url = {https://github.com/shibing624/textgen},
}
```


## Reference
- https://github.com/ymcui/Chinese-LLaMA-Alpaca

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_shibing624__chinese-alpaca-plus-7b-hf)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 42.46   |
| ARC (25-shot)         | 49.23          |
| HellaSwag (10-shot)   | 70.48    |
| MMLU (5-shot)         | 38.39         |
| TruthfulQA (0-shot)   | 39.72   |
| Winogrande (5-shot)   | 70.09   |
| GSM8K (5-shot)        | 0.68        |
| DROP (3-shot)         | 28.61         |
