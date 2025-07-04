

# Llama-2-7b-hf_open-platypus


**llama-2-7b-hf_open-platypus** is an instruction fine-tuned model based on the LLaMA2-7B transformer architecture.


### Benchmark Metrics


| Metric                | llama-2-7b-hf_open-platypus | garage-bAInd/Platypus2-7B| meta-llama/Llama-2-7b-hf  (base) |
|-----------------------|-------|-------|-------|
| Avg.                  | 54.35|**56.13** | 54.32 |
| ARC (25-shot)         | 51.45 |**55.2**| 53.07 |
| HellaSwag (10-shot)   | 78.63 |**78.84**| 78.59 |
| MMLU (5-shot)         | 43.6 |**49.83**| 46.87 |
| TruthfulQA (0-shot)   | **43.71** |40.64| 38.76 |


We use state-of-the-art [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) to run the benchmark tests above, using the same version as the HuggingFace LLM Leaderboard. Please see below for detailed instructions on reproducing benchmark results.

### Model Details

* **Trained by**: Luiz G A Alves
* **Model type:**  **llama-2-7b-hf_open-platypus** is an auto-regressive language model based on the LLaMA2 transformer architecture.
* **Language(s)**: English

### How to use:

```python
# Use a pipeline as a high-level helper
>>> from transformers import pipeline
>>> pipe = pipeline("text-generation", model="lgaalves/llama-2-7b-hf_open-platypus")
>>> question = "What is a large language model?"
>>> answer = pipe(question)
>>> print(answer[0]['generated_text'])

```

or, you can load the model direclty using:

```python
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("lgaalves/llama-2-7b-hf_open-platypus")
model = AutoModelForCausalLM.from_pretrained("lgaalves/llama-2-7b-hf_open-platypus")
```

### Training Dataset

`lgaalves/llama-2-7b-hf_open-platypus` trained using STEM and logic based dataset [`garage-bAInd/Open-Platypus`](https://huggingface.co/datasets/garage-bAInd/Open-Platypus).


### Training Procedure

`lgaalves/llama-2-7b-hf_open-platypus` was instruction fine-tuned using LoRA on 1 Tesla V100-SXM2-16GB. 


### Limitations and bias

Llama 2 and fine-tuned variants are a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2 and any fine-tuned varient's potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2 variants, developers should perform safety testing and tuning tailored to their specific applications of the model.

Please see the Responsible Use Guide available at https://ai.meta.com/llama/responsible-use-guide/
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_lgaalves__llama-2-7b-hf_open-platypus)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 43.49   |
| ARC (25-shot)         | 51.45          |
| HellaSwag (10-shot)   | 78.63    |
| MMLU (5-shot)         | 43.6         |
| TruthfulQA (0-shot)   | 43.71   |
| Winogrande (5-shot)   | 74.43   |
| GSM8K (5-shot)        | 6.6        |
| DROP (3-shot)         | 5.99         |
