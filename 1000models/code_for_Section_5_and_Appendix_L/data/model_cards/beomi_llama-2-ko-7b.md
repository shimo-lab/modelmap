
**Update Log**

- 2023.12.27
  - New Model is here! Trained with only open-accessible Korean text corpus: https://huggingface.co/beomi/open-llama-2-ko-7b
- 2023.10.19
  - Fix Tokenizer bug(space not applied when decoding) after `transforemrs>=4.34.0`


# **Llama-2-Ko** 🦙🇰🇷

Llama-2-Ko serves as an advanced iteration of Llama 2, benefiting from an expanded vocabulary and the inclusion of a Korean corpus in its further pretraining. Just like its predecessor, Llama-2-Ko operates within the broad range of generative text models that stretch from 7 billion to 70 billion parameters. This repository focuses on the 7B pretrained version, which is tailored to fit the Hugging Face Transformers format. For access to the other models, feel free to consult the index provided below.

## Model Details

**Model Developers** Junbum Lee (Beomi)

**Variations** Llama-2-Ko will come in a range of parameter sizes — 7B, 13B, and 70B — as well as pretrained and fine-tuned variations.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture** 

Llama-2-Ko is an auto-regressive language model that uses an optimized transformer architecture based on Llama-2.

||Training Data|Params|Content Length|GQA|Tokens|LR|
|---|---|---|---|---|---|---|
|Llama 2|*A new mix of Korean online data*|7B|4k|&#10007;|>40B*|1e<sup>-5</sup>|
*Plan to train upto 200B tokens

**Vocab Expansion**

| Model Name | Vocabulary Size | Description | 
| --- | --- | --- |
| Original Llama-2 | 32000 | Sentencepiece BPE |
| **Expanded Llama-2-Ko** | 46336 | Sentencepiece BPE. Added Korean vocab and merges |

**Tokenizing "안녕하세요, 오늘은 날씨가 좋네요."**

| Model | Tokens |
| --- | --- |
| Llama-2 | `['▁', '안', '<0xEB>', '<0x85>', '<0x95>', '하', '세', '요', ',', '▁', '오', '<0xEB>', '<0x8A>', '<0x98>', '은', '▁', '<0xEB>', '<0x82>', '<0xA0>', '씨', '가', '▁', '<0xEC>', '<0xA2>', '<0x8B>', '<0xEB>', '<0x84>', '<0xA4>', '요']` |
| Llama-2-Ko | `['▁안녕', '하세요', ',', '▁오늘은', '▁날', '씨가', '▁좋네요']` |

**Tokenizing "Llama 2: Open Foundation and Fine-Tuned Chat Models"**

| Model | Tokens |
| --- | --- |
| Llama-2 | `['▁L', 'l', 'ama', '▁', '2', ':', '▁Open', '▁Foundation', '▁and', '▁Fine', '-', 'T', 'un', 'ed', '▁Ch', 'at', '▁Mod', 'els']` |
| Llama-2-Ko | `['▁L', 'l', 'ama', '▁', '2', ':', '▁Open', '▁Foundation', '▁and', '▁Fine', '-', 'T', 'un', 'ed', '▁Ch', 'at', '▁Mod', 'els']` |

# **Model Benchmark**

## LM Eval Harness - Korean (polyglot branch)

- Used EleutherAI's lm-evaluation-harness https://github.com/EleutherAI/lm-evaluation-harness/tree/polyglot

### NSMC (Acc) -  50000 full test

TBD

### COPA (F1)

<img src=https://user-images.githubusercontent.com/11323660/255575809-c037bc6e-0566-436a-a6c1-2329ac92187a.png style="max-width: 700px; width: 100%" />

