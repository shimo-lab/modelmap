Mistral 7B model fine-tuned on AEZAKMI v1 dataset that is derived from airoboros 2.2.1 and airoboros 2.2.
Finetuned with axolotl, using qlora and nf4 double quant, around 2 epochs, batch size 8, lr 0.00008, lr scheduler cosine. Scheduled training was 5 epochs, but loss seemed fine after 2 so I finished it quicker. 
Training took around 10 hours on single RTX 3090 Ti.

Main feature of this model is that it's output is free of refusals and it feels somehow more natural.
Prompt format is standard chatml. 
Don't expect it to be good at math, riddles or be crazy smart. My end goal with AEZAKMI is to create a cozy free chatbot. 


Not sure what license it needs to have, given license of airoboros dataset. I'll leave it as other for now. 
