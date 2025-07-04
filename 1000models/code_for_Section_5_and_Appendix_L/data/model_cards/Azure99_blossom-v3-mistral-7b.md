# **BLOSSOM-v3-mistral-7b**

[💻Github](https://github.com/Azure99/BlossomLM) • [🚀Blossom Chat Demo](https://blossom-chat.com/)

### Introduction

Blossom is a conversational large language model, fine-tuned on the Blossom Orca/Wizard/Chat/Math mixed dataset based on the Mistral-7B-v0.1 pre-trained model. Blossom possesses robust general capabilities and context comprehension. Additionally, the high-quality Chinese and English datasets used for training have been made open source.

Training was conducted in two stages. The first stage used 100K Wizard, 100K Orca single-turn instruction datasets, training for 1 epoch; the second stage used a 2K Blossom math reasoning dataset, 50K Blossom chat multi-turn dialogue dataset, and 1% randomly sampled data from the first stage, training for 3 epochs.

Note: The Mistral-7B-v0.1 pre-trained model is somewhat lacking in Chinese knowledge, so for Chinese scenarios, it is recommended to use [blossom-v3-baichuan2-7b](https://huggingface.co/Azure99/blossom-v3-baichuan2-7b).

### Inference

Inference is performed in the form of dialogue continuation.

Single-turn dialogue

```
A chat between a human and an artificial intelligence bot. The bot gives helpful, detailed, and polite answers to the human's questions.
|Human|: hello
|Bot|: Hello! How can I assist you today?
```

Multi-turn dialogue

```
A chat between a human and an artificial intelligence bot. The bot gives helpful, detailed, and polite answers to the human's questions.
|Human|: hello
|Bot|: Hello! How can I assist you today?</s>
|Human|: Generate a random number using python
|Bot|: 
```

Note: At the end of the Bot's output in the historical conversation, append a `</s>`.