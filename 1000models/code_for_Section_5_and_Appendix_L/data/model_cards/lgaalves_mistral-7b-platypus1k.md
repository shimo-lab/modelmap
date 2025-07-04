

# mistral-7b-v0.1-platypus1k


**mistral-7b-v0.1-platypus1k** is an instruction fine-tuned model based on the Mistral-7B transformer architecture.


### Benchmark Metrics


| Metric                | mistral-7b-v0.1-platypus1k | mistralai/Mistral-7B-v0.1 |garage-bAInd/Platypus2-7B| 
|-----------------------|-------|-------|-------|
| Avg.                  | **63.66** | 62.4 |56.13| 
| ARC (25-shot)         | **61.60** | 59.98|55.20|
| HellaSwag (10-shot)   | 82.93 |**83.31** |78.84| 
| MMLU (5-shot)         | 63.16 |**64.16** |49.83| 
| TruthfulQA (0-shot)   | **46.96** | 42.15 |40.64|


We use state-of-the-art [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) to run the benchmark tests above, using the same version as the HuggingFace LLM Leaderboard. Please see below for detailed instructions on reproducing benchmark results.

### Model Details

* **Trained by**: Luiz G A Alves
* **Model type:**  **mistral-7b-v0.1-platypus1k** is an auto-regressive language model based on the Mistral-7B transformer architecture.
* **Language(s)**: English

### How to use:

```python
# Use a pipeline as a high-level helper
>>> from transformers import pipeline
>>> pipe = pipeline("text-generation", model="lgaalves/mistral-7b-v0.1-platypus1k")
>>> question = "What is a large language model?"
>>> answer = pipe(question)
>>> print(answer[0]['generated_text'])

```

or, you can load the model direclty using:

```python
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("lgaalves/mistral-7b-v0.1-platypus1k")
model = AutoModelForCausalLM.from_pretrained("lgaalves/mistral-7b-v0.1-platypus1k")
```

### Training Dataset

`lgaalves/mistral-7b-v0.1-platypus1k` trained using STEM and logic based dataset [`garage-bAInd/Open-Platypus`](https://huggingface.co/datasets/garage-bAInd/Open-Platypus).


### Training Procedure

`lgaalves/mistral-7b-v0.1-platypus1k` was instruction fine-tuned using LoRA on 1 Tesla V100-SXM2-16GB. 


### Limitations and bias

Mistral 7B and fine-tuned variants are a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2 and any fine-tuned varient's potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2 variants, developers should perform safety testing and tuning tailored to their specific applications of the model.

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_lgaalves__mistral-7b-platypus1k)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 50.74   |
| ARC (25-shot)         | 61.6          |
| HellaSwag (10-shot)   | 82.93    |
| MMLU (5-shot)         | 63.16         |
| TruthfulQA (0-shot)   | 46.96   |
| Winogrande (5-shot)   | 78.14   |
| GSM8K (5-shot)        | 16.38        |
| DROP (3-shot)         | 5.99         |
