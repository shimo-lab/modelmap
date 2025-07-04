It remain factual and reliable even in dramatic situations.

---

### Model Card for kevin009/llamaRAGdrama

#### Model Details
- **Model Name:** kevin009/llamaRAGdrama
- **Model Type:** Fine-tuned for Q&A, RAG.
- **Fine-tuning Objective:** Synthesis text content in Q&A, RAG scenarios.

#### Intended Use
- **Applications:** RAG, Q&A

#### Training Data
- **Sources:** Includes a diverse dataset of dramatic texts, enriched with factual databases and reliable sources to train the model on generating content that remains true to real-world facts.
- **Preprocessing:** In addition to removing non-content text, data was annotated to distinguish between purely creative elements and those that require factual accuracy, ensuring a balanced training approach.

#### How to Use
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("kevin009/llamaRAGdrama")
model = AutoModelForCausalLM.from_pretrained("kevin009/llamaRAGdrama")

input_text = "Enter your prompt here"
input_tokens = tokenizer.encode(input_text, return_tensors='pt')
output_tokens = model.generate(input_tokens, max_length=100, num_return_sequences=1, temperature=0.9)
generated_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

print(generated_text)
```
Replace `"Enter your prompt here"` with your starting text. Adjust `temperature` for creativity level.

#### Limitations and Biases
- **Content Limitation:** While designed to be truthful, It may not be considered safe.
- **Biases:** It may remain biases and inaccurate.

#### Licensing and Attribution
- **License:** Apache-2.0
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_kevin009__llamaRAGdrama)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |74.65|
|AI2 Reasoning Challenge (25-Shot)|72.01|
|HellaSwag (10-Shot)              |88.83|
|MMLU (5-Shot)                    |64.50|
|TruthfulQA (0-shot)              |70.24|
|Winogrande (5-shot)              |86.66|
|GSM8k (5-shot)                   |65.66|

