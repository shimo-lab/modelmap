
> Update @ 2024.01.29 New Model [beomi/Yi-Ko-DUS-9B](https://huggingface.co/beomi/Yi-Ko-DUS-9B) Released! 🎉

> Update @ 2023.12.03 Yi-Ko(KoEN)-6B Achieved #1🥇 Pretrained Models at [Open Korean LLM Leaderboard](https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard)! 🎉

> Update @ 2023.12.01 Alpha Release of Yi-Ko(KoEN)-6B model 🎉

# **beomi/Yi-Ko-6B**

Yi-Ko series models serve as advanced iterations of 01-ai/Yi models, 
benefiting from an expanded vocabulary and the inclusion of Korean/English corpus in its further pretraining. 
Just like its predecessor, Yi-Ko series models operate within the broad range of generative text models that stretch from 6 billion to 34 billion parameters.
This repository focuses on the **6B** pretrained version,
which is tailored to fit the Hugging Face Transformers format. 
For access to the other models, feel free to consult the index provided below.

## Model Details

**Model Developers** Junbum Lee (Beomi)

**Variations** Yi-Ko series will come in a range of parameter sizes — 6B and 34B variations.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture** 

Yi-Ko series models are an auto-regressive language model that uses an optimized transformer architecture based on Llama-2*.

<small>*Yi model architecture is based on Llama2, so it can be loaded via `LlamaForCausalLM` class on HF.</small>

|Model Name|Training Data|Params|Context Length|GQA|Trained Tokens|LR|Batch Size(per step)|
|---|---|---|---|---|---|---|---|
|Yi-Ko-6B|*A mix of Korean + English online data*|6B|4k|O|>60B|5e<sup>-5</sup>|2048|

**Vocab Expansion**

| Model Name | Vocabulary Size | Description | 
| --- | --- | --- |
| Original Yi-Series | 64000 | Sentencepiece BPE |
| **Expanded Yi-Ko Series** | 78464 | Sentencepiece BPE. Added Korean vocab and merges |

**Tokenizing "안녕하세요, 오늘은 날씨가 좋네요.ㅎㅎ"**

| Model | # of tokens | Tokens |
| --- | --- | --- |
| Original Yi-Series | 47 | `['<0xEC>', '<0x95>', '<0x88>', '<0xEB>', '<0x85>', '<0x95>', '하', '<0xEC>', '<0x84>', '<0xB8>', '<0xEC>', '<0x9A>', '<0x94>', ',', '▁', '<0xEC>', '<0x98>', '<0xA4>', '<0xEB>', '<0x8A>', '<0x98>', '은', '▁', '<0xEB>', '<0x82>', '<0xA0>', '<0xEC>', '<0x94>', '<0xA8>', '가', '▁', '<0xEC>', '<0xA2>', '<0x8B>', '<0xEB>', '<0x84>', '<0xA4>', '<0xEC>', '<0x9A>', '<0x94>', '.', '<0xE3>', '<0x85>', '<0x8E>', '<0xE3>', '<0x85>', '<0x8E>']` |
| **Expanded Yi-Ko Series** | 10 | `['▁안녕', '하세요', ',', '▁오늘은', '▁날', '씨가', '▁좋네요', '.', 'ㅎ', 'ㅎ']` |
|<small>*Equal Korean vocab with Llama-2-Ko Series</small>||

**Tokenizing "Llama 2: Open Foundation and Fine-Tuned Chat Models"**

| Model | # of tokens | Tokens |
| --- | --- | --- |
| Original Yi-Series | 21 | `['The', '▁Y', 'i', '▁series', '▁models', '▁are', '▁large', '▁language', '▁models', '▁trained', '▁from', '▁scratch', '▁by', '▁developers', '▁at', '▁', '0', '1', '.', 'AI', '.']` |
| **Expanded Yi-Ko Series** | 21 | `['▁The', '▁Y', 'i', '▁series', '▁models', '▁are', '▁large', '▁language', '▁models', '▁trained', '▁from', '▁scratch', '▁by', '▁developers', '▁at', '▁', '0', '1', '.', 'AI', '.']` |
|<small>*Equal Korean vocab with Llama-2-Ko Series</small>| | <small>*Since **Expanded Yi-Ko Series** prepends `_` at the beginning of the text(to ensure same tokenization for Korean sentences), it shows negilible difference for the first token on English tokenization. </small>|

# **Model Benchmark**

## LM Eval Harness - Korean (polyglot branch)

| beomi/Yi-Ko-6B                   |        0 |        5 |       10 |       50 |
|:---------------------------------|---------:|---------:|---------:|---------:|
| kobest_boolq (macro_f1)          | 0.705806 | 0.79905  | 0.814299 | 0.81704  |
| kobest_copa (macro_f1)           | 0.775604 | 0.808899 | 0.816866 | 0.842943 |
| kobest_hellaswag (macro_f1)      | 0.500876 | 0.498673 | 0.493507 | 0.492183 |
| kobest_sentineg (macro_f1)       | 0.404371 | 0.967254 | 0.982368 | 0.974811 |
| kohatespeech (macro_f1)          | 0.353428 | 0.351804 | 0.402423 | 0.503764 |
| kohatespeech_apeach (macro_f1)   | 0.337667 | 0.498679 | 0.471962 | 0.608401 |
| kohatespeech_gen_bias (macro_f1) | 0.124535 | 0.484745 | 0.474475 | 0.461714 |
| korunsmile (f1)                  | 0.382804 | 0.349344 | 0.391383 | 0.432875 |
| nsmc (acc)                       | 0.55064  | 0.8801   | 0.89866  | 0.9071   |
| pawsx_ko (acc)                   | 0.5145   | 0.54     | 0.538    | 0.5165   |

## LICENSE

Apache 2.0 (for research)

> For commercial purpose,
> mailto: jun@beomi.net to acquire Yi-Ko sereis commercial license.

## Citation

Please use this bibtex below:

```
@misc {lee_junbum_2024,
	author       = { {Lee Junbum} },
	title        = { Yi-Ko-6B (Revision 205083a) },
	year         = 2024,
	url          = { https://huggingface.co/beomi/Yi-Ko-6B },
	doi          = { 10.57967/hf/1708 },
	publisher    = { Hugging Face }
}
```

## Acknowledgement

The training is supported by [TPU Research Cloud](https://sites.research.google/trc/) program.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_beomi__Yi-Ko-6B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |50.27|
|AI2 Reasoning Challenge (25-Shot)|48.89|
|HellaSwag (10-Shot)              |74.48|
|MMLU (5-Shot)                    |55.72|
|TruthfulQA (0-shot)              |37.09|
|Winogrande (5-shot)              |72.93|
|GSM8k (5-shot)                   |12.51|

