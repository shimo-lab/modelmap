
<!-- header start -->
<div style="width: 100%;">
    <img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p><a href="https://discord.gg/theblokeai">Chat & support: my new Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<!-- header end -->

# Open BMB's UltraLM 13B fp16

These files are pytorch format fp16 model files for [Open BMB's UltraLM 13B](https://huggingface.co/openbmb/UltraLM-13b).

It is the result of merging and/or converting the source repository to float16.

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/UltraLM-13B-fp16)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/UltraLM-13B-GGML)
* [Merged, unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/TheBloke/UltraLM-13B-fp16)

## Prompt template: Vicuna 1.1

```
USER: prompt
ASSISTANT:
```

<!-- footer start -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/theblokeai)

## Thanks, and how to contribute.

Thanks to the [chirper.ai](https://chirper.ai) team!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Special thanks to**: Luke from CarbonQuill, Aemon Algiz, Dmitriy Samsonov.

**Patreon special mentions**: zynix, ya boyyy, Trenton Dambrowitz, Imad Khwaja, Alps Aficionado, chris gileta, John Detwiler, Willem Michiel, RoA, Mano Prime, Rainer Wilmers, Fred von Graf, Matthew Berman, Ghost , Nathan LeClaire, Iucharbius , Ai Maven, Illia Dulskyi, Joseph William Delisle, Space Cruiser, Lone Striker, Karl Bernard, Eugene Pentland, Greatston Gnanesh, Jonathan Leane, Randy H, Pierre Kircher, Willian Hasse, Stephen Murray, Alex , terasurfer , Edmond Seymore, Oscar Rangel, Luke Pendergrass, Asp the Wyvern, Junyu Yang, David Flickinger, Luke, Spiking Neurons AB, subjectnull, Pyrater, Nikolai Manek, senxiiz, Ajan Kanaga, Johann-Peter Hartmann, Artur Olbinski, Kevin Schuppel, Derek Yates, Kalila, K, Talal Aujan, Khalefa Al-Ahmad, Gabriel Puliatti, John Villwock, WelcomeToTheClub, Daniel P. Andersen, Preetika Verma, Deep Realms, Fen Risland, trip7s trip, webtim, Sean Connelly, Michael Levine, Chris McCloskey, biorpg, vamX, Viktor Bowallius, Cory Kujawski.

Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: Open BMB's UltraLM 13B

# UltraLM-13b

<!-- Provide a quick summary of what the model is/does. -->

This is UltraLM-13b delta weights, a chat language model trained upon [UltraChat](https://github.com/thunlp/UltraChat)


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

The model is fine-tuned based on LLaMA-13b with a multi-turn chat-format template as below

```
User: instruction 1<eos_token>
Assistant: response 1<eos_token>
User: instruction 2<eos_token>
Assistant: response 2<eos_token>
...
```

- **License:** UltraLM is based on LLaMA and should be used under LLaMA's [model license](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md).
- **Finetuned from model:** LLaMA-13b
- **Finetuned on data:** [UltraChat](https://github.com/thunlp/UltraChat)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** [UltraChat](https://github.com/thunlp/UltraChat)
- **Paper:** [arxiv](https://arxiv.org/abs/2305.14233)
- **Demo:** [More Information Needed]

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
To use this model, you need to [recover](https://github.com/thunlp/UltraChat/tree/main/UltraLM) the full model from the delta weights and perform inference following the template below:

```
[Optional]User: system prompt<eos_token>
User: user input<eos_token>
Assistant: 
```
