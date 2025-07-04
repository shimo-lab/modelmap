# **BLOSSOM-v2-llama2-7b**

[💻Github](https://github.com/Azure99/BlossomLM) • [🚀Blossom Chat Demo](https://blossom-chat.com/)

### 介绍

Blossom是一个对话式语言模型，基于Llama-2-7b预训练模型，在Blossom、Wizard、Dolphin混合数据集上进行指令精调得来。

训练分为两阶段，第一阶段使用120K Wizard、180K Dolphin单轮指令数据集，训练1个epoch；第二阶段使用60K Blossom chat、2K Blossom math多轮对话数据集，训练3个epoch。

注意：Llama-2-7b预训练模型的中文知识较为欠缺，因此对于中文场景，更推荐使用[blossom-v2-baichuan-7b](https://huggingface.co/Azure99/blossom-v2-baichuan-7b)

### 推理

推理采用对话续写的形式。

单轮对话

```
A chat between a human and an artificial intelligence bot. The bot gives helpful, detailed, and polite answers to the human's questions.
|Human|: 你好
|Bot|: 
```

多轮对话

```
A chat between a human and an artificial intelligence bot. The bot gives helpful, detailed, and polite answers to the human's questions.
|Human|: 你好
|Bot|: 你好，有什么我能帮助你的？</s>
|Human|: 介绍下中国的首都吧
|Bot|: 
```

注意：在历史对话的Bot输出结尾，拼接一个&lt;/s&gt;