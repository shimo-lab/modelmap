
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

# rewoo's Planner 7B GGML

These files are fp16 pytorch format model files for [rewoo's Planner 7B](https://huggingface.co/rewoo/planner_7B).

They are the result of merging the LoRA adapter at the above repo with the base LLaMa 7B model.

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/Planner-7B-GPTQ)
* [4-bit, 5-bit, and 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/Planner-7B-GGML)
* [Unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/TheBloke/Planner-7B-fp16)

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

**Special thanks to**: Luke from CarbonQuill, Aemon Algiz, Dmitriy Samsonov.

**Patreon special mentions**: Derek Yates, Sean Connelly, Luke, Nathan LeClaire, Trenton Dambrowitz, Mano Prime, David Flickinger, vamX, Nikolai Manek, senxiiz, Khalefa Al-Ahmad, Illia Dulskyi, trip7s trip, Jonathan Leane, Talal Aujan, Artur Olbinski, Cory Kujawski, Joseph William Delisle, Pyrater, Oscar Rangel, Lone Striker, Luke Pendergrass, Eugene Pentland, Johann-Peter Hartmann.

Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: rewoo's Planner 7B


Alpaca Lora adapter weight fine-tuned on following instruction dataset.

https://huggingface.co/datasets/rewoo/planner_instruction_tuning_2k/blob/main/README.md

Training script: borrowed from the official [Alpaca-LoRA](https://github.com/tloen/alpaca-lora) implementation

We use following parameter.

```
python finetune.py \
    --base_model 'decapoda-research/llama-7b-hf' \
    --data_path 'rewoo/planner_instruction_tuning_2k' \
    --output_dir './lora-alpaca-planner' \
    --batch_size 128 \
    --micro_batch_size 8 \
    --num_epochs 10 \
    --learning_rate 1e-4 \
    --cutoff_len 1024 \
    --val_set_size 200 \
    --lora_r 8 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --lora_target_modules '[q_proj,v_proj]' \
    --train_on_inputs \
    --group_by_length \
    --resume_from_checkpoint 'tloen/alpaca-lora-7b'
```
