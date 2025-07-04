
<p><h1>🐋 The First Llong Context Orca! 🐋</h1></p>


![OpenOrca Logo](https://huggingface.co/datasets/Open-Orca/OpenOrca/resolve/main/OpenOrcaLogo.png "OpenOrca Logo")


# OpenOrca - LlongOrca - 7B - 16k

We have used our own [OpenOrca dataset](https://huggingface.co/datasets/Open-Orca/OpenOrca) to fine-tune on top of [LLongMA-2-7b-16k](https://huggingface.co/conceptofmind/LLongMA-2-7b-16k). 
This dataset is our attempt to reproduce the dataset generated for Microsoft Research's [Orca Paper](https://arxiv.org/abs/2306.02707).
We use [OpenChat](https://huggingface.co/openchat) packing, trained with [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl).

This release is trained on a curated filtered subset of most of our GPT-4 augmented data.
It is the same subset of our data as was used in our [OpenOrcaxOpenChat-Preview2-13B model](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B).

This release reveals that stacking our training on an existing long context fine-tuned model yields significant improvements to model performance.
We measured this with BigBench-Hard and AGIEval results, finding **~134%** of the base Llongma2-16k model's performance on average.

We have run extensive evaluations internally and expect this model to place number 4 on the HuggingFaceH4 Open LLM Leaderboard for 7B models, but with >99% performance of the first place and **place number 1** for longer context 7B models.

We did this training as part of testing integration of OpenChat's [MultiPack algorithm](https://github.com/imoneoi/multipack_sampler) into the Axolotl trainer.
MultiPack achieves 99.85% bin-packing efficiency on our dataset.
This has significantly reduced training time, with efficiency improvement of 3-10X over traditional methods.


<img src="https://raw.githubusercontent.com/imoneoi/openchat/master/assets/logo_new.png" style="width: 300px">


Want to visualize our full (pre-filtering) dataset? Check out our [Nomic Atlas Map](https://atlas.nomic.ai/map/c1b88b47-2d9b-47e0-9002-b80766792582/2560fd25-52fe-42f1-a58f-ff5eccc890d2).


[<img src="https://huggingface.co/Open-Orca/OpenOrca-Preview1-13B/resolve/main/OpenOrca%20Nomic%20Atlas.png" alt="Atlas Nomic Dataset Map" width="400" height="400" />](https://atlas.nomic.ai/map/c1b88b47-2d9b-47e0-9002-b80766792582/2560fd25-52fe-42f1-a58f-ff5eccc890d2)


Many thanks to @EnricoShippole, @theemozilla, and @kaiokendev1 for the fine work on creating the LlongMA-2-7b-16k model this was trained on top of!

We are in-process with training more models, so keep a look out on our org for releases coming soon with exciting partners.

We will also give sneak-peak announcements on our Discord, which you can find here:

https://AlignmentLab.ai

# Prompt Template

We used [OpenAI's Chat Markup Language (ChatML)](https://github.com/openai/openai-python/blob/main/chatml.md) format, with `<|im_start|>` and `<|im_end|>` tokens added to support this.

## Example Prompt Exchange

```
<|im_start|>system
You are LlongOrca, a large language model trained by Alignment Lab AI. Write out your reasoning step-by-step to be sure you get the right answers!
<|im_end|>
<|im_start|>user
How are you<|im_end|>
<|im_start|>assistant
I am doing well!<|im_end|>
<|im_start|>user
How are you now?<|im_end|>
```


# Evaluation

We have evaluated using the methodology and tools for the HuggingFace Leaderboard, and find that we have significantly improved upon the base long context model.
As well, we should place #4 among all 7B models (and #1 for a model with long context) at release time!

## AGIEval Performance

We present our performance on AGI Eval in comparison to base Llama2-7B and to [Llongma2-7b-16k](https://huggingface.co/conceptofmind/LLongMA-2-7b-16k), which we trained on top of.
This demonstrates the benefits of stacking OpenOrca dataset training on existing models.
Most notably, there is a very dramatic improvement of nearly 3X in the English writing performance.

![LlongOrca 7B 16k AGIEval Performance](https://huggingface.co/Open-Orca/LlongOrca-7B-16k/resolve/main/Images/LlongOrca7BAGIEval.png "AGIEval Performance")

## BigBench-Hard Performance

We present our performance on BigBench-Hard in comparison to base Llama2-7B and to [Llongma2-7b-16k](https://huggingface.co/conceptofmind/LLongMA-2-7b-16k), which we trained on top of.
This demonstrates the benefits of stacking OpenOrca dataset training on existing models.

![LlongOrca 7B 16k BigBench-Hard Performance](https://huggingface.co/Open-Orca/LlongOrca-7B-16k/resolve/main/Images/LlongOrca7BBigBenchHard.png "BigBench-Hard Performance")

## HuggingFaceH4 Open LLM Leaderboard Performance

We have run our own tests using parameters matching the [HuggingFaceH4 Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) evals.

We place #4 for all 7B models at release time, and #1 for long context models.

![LlongOrca 7B 16k Leaderboard Internal Performance](https://huggingface.co/Open-Orca/LlongOrca-7B-16k/resolve/main/Images/LlongOrca7BHFLeaderboard.png "HuggingFace Leaderboard Internal Performance")


# Dataset

We used a curated, filtered selection of most of the GPT-4 augmented data from our OpenOrca dataset, which aims to reproduce the Orca Research Paper dataset.
Further details of our curation practices will be forthcoming with our full model releases.


# Training

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

We trained with 8x A6000-48GB (first-gen) GPUs for 37 hours, completing 4 epochs of full fine tuning on our dataset in one training run.
Commodity cost was ~$200.
Axolotl training parameters can be found in [configs/oo7b.yml](https://huggingface.co/Open-Orca/LlongOrca-7B-16k/blob/main/configs/oo-7b.yml).
We used the `packing-attn` branch of Axolotl during training.

# Citation

```bibtex
@software{lian2023llongorca7b,
  title = {LlongOrca7B: Llama2-7B Model Instruct-tuned for Long Context on Filtered OpenOrcaV1 GPT-4 Dataset},
  author = {Wing Lian and Bleys Goodson and Guan Wang and Eugene Pentland and Austin Cook and Chanvichet Vong and "Teknium"},
  year = {2023},
  publisher = {HuggingFace},
  journal = {HuggingFace repository},
  howpublished = {\url{https://https://huggingface.co/Open-Orca/LlongOrca-7B-16k},
}
@software{openchat,
  title = {{OpenChat: Advancing Open-source Language Models with Imperfect Data}},
  author = {Wang, Guan and Cheng, Sijie and Yu, Qiying and Liu, Changling},
  doi = {10.5281/zenodo.8105775},
  url = {https://github.com/imoneoi/openchat},
  version = {pre-release},
  year = {2023},
  month = {7},
}
@misc{mukherjee2023orca,
      title={Orca: Progressive Learning from Complex Explanation Traces of GPT-4}, 
      author={Subhabrata Mukherjee and Arindam Mitra and Ganesh Jawahar and Sahaj Agarwal and Hamid Palangi and Ahmed Awadallah},
      year={2023},
      eprint={2306.02707},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
@misc{longpre2023flan,
      title={The Flan Collection: Designing Data and Methods for Effective Instruction Tuning}, 
      author={Shayne Longpre and Le Hou and Tu Vu and Albert Webson and Hyung Won Chung and Yi Tay and Denny Zhou and Quoc V. Le and Barret Zoph and Jason Wei and Adam Roberts},
      year={2023},
      eprint={2301.13688},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
@misc{touvron2023llama,
    title={Llama 2: Open Foundation and Fine-Tuned Chat Models}, 
    author={Hugo Touvron and Louis Martin and Kevin Stone and Peter Albert and Amjad Almahairi and Yasmine Babaei and Nikolay Bashlykov and Soumya Batra and Prajjwal Bhargava and Shruti Bhosale and Dan Bikel and Lukas Blecher and Cristian Canton Ferrer and Moya Chen and Guillem Cucurull and David Esiobu and Jude Fernandes and Jeremy Fu and Wenyin Fu and Brian Fuller and Cynthia Gao and Vedanuj Goswami and Naman Goyal and Anthony Hartshorn and Saghar Hosseini and Rui Hou and Hakan Inan and Marcin Kardas and Viktor Kerkez and Madian Khabsa and Isabel Kloumann and Artem Korenev and Punit Singh Koura and Marie-Anne Lachaux and Thibaut Lavril and Jenya Lee and Diana Liskovich and Yinghai Lu and Yuning Mao and Xavier Martinet and Todor Mihaylov and Pushkar Mishra and Igor Molybog and Yixin Nie and Andrew Poulton and Jeremy Reizenstein and Rashi Rungta and Kalyan Saladi and Alan Schelten and Ruan Silva and Eric Michael Smith and Ranjan Subramanian and Xiaoqing Ellen Tan and Binh Tang and Ross Taylor and Adina Williams and Jian Xiang Kuan and Puxin Xu and Zheng Yan and Iliyan Zarov and Yuchen Zhang and Angela Fan and Melanie Kambadur and Sharan Narang and Aurelien Rodriguez and Robert Stojnic and Sergey Edunov and Thomas Scialom},
    year={2023},
    eprint={2307.09288},
    archivePrefix={arXiv},
}
```