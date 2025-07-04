# 🌟 Falcon-RW-1B-Chat

**Falcon-RW-1B-Chat is a conversational model with 1 billion parameters.** It's a further refinement of the [Falcon-RW-1B-Instruct-OpenOrca](https://huggingface.co/ericzzz/falcon-rw-1b-instruct-openorca), trained on selected data from the [HuggingFaceH4/ultrachat_200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) and [openchat/openchat_sharegpt4_dataset](https://huggingface.co/datasets/openchat/openchat_sharegpt4_dataset) datasets.

**✨Try it out at our [Tiny Chat](https://huggingface.co/spaces/ericzzz/tiny-chat) space running on free-tier hardware!✨**

The underlying Falcon-RW-1B-Instruct-OpenOrca model is built on the [Falcon-RW-1B](https://huggingface.co/tiiuae/falcon-rw-1b), a causal decoder-only model. It has been instruction-finetuned using the [Open-Orca/SlimOrca](https://huggingface.co/datasets/Open-Orca/SlimOrca) dataset.

**🎯 Purpose**

The Falcon-RW-1B-Chat aims to add conversational capabilities to the Falcon-RW-1B-Instruct-OpenOrca model. This initiative is driven by the need for a smaller, open-source, instruction-finetuned, ready-to-use model, suitable for users with limited computational resources, like lower-end consumer GPUs.

## [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ericzzz__falcon-rw-1b-chat)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |37.37|
|AI2 Reasoning Challenge (25-Shot)|35.58|
|HellaSwag (10-Shot)              |61.12|
|MMLU (5-Shot)                    |24.51|
|TruthfulQA (0-shot)              |39.62|
|Winogrande (5-shot)              |61.72|
|GSM8k (5-shot)                   | 1.67|

## 📖 Example Code

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "ericzzz/falcon-rw-1b-chat"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, device_map="auto", torch_dtype=torch.bfloat16
)

chat_history = [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hello! How can I assist you today?"},
    {"role": "user", "content": "Explain what AI is."},
]

input_ids = tokenizer.apply_chat_template(
    chat_history, tokenize=True, add_generation_prompt=True, return_tensors="pt"
).to(model.device)
output_tokens = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.7,
    repetition_penalty=1.05,
    max_new_tokens=200,
)
output_text = tokenizer.decode(
    output_tokens[0][len(input_ids[0]) :], skip_special_tokens=True
)

print(output_text)
```

## ⚠️ Limitations

This model may generate inaccurate or misleading information and is prone to hallucination, creating plausible but false narratives. It lacks the ability to discern factual content from fiction and may inadvertently produce biased, harmful or offensive content. Its understanding of complex, nuanced queries is limited. Users should be aware of this and verify any information obtained from the model.

The model is provided 'as is' without any warranties, and the creators are not liable for any damages arising from its use. Users are responsible for their interactions with the model.

## 📬 Contact

For further inquiries or feedback, please contact at eric.fu96@aol.com.

