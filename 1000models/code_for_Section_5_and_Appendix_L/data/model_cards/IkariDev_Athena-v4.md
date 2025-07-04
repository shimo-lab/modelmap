
![image/png](https://cdn-uploads.huggingface.co/production/uploads/630dfb008df86f1e5becadc3/XKvu-iA8ZJaw2rRLm1sVn.png)

Experimental Athena v4 model. Use Alpaca format. Suitable for RP, ERP and general stuff.

I should state here that this is a HIGHLY experimental model!

<!-- description start -->
## Description

<!-- [Recommended settings - contributed by localfultonextractor](https://files.catbox.moe/ue0tja.json) -->

This repo contains fp16 files of Athena-V4.

[GGUF - By TheBloke](https://huggingface.co/TheBloke/Athena-v4-GGUF)

[GPTQ - By TheBloke](https://huggingface.co/TheBloke/Athena-v4-GPTQ)

[exl2 - by waldie](https://huggingface.co/waldie/Athena-v4-8bpw-h8-exl2)

[AWQ - By TheBloke](https://huggingface.co/TheBloke/Athena-v4-AWQ)

[fp16 - by IkariDev+Undi95](https://huggingface.co/IkariDev/Athena-v4)

<!-- [GGUF - by IkariDev](https://huggingface.co/IkariDev/Athena-v4-GGUF)-->
[OLD(GGUF - by IkariDev+Undi95)](https://huggingface.co/IkariDev/Athena-v4-GGUF)

## Ratings:

Note: I have permission of all users to upload their ratings, i DONT screenshot random reviews without asking if i can put them here!

![image/png](https://cdn-uploads.huggingface.co/production/uploads/630dfb008df86f1e5becadc3/8kA_i7BVItCTiUGRdHkoy.png)

If you want your rating to be here, send me a message over on DC and ill put up a screenshot of it here. DC name is "ikaridev".

<!-- description end -->
<!-- description start -->
## Models+loras used and recipe

- Athena-v3
- Xwin-LM/Xwin-LM-13B-V0.1
- Undi95/PsyMedRP-v1-13B
- cgato/Thespis-13b-v0.2
- jondurbin/airoboros-l2-13b-3.0
```
Athena-v4-tmp1 = [ Athena-v3(0.85)+Xwin-LM/Xwin-LM-13B-V0.1(0.15) ]
Athena-v4-tmp2 = [ Undi95/PsyMedRP-v1-13B(0.55)+cgato/Thespis-13b-v0.2(0.45) ]

Athena-v4-tmp3 = Athena-v4-tmp1(0.55) + Athena-v4-tmp2(0.35)

Athena-v4 = Athena-v4-tmp3 + jondurbin/airoboros-l2-13b-3.0(0.1)
```
<!-- description end -->
<!-- prompt-template start -->
## Prompt template: Alpaca

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:

```

Thanks to [Undi95](https://huggingface.co/Undi95) for providing the machine for Athena v2 and Athena v3, and giving me infos about how things work. Going forward i will use a merging server provided by a friend.