| Model | 0-shot | 5-shot | 10-shot | 50-shot |
| --- | --- | --- | --- | --- |
| https://huggingface.co/skt/ko-gpt-trinity-1.2B-v0.5 | 0.6696 | 0.6477 | 0.6419 | 0.6514 |
| https://huggingface.co/kakaobrain/kogpt | 0.7345 | 0.7287 | 0.7277 | 0.7479 |
| https://huggingface.co/facebook/xglm-7.5B | 0.6723 | 0.6731 | 0.6769 | 0.7119 |
| https://huggingface.co/EleutherAI/polyglot-ko-1.3b | 0.7196 | 0.7193 | 0.7204 | 0.7206 |
| https://huggingface.co/EleutherAI/polyglot-ko-3.8b | 0.7595 | 0.7608 | 0.7638 | 0.7788 |
| https://huggingface.co/EleutherAI/polyglot-ko-5.8b | 0.7745 | 0.7676 | 0.7775 | 0.7887 |
| https://huggingface.co/EleutherAI/polyglot-ko-12.8b | 0.7937 | 0.8108 | 0.8037 | 0.8369 |
| Llama-2 Original 7B* | 0.562033 | 0.575982 | 0.576216 | 0.595532 |
| Llama-2-Ko-7b 20B (10k) | 0.738780 | 0.762639 | 0.780761 | 0.797863 |
| Llama-2-Ko-7b 40B (20k) | 0.743630 | 0.792716 | 0.803746 | 0.825944 |
*Llama-2 Original 7B used https://huggingface.co/meta-llama/Llama-2-7b-hf (w/o tokenizer updated)

### HellaSwag (F1)

<img src=https://user-images.githubusercontent.com/11323660/255576090-a2bfc1ae-d117-44b7-9f7b-262e41179ec1.png style="max-width: 700px; width: 100%" />

| Model | 0-shot | 5-shot | 10-shot | 50-shot |
| --- | --- | --- | --- | --- |
| https://huggingface.co/skt/ko-gpt-trinity-1.2B-v0.5 | 0.5243 | 0.5272 | 0.5166 | 0.5352 |
| https://huggingface.co/kakaobrain/kogpt | 0.5590 | 0.5833 | 0.5828 | 0.5907 |
| https://huggingface.co/facebook/xglm-7.5B | 0.5665 | 0.5689 | 0.5565 | 0.5622 |
| https://huggingface.co/EleutherAI/polyglot-ko-1.3b | 0.5247 | 0.5260 | 0.5278 | 0.5427 |
| https://huggingface.co/EleutherAI/polyglot-ko-3.8b | 0.5707 | 0.5830 | 0.5670 | 0.5787 |
| https://huggingface.co/EleutherAI/polyglot-ko-5.8b | 0.5976 | 0.5998 | 0.5979 | 0.6208 |
| https://huggingface.co/EleutherAI/polyglot-ko-12.8b | 0.5954 | 0.6306 | 0.6098 | 0.6118 |
| Llama-2 Original 7B* | 0.415390 | 0.431382 | 0.421342 | 0.442003 |
| Llama-2-Ko-7b 20B (10k) | 0.451757 | 0.466751 | 0.472607 | 0.482776 |
| Llama-2-Ko-7b 40B (20k) | 0.456246 | 0.465665 | 0.469810 | 0.477374 |
*Llama-2 Original 7B used https://huggingface.co/meta-llama/Llama-2-7b-hf (w/o tokenizer updated)

### BoolQ (F1)

<img src=https://user-images.githubusercontent.com/11323660/255576343-5d847a6f-3b6a-41a7-af37-0f11940a5ea4.png style="max-width: 700px; width: 100%" />

| Model | 0-shot | 5-shot | 10-shot | 50-shot |
| --- | --- | --- | --- | --- |
| https://huggingface.co/skt/ko-gpt-trinity-1.2B-v0.5 | 0.3356 | 0.4014 | 0.3640 | 0.3560 |
| https://huggingface.co/kakaobrain/kogpt | 0.4514 | 0.5981 | 0.5499 | 0.5202 |
| https://huggingface.co/facebook/xglm-7.5B | 0.4464 | 0.3324 | 0.3324 | 0.3324 |
| https://huggingface.co/EleutherAI/polyglot-ko-1.3b | 0.3552 | 0.4751 | 0.4109 | 0.4038 |
| https://huggingface.co/EleutherAI/polyglot-ko-3.8b | 0.4320 | 0.5263 | 0.4930 | 0.4038 |
| https://huggingface.co/EleutherAI/polyglot-ko-5.8b | 0.4356 | 0.5698 | 0.5187 | 0.5236 |
| https://huggingface.co/EleutherAI/polyglot-ko-12.8b | 0.4818 | 0.6041 | 0.6289 | 0.6448 |
| Llama-2 Original 7B* | 0.352050 | 0.563238 | 0.474788 | 0.419222 |
| Llama-2-Ko-7b 20B (10k) | 0.360656 | 0.679743 | 0.680109 | 0.662152 |
| Llama-2-Ko-7b 40B (20k) | 0.578640 | 0.697747 | 0.708358 | 0.714423 |
*Llama-2 Original 7B used https://huggingface.co/meta-llama/Llama-2-7b-hf (w/o tokenizer updated)

