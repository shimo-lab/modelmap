
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

# NousResearch's Nous-Hermes-13B fp16

This is fp16 pytorch format model files for [NousResearch's Nous-Hermes-13B](https://huggingface.co/NousResearch/Nous-Hermes-13b) merged with [Kaio Ken's SuperHOT 8K](https://huggingface.co/kaiokendev/superhot-13b-8k-no-rlhf-test).

[Kaio Ken's SuperHOT 13b LoRA](https://huggingface.co/kaiokendev/superhot-13b-8k-no-rlhf-test) is merged on to the base model, and then 8K context can be achieved during inference by using `trust_remote_code=True`.

Note that `config.json` has been set to a sequence length of 8192. This can be modified to 4096 if you want to try with a smaller sequence length.

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/Nous-Hermes-13B-SuperHOT-8K-GPTQ)
* [Unquantised SuperHOT fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/TheBloke/Nous-Hermes-13B-SuperHOT-8K-fp16)
* [Unquantised base fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/NousResearch/Nous-Hermes-13b)

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

**Patreon special mentions**: Pyrater, WelcomeToTheClub, Kalila, Mano Prime, Trenton Dambrowitz, Spiking Neurons AB, Pierre Kircher, Fen Risland, Kevin Schuppel, Luke, Rainer Wilmers, vamX, Gabriel Puliatti, Alex , Karl Bernard, Ajan Kanaga, Talal Aujan, Space Cruiser, ya boyyy, biorpg, Johann-Peter Hartmann, Asp the Wyvern, Ai Maven, Ghost , Preetika Verma, Nikolai Manek, trip7s trip, John Detwiler, Fred von Graf, Artur Olbinski, subjectnull, John Villwock, Junyu Yang, Rod A, Lone Striker, Chris McCloskey, Iucharbius , Matthew Berman, Illia Dulskyi, Khalefa Al-Ahmad, Imad Khwaja, chris gileta, Willem Michiel, Greatston Gnanesh, Derek Yates, K, Alps Aficionado, Oscar Rangel, David Flickinger, Luke Pendergrass, Deep Realms, Eugene Pentland, Cory Kujawski, terasurfer , Jonathan Leane, senxiiz, Joseph William Delisle, Sean Connelly, webtim, zynix , Nathan LeClaire.

Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: Kaio Ken's SuperHOT 8K

### SuperHOT Prototype 2 w/ 8K Context

This is a second prototype of SuperHOT, this time 30B with 8K context and no RLHF, using the same technique described in [the github blog](https://kaiokendev.github.io/til#extending-context-to-8k).
Tests have shown that the model does indeed leverage the extended context at 8K.

You will need to **use either the monkeypatch** or, if you are already using the monkeypatch, **change the scaling factor to 0.25 and the maximum sequence length to 8192**

#### Looking for Merged & Quantized Models?
- 30B 4-bit CUDA: [tmpupload/superhot-30b-8k-4bit-safetensors](https://huggingface.co/tmpupload/superhot-30b-8k-4bit-safetensors)
- 30B 4-bit CUDA 128g: [tmpupload/superhot-30b-8k-4bit-128g-safetensors](https://huggingface.co/tmpupload/superhot-30b-8k-4bit-128g-safetensors)


#### Training Details
I trained the LoRA with the following configuration:
- 1200 samples (~400 samples over 2048 sequence length)
  - learning rate of 3e-4
  - 3 epochs
  - The exported modules are:
  - q_proj
  - k_proj
  - v_proj
  - o_proj
  - no bias
  - Rank = 4
  - Alpha = 8
  - no dropout
  - weight decay of 0.1
  - AdamW beta1 of 0.9 and beta2 0.99, epsilon of 1e-5
  - Trained on 4-bit base model

# Original model card: NousResearch's Nous-Hermes-13B


# Model Card: Nous-Hermes-13b

## Model Description

Nous-Hermes-13b is a state-of-the-art language model fine-tuned on over 300,000 instructions. This model was fine-tuned by Nous Research, with Teknium and Karan4D leading the fine tuning process and dataset curation, Redmond AI sponsoring the compute, and several other contributors. The result is an enhanced Llama 13b model that rivals GPT-3.5-turbo in performance across a variety of tasks.

This model stands out for its long responses, low hallucination rate, and absence of OpenAI censorship mechanisms. The fine-tuning process was performed with a 2000 sequence length on an 8x a100 80GB DGX machine for over 50 hours. 

## Model Training

The model was trained almost entirely on synthetic GPT-4 outputs. This includes data from diverse sources such as GPTeacher, the general, roleplay v1&2, code instruct datasets, Nous Instruct & PDACTL (unpublished), CodeAlpaca, Evol_Instruct Uncensored, GPT4-LLM, and Unnatural Instructions. 

Additional data inputs came from Camel-AI's Biology/Physics/Chemistry and Math Datasets, Airoboros' GPT-4 Dataset, and more from CodeAlpaca. The total volume of data encompassed over 300,000 instructions.

## Collaborators
The model fine-tuning and the datasets were a collaboration of efforts and resources between Teknium, Karan4D, Nous Research, Huemin Art, and Redmond AI. 
  
Huge shoutout and acknowledgement is deserved for all the dataset creators who generously share their datasets openly. 

Special mention goes to @winglian, @erhartford, and @main_horse for assisting in some of the training issues.

Among the contributors of datasets, GPTeacher was made available by Teknium, Wizard LM by nlpxucan, and the Nous Research Instruct Dataset was provided by Karan4D and HueminArt.  
The GPT4-LLM and Unnatural Instructions were provided by Microsoft, Airoboros dataset by jondurbin, Camel-AI datasets are from Camel-AI, and CodeAlpaca dataset by Sahil 2801.
If anyone was left out, please open a thread in the community tab.

## Prompt Format

The model follows the Alpaca prompt format:
```
### Instruction:

### Response:
```

or 

```
### Instruction:

### Input:

### Response:
```  

## Resources for Applied Use Cases:
For an example of a back and forth chatbot using huggingface transformers and discord, check out: https://github.com/teknium1/alpaca-discord  
For an example of a roleplaying discord bot, check out this: https://github.com/teknium1/alpaca-roleplay-discordbot  

## Future Plans
The model is currently being uploaded in FP16 format, and there are plans to convert the model to GGML and GPTQ 4bit quantizations. The team is also working on a full benchmark, similar to what was done for GPT4-x-Vicuna. We will try to get in discussions to get the model included in the GPT4All.

## Benchmark Results
```
|    Task     |Version| Metric |Value |   |Stderr|
|-------------|------:|--------|-----:|---|-----:|
|arc_challenge|      0|acc     |0.4915|±  |0.0146|
|             |       |acc_norm|0.5085|±  |0.0146|
|arc_easy     |      0|acc     |0.7769|±  |0.0085|
|             |       |acc_norm|0.7424|±  |0.0090|
|boolq        |      1|acc     |0.7948|±  |0.0071|
|hellaswag    |      0|acc     |0.6143|±  |0.0049|
|             |       |acc_norm|0.8000|±  |0.0040|
|openbookqa   |      0|acc     |0.3560|±  |0.0214|
|             |       |acc_norm|0.4640|±  |0.0223|
|piqa         |      0|acc     |0.7965|±  |0.0094|
|             |       |acc_norm|0.7889|±  |0.0095|
|winogrande   |      0|acc     |0.7190|±  |0.0126|
```

These benchmarks currently have us at #1 on ARC-c, ARC-e, Hellaswag, and OpenBookQA, and 2nd place on Winogrande, comparing to GPT4all's benchmarking list. 

## Model Usage
The model is available for download on Hugging Face. It is suitable for a wide range of language tasks, from generating creative text to understanding and following complex instructions.
  
Compute provided by our project sponsor Redmond AI, thank you!!
