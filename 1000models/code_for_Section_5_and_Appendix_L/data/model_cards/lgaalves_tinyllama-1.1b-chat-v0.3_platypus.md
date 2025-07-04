


# tinyllama-1.1b-chat-v0.3_platypus

**tinyllama-1.1b-chat-v0.3_platypus** is an instruction fine-tuned model based on the tinyllama transformer architecture.


### Benchmark Metrics

| Metric                |lgaalves/tinyllama-1.1b-chat-v0.3_platypus | tinyllama-1.1b-chat-v0.3 |
|-----------------------|-------|-------|
| Avg.                  | 37.67 | **38.74** |
| ARC (25-shot)         | 30.29 | **35.07** |
| HellaSwag (10-shot)   | 55.12 | **57.7** |
| MMLU (5-shot)         | **26.13** | 25.53 |
| TruthfulQA (0-shot)   | **39.15** | 36.67 |


We use state-of-the-art [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) to run the benchmark tests above, using the same version as the HuggingFace LLM Leaderboard. Please see below for detailed instructions on reproducing benchmark results.

### Model Details

* **Trained by**: Luiz G A Alves
* **Model type:**  **tinyllama-1.1b-chat-v0.3_platypus** is an auto-regressive language model based on the tinyllama transformer architecture.
* **Language(s)**: English

### How to use:

```python
# Use a pipeline as a high-level helper
>>> from transformers import pipeline
>>> pipe = pipeline("text-generation", model="lgaalves/tinyllama-1.1b-chat-v0.3_platypus")
>>> question = "What is a large language model?"
>>> answer = pipe(question)
>>> print(answer[0]['generated_text'])
```

or, you can load the model direclty using:

```python
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("lgaalves/tinyllama-1.1b-chat-v0.3_platypus")
model = AutoModelForCausalLM.from_pretrained("lgaalves/tinyllama-1.1b-chat-v0.3_platypus")
```

### Training Dataset

`lgaalves/tinyllama-1.1b-chat-v0.3_platypus` trained using STEM and logic based dataset [garage-bAInd/Open-Platypus](https://huggingface.co/datasets/garage-bAInd/Open-Platypus).

### Training Procedure

`lgaalves/tinyllama-1.1b-chat-v0.3_platypus` was instruction fine-tuned using LoRA on 1 V100 GPU on Google Colab. It took about 43 minutes to train it.  


# Intended uses, limitations & biases

You can use the raw model for text generation or fine-tune it to a downstream task. The model was not extensively tested and may produce false information. It contains a lot of unfiltered content from the internet, which is far from neutral.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_lgaalves__tinyllama-1.1b-chat-v0.3_platypus)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 30.28   |
| ARC (25-shot)         | 30.29          |
| HellaSwag (10-shot)   | 55.12    |
| MMLU (5-shot)         | 26.13         |
| TruthfulQA (0-shot)   | 39.15   |
| Winogrande (5-shot)   | 55.8   |
| GSM8K (5-shot)        | 0.53        |
| DROP (3-shot)         | 4.94         |
