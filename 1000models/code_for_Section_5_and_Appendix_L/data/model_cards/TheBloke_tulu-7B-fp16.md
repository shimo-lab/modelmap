
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

# Allen AI's Tulu 7B fp16

These files are pytorch format fp16 model files for [Allen AI's Tulu 7B](https://huggingface.co/allenai/tulu-7b).

It is the result of merging and/or converting the source repository to float16.

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/tulu-7B-fp16)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/tulu-7B-GGML)
* [Unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/TheBloke/tulu-7B-fp16)

## Prompt template

The following template should be used:

```
<|user|>
prompt goes here
<|assistant|>

```

**Note**: There should be a newline after `<|assistant|>`. This appears to be very important for getting this model to respond correctly.

In other words, the prompt is:

```
<|user|>\nprompt goes here\n<|assistant|>\n
```

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

**Patreon special mentions**: Oscar Rangel, Eugene Pentland, Talal Aujan, Cory Kujawski, Luke, Asp the Wyvern, Ai Maven, Pyrater, Alps Aficionado, senxiiz, Willem Michiel, Junyu Yang, trip7s trip, Sebastain Graf, Joseph William Delisle, Lone Striker, Jonathan Leane, Johann-Peter Hartmann, David Flickinger, Spiking Neurons AB, Kevin Schuppel, Mano Prime, Dmitriy Samsonov, Sean Connelly, Nathan LeClaire, Alain Rossmann, Fen Risland, Derek Yates, Luke Pendergrass, Nikolai Manek, Khalefa Al-Ahmad, Artur Olbinski, John Detwiler, Ajan Kanaga, Imad Khwaja, Trenton Dambrowitz, Kalila, vamX, webtim, Illia Dulskyi.

Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: Allen AI's Tulu 7B


# Tulu 7B

This model is a 7B LLaMa model finetuned on a mixture of instruction datasets (FLAN V2, CoT, Dolly, Open Assistant 1, GPT4-Alpaca, Code-Alpaca, and ShareGPT).
*Please note this is a model diff - see below for usage instructions*.

This was trained as part of the paper [How Far Can Camels Go? Exploring the State of Instruction Tuning on Open Resources](https://arxiv.org/abs/2306.04751).
The codebase used to train and evaluate this model can be found at [https://github.com/allenai/open-instruct](https://github.com/allenai/open-instruct).

This model is licensed under the AI model license given in LICENSE.txt along with the original Llama license (llama_license.txt).

## Usage

We assume you have access to a LLaMa model in HF format already. You can find details on getting access and converting the model here:
[https://huggingface.co/docs/transformers/main/model_doc/llama](https://huggingface.co/docs/transformers/main/model_doc/llama)

Clone [https://github.com/allenai/open-instruct](https://github.com/allenai/open-instruct) and install the required dependencies, or just copy `scripts/weight_diff.py`
and install the minimal requirements listed in `weight-diff-requirements.txt`. Then download or clone this model diff to the same machine.

Then, run:
```bash
python scripts/weight_diff.py recover --path_raw ${hf_llama_path} --path_tuned ${output_path} --path_diff ${diff_location}
```

And you will have a recovered model! Note this takes up a decent amount of RAM, especially for the larger models.

## Input Format

The model is trained to use the following format (note the newlines):
```
<|user|>
Your message here!
<|assistant|>
```

For best results, format all inputs in this manner.

## Performance

Here is the performance of this model across benchmarks explored in our paper [How Far Can Camels Go? Exploring the State of Instruction Tuning on Open Resources](https://arxiv.org/abs/2306.04751):

| MMLU 0-shot | MMLU 5-shot | GSM Direct | GSM CoT | BBH Direct | BBH CoT | TydiQA Gold-Passage | TydiQA Closed-book | Codex-Eval Pass@1 | Codex-Eval Pass@10 | AlpacaFarm vs Davinci-003 | Average |
|:-----------:|:-----------:|:----------:|:-------:|:----------:|:-------:|:-------------------:|:------------------:|:-----------------:|:------------------:|:-------------------------:|---------|
| 44.5 | 47.0 | 6.0 | 27.0 | 38.1 | 39.2 | 45.7 | 7.7 | 17.5 | 27.8 | 48.3 | 33.1 |

If you use this model, please cite our work, the llama paper, and the original datasets:

```
@misc{wang2023far,
      title={How Far Can Camels Go? Exploring the State of Instruction Tuning on Open Resources}, 
      author={Yizhong Wang and Hamish Ivison and Pradeep Dasigi and Jack Hessel and Tushar Khot and Khyathi Raghavi Chandu and David Wadden and Kelsey MacMillan and Noah A. Smith and Iz Beltagy and Hannaneh Hajishirzi},
      year={2023},
      eprint={2306.04751},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```
@misc{touvron2023llama,
      title={LLaMA: Open and Efficient Foundation Language Models}, 
      author={Hugo Touvron and Thibaut Lavril and Gautier Izacard and Xavier Martinet and Marie-Anne Lachaux and Timothée Lacroix and Baptiste Rozière and Naman Goyal and Eric Hambro and Faisal Azhar and Aurelien Rodriguez and Armand Joulin and Edouard Grave and Guillaume Lample},
      year={2023},
      eprint={2302.13971},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```
@misc{dolly,
  author = {Databricks},
  title = {Free Dolly: Introducing the World's First Truly Open Instruction-Tuned LLM},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {Blog post},
  url = {https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm}
}
```

```
@article{longpre2023flan,
  title={The Flan Collection: Designing Data and Methods for Effective Instruction Tuning},
  author={Longpre, Shayne and Hou, Le and Vu, Tu and Webson, Albert and Chung, Hyung Won and Tay, Yi and Zhou, Denny and Le, Quoc V and Zoph, Barret and Wei, Jason and others},
  journal={arXiv preprint arXiv:2301.13688},
  year={2023}
}
```

```
@misc{köpf2023openassistant,
      title={OpenAssistant Conversations -- Democratizing Large Language Model Alignment}, 
      author={Andreas Köpf and Yannic Kilcher and Dimitri von Rütte and Sotiris Anagnostidis and Zhi-Rui Tam and Keith Stevens and Abdullah Barhoum and Nguyen Minh Duc and Oliver Stanley and Richárd Nagyfi and Shahul ES and Sameer Suri and David Glushkov and Arnav Dantuluri and Andrew Maguire and Christoph Schuhmann and Huu Nguyen and Alexander Mattick},
      year={2023},
      eprint={2304.07327},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```
@article{peng2023instruction,
  title={Instruction Tuning with GPT-4},
  author={Peng, Baolin and Li, Chunyuan and He, Pengcheng and Galley, Michel and Gao, Jianfeng},
  journal={arXiv preprint arXiv:2304.03277},
  year={2023}
}
```

```
@misc{codealpaca,
  author = {Sahil Chaudhary},
  title = {Code Alpaca: An Instruction-following LLaMA model for code generation},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/sahil280114/codealpaca}},
}
```
