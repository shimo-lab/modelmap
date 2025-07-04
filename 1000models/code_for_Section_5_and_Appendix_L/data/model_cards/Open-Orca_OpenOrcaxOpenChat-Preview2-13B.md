
<p><h1>🐋 The Second OpenOrca Model Preview! 🐋</h1></p>


![OpenOrca Logo](https://huggingface.co/datasets/Open-Orca/OpenOrca/resolve/main/OpenOrcaLogo.png "OpenOrca Logo")


# OpenOrca x OpenChat - Preview2 - 13B

We have used our own [OpenOrca dataset](https://huggingface.co/datasets/Open-Orca/OpenOrca) to fine-tune Llama2-13B using [OpenChat](https://huggingface.co/openchat) packing.
This dataset is our attempt to reproduce the dataset generated for Microsoft Research's [Orca Paper](https://arxiv.org/abs/2306.02707).

This second preview release is trained on a curated filtered subset of most of our GPT-4 augmented data.

This release highlights that our dataset and training methods have surpassed performance parity with the Orca paper.
We measured this with BigBench-Hard and AGIEval results with the same methods as used in the Orca paper, finding **~103%** of original Orca's performance on average.
As well, this is done with <1/10th the compute requirement and using <20% of the dataset size from the original Orca paper.

We have run extensive evaluations internally and expect this model to **place number 1** on both the HuggingFaceH4 Open LLM Leaderboard and the GPT4ALL Leaderboard for 13B models.

"One" of [OpenChat](https://huggingface.co/openchat) has joined our team, and we'd like to provide special thanks for their training of this model!
We have utilized OpenChat [MultiPack algorithm](https://github.com/imoneoi/multipack_sampler) which achieves 99.85% bin-packing efficiency on our dataset.
This has significantly reduced training time, with efficiency improvement of 3-10X over traditional methods.


<img src="https://raw.githubusercontent.com/imoneoi/openchat/master/assets/logo_new.png" style="width: 40%">


Want to visualize our full (pre-filtering) dataset? Check out our [Nomic Atlas Map](https://atlas.nomic.ai/map/c1b88b47-2d9b-47e0-9002-b80766792582/2560fd25-52fe-42f1-a58f-ff5eccc890d2).


[<img src="https://huggingface.co/Open-Orca/OpenOrca-Preview1-13B/resolve/main/OpenOrca%20Nomic%20Atlas.png" alt="Atlas Nomic Dataset Map" width="400" height="400" />](https://atlas.nomic.ai/map/c1b88b47-2d9b-47e0-9002-b80766792582/2560fd25-52fe-42f1-a58f-ff5eccc890d2)


We are in-process with training more models, so keep a look out on our org for releases coming soon with exciting partners.

We will also give sneak-peak announcements on our Discord, which you can find here:

https://AlignmentLab.ai

# Prompt Template

We use our own prompt template which we call "`OpenChat Llama2 V1`".

The model is heavily conditioned to work using this format only and will likely encounter issues such as run-on output which emulates a chat between a user and assistant if this format is not properly followed.


Examples:
```
# Single-turn `OpenChat Llama2 V1`
tokenize("You are OpenOrcaChat.<|end_of_turn|>User: Hello<|end_of_turn|>Assistant:")
# [1, 887, 526, 4673, 2816, 1113, 1451, 271, 29889, 32000, 4911, 29901, 15043, 32000, 4007, 22137, 29901]

# Multi-turn `OpenChat Llama2 V1`
tokenize("You are OpenOrcaChat.<|end_of_turn|>User: Hello<|end_of_turn|>Assistant: Hi<|end_of_turn|>User: How are you today?<|end_of_turn|>Assistant:")
# [1, 887, 526, 4673, 2816, 1113, 1451, 271, 29889, 32000, 4911, 29901, 15043, 32000, 4007, 22137, 29901, 6324, 32000, 4911, 29901, 1128, 526, 366, 9826, 29973, 32000, 4007, 22137, 29901]
```

For UIs with Prefix and Suffix fields, these will likely work:

Prefix (include a space after colon):
```
User: 
```

Suffix (space after colon):
```
<|end_of_turn|>\nAssistant: 
```

**Oobabooga's text-generation-webui instructions can be found [further down the page](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B#serving-with-oobabooga--text-generation-webui).**


# Evaluation

We have evaluated **OpenOrcaxOpenChat-Preview2-13B** on hard reasoning tasks from BigBench-Hard and AGIEval as outlined in the Orca paper.

Our average performance for BigBench-Hard: 0.488

Average for AGIEval: 0.447

We find our score averages to **~103%** of the total performance that was shown in the Orca paper, using the same evaluation methods as outlined in the paper.

So we are surpassing Orca performance with <20% of the dataset size and <1/10th the training budget!

As well, we have evaluated using the methodology and tools for the HuggingFace Leaderboard and GPT4ALL Leaderboard, and find that we place #1 on both for all 13B models at release time!

## AGIEval Performance

We present our results in two columns.
The column for "`(Orca Paper eval)`" uses the methods outlined in the Orca paper, so as to be a direct apples-to-apples comparison with the results from the paper.
The column for "`(HF Leaderboard eval)`" uses EleutherAI's LM Evaluation Harness with settings outlined by HuggingFace. These results are not comparable to the other columns, as the methods are different.

![OpenOrca Preview2 AGIEval Performance](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B/resolve/main/Images/OpenOrcaP2AGIEval.png "AGIEval Performance")

## BigBench-Hard Performance

We present our results in two columns.
The column for "`(Orca Paper eval)`" uses the methods outlined in the Orca paper, so as to be a direct apples-to-apples comparison with the results from the paper.
The column for "`(HF Leaderboard eval)`" uses EleutherAI's LM Evaluation Harness with settings outlined by HuggingFace. These results are not comparable to the other columns, as the methods are different.

![OpenOrca Preview2 BigBench-Hard Performance](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B/resolve/main/Images/OpenOrcaP2BigBenchHardEval.png "BigBench-Hard Performance")

## HuggingFaceH4 Open LLM Leaderboard Performance

We have run our own tests using parameters matching the [HuggingFaceH4 Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) evals.

We place #1 for all 13B models at release time!

![OpenOrca Preview2 HuggingFace Leaderboard Internal Performance](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B/resolve/main/Images/OpenOrcaP2HuggingFaceLeaderboard.png "HuggingFace Leaderboard Internal Performance")

**Update Aug 10th:** The official results on the leaderboard are below.

![OpenOrca Preview2 HuggingFace Leaderboard Performance](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B/resolve/main/Images/OpenOrcaP2HFLeaderboardOfficial.png "HuggingFace Leaderboard Performance")

Since our release, a new model which merges an Orca-style model with a Platypus (trained on STEM and logic) model places narrowly above ours, but we were #1 at release time.

Below we also highlight how our model fits relative to models of all sizes on the current (as of Aug 10th, 2023) leaderboard.

![OpenOrca Preview2 HuggingFace Leaderboard Performance](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B/resolve/main/Images/OpenOrcaP2HFLeaderboardFull.png "HuggingFace Full Leaderboard")

Notably, performance is beyond falcon-40b-instruct, and close to LLaMA1-65B base.

## GPT4ALL Leaderboard Performance

We have tested using parameters matching the GPT4ALL Benchmark Suite and report our results and placement vs their official reporting below.

We place #1 for all open models and come within comparison of `text-davinci-003`, a proprietary OpenAI model an order of magnitude larger.

![OpenOrca Preview2 GPT4ALL Performance](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B/resolve/main/Images/OpenOrcaP2GPT4ALL_Leaderboard.png "GPT4ALL Performance")


# Dataset

We used a curated, filtered selection of most of the GPT-4 augmented data from our OpenOrca dataset, which aims to reproduce the Orca Research Paper dataset.
Further details of our curation practices will be forthcoming with our full model releases.


# Training

We trained with 8x A100-80G GPUs for 46 hours, completing 5 epochs of full fine tuning on our dataset in one training run.
This contrasts with the 20x A100-80G GPUs for 200 hours used in the Orca paper, for only 3 epochs, and requiring stacked training (which is known to suffer catastrophic forgetting).
Our compute requirement was <1/10th that of the original Orca.
Commodity cost was ~$600.

Please await our full releases for further training details.


# Serving

This model is most easily served with [OpenChat's](https://github.com/imoneoi/openchat) customized vLLM OpenAI-compatible API server.
This is highly recommended as it is by far the fastest in terms of inference speed and is a quick and easy option for setup.
We also illustrate setup of Oobabooga/text-generation-webui below. The settings outlined there will also apply to other uses of `Transformers`.

## Serving Quantized

Pre-quantized models are now available courtesy of our friend TheBloke:

* **GGML**: https://huggingface.co/TheBloke/OpenOrcaxOpenChat-Preview2-13B-GGML
* **GPTQ**: https://huggingface.co/TheBloke/OpenOrcaxOpenChat-Preview2-13B-GPTQ

The serving instructions below only apply to the unquantized model being presented in the repository you are viewing here.
There are some notes, such as on use of the prompt format, that will still apply to the quantized models though.

## Serving with OpenChat

[Install OpenChat](https://github.com/imoneoi/openchat/#installation)

After installation, run:

```bash
python -m ochat.serving.openai_api_server \
  --model-type openchat_llama2 \
  --model Open-Orca/OpenOrcaxOpenChat-Preview2-13B \
  --engine-use-ray --worker-use-ray --max-num-batched-tokens 5120
```

Follow the OpenChat documentation to use features such as tensor parallelism on consumer GPUs, API keys, and logging.
You may then connect to the OpenAI-compatible API endpoint with tools such as [BetterGPT.chat](https://bettergpt.chat).

## Serving with Oobabooga / text-generation-webui

The model may also be loaded via [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui/) in a similar manner to other models.
See the requirements below. Note that inference with just the Transformers library is significantly slower than using the recommended OpenChat vLLM server.

### Oobabooga Key Requirements

* You will first need to download the model as you normally do to the "`models/`" folder of your `text-generation-webui` installation.
* To use the unquantized model presented here, select "`Transformers`"" in the webui's "`Model`" tab "`Model loader`" dropdown.
  * You will likely want to tick "`auto-devices`". The model will require >40GB VRAM after loading in context for inference.
  * The model was trained in bf16, so tick the "`bf16`" box for best performance.
  * It will run safely on single GPUs with VRAM >=48GB (e.g. A6000)
    * If using consumer GPUs, e.g. 2x RTX3090 24GB, you will likely want to enter "18,17" under "`tensor_split`" to split the model across both GPUs
* The model will perform significantly better if you use the appropriate prompting template
  * We will submit a PR to include our prompting template into text-generation-webui soon
  * For now, manually enter the settings described in the following sections:

### Oobabooga Chat Settings

In the "`Chat settings`" tab, select the following settings:

For "`User String`" ...
```
User:
```
For "`Bot string`" ...
```
Assistant:
```
For "`Context`", this is analogous to system prompt.
It is not necessary, but we have found good results with the below example.
System prompts used in the Orca training also work well. ...
```
You are a helpful assistant. Please answer truthfully and write out your thinking step by step to be sure you get the right answer. If you make a mistake or encounter an error in your thinking, say so out loud and attempt to correct it. If you don't know or aren't sure about something, say so clearly. You will act as a professional logician, mathematician, and physicist. You will also act as the most appropriate type of expert to answer any particular question or solve the relevant problem; state which expert type your are, if so. Also think of any particular named expert that would be ideal to answer the relevant question or solve the relevant problem; name and act as them, if appropriate.
```
For "`Turn template`", this is absolutely essential to have. You will get poor, mixed up output without this template ...
```
<|user|> <|user-message|><|end_of_turn|>\n<|bot|> <|bot-message|>\n
```

When done, it should look as below:
<img src="https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B/resolve/main/Images/OpenOrcaLlama2OobaboogaChatInstructionTemplate.png" style="width: 40%">

You may then save this as a named template preset by clicking the "Floppy" icon and giving it an appropriate name in the popup, e.g. "`OpenOrcaxOpenChat Llama2`".

### Oobabooga Text Generation Mode

In the "`Text generation`" tab, select "`instruct`" as the mode:

#### Mode Illustration
It should look as below:
<img src="https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B/resolve/main/Images/OpenOrcaLlama2OobaboogaInstructMode.png" style="width: 40%">

Then you should be ready to generate!

# Citation

```bibtex
@software{OpenOrcaxOpenChatPreview2,
  title = {OpenOrcaxOpenChatPreview2: Llama2-13B Model Instruct-tuned on Filtered OpenOrcaV1 GPT-4 Dataset},
  author = {Guan Wang and Bleys Goodson and Wing Lian and Eugene Pentland and Austin Cook and Chanvichet Vong and "Teknium"},
  year = {2023},
  publisher = {HuggingFace},
  journal = {HuggingFace repository},
  howpublished = {\url{https://https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B},
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
