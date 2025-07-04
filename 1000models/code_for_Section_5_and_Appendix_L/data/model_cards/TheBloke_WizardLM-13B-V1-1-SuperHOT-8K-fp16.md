
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

# WizardLM's WizardLM 13B V1.1 fp16

These are fp16 pytorch format model files for [WizardLM's WizardLM 13B V1.1](https://huggingface.co/WizardLM/WizardLM-13B-V1.1) merged with [Kaio Ken's SuperHOT 8K](https://huggingface.co/kaiokendev/superhot-13b-8k-no-rlhf-test).

[Kaio Ken's SuperHOT 13b LoRA](https://huggingface.co/kaiokendev/superhot-13b-8k-no-rlhf-test) is merged on to the base model, and then 8K context can be achieved during inference by using `trust_remote_code=True`.

Note that `config.json` has been set to a sequence length of 8192. This can be modified to 4096 if you want to try with a smaller sequence length.

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/WizardLM-13B-V1-1-SuperHOT-8K-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU inference](https://huggingface.co/TheBloke/WizardLM-13B-V1-1-SuperHOT-8K-GGML)
* [Unquantised SuperHOT fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/TheBloke/WizardLM-13B-V1-1-SuperHOT-8K-fp16)
* [Unquantised base fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/WizardLM/WizardLM-13B-V1.1)

## How to use this model from Python code

First make sure you have Einops installed:

```
pip3 install auto-gptq
```

Then run the following code. `config.json` has been default to a sequence length of 8192, but you can also configure this in your Python code.

The provided modelling code, activated with `trust_remote_code=True` will automatically set the `scale` parameter from the configured `max_position_embeddings`. Eg for 8192, `scale` is set to `4`.

```python
from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM, pipeline
import argparse

model_name_or_path = "TheBloke/WizardLM-13B-V1-1-SuperHOT-8K-fp16"

use_triton = False

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

config = AutoConfig.from_pretrained(model_name_or_path, trust_remote_code=True)
# Change this to the sequence length you want
config.max_position_embeddings = 8192

model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
        config=config,
        trust_remote_code=True,
        device_map='auto')

# Note: check to confirm if this is correct prompt template is correct for this model!
prompt = "Tell me about AI"
prompt_template=f'''USER: {prompt}
ASSISTANT:'''

print("\n\n*** Generate:")

input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
output = model.generate(inputs=input_ids, temperature=0.7, max_new_tokens=512)
print(tokenizer.decode(output[0]))

# Inference can also be done using transformers' pipeline

print("*** Pipeline:")
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.15
)

print(pipe(prompt_template)[0]['generated_text'])
```

## Using other UIs: monkey patch

Provided in the repo is `llama_rope_scaled_monkey_patch.py`, written by @kaiokendev.

It can be theoretically be added to any Python UI or custom code to enable the same result as `trust_remote_code=True`.  I have not tested this, and it should be superseded by using `trust_remote_code=True`, but I include it for completeness and for interest.

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

**Special thanks to**: Luke from CarbonQuill, Aemon Algiz.

**Patreon special mentions**: RoA, Lone Striker, Gabriel Puliatti, Derek Yates, Randy H, Jonathan Leane, Eugene Pentland, Karl Bernard, Viktor Bowallius, senxiiz, Daniel P. Andersen, Pierre Kircher, Deep Realms, Cory Kujawski, Oscar Rangel, Fen Risland, Ajan Kanaga, LangChain4j, webtim, Nikolai Manek, Trenton Dambrowitz, Raven Klaugh, Kalila, Khalefa Al-Ahmad, Chris McCloskey, Luke @flexchar, Ai Maven, Dave, Asp the Wyvern, Sean Connelly, Imad Khwaja, Space Cruiser, Rainer Wilmers, subjectnull, Alps Aficionado, Willian Hasse, Fred von Graf, Artur Olbinski, Johann-Peter Hartmann, WelcomeToTheClub, Willem Michiel, Michael Levine, Iucharbius , Spiking Neurons AB, K, biorpg, John Villwock, Pyrater, Greatston Gnanesh, Mano Prime, Junyu Yang, Stephen Murray, John Detwiler, Luke Pendergrass, terasurfer , Pieter, zynix , Edmond Seymore, theTransient, Nathan LeClaire, vamX, Kevin Schuppel, Preetika Verma, ya boyyy, Alex , SuperWojo, Ghost , Joseph William Delisle, Matthew Berman, Talal Aujan, chris gileta, Illia Dulskyi.

Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: Kaio Ken's SuperHOT 8K


### SuperHOT Prototype 2 w/ 8K Context

This is a second prototype of SuperHOT, a NSFW focused LoRA, this time 7B with 8K context and no RLHF, using the same technique described in [the github blog](https://kaiokendev.github.io/til#extending-context-to-8k).

#### Looking for Merged & Quantized Models?
Make some please :)

#### Using the monkey-patch?
You will **NEED** to **apply the monkeypatch** or, if you are already using the monkeypatch, **change the scaling factor to 0.25 and the maximum sequence length to 8192**

The monkeypatch is only necessary if you are using a front-end/back-end that does not already support scaling and said front-end/back-end is Python-based (i.e. Huggingface Transformers). To apply the patch, you will need to copy the `llama_rope_scaled_monkey_patch.py` into your working directory and call the exported function `replace_llama_rope_with_scaled_rope` at the very start of your Python program. It will modify the Transformers library's implementation of RoPE to properly apply the scaling factor.

#### Using Oobabooga with Exllama?
Switch your loader to `exllama` or `exllama_hf` Add the arguments `max_seq_len 8192` and `compress_pos_emb 4`. **While the model may work well with `compress_pos_emb 2`, it was trained on 4, so that is what I advocate for you to use**

Example in the command-line:
- `python server.py --max_seq_len 8192 --compress_pos_emb 4 --loader exllama_hf`

In the UI, you will see the loader option in the `Models` tab. Once you select either `exllama` or `exllama_hf`, the `max_seq_len` and `compress_pos_emb` settings will appear.

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
- Cutoff length: 4096

# Original model card: WizardLM's WizardLM 13B V1.1



This is the **Full-Weight** of WizardLM-13B V1.1 model.

**Repository**: https://github.com/nlpxucan/WizardLM

**Twitter**: https://twitter.com/WizardLM_AI/status/1677282955490918401


- 🔥🔥🔥 [7/7/2023] We released **WizardLM V1.1** models. The **WizardLM-13B-V1.1** is here ([Demo_13B-V1.1](https://e8a06366ccd1c4d1.gradio.app), [Demo_13B-V1.1_bak-1](https://59da107262a25764.gradio.app), [Demo_13B-V1.1_bak-2](https://dfc5113f66739c80.gradio.app), [Full Model Weight](https://huggingface.co/WizardLM/WizardLM-13B-V1.1)). **WizardLM-7B-V1.1**,  **WizardLM-30B-V1.1**, and **WizardLM-65B-V1.1** are coming soon. Please checkout the [Full Model Weights](https://huggingface.co/WizardLM) and [paper](https://arxiv.org/abs/2304.12244).
- 🔥🔥🔥 [7/7/2023] The **WizardLM-13B-V1.1** achieves **6.74** on [MT-Bench Leaderboard](https://chat.lmsys.org/?leaderboard), **86.32%** on [AlpacaEval Leaderboard](https://tatsu-lab.github.io/alpaca_eval/), and **99.3%** on [WizardLM Eval](https://github.com/nlpxucan/WizardLM/blob/main/WizardLM/data/WizardLM_testset.jsonl). (Note: MT-Bench and AlpacaEval are all self-test, will push update and request review. All tests are completed under their official settings.)


