<!-- header start -->
<div style="width: 100%;">
    <img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p><a href="https://discord.gg/Jq4vkcDakD">Chat & support: my new Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<!-- header end -->
# Wizard-Vicuna-13B-HF

This is a float16 HF format repo for [junelee's wizard-vicuna 13B](https://huggingface.co/junelee/wizard-vicuna-13b).

June Lee's repo was also HF format. The reason I've made this is that the original repo was in float32, meaning it required 52GB disk space, VRAM and RAM.

This model was converted to float16 to make it easier to load and manage.

## Repositories available

* [4bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/wizard-vicuna-13B-GPTQ).
* [4bit and 5bit GGML models for CPU inference](https://huggingface.co/TheBloke/wizard-vicuna-13B-GGML).
* [float16 HF format model for GPU inference](https://huggingface.co/TheBloke/wizard-vicuna-13B-HF).

<!-- footer start -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/Jq4vkcDakD)

## Thanks, and how to contribute.

Thanks to the [chirper.ai](https://chirper.ai) team!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Patreon special mentions**: Aemon Algiz, Dmitriy Samsonov, Nathan LeClaire, Trenton Dambrowitz, Mano Prime, David Flickinger, vamX, Nikolai Manek, senxiiz, Khalefa Al-Ahmad, Illia Dulskyi, Jonathan Leane, Talal Aujan, V. Lukas, Joseph William Delisle, Pyrater, Oscar Rangel, Lone Striker, Luke Pendergrass, Eugene Pentland, Sebastain Graf, Johann-Peter Hartman.

Thank you to all my generous patrons and donaters!
<!-- footer end -->

# Original WizardVicuna-13B model card

Github page: https://github.com/melodysdreamj/WizardVicunaLM

# WizardVicunaLM
### Wizard's dataset + ChatGPT's conversation extension + Vicuna's tuning method
I am a big fan of the ideas behind WizardLM and VicunaLM. I particularly like the idea of WizardLM handling the dataset itself more deeply and broadly, as well as VicunaLM overcoming the limitations of single-turn conversations by introducing multi-round conversations. As a result, I combined these two ideas to create WizardVicunaLM. This project is highly experimental and designed for proof of concept, not for actual usage.


## Benchmark
### Approximately 7% performance improvement over VicunaLM
![](https://user-images.githubusercontent.com/21379657/236088663-3fa212c9-0112-4d44-9b01-f16ea093cb67.png)


### Detail

The questions presented here are not from rigorous tests, but rather, I asked a few questions and requested GPT-4 to score them. The models compared were ChatGPT 3.5, WizardVicunaLM, VicunaLM, and WizardLM, in that order.

|     | gpt3.5 | wizard-vicuna-13b | vicuna-13b | wizard-7b | link     |
|-----|--------|-------------------|------------|-----------|----------|
| Q1  | 95     | 90                | 85         | 88        | [link](https://sharegpt.com/c/YdhIlby) |
| Q2  | 95     | 97                | 90         | 89        | [link](https://sharegpt.com/c/YOqOV4g) |
| Q3  | 85     | 90                | 80         | 65        | [link](https://sharegpt.com/c/uDmrcL9) |
| Q4  | 90     | 85                | 80         | 75        | [link](https://sharegpt.com/c/XBbK5MZ) |
| Q5  | 90     | 85                | 80         | 75        | [link](https://sharegpt.com/c/AQ5tgQX) |
| Q6  | 92     | 85                | 87         | 88        | [link](https://sharegpt.com/c/eVYwfIr) |
| Q7  | 95     | 90                | 85         | 92        | [link](https://sharegpt.com/c/Kqyeub4) |
| Q8  | 90     | 85                | 75         | 70        | [link](https://sharegpt.com/c/M0gIjMF) |
| Q9  | 92     | 85                | 70         | 60        | [link](https://sharegpt.com/c/fOvMtQt) |
| Q10 | 90     | 80                | 75         | 85        | [link](https://sharegpt.com/c/YYiCaUz) |
| Q11 | 90     | 85                | 75         | 65        | [link](https://sharegpt.com/c/HMkKKGU) |
| Q12 | 85     | 90                | 80         | 88        | [link](https://sharegpt.com/c/XbW6jgB) |
| Q13 | 90     | 95                | 88         | 85        | [link](https://sharegpt.com/c/JXZb7y6) |
| Q14 | 94     | 89                | 90         | 91        | [link](https://sharegpt.com/c/cTXH4IS) |
| Q15 | 90     | 85                | 88         | 87        | [link](https://sharegpt.com/c/GZiM0Yt) |
|     | 91     | 88                | 82         | 80        |          |


## Principle

We adopted the approach of WizardLM, which is to extend a single problem more in-depth. However, instead of using individual instructions, we expanded it using Vicuna's conversation format and applied Vicuna's fine-tuning techniques.

Turning a single command into a rich conversation is what we've done [here](https://sharegpt.com/c/6cmxqq0).

After creating the training data, I later trained it according to the Vicuna v1.1 [training method](https://github.com/lm-sys/FastChat/blob/main/scripts/train_vicuna_13b.sh).


## Detailed Method

First, we explore and expand various areas in the same topic using the 7K conversations created by WizardLM. However, we made it in a continuous conversation format instead of the instruction format. That is, it starts with WizardLM's instruction, and then expands into various areas in one conversation using ChatGPT 3.5.

After that, we applied the following model using Vicuna's fine-tuning format.

## Training Process

Trained with 8 A100 GPUs for 35 hours.

## Weights
You can see the [dataset](https://huggingface.co/datasets/junelee/wizard_vicuna_70k) we used for training and the [13b model](https://huggingface.co/junelee/wizard-vicuna-13b) in the huggingface.

## Conclusion
If we extend the conversation to gpt4 32K, we can expect a dramatic improvement, as we can generate 8x more, more accurate and richer conversations.

## License
The model is licensed under the LLaMA model, and the dataset is licensed under the terms of OpenAI because it uses ChatGPT. Everything else is free.

## Author

[JUNE LEE](https://github.com/melodysdreamj) - He is active in Songdo Artificial Intelligence Study and GDG Songdo.
