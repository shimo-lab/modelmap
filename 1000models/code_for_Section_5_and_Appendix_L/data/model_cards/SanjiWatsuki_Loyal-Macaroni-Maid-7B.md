
![image/png](https://huggingface.co/SanjiWatsuki/Loyal-Macaroni-Maid-7B/resolve/main/macaroni-maid.jpg)

<!-- description start -->
## Description

This repository hosts **Loyal-Macaroni-Maid-7B**, a 7B model aimed at having engaging RP with solid character card adherence and being a smart cookie at the same time. Quants can be found [here](https://huggingface.co/collections/SanjiWatsuki/loyal-macaroni-maid-7b-658a9f424f349f95cf0648b0).

In my limited testing, it's a great RP model suitable for RP/ERP with sharp reasoning skills for a 7B.

On benchmarks like MT-Bench, this RP model scores shockingly well.

| Model                  | MT Bench | MMLU |
|------------------------|----------|------|
| GPT-4-Turbo            | 9.32     |      |
| GPT-4                  | 8.99     | 86.4 |
| Starling-7B            | 8.09     | 63.9 |
| Claude-2               | 8.06     | 78.5 |
| **Loyal-Macaroni-Maid-7B** | 7.95     | ~64.9|
| GPT-3.5-Turbo          | 7.94     | 70   |
| Claude-1               | 7.9      | 77   |
| Openchat-3.5           | 7.81     | 64.3 |
| Zephyr-7B-beta         | 7.34     | 61.4 |
| Llama-2-70b-chat-hf    | 6.86     | 63   |
| Neural-chat-7b-v3-1    | 6.84     | 62.4 | 

<!-- description end -->
<!-- prompt-template start -->
## Prompt template: Custom format, or Alpaca

### Custom format:
I found the best SillyTavern results from using the Noromaid template.

SillyTavern config files: [Context](https://files.catbox.moe/ifmhai.json), [Instruct](https://files.catbox.moe/ttw1l9.json). Additionally, here is my [Text Completion preset](https://huggingface.co/SanjiWatsuki/Loyal-Macaroni-Maid-7B/blob/main/Characters/MinP.json)

Otherwise, I tried to ensure that most of the underlying merged models were Alpaca-ish.

### Alpaca:
```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:

```

## Helpful Tips

For SFW RP, I found that I got the most use out of this model when I had an RPG Narrator in a group chat with the characters I wanted to RP with. Here is an importable character card for the best RPG Narrator I found thus far.

![image/png](https://huggingface.co/SanjiWatsuki/Loyal-Macaroni-Maid-7B/resolve/main/Characters/RPGNarrator.png)

For basic ChatGPT tasks, here is the basic Assistant card that I use. I found it works best with Default context template / Alpaca instruct template in Silly Tavern.

![image/png](https://huggingface.co/SanjiWatsuki/Loyal-Macaroni-Maid-7B/resolve/main/Characters/Indigo.png)

## Frankenstein's Merger

**tl;dr: This is a bunch of model merger slop with a bunch of RP cherries on top.**

I'll keep it a buck - I'm not a fan of this model's composition. Based on my testing, it seemed like models that were built from a merger of OpenChat-3.5/Starling and NeuralChat v3.1 had surprisingly good character card coherence for a 7B model - better than either one in isolation. This is validated both in my personal benchmarks as well as the [Ayumi NSFW ERP ALC-IQ3 metric](http://ayumi.m8geil.de/ayumi_bench_v3_results.html) which rates character card coherence and is dominated by OpenNeuralChat mergers for small models.

The issue is... prompt format.

OpenChat-3.5 uses an abomination of a prompt format with "GPT4 Correct User/Assistant" all over it in a ChatML-style prompt with extra tokens for padding and end-of-turn. NeuralChat v3.1 uses a weird Alpaca-like format with "### System/User/Assistant" all over it. Almost every RP finetune standardized on Alpaca or an expanded Alpaca with janky multi-turn prompting (since Alpaca doesn't have multi-turn prompting).

Most model mergers like [Q-bert/MetaMath-Cybertron-Starling](https://huggingface.co/Q-bert/MetaMath-Cybertron-Starling) just slam them together and toss the extra ChatML tokens, resulting in a half-Alpaca-like half-ChatML-like Frankenstein's monster. For the most part, using Alpaca as the lingua franca just kinda works but [there are exceptions that can make a generation go off the rails](https://huggingface.co/AIDC-ai-business/Marcoroni-7B-v3/discussions/6). I found this to be a bit of an issue in certain SillyTavern test cases.

Regardless, the strong Chat Arena performances from 7B models continues to lead me to believe they're the strongest base for an all-purpose model.

### The sauce (All You Need is DARE)

**tl;dr: It's an OpenChat/NeuralChat merger with as much RP as possible stuffed in using the DARE TIES merger method.**

This model is a DARE TIES merger between Toten5/Marcoroni-neural-chat-7B-v2, chargoddard/loyal-piano-m7, Undi95/Toppy-M-7B, NeverSleep/Noromaid-7b-v0.2, and athirdpath/NSFW_DPO_vmgb-7b on top of a mistralai/Mistral-7B-v0.1 base.

```
models:
  - model: mistralai/Mistral-7B-v0.1
    # no parameters necessary for base model
  - model: Toten5/Marcoroni-neural-chat-7B-v2
    parameters:
      weight: 0.3
      density: 0.8
  - model: chargoddard/loyal-piano-m7
    parameters:
      weight: 0.4
      density: 0.8
  - model: Undi95/Toppy-M-7B
    parameters:
      weight: 0.2
      density: 0.4
  - model: NeverSleep/Noromaid-7b-v0.2
    parameters:
      weight: 0.2
      density: 0.4
  - model: athirdpath/NSFW_DPO_vmgb-7b
    parameters:
      weight: 0.2
      density: 0.4
merge_method: dare_ties
base_model: mistralai/Mistral-7B-v0.1
parameters:
  int8_mask: true
dtype: bfloat16
```

There's a lot to unpack here. I went with DARE TIES because it appeared to be a viable way to combine information into models without losing smarts. Directly SLERPing a smart cookie model with an ERP brained model will often dilute both the model's smarts and RPing ability. This is an attempt to have my cookie and eat it, too.

First, there are two high density high weight models:

[chargoddard/loyal-piano-m7](https://huggingface.co/chargoddard/loyal-piano-m7) is the easy primary model choice. It's an Alpaca prompt format model that scores highly, is very creative for a 7B, and is primarily trained on RP data.

[Toten5/Marcoroni-neural-chat-7B-v2](https://huggingface.co/Toten5/Marcoroni-neural-chat-7B-v2) is the unintuitive second model pick. It is a merger of mergers that chains back to being an OpenChat/NeuralChat merger being SLERPed back into NeuralChat a second time. Despite SLERPing NeuralChat in multiple times, it retains its high benchmark scores. I opted to pick this model as my base because I believed it was the OpenChat/NeuralChat model that benchmarked well that was closest to the O.G. NeuralChat which has the most Alpaca-like prompt.

By picking a density of 0.8, these models have a 96% chance of showing up for any TIE merger. This should ensure that there is a solid "base" of deltas from the base Mistral model that captures most of what makes these models good. High density with 0.3-0.4 weights have been shown in mergers like [jan-hq/supermario-v2](https://huggingface.co/jan-hq/supermario-v2)

Next, there are 3 RP models merged in with medium density. [Undi95/Toppy-M-7B](https://huggingface.co/Undi95/Toppy-M-7B), [NeverSleep/Noromaid-7b-v0.2](https://huggingface.co/NeverSleep/Noromaid-7b-v0.2), and [athirdpath/NSFW_DPO_vmgb-7b](https://huggingface.co/athirdpath/NSFW_DPO_vmgb-7b). Toppy-M-7B is an easy pick for being a well regarded 7B RP model - although, it is a merger of many mergers which might dilute its effectiveness as a lower density merge. NeverSleep/Noromaid-7b-v0.2 pulls in the unique private Noromaid RP dataset. Finally, athirdpath/NSFW_DPO_vmgb-7b is another Frankenstein OpenNeuralChat merger that happens to be DPOed on athirdpath's NSFW Alpaca pairs which seemed like another good RP addition to the model (plus, maybe it tilts it to being more Alpaca-flavored, idk).

By picking a density of 0.4, these models should *largely* impart some of their flavor onto the merger. I suspect the density could go even lower and the models could be used even more like a LoRA-like merger on top.

The DARE TIES merger is intentionally overweight and non-normalized at 1.3 total weight. I intentionally went overweight to try and better capture the individual characteristics from the various models. With wide mergers, a weight of 1.0 can often become incoherent like [jan-hq/supermario-v1](https://huggingface.co/jan-hq/supermario-v1).

Putting it all together, ~60% of the model is "base models" like OpenChat/NeuralChat/Loyal-Piano-M7. ~40% of the model is effectively me trying to extract RP information from existing RP models. The only non-RP model is the Marcoroni base which means that almost 80% of this model is intended for RP.

Not that the benchmarks matter, but if this merger works right, it'll be a high benchmarking 7B that is both smart and strong at RP.