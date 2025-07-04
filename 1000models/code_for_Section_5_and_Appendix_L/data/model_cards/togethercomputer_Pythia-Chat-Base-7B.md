
***<p style="font-size: 24px">Feel free to try out our [OpenChatKit feedback app](https://huggingface.co/spaces/togethercomputer/OpenChatKit)!</p>***

# Pythia-Chat-Base-7B-v0.16

> TLDR: As part of OpenChatKit (codebase available [here](https://github.com/togethercomputer/OpenChaT)),
> Pythia-Chat-Base-7B-v0.16 is a 7B parameter language model, fine-tuned from EleutherAI’s Pythia 7B with over 40 million instructions on 100% carbon negative compute.

Pythia-Chat-Base-7B-v0.16 is based on ElutherAI’s Pythia-7B model, and is fine-tuned with data focusing on dialog-style interactions. 
We focused the tuning on several tasks such as question answering, classification, extraction, and summarization. 
We’ve fine-tuned the model with a collection of 43 million high-quality instructions.
Together partnered with LAION and Ontocord.ai, who both helped curate the dataset the model is based on.
You can read more about this process and the availability of this dataset in LAION’s blog post [here](https://laion.ai/blog/oig-dataset/). 

In addition to the aforementioned fine-tuning, Pythia-Chat-Base-7B-v0.16 has also undergone further fine-tuning via a small amount of feedback data. 
This process allows the model to better adapt to human preferences in the conversations.

One of the notable features of Pythia-Chat-Base-7B-v0.16 is its ability to **run inference on a 12GB GPU**, thanks to the quantization technique. 
It helps maintain the dialogue capabilities while making the model more accessible to a wider range of users and hardware configurations.

## Model Details
- **Developed by**: Together Computer.
- **Model type**: Language Model
- **Language(s)**: English
- **License**: Apache 2.0
- **Model Description**: A 7B parameter open source chat model, fine-tuned from EleutherAI’s Pythia with over 40M instructions on 100% carbon negative compute
- **Resources for more information**: [GitHub Repository](https://github.com/togethercomputer/OpenChaT).

# Quick Start

## GPU Inference

This requires a GPU with 24GB memory.
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/Pythia-Chat-Base-7B-v0.16")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/Pythia-Chat-Base-7B-v0.16", torch_dtype=torch.float16)
model = model.to('cuda:0')

# infer
inputs = tokenizer("<human>: Hello!\n<bot>:", return_tensors='pt').to(model.device)
outputs = model.generate(**inputs, max_new_tokens=10, do_sample=True, temperature=0.8)
output_str = tokenizer.decode(outputs[0])
print(output_str)
```

## GPU Inference in Int8

This requires a GPU with 12GB memory.
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/Pythia-Chat-Base-7B-v0.16")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/Pythia-Chat-Base-7B-v0.16", device_map="auto", load_in_8bit=True)

# infer
inputs = tokenizer("<human>: Hello!\n<bot>:", return_tensors='pt').to(model.device)
outputs = model.generate(**inputs, max_new_tokens=10, do_sample=True, temperature=0.8)
output_str = tokenizer.decode(outputs[0])
print(output_str)
```


## CPU Inference

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/Pythia-Chat-Base-7B-v0.16")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/Pythia-Chat-Base-7B-v0.16", torch_dtype=torch.bfloat16)

# infer
inputs = tokenizer("<human>: Hello!\n<bot>:", return_tensors='pt').to(model.device)
outputs = model.generate(**inputs, max_new_tokens=10, do_sample=True, temperature=0.8)
output_str = tokenizer.decode(outputs[0])
print(output_str)
```


## Strengths of the model

There are several tasks that OpenChatKit excels at out of the box. This includes: 

- Summarization and question answering within context.
- Extraction.
- Classification.

In addition, the model does well on few-shot prompts. For both classification and extraction, the model performs even better with few shots, as in most HELM tasks. [Contact us](https://www.together.xyz/contact) if you’re interested in trying few-shot prompts with the model. 

## Weaknesses of the model

That said, there are several areas where we have more work to do, and we need your help! Some of these include: 

- Knowledge-based closed question and answering: The chatbot may hallucinate and give incorrect results. Be sure to fact check, and if possible provide feedback with the corrected information.
- Coding tasks: The chatbot was not trained on a large enough corpus of source code to excel at writing code. We welcome contributions of additional datasets to improve this!
- Repetition: Sometimes the chatbot will repeat its response. We’re working to improve this, but in the meantime you can click the refresh button to start a new conversation.
- Context switching: If you change the topic in the middle of a conversation the chatbot often cannot make the switch automatically and will continue to give answers related to the prior topic.
- Creative writing and longer answers: The chatbot does not generate long, creative text such as an essay or story.

We are excited to work with you to address these weaknesses by getting your feedback, bolstering data sets, and improving accuracy.

# Uses

## Direct Use 

The model is intended for research purposes. Possible research areas and tasks include

- Safe deployment of models which have the potential to generate harmful content.
- Probing and understanding the limitations and biases of dialogue models or language models.
- Generation of artworks and use in design and other artistic processes.
- Applications in educational or creative tools.
- Research on dialogue models or language models.

Excluded uses are described below.

### Misuse, Malicious Use, and Out-of-Scope Use

The OpenChatKit community provides Pythia-Chat-Base-7B-v0.16 as an open source tool for building chatbots. 
The community is not responsible for any misuse, malicious use, or out-of-scope use of the model. 
It is the responsibility of the end user to ensure that the model is used in a responsible and ethical manner.

#### Out-of-Scope Use

Pythia-Chat-Base-7B-v0.16 is designed for use in chatbot applications and may not perform well for other use cases outside of its intended scope. 
For example, it may not be suitable for use in safety-critical applications or for making decisions that have a significant impact on individuals or society. 
It is important to consider the limitations of the model and to only use it for its intended purpose.

#### Misuse and Malicious Use

Pythia-Chat-Base-7B-v0.16 is designed for use in chatbot applications and should not be used for any other purpose.
Misuse of the model, such as using it to engage in illegal or unethical activities, is strictly prohibited and goes against the principles of the OpenChatKit community project.

Using the model to generate content that is cruel to individuals is a misuse of this model. This includes, but is not limited to:

- Generating fake news, misinformation, or propaganda
- Promoting hate speech, discrimination, or violence against individuals or groups
- Impersonating individuals or organizations without their consent
- Engaging in cyberbullying or harassment
- Defamatory content
- Spamming or scamming
- Sharing confidential or sensitive information without proper authorization
- Violating the terms of use of the model or the data used to train it
- Creating automated bots for malicious purposes such as spreading malware, phishing scams, or spamming

## Limitations

Pythia-Chat-Base-7B-v0.16, like other language model-based chatbots, has limitations that should be taken into consideration. 
For example, the model may not always provide accurate or relevant answers, particularly for questions that are complex, ambiguous, or outside of its training data. 
We therefore welcome contributions from individuals and organizations, and encourage collaboration towards creating a more robust and inclusive chatbot.

## Training

**Training Data**

Please refer to [togethercomputer/OpenDataHub](https://github.com/togethercomputer/OpenDataHub)

**Training Procedure**

- **Hardware:** 8 x A100 GPUs
- **Optimizer:** [8bit-AdamW](https://github.com/TimDettmers/bitsandbytes)
- **Gradient Accumulations**: 4
- **Batch:** 4 x 4 x 16 x 2048 = 524288 tokens
- **Learning rate:** warmup to 1e-5 for 100 steps and then kept constant

## Community

Join us on [Together Discord](https://discord.gg/6ZVDU8tTD4)