<p align="center">
<img width="500px" alt="Project Baize" src="https://user-images.githubusercontent.com/22514219/229195563-0cddfa74-e52f-4413-b4b4-e4ba489c4b3d.png">
</p>
<hr>

## ⚠️Warning
Using Baize checkpoints directly without the following format will not work. 
```
The following is a conversation between a human and an AI assistant named Baize (named after a mythical creature in Chinese folklore). Baize is an open-source AI assistant developed by UCSD and Sun Yat-Sen University. The human and the AI assistant take turns chatting. Human statements start with [|Human|] and AI assistant statements start with [|AI|]. The AI assistant always provides responses in as much detail as possible, and in Markdown format. The AI assistant always declines to engage with topics, questions and instructions related to unethical, controversial, or sensitive issues. Complete the transcript in exactly that format.\n[|Human|]Hello!\n[|AI|]Hi!
```
`[|Human|]` and `[|AI|]` are required to mark the messages from the user and Baize. We recommend checking out our [GitHub](https://github.com/project-baize/baize) to find the best way to use Baize with our demo or Fastchat.

## Demo
https://huggingface.co/spaces/project-baize/chat-with-baize

## What's Baize?
Baize is an open-source chat model fine-tuned with [LoRA](https://github.com/microsoft/LoRA). This model is a **7B Baize-v2**, trained with supervised fine-tuning (SFT) and self-distillation with feedback (SDF). This checkpoint has been merged with LLaMA so it's ready for use.

## Why it's called Baize?
Baize (白泽) is a mythical creature in Chinese folklore, who speaks human languages and knows everything. This is exactly what we expect from a chat model.

## How to use it: local demo, API and SDK
More details can be found in the Baize [GitHub](https://github.com/project-baize/baize) and [Paper](https://arxiv.org/abs/2304.01196).