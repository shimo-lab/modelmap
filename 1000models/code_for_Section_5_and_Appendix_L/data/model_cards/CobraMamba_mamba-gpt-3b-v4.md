# Model Card

**One of the Best 3B Model! Surpassing dolly-v2-12b in the Open LLM Leaderboard!**

One of the best 3B model on the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard), with performance surpassing dolly-v2-12b!

| Metric                | Value |
|-----------------------|-------|
| MMLU (5-shot)         | 30.0  |
| ARC (25-shot)         | 42.6  |
| HellaSwag (10-shot)   | 71.0  |
| TruthfulQA (0-shot)   | 37.3  |
| Avg.                  | 45.2  |

We used the SOTA(State Of The Art) [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) to run the benchmark tests above.


The following is the performance under 0-shot testing, mostly better than acrastt/Marx-3B-V2


hf-causal (pretrained=CobraMamba/mamba-gpt-3b-v4), limit: None, provide_description: False, num_fewshot: 0, batch_size: None


The training code and data will be open sourced later on Github(https://github.com/chi2liu/mamba-gpt-3b).


## Training Dataset

` mamba-gpt-3b-v4 ` is trained on multiple datasets:
  - [Stanford Alpaca (en)](https://github.com/tatsu-lab/stanford_alpaca)
  - [Open Assistant (multilingual)](https://huggingface.co/datasets/OpenAssistant/oasst1)
  - [LIMA (en)](https://huggingface.co/datasets/GAIR/lima)
  - [CodeAlpaca 20k (en)](https://huggingface.co/datasets/sahil2801/CodeAlpaca-20k)
  - [GPT-4 Generated Data (en&zh)](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)
  - [UltraChat (en)](https://github.com/thunlp/UltraChat)


## Summary

We have fine-tuned the OpenLLaMA model and surpassed the original model in multiple evaluation subtasks, making it currently one of the best performing 3B model, with comparable performance to llama-7b.
- Base model: [openlm-research/open_llama_3b_v2](https://huggingface.co/openlm-research/open_llama_3b_v2)


## Usage

To use the model with the `transformers` library on a machine with GPU(s), first make sure you have the `transformers`, `accelerate` and `torch` libraries installed.

```bash
pip install transformers==4.29.2
pip install accelerate==0.19.0
pip install torch==2.0.0
```

Then, run the following Python snippet:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("CobraMamba/mamba-gpt-3b-v4")
model = AutoModelForCausalLM.from_pretrained("CobraMamba/mamba-gpt-3b-v4", trust_remote_code=True, torch_dtype=torch.float16)

# we use alpaca prompt
input_content = "Your text here"
input_ids = tokenizer.encode(input_content, return_tensors="pt")
output = model.generate(input_ids, max_length=128, temperature=0.7)
output_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(output_text)

```


## Citation

If this work is helpful, please kindly cite as:

```bibtex
@Misc{mamba-gpt-3b-v4,
  title = {Mamba-GPT-3b-v4},
  author = {chiliu},
  howpublished = {\url{https://huggingface.co/CobraMamba/mamba-gpt-3b-v4}},
  year = {2023}
}
```


## Disclaimer

Please read this disclaimer carefully before using the large language model provided in this repository. Your use of the model signifies your agreement to the following terms and conditions.

- Biases and Offensiveness: The large language model is trained on a diverse range of internet text data, which may contain biased, racist, offensive, or otherwise inappropriate content. By using this model, you acknowledge and accept that the generated content may sometimes exhibit biases or produce content that is offensive or inappropriate. The developers of this repository do not endorse, support, or promote any such content or viewpoints.
- Limitations: The large language model is an AI-based tool and not a human. It may produce incorrect, nonsensical, or irrelevant responses. It is the user's responsibility to critically evaluate the generated content and use it at their discretion.
- Use at Your Own Risk: Users of this large language model must assume full responsibility for any consequences that may arise from their use of the tool. The developers and contributors of this repository shall not be held liable for any damages, losses, or harm resulting from the use or misuse of the provided model.
