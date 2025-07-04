# LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models

<font size=6><div align='center' > <a href=http://arxiv.org/abs/2309.12307>**Paper**</a> | <a href="https://huggingface.co/Yukang">**Models**</a> | <a href="https://github.com/dvlab-research/LongLoRA">**Code**</a> </div></font>

**LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models [[Paper](http://arxiv.org/abs/2309.12307)]** <br />
[Yukang Chen](https://scholar.google.com/citations?user=6p0ygKUAAAAJ&hl=en),
[Shengju Qian](https://scholar.google.com/citations?user=QNnWmasAAAAJ),
[Haotian Tang](https://scholar.google.com/citations?user=WxL13BAAAAAJ&hl),
[Xin Lai](https://scholar.google.com/citations?user=tqNDPA4AAAAJ&hl=zh-CN),
[Zhijian Liu](https://scholar.google.com/citations?user=3coYSTUAAAAJ&hl=en),
[Song Han](https://scholar.google.com/citations?user=E0iCaa4AAAAJ&hl=zh-CN),
[Jiaya Jia](https://scholar.google.com/citations?user=XPAkzTEAAAAJ&hl=en)<br />

## Abstract
We present LongLoRA, an efficient fine-tuning approach that extends the context sizes of pre-trained large language models (LLMs), with limited computation cost.
Typically, training LLMs with long context sizes is computationally expensive, requiring extensive training hours and GPU resources.
In this paper, we speed up the context extension of LLMs in two aspects. On the one hand, although dense global attention is needed during inference, fine-tuning the model can be effectively and efficiently done by sparse local attention. The proposed shift short attention effectively enables context extension, leading to non-trivial computation saving with similar performance to fine-tuning with vanilla attention. On the other hand, we find that LoRA for context extension works well under the premise of trainable embedding and normalization. LongLoRA demonstrates strong empirical results on various tasks on LLaMA2 models from 7B/13B to 70B. LongLoRA adopts LLaMA2 7B from 4k context to 100k, or LLaMA2 70B to 32k on a single 8x A100 machine. LongLoRA extends models' context while retaining their original architectures, and is compatible with most existing techniques, like FlashAttention-2. In addition, to make LongLoRA practical, we collect a dataset, LongQA, for supervised fine-tuning. It contains more than 3k long context question-answer pairs. For more details, please refer to the [paper](http://arxiv.org/abs/2309.12307).


## Highlights
**LongLoRA** speed up the context extension of pre-trained large language models in both attention-level and weight-level.
1. The proposed shifted short attention is easy to implement, compatible with Flash-Attention, and not required during inference. 
2. We release all our models, including models from 7B to 70B, context length from 8k to 100k, including [LLaMA2-LongLoRA-7B-100k](https://huggingface.co/Yukang/Llama-2-7b-longlora-100k-ft), [LLaMA2-LongLoRA-13B-64k](https://huggingface.co/Yukang/Llama-2-13b-longlora-64k), and [LLaMA2-LongLoRA-70B-32k](https://huggingface.co/Yukang/Llama-2-70b-longlora-32k).
3. We build up a long-context QA dataset, LongQA, for supervised fine-tuning (SFT). We release 13B and 70B 32k models with SFT,  [Llama-2-13b-chat-longlora-32k-sft](https://huggingface.co/Yukang/Llama-2-13b-chat-longlora-32k-sft) and [Llama-2-70b-chat-longlora-32k-sft](https://huggingface.co/Yukang/Llama-2-70b-chat-longlora-32k-sft). We will further release the dataset next week.

## Released models

### Models with supervised fine-tuning
| Model                             | Size | Context | Train   | Link                                                                    |
|:----------------------------------|------|---------|---------|-------------------------------------------------------------------------|
| Llama-2-13b-chat-longlora-32k-sft | 13B  | 32768   | LoRA+   | [link](https://huggingface.co/Yukang/Llama-2-13b-chat-longlora-32k-sft) |
| Llama-2-70b-chat-longlora-32k-sft | 70B  | 32768   | LoRA+   | [link](https://huggingface.co/Yukang/Llama-2-70b-chat-longlora-32k-sft) |

### Models with context extension via fully fine-tuning
| Model                       | Size | Context | Train | Link                                                              |
|:----------------------------|------|---------|-------|-------------------------------------------------------------------|
| Llama-2-7b-longlora-8k-ft   | 7B   | 8192    | Full FT    | [link](https://huggingface.co/Yukang/Llama-2-7b-longlora-8k-ft)   |
| Llama-2-7b-longlora-16k-ft  | 7B   | 16384   | Full FT    | [link](https://huggingface.co/Yukang/Llama-2-7b-longlora-16k-ft)  |
| Llama-2-7b-longlora-32k-ft  | 7B   | 32768   | Full FT    | [link](https://huggingface.co/Yukang/Llama-2-7b-longlora-32k-ft)  |
| Llama-2-7b-longlora-100k-ft | 7B   | 100000  | Full FT    | [link](https://huggingface.co/Yukang/Llama-2-7b-longlora-100k-ft) |
| Llama-2-13b-longlora-8k-ft  | 13B  | 8192    | Full FT    | [link](https://huggingface.co/Yukang/Llama-2-13b-longlora-8k-ft)  |
| Llama-2-13b-longlora-16k-ft | 13B  | 16384   | Full FT    | [link](https://huggingface.co/Yukang/Llama-2-13b-longlora-16k-ft) |
| Llama-2-13b-longlora-32k-ft | 13B  | 32768   | Full FT    | [link](https://huggingface.co/Yukang/Llama-2-13b-longlora-32k-ft) |

### Models with context extension via improved LoRA fine-tuning
| Model                       | Size | Context | Train | Link                                                              |
|:----------------------------|------|---------|-------|-------------------------------------------------------------------|
| Llama-2-7b-longlora-8k      | 7B   | 8192    | LoRA+ | [link](https://huggingface.co/Yukang/Llama-2-7b-longlora-8k)      |
| Llama-2-7b-longlora-16k     | 7B   | 16384   | LoRA+ | [link](https://huggingface.co/Yukang/Llama-2-7b-longlora-16k)     |
| Llama-2-7b-longlora-32k     | 7B   | 32768   | LoRA+ | [link](https://huggingface.co/Yukang/Llama-2-7b-longlora-32k)     |
| Llama-2-13b-longlora-8k     | 13B  | 8192    | LoRA+ | [link](https://huggingface.co/Yukang/Llama-2-13b-longlora-8k)     |
| Llama-2-13b-longlora-16k    | 13B  | 16384   | LoRA+ | [link](https://huggingface.co/Yukang/Llama-2-13b-longlora-16k)    |
| Llama-2-13b-longlora-32k    | 13B  | 32768   | LoRA+ | [link](https://huggingface.co/Yukang/Llama-2-13b-longlora-32k)    |
| Llama-2-13b-longlora-64k    | 13B  | 65536   | LoRA+ | [link](https://huggingface.co/Yukang/Llama-2-13b-longlora-64k)    |
| Llama-2-70b-longlora-32k    | 70B  | 32768   | LoRA+ | [link](https://huggingface.co/Yukang/Llama-2-70b-longlora-32k)    |
| Llama-2-70b-chat-longlora-32k    | 70B  | 32768   | LoRA+ | [link](https://huggingface.co/Yukang/Llama-2-70b-chat-longlora-32k)    |

## Citation 
If you find this project useful in your research, please consider citing:

```
@article{longlora,
  title={LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models},
  author={Yukang Chen and Shengju Qian and Haotian Tang and Xin Lai and Zhijian Liu and Song Han and Jiaya Jia},
  journal={arXiv:2309.12307},
  year={2023}
}
```

## Acknowledgement
-  This work is built upon the [LLaMA2](https://ai.meta.com/llama) as the pre-trained models.
- This work is based on [DeepSpeed](https://github.com/microsoft/DeepSpeed), [peft](https://github.com/huggingface/peft), and [Flash-Attention2](https://github.com/Dao-AILab/flash-attention) for acceleration.
- The perplexity evaluation code is modified upon [Landmark Attention](https://github.com/epfml/landmark-attention).
- We use [LongChat](https://github.com/DachengLi1/LongChat) for the retrieval evaluation.

