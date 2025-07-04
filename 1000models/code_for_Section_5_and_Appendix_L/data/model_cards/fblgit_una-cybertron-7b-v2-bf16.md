
# Model Card for una-cybertron-7b-v2-bf16 (UNA: Uniform Neural Alignment)

We strike back, introducing **Cybertron 7B v2** a 7B MistralAI based model, best on it's series. Trained on SFT, DPO and UNA (Unified Neural Alignment) on multiple datasets.
He scores [EXACTLY](https://huggingface.co/datasets/open-llm-leaderboard/details_fblgit__una-cybertron-7b-v2-bf16)  **#1** with **69.67**+ score on HF LeaderBoard board, **#8** ALL SIZES top score.

* v1 Scoring **#1** at 2 December 2023 with 69.43 ..few models were releasse .. but only 1 can survive: CYBERTRON!
* v2 Scoring **#1** at 5 December 2023 with 69.67

  
| Model | Average | ARC (25-s) | HellaSwag (10-s) | MMLU (5-s) | TruthfulQA (MC) (0-s) | Winogrande (5-s) | GSM8K (5-s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) | 60.97 | 59.98  | 83.31  | 64.16  | 42.15 | 78.37 | 37.83 |
| [Intel/neural-chat-7b-v3-2](https://huggingface.co/Intel/neural-chat-7b-v3-2) | 68.29 | 67.49  | 83.92  | 63.55  | 59.68 | 79.95 | 55.12 |
| [perlthoughts/Chupacabra-7B-v2](https://huggingface.co/perlthoughts/Chupacabra-7B-v2) | 63.54 | 66.47 | 85.17 | 64.49  | 57.6 | 79.16 | 28.35 |
| [fblgit/una-cybertron-7b-v1-fp16](https://huggingface.co/fblgit/una-cybertron-7b-v1-fp16) | **69.49** | **68.43** | **85.85** | 63.34  | **63.28** | **80.90** | **55.12** |
| [fblgit/una-cybertron-7b-v2-bf16](https://huggingface.co/fblgit/una-cybertron-7b-v2-bf16) | **69.67** | **68.26** | **85.?4** | 63.23  | **64.63** | **81.37** | **55.04** |

The model excels in mathematics, logic, reasoning, overall very smart. He can make a deep reasoning over the context and prompt, it gives the impression of not missing details around.


## Model Details

Adiestrated with UNA: Uniform Neural Alignment technique (paper going out soon). 
* What is **NOT** UNA? Its not a merged layers model. Is not SLERP or SLURP or similar.
* What **is** UNA? A formula & A technique to *TAME* models
* When will be released the code and paper? When have time, contribute and it'll be faster.

### Model Description

- **Developed by:** [juanako.ai](https://juanako.ai)
- **Author:** [Xavier M.](xavi@juanako.ai)
- **Investors** [CONTACT HERE](billing@juanako.ai)
- **Model type:** MistralAI 7B
- **Funded by Cybertron's H100's** with few hours training.

### Prompt
The model is very good, works well on almost any prompt but ChatML format and Alpaca System gets the best
```
<|im_start|>system
- You are a helpful assistant chatbot trained by MosaicML.
- You answer questions.
- You are excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.
- You are more than just an information source, you are also able to write poetry, short stories, and make jokes.<|im_end|>
<|im_start|>user
Explain QKV<|im_end|>
<|im_start|>assistant
```
```
### Assistant: I am StableVicuna, a large language model created by CarperAI. I am here to chat!

### Human: Explain QKV
### Assistant:
```
```
[Round <|round|>]
问：Explain QKV
答：
```
```
[Round <|round|>]
Question：Explain QKV
Answer：
```
```
Question：Explain QKV
Answer：
```
Using Exllamav2_HF set alpha=2.5 for 16K Context

**Users also report that exllamav2_HF loader, 8bpw-h8 exl2 quant, simple-1 preset provides good results**


### Framework versions

- Transformers 4.35.0-UNA
- Pytorch 2.1.0
- Datasets 2.14.6
- Tokenizers 0.14.1

### Citations
    If you find Cybertron, Juanako or any of our models useful, specially if you use it for your big brand.. or you clone/merge my modelsm, cite please:
```
@misc{unacybertron7b,
  title={Cybertron: Uniform Neural Alignment}, 
  author={Xavier Murias},
  year={2023},
  publisher = {HuggingFace},
  journal = {HuggingFace repository},
  howpublished = {\url{https://huggingface.co/fblgit/una-cybertron-7b-v2-bf16}},
}
```

Special thanks to @TheBloke & @bartowski for converting the models and their support to the community. Thank you!
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_fblgit__una-cybertron-7b-v2-bf16)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |69.67|
|AI2 Reasoning Challenge (25-Shot)|68.26|
|HellaSwag (10-Shot)              |85.85|
|MMLU (5-Shot)                    |63.23|
|TruthfulQA (0-shot)              |64.63|
|Winogrande (5-shot)              |80.98|
|GSM8k (5-shot)                   |55.04|

