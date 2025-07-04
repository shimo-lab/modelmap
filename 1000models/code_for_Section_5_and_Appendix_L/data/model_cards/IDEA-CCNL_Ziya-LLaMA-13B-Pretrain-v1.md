
# Ziya-LLaMA-13B-Pretrain-v1

- Main Page:[Fengshenbang](https://fengshenbang-lm.com/)
- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)

（LLaMA权重的许可证限制，我们无法直接发布完整的模型权重，用户需要参考[使用说明](#-使用-usage-)进行合并)

# 姜子牙系列模型

- [Ziya-LLaMA-13B-v1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1)
- [Ziya-LLaMA-7B-Reward](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-7B-Reward)
- [Ziya-LLaMA-13B-Pretrain-v1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-Pretrain-v1)
- [Ziya-BLIP2-14B-Visual-v1](https://huggingface.co/IDEA-CCNL/Ziya-BLIP2-14B-Visual-v1)

## 简介 Brief Introduction

Ziya-LLaMA-13B-Pretrain-v1 是基于LLaMa的130亿参数大规模预训练模型，针对中文分词优化，并完成了中英文 110B tokens 的增量预训练，进一步提升了中文生成和理解能力。目前姜子牙通用大模型 [Ziya-LLaMA-13B-v1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1) 在本模型上，进一步完成了多任务有监督微调和人类反馈学习阶段的训练过程，具备翻译，编程，文本分类，信息抽取，摘要，文案生成，常识问答和数学计算等能力。

**用户须知**：为了遵循 Meta 发布的 LLaMA 模型许可，本模型发布的是训练前后的权重增量，最终模型可方便地通过脚本获得（参考 Usage 中的步骤）。

The Ziya-LLaMA-13B-Pretrain-v1 is a large-scale pre-trained model based on LLaMA with 13 billion parameters. We optimizes LLaMAtokenizer on chinese, and incrementally train 110 billion tokens of data based on LLaMa-13B model, which significantly improved the understanding and generation ability on Chinese. Based on the Ziya-LLaMA-13B-Pretrain-v1, the [Ziya-LLaMA-13B-v1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1) is furtherly trained with 2 stages: multi-task supervised fine-tuning (SFT), and human feedback learning (RM, PPO). The Ziya-LLaMA-13B-v1 has the ability to perform tasks such as translation, programming, text classification, information extraction, summarization, copywriting, common sense Q&A, and mathematical calculation. 

**README**: To follow the License of LLaMA released by Meta, we only release the incremental weights after continual pretraining. The final model Ziya-LLaMA-13B-Pretrain-v1 could be easily got via the script (refer to Usage). 

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General | AGI模型 | 姜子牙 Ziya | LLaMA |     13B    |     English&Chinese     |

## 模型信息 Model Information

### 继续预训练 Continual Pretraining

原始数据包含英文和中文，其中英文数据来自openwebtext、Books、Wikipedia和Code，中文数据来自清洗后的悟道数据集、自建的中文数据集。在对原始数据进行去重、模型打分、数据分桶、规则过滤、敏感主题过滤和数据评估后，最终得到125B tokens的有效数据。

为了解决LLaMA原生分词对中文编解码效率低下的问题，我们在LLaMA词表的基础上增加了7k+个常见中文字，通过和LLaMA原生的词表去重，最终得到一个39410大小的词表，并通过复用Transformers里LlamaTokenizer来实现了这一效果。

在增量训练过程中，我们使用了160张40GB的A100，采用2.6M tokens的训练集样本数量和FP 16的混合精度，吞吐量达到118 TFLOP per GPU per second。因此我们能够在8天的时间里在原生的LLaMA-13B模型基础上，增量训练110B tokens的数据。据我们所知，这也是至今为止LLaMA-13B上最大规模增量训练。

训练期间，虽然遇到了机器宕机、底层框架bug、loss spike等各种问题，但我们通过快速调整，保证了增量训练的稳定性。我们也放出训练过程的loss曲线，让大家了解可能出现的问题。

The original data contains both English and Chinese, with English data from openwebtext, Books, Wikipedia, and Code, and Chinese data from the cleaned Wudao dataset and self-built Chinese dataset. After deduplication, model scoring, data bucketing, rule filtering, sensitive topic filtering, and data evaluation, we finally obtained 125 billion tokens of data. 

To address the issue of low efficiency in Chinese encoding and decoding caused by the tokenizer of LLaMa, we added 8,000 commonly used Chinese characters to the LLaMa SentencePiece vocabulary. Deduplicating with the original LLaMa vocabulary, we finally obtained a vocabulary of size 39,410. We achieved this by reusing the LlamaTokenizer in Transformers. 

During the incremental training process, we used 160 A100s with a total of 40GB memory, using a training dataset with 2.6 million tokens and mixed precision of FP16. The throughput reached 118 TFLOP per GPU per second. As a result, we were able to incrementally train 110 billion tokens of data based on LLaMa-13B model in just 8 days.As far as we know, it is the largest increamental training on LLaMA-13B so far.

Throughout the training process, we encountered various issues such as machine crashes, underlying framework bugs, and loss spikes. However, we ensured the stability of the incremental training by making rapid adjustments. We have also released the loss curve during the training process to help everyone understand the potential issues that may arise.

<img src="https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-Pretrain-v1/resolve/main/loss.png" width=1000 height=600>

### 效果评估 Performance

以下是 Ziya-LLaMA-13B-Pertrain-v1 和继续训练前的LLaMA 模型在英文公开评测 [HeLM](https://crfm.stanford.edu/helm/latest/) 和中文多项选择评测集上的评估效果对比。

Here are comparisons of the Ziya-LLaMA-13B-Pretrain-v1 model and the LLaMA model before continual pre-training, evaluated on the English benchmark (HeLM), and our Chinese multiple-choice evaluation datasets.

<img src="https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-Pretrain-v1/resolve/main/ziya_en_eval.png" width=2542 height=1045>


| Model                      | Meanwin_rate | MMLU | BoolQ | NarrativeQA | NaturalQuestion(closed-book) | NaturalQuestion(open-book) | QuAC | TruthfulQA | IMDB |
| -------------------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| LLaMA-13B                  | 0.500 | 0.424 | 0.718 | 0.440 | 0.349 | 0.591 | 0.318 | 0.326 | 0.487 |
| Ziya-LLaMA-13B-Pretrain-v1 | 0.650 | 0.433 | 0.753 | 0.445 | 0.348 | 0.528 | 0.335 | 0.249 | 0.497 |

<img src="https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-Pretrain-v1/resolve/main/ziya_zh_eval.png" width=2340 height=1523>

| 模型                      | incontext  | c3     | 常识     | 语文     | 数学     | 英语     | 物理     | 化学     | 生物     | 历史     | 政治     | 地理     |
|-------------------------|------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|  LLaMA-13B                | 0-shot     | 0.4817 | 0.3088 | 0.2674 | 0.2882 | 0.3399 | 0.2581 | 0.2478 | 0.2271 | 0.3380  | 0.3275 | 0.296  |
| Ziya-LLaMA-13B-Pretrain-v1 | 0-shot     | 0.5354 | 0.3373 | 0.2925 | 0.3059 | 0.3428 | 0.2903 | 0.2655 | 0.3215 | 0.4190  | 0.4123 | 0.4425 |
| LLaMA-13B                | 5-shot     | 0.5314 | 0.3586 | 0.2813 | 0.2912 | 0.4476 | 0.2939 | 0.2301 | 0.2330  | 0.3268 | 0.3187 | 0.3103 |
| Ziya-LLaMA-13B-Pretrain-v1 | 5-shot     | 0.6037 | 0.4330  | 0.2802 | 0.2912 | 0.4363 | 0.2975 | 0.2802 | 0.3422 | 0.4358 | 0.4357 | 0.4540  |



<!-- 
<img src="" width=1000 height=600> -->

## <span id="jump"> 使用 Usage </span>

由于LLaMA权重的许可限制，该模型不能用于商业用途，请严格遵守LLaMA的使用政策。考虑到LLaMA权重的许可证限制，我们无法直接发布完整的模型权重。因此，我们使用了[FastChat开源工具](https://github.com/lm-sys/FastChat/blob/main/fastchat/model/apply_delta.py)作为基础，并对其进行了进一步的优化。我们计算并发布了Ziya-LLaMA-13B-v1权重与原始LLaMA权重之间的差值。用户可以按照以下步骤操作以获得Ziya-LLaMA-13B-v1完整权重，具体步骤如下：

Step 1:获取[LLaMA](https://docs.google.com/forms/d/e/1FAIpQLSfqNECQnMkycAp2jP4Z9TFX0cGR4uf7b_fBxjY_OjhJILlKGA/viewform)权重并转成Hugging Face Transformers模型格式，可参考转换[脚本](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/convert_llama_weights_to_hf.py)（若已经有huggingface权重则跳过）
```
python src/transformers/models/llama/convert_llama_weights_to_hf.py \
    --input_dir /path/to/downloaded/llama/weights --model_size 13B --output_dir /output/path
```

Step 2:下载Ziya-LLaMA-13B-v1的delta权重以及step 1中转换好的原始LLaMA权重，使用如下脚本转换：https://github.com/IDEA-CCNL/Fengshenbang-LM/blob/main/fengshen/utils/apply_delta.py. 

```
python3 -m apply_delta --base ~/model_weights/llama-13b --target ~/model_weights/Ziya-LLaMA-13B --delta ~/model_weights/Ziya-LLaMA-13B-v1
```

Step 3: 加载step 2得到的模型推理
```python3
from transformers import AutoTokenizer
from transformers import LlamaForCausalLM
import torch


device = torch.device("cuda")

query="帮我写一份去西安的旅游计划"
model = LlamaForCausalLM.from_pretrained(ckpt, torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(ckpt)
inputs =  query.strip()
      
input_ids = tokenizer(inputs, return_tensors="pt").input_ids.to(device)
generate_ids = model.generate(
            input_ids,
            max_new_tokens=1024, 
            do_sample = True, 
            top_p = 0.85, 
            temperature = 1.0, 
            repetition_penalty=1., 
            eos_token_id=2, 
            bos_token_id=1, 
            pad_token_id=0)
output = tokenizer.batch_decode(generate_ids)[0]
print(output)
```

Step 1: Obtain the [LLaMA](https://huggingface.co/docs/transformers/main/en/model_doc/llama#overview) weights and convert them into the Hugging Face Transformers format. You can refer to the [script](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/convert_llama_weights_to_hf.py) (skip this step if you already have the Hugging Face weights).

```
python src/transformers/models/llama/convert_llama_weights_to_hf.py \
    --input_dir /path/to/downloaded/llama/weights --model_size 13B --output_dir /output/path
```

Step 2: Download the delta weights for Ziya-LLaMA-13B-v1 and the pre-converted original LLaMA weights from step 1. Use the following script for conversion: https://github.com/IDEA-CCNL/Fengshenbang-LM/blob/main/fengshen/utils/apply_delta.py
```
python3 -m apply_delta --base ~/model_weights/llama-13b --target ~/model_weights/Ziya-LLaMA-13B --delta ~/model_weights/Ziya-LLaMA-13B-v1(huggingface下载)
```

Step 3: Load the model obtained in Step 2 for inference.

## 微调示例 Finetune Example

Refer to [ziya_finetune](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/ziya_llama)

## 推理量化示例 Inference & Quantization Example

Refer to [ziya_inference](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/ziya_inference)

## 引用 Citation

如果您在您的工作中使用了我们的模型，可以引用我们的[论文](https://arxiv.org/abs/2210.08590)：

If you are using the resource for your work, please cite the our [paper](https://arxiv.org/abs/2210.08590):

```text
@article{fengshenbang,
  author    = {Jiaxing Zhang and Ruyi Gan and Junjie Wang and Yuxiang Zhang and Lin Zhang and Ping Yang and Xinyu Gao and Ziwei Wu and Xiaoqun Dong and Junqing He and Jianheng Zhuo and Qi Yang and Yongfeng Huang and Xiayu Li and Yanghan Wu and Junyu Lu and Xinyu Zhu and Weifeng Chen and Ting Han and Kunhao Pan and Rui Wang and Hao Wang and Xiaojun Wu and Zhongshen Zeng and Chongpei Chen},
  title     = {Fengshenbang 1.0: Being the Foundation of Chinese Cognitive Intelligence},
  journal   = {CoRR},
  volume    = {abs/2209.02970},
  year      = {2022}
}
```

You can also cite our [website](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

欢迎引用我们的[网站](https://github.com/IDEA-CCNL/Fengshenbang-LM/):
```text
@misc{Fengshenbang-LM,
  title={Fengshenbang-LM},
  author={IDEA-CCNL},
  year={2021},
  howpublished={\url{https://github.com/IDEA-CCNL/Fengshenbang-LM}},
}
```
