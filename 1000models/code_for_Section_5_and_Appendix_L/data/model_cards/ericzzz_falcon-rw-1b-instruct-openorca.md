
# 🌟 Falcon-RW-1B-Instruct-OpenOrca

Falcon-RW-1B-Instruct-OpenOrca is a 1B parameter, causal decoder-only model based on [Falcon-RW-1B](https://huggingface.co/tiiuae/falcon-rw-1b) and finetuned on the [Open-Orca/SlimOrca](https://huggingface.co/datasets/Open-Orca/SlimOrca) dataset.

**✨Check out our new conversational model [Falcon-RW-1B-Chat](https://huggingface.co/ericzzz/falcon-rw-1b-chat)!✨**

**📊 Evaluation Results**

Falcon-RW-1B-Instruct-OpenOrca was the #1 ranking model (unfortunately not anymore) on [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) in ~1.5B parameters category! A detailed result can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ericzzz__falcon-rw-1b-instruct-openorca).

| Metric     | falcon-rw-1b-instruct-openorca | falcon-rw-1b |
|------------|-------------------------------:|-------------:|
| ARC        |                          34.56 |        35.07 |
| HellaSwag  |                          60.93 |        63.56 |
| MMLU       |                          28.77 |        25.28 |
| TruthfulQA |                          37.42 |        35.96 |
| Winogrande |                          60.69 |        62.04 |
| GSM8K      |                           3.41 |         0.53 |
| **Average**|                      **37.63** |    **37.07** |

**🚀 Motivations**
1. To create a smaller, open-source, instruction-finetuned, ready-to-use model accessible for users with limited computational resources (lower-end consumer GPUs).
2. To harness the strength of Falcon-RW-1B, a competitive model in its own right, and enhance its capabilities with instruction finetuning.

## 📖 How to Use

The model operates with a structured prompt format, incorporating `<SYS>`, `<INST>`, and `<RESP>` tags to demarcate different parts of the input. The system message and instruction are placed within these tags, with the `<RESP>` tag triggering the model's response.

**📝 Example Code**

 ```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = 'ericzzz/falcon-rw-1b-instruct-openorca'

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    'text-generation',
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    device_map='auto',
)

system_message = 'You are a helpful assistant. Give short answers.'
instruction = 'What is AI? Give some examples.'
prompt = f'<SYS> {system_message} <INST> {instruction} <RESP> '

response = pipeline(
    prompt, 
    max_length=200,
    repetition_penalty=1.05
)

print(response[0]['generated_text'])
# AI, or Artificial Intelligence, refers to the ability of machines and software to perform tasks that require human intelligence, such as learning, reasoning, and problem-solving. It can be used in various fields like computer science, engineering, medicine, and more. Some common applications include image recognition, speech translation, and natural language processing.
```

## ⚠️ Limitations
This model may generate inaccurate or misleading information and is prone to hallucination, creating plausible but false narratives. It lacks the ability to discern factual content from fiction and may inadvertently produce biased, harmful or offensive content. Its understanding of complex, nuanced queries is limited. Users should be aware of this and verify any information obtained from the model.

The model is provided 'as is' without any warranties, and the creators are not liable for any damages arising from its use. Users are responsible for their interactions with the model.

## 📬 Contact
For further inquiries or feedback, please contact at eric.fu96@aol.com.

## [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ericzzz__falcon-rw-1b-instruct-openorca)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |37.63|
|AI2 Reasoning Challenge (25-Shot)|34.56|
|HellaSwag (10-Shot)              |60.93|
|MMLU (5-Shot)                    |28.77|
|TruthfulQA (0-shot)              |37.42|
|Winogrande (5-shot)              |60.69|
|GSM8k (5-shot)                   | 3.41|

