
# 🇹🇭 OpenThaiGPT 13b 1.0.0-beta Chat with 16 bits in Huggingface's format.
<img src="https://1173516064-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvvbWvIIe82Iv1yHaDBC5%2Fuploads%2Fb8eiMDaqiEQL6ahbAY0h%2Fimage.png?alt=media&token=6fce78fd-2cca-4c0a-9648-bd5518e644ce
https://openthaigpt.aieat.or.th/" width="200px">

🇹🇭 OpenThaiGPT 13b Version 1.0.0-beta is a Thai language 13B-parameter LLaMA v2 Chat model finetuned to follow Thai translated instructions and extend more than 10,000 most popular Thai words vocabularies into LLM's dictionary for turbo speed.

## Licenses
**Source Code**: License Apache Software License 2.0.<br>
**Weight**: Research and **Commercial uses**.<br>

## Codes and Weight
**Finetune Code**: https://github.com/OpenThaiGPT/openthaigpt-finetune-010beta<br>
**Inference Code**: https://github.com/OpenThaiGPT/openthaigpt<br>
**Weight (Huggingface Checkpoint)**: https://huggingface.co/openthaigpt/openthaigpt-1.0.0-beta-13b-chat-hf

## Sponsors
<img src="https://cdn-uploads.huggingface.co/production/uploads/5fcd9c426d942eaf4d1ebd30/42d-GioSs4evIdNuMAaPB.png" width="600px">

## Supports
- Official website: https://openthaigpt.aieat.or.th
- Facebook page: https://web.facebook.com/groups/openthaigpt
- A Discord server for discussion and support [here](https://discord.gg/rUTp6dfVUF)
- E-mail: kobkrit@aieat.or.th

## Description
Prompt format is Llama2
```
<s>[INST] <<SYS>>
system_prompt
<</SYS>>

question [/INST]
```
System prompt:
You are a question answering assistant. Answer the question as truthful and helpful as possible คุณคือผู้ช่วยตอบคำถาม จงตอบคำถามอย่างถูกต้องและมีประโยชน์ที่สุด

## How to use

1. install VLLM (https://github.com/vllm-project/vllm)
2. python -m vllm.entrypoints.api_server --model /path/to/model --tensor-parallel-size num_gpus
3. run inference (CURL example)

```
curl --request POST \
    --url http://localhost:8000/generate \
    --header "Content-Type: application/json" \
    --data '{"prompt": "<s>[INST] <<SYS>>\nYou are a question answering assistant. Answer the question as truthful and helpful as possible คุณคือผู้ช่วยตอบคำถาม จงตอบคำถามอย่างถูกต้องและมีประโยชน์ที่สุด\n<</SYS>>\n\nอยากลดความอ้วนต้องทำอย่างไร [/INST]","use_beam_search": false, "temperature": 0.1, "max_tokens": 512, "top_p": 0.75, "top_k": 40, "frequency_penalty": 0.3 "stop": "</s>"}'
```

### Authors
* Kobkrit Viriyayudhakorn (kobkrit@aieat.or.th)
* Sumeth Yuenyong (sumeth.yue@mahidol.edu)
* Thaweewat Rugsujarit (thaweewr@scg.com)
* Jillaphat Jaroenkantasima (autsadang41@gmail.com)
* Norapat Buppodom (new@norapat.com)
* Koravich Sangkaew (kwankoravich@gmail.com)
* Peerawat Rojratchadakorn (peerawat.roj@gmail.com)
* Surapon Nonesung (nonesungsurapon@gmail.com)
* Chanon Utupon (chanon.utupon@gmail.com)
* Sadhis Wongprayoon (sadhis.tae@gmail.com)
* Nucharee Thongthungwong (nuchhub@hotmail.com)
* Chawakorn Phiantham (mondcha1507@gmail.com)
* Patteera Triamamornwooth (patt.patteera@gmail.com)
* Nattarika Juntarapaoraya (natt.juntara@gmail.com)
* Kriangkrai Saetan (kraitan.ss21@gmail.com)
* Pitikorn Khlaisamniang (pitikorn32@gmail.com)

<i>Disclaimer: Provided responses are not guaranteed.</i>