### SentiNeg (F1)

<img src=https://user-images.githubusercontent.com/11323660/255576572-b005a81d-fa4d-4709-b48a-f0fe4eed17a3.png style="max-width: 700px; width: 100%" />

| Model | 0-shot | 5-shot | 10-shot | 50-shot |
| --- | --- | --- | --- | --- |
| https://huggingface.co/skt/ko-gpt-trinity-1.2B-v0.5 | 0.6065 | 0.6878 | 0.7280 | 0.8413 |
| https://huggingface.co/kakaobrain/kogpt | 0.3747 | 0.8942 | 0.9294 | 0.9698 |
| https://huggingface.co/facebook/xglm-7.5B | 0.3578 | 0.4471 | 0.3964 | 0.5271 |
| https://huggingface.co/EleutherAI/polyglot-ko-1.3b | 0.6790 | 0.6257 | 0.5514 | 0.7851 |
| https://huggingface.co/EleutherAI/polyglot-ko-3.8b | 0.4858 | 0.7950 | 0.7320 | 0.7851 |
| https://huggingface.co/EleutherAI/polyglot-ko-5.8b | 0.3394 | 0.8841 | 0.8808 | 0.9521 |
| https://huggingface.co/EleutherAI/polyglot-ko-12.8b | 0.9117 | 0.9015 | 0.9345 | 0.9723 |
| Llama-2 Original 7B* | 0.347502 | 0.529124 | 0.480641 | 0.788457 |
| Llama-2-Ko-7b 20B (10k) | 0.485546 | 0.829503 | 0.871141 | 0.851253 |
| Llama-2-Ko-7b 40B (20k) | 0.459447 | 0.761079 | 0.727611 | 0.936988 |
*Llama-2 Original 7B used https://huggingface.co/meta-llama/Llama-2-7b-hf (w/o tokenizer updated)


## Note for oobabooga/text-generation-webui

Remove `ValueError` at `load_tokenizer` function(line 109 or near), in `modules/models.py`.

```python
diff --git a/modules/models.py b/modules/models.py
index 232d5fa..de5b7a0 100644
--- a/modules/models.py
+++ b/modules/models.py
@@ -106,7 +106,7 @@ def load_tokenizer(model_name, model):
                 trust_remote_code=shared.args.trust_remote_code,
                 use_fast=False
             )
-        except ValueError:
+        except:
             tokenizer = AutoTokenizer.from_pretrained(
                 path_to_model,
                 trust_remote_code=shared.args.trust_remote_code,
```

Since Llama-2-Ko uses FastTokenizer provided by HF tokenizers NOT sentencepiece package, 
it is required to use `use_fast=True` option when initialize tokenizer.

Apple Sillicon does not support BF16 computing, use CPU instead. (BF16 is supported when using NVIDIA GPU)

## Citation

```
@misc {l._junbum_2023,
	author       = { {L. Junbum} },
	title        = { llama-2-ko-7b (Revision 4a9993e) },
	year         = 2023,
	url          = { https://huggingface.co/beomi/llama-2-ko-7b },
	doi          = { 10.57967/hf/1098 },
	publisher    = { Hugging Face }
}
```

## Acknowledgement

The training is supported by [TPU Research Cloud](https://sites.research.google/trc/) program.


# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_beomi__llama-2-ko-7b)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 39.43   |
| ARC (25-shot)         | 48.46          |
| HellaSwag (10-shot)   | 75.28    |
| MMLU (5-shot)         | 39.56         |
| TruthfulQA (0-shot)   | 34.49   |
| Winogrande (5-shot)   | 72.14   |
| GSM8K (5-shot)        | 1.97        |
| DROP (3-shot)         | 4.1         |
