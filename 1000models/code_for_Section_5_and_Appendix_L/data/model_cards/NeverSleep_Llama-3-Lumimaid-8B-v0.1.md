
## Lumimaid 0.1

<center><div style="width: 100%;">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/630dfb008df86f1e5becadc3/d3QMaxy3peFTpSlWdWF-k.png" style="display: block; margin: auto;">
</div></center>

This model uses the Llama3 **prompting format**

Llama3 trained on our RP datasets, we tried to have a balance between the ERP and the RP, not too horny, but just enough.

We also added some non-RP dataset, making the model less dumb overall. It should look like a 40%/60% ratio for Non-RP/RP+ERP data.

This model includes the new Luminae dataset from Ikari.


If you consider trying this model please give us some feedback either on the Community tab on hf or on our [Discord Server](https://discord.gg/MtCVRWTZXY).

## Credits:
- Undi
- IkariDev

## Description

This repo contains FP16 files of Lumimaid-8B-v0.1.

Switch: [8B](https://huggingface.co/NeverSleep/Llama-3-Lumimaid-8B-v0.1) - [70B](https://huggingface.co/NeverSleep/Llama-3-Lumimaid-70B-v0.1) - [70B-alt](https://huggingface.co/NeverSleep/Llama-3-Lumimaid-70B-v0.1-alt) - [8B-OAS](https://huggingface.co/NeverSleep/Llama-3-Lumimaid-8B-v0.1-OAS) - [70B-OAS](https://huggingface.co/NeverSleep/Llama-3-Lumimaid-70B-v0.1-OAS)

## Training data used:
- [Aesir datasets](https://huggingface.co/MinervaAI)
- [NoRobots](https://huggingface.co/datasets/Doctor-Shotgun/no-robots-sharegpt)
- [limarp](https://huggingface.co/datasets/lemonilia/LimaRP) - 8k ctx
- [toxic-dpo-v0.1-sharegpt](https://huggingface.co/datasets/Undi95/toxic-dpo-v0.1-sharegpt)
- [ToxicQAFinal](https://huggingface.co/datasets/NobodyExistsOnTheInternet/ToxicQAFinal)
- Luminae-i1 (70B/70B-alt) (i2 was not existing when the 70b started training) | Luminae-i2 (8B) (this one gave better results on the 8b) - Ikari's Dataset
- [Squish42/bluemoon-fandom-1-1-rp-cleaned](https://huggingface.co/datasets/Squish42/bluemoon-fandom-1-1-rp-cleaned) - 50% (randomly)
- [NobodyExistsOnTheInternet/PIPPAsharegptv2test](https://huggingface.co/datasets/NobodyExistsOnTheInternet/PIPPAsharegptv2test) - 5% (randomly)
- [cgato/SlimOrcaDedupCleaned](https://huggingface.co/datasets/cgato/SlimOrcaDedupCleaned) - 5% (randomly)
- Airoboros (reduced)
- [Capybara](https://huggingface.co/datasets/Undi95/Capybara-ShareGPT/) (reduced)


## Models used (only for 8B)

- Initial LumiMaid 8B Finetune
- Undi95/Llama-3-Unholy-8B-e4
- Undi95/Llama-3-LewdPlay-8B

## Prompt template: Llama3

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{output}<|eot_id|>
```

## Others

Undi: If you want to support us, you can [here](https://ko-fi.com/undiai).

IkariDev: Visit my [retro/neocities style website](https://ikaridevgit.github.io/) please kek