
# FinanceConnect

FinanceConnect is a state-of-the-art, open-source chat model tailored for finance and economic discussions. Built on the robust Llama2-13B architecture, this model has been fine-tuned on a combination of FinTalk-19k and Alpaca datasets, making it a valuable resource for finance professionals, researchers, and enthusiasts.

## Model Details

- Architecture: Llama2-13B
- Training Dataset: [FinTalk-19k](https://huggingface.co/datasets/ceadar-ie/FinTalk-19k), [Alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca)

## Dataset Utilized: FinTalk-19k and Alpaca

Drawing strength from the FinTalk-19k and Alpaca dataset, a curated collection focused on financial knowledge, this model provides insights and information related to the finance industry. For a deeper dive into the dataset, visit: [FinTalk-19k](https://huggingface.co/datasets/ceadar-ie/FinTalk-19k), [Alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca)

## Model Specification

- **Developed by:** CeADAR Connect Group
- **Model type:** Large Language Model
- **Language(s):** en
- **Finetuned from model:** Llama2-13B

## Key Features and Functionalities

- **Domain Specialization:** The FinanceConnect model is specialized in Finance conversations, serving as a resource for financial researchers, and enthusiasts.
- **Model API Accessibility:** Offers a straightforward Python integration for generating financial content insights.
- **Performance Optimisation:** Efficient performance across both CPU and GPU platforms.
- **Data Representation:** Utilises a combination of comprehensive Finance dataset, enabling content generation to professional standards.

## Benchmarks
| **Benchmark** | **BloombergGPT 50B** | **FinanceConnect 13B** |
|--------------|--------------|--------------|
| MMLU | 39.8 | 52.08 |
| FPB | 51.1 | 57.2 |
| **Cost**| **$2.67 Million** | **$27** |

| **Benchmark** | **FinanceConnect 13B** |
|--------------|--------------
| MMLU | 52.08 |
| ARC | 55.12 |
| HellaSwag | 77.73 |
| TruthfulQA | 38.80 |
| Winogrande | 71.82 |
| GSM8K | 1.6 |

## Model Usage
Experience the capabilities of the FinanceConnect model through a well-structured Python interface. To kick-start your exploration, follow the steps and snippets given below:

### Prerequisites
#### 1. Ensure required packages are available

```python
import torch
from typing import Any, Dict
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    PreTrainedTokenizerFast,
    pipeline,
    logging,
)
import time
```

#### 2. Initiate the model and tokenizer

```python
model_name = "ceadar-ie/FinanceConnect-13B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, load_in_8bit = True, device_map = "auto", trust_remote_code=True)
```

#### 3. Create a function for generating text

```python
def generate_text(input_text):
    tokenizer.padding_side = "right"
    num_words_input = len(input_text.split())

    start_time = time.time()
    
    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length = 1000)
    prompt = f"<s>[INST] {input_text} [/INST]"
    #prompt = input_text
    result = pipe(prompt)
    generated_text = result[0]['generated_text'].replace(prompt, "").strip()

    end_time = time.time()
    time_taken = end_time - start_time

    num_words_generated = len(generated_text.split())

    print("Generated Output:")
    print(generated_text)
    print('=' * 60 )
    print("\nNumber of Words in Input Text:", num_words_input)
    print("Number of Words in Generated Output:", num_words_generated)
    print("Time Taken to Generate Output: {:.2f} seconds".format(time_taken))
```

## Example Evaluation and Use
### Example Prompt 1:
List in detail ten key factors influencing the current state of the global economy.

### Generated Output:
The current state of the global economy is influenced by several factors, including:

1. Globalization: The increasing interconnectedness of economies through trade, investment, and the movement of people.
2. Technological advancements: The rapid pace of technological innovation and its impact on industries and jobs.
3. Political factors: Government policies and decisions that affect economic growth and stability.
4. Demographics: Changes in population demographics, such as aging populations and youth bulges, can impact economic growth and stability.
5. Environmental factors: Climate change, natural disasters, and other environmental factors can disrupt economic activity and impact growth.
6. International trade: The rise of protectionism and trade tensions between countries can impact economic growth and stability.
7. Financial factors: The performance of financial markets and the availability of credit can impact economic growth and stability.
8. Infrastructure: The availability and quality of infrastructure, such as transportation and communication networks, can impact economic growth and stability.
9. Education: The availability and quality of education can impact economic growth and stability by influencing the supply of skilled workers and the ability of countries to adapt to changing economic conditions.
10. Health: The availability and quality of healthcare can impact economic growth and stability by influencing the productivity of the workforce and the ability of countries to attract and retain talent.

### Example Prompt 2:
Explain the concept of quantitative easing and its impact on financial markets.

### Generated Output:
Quantitative easing is a monetary policy tool used by central banks to stimulate economic growth and combat inflation. It involves the purchase of assets such as government bonds, mortgage-backed securities, and corporate bonds by a central bank. This increases the amount of money in circulation, lowers interest rates, and encourages banks to lend more, which can boost economic growth. However, quantitative easing can also lead to inflation if it is not implemented carefully, as it can cause prices to rise more than wages can keep up with.

### Example Prompt 3:
I've recently started working and want to manage my finances. Give me a detailed answer in 10 points on how do I set up a budget?

### Generated Output:
Setting up a budget can help manage finances and save money. Here are some tips:

1. Determine your income and expenses.
2. Create a budget that includes all necessary expenses, such as rent, utilities, and groceries.
3. Set aside a portion of your income for savings and investments.
4. Monitor your spending regularly and adjust your budget as needed.
5. Use cash or debit cards instead of credit cards to avoid overspending.
6. Cut back on unnecessary expenses, such as eating out or subscriptions.
7. Consider using a budgeting app or tool to help track your spending.
8. Prioritize your spending based on your financial goals.
9. Review your budget regularly and make adjustments as needed.
10. Be flexible and willing to make changes to your budget as your financial situation changes.

## Training Details
### Training Hyperparameters
- per_device_train_batch_size = 10
- gradient_accumulation_steps = 4
- optim = "paged_adamw_32bit"
- learning_rate = 2e-4
- max_grad_norm = 0.3
- warmup_ratio = 0.03

## Licensing
The FinanceConnect model, developed by CeADAR Connect Group, combines the licensing frameworks of Llama2, FinTalk-8k and Alpaca. Under Meta's terms, users are granted a non-exclusive, worldwide, non-transferable, royalty-free limited license for the use and modification of Llama Materials, inclusive of the Llama2 model and its associated documentation. When redistributing, the provided Agreement and a specific attribution notice must be included. Further, in alignment with the FinTalk dataset's(Apache 2.0) licensing and Alpaca dataset's(cc-by-nc-4.0) licensing, the model is distributed under the umbrella of all three licenses.

## Model Limitations
### Out-of-Scope Use
FinanceConnect is specifically tailored for finanical discussions and knowledge. It is not optimized for:
- General conversations.
- Domain-specific tasks outside financial tasks.
- Direct interfacing with physical devices or applications.

### Bias, Risks, and Limitations
- Dataset Biases: The FinTalk-19k and Alpaca dataset may contain inherent biases that influence the model's outputs.
- Over-reliance: The model is an aid, not a replacement for human expertise. Decisions should be made with careful consideration.
- Content Understanding: The model lacks human-like understanding and cannot judge the veracity of knowledge.
- Language Limitations: The model's primary language is English. Performance may decrease with other languages.
- Knowledge Cut-off: The model may not be aware of events or trends post its last training update.

## Citation
```
@misc {ceadar_2023,
	author       = { {CeADAR} },
	title        = { FinanceConnect-13B (Revision 5f7841d) },
	year         = 2023,
	url          = { https://huggingface.co/ceadar-ie/FinanceConnect-13B },
	doi          = { 10.57967/hf/1405 },
	publisher    = { Hugging Face }
}
```
## Contact
For any further inquiries or feedback concerning FinanceConnect, please forward your communications to ahtsham.zafar@ucd.ie
