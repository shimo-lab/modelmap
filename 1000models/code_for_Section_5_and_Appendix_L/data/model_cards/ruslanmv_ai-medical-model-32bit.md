
# ai-medical-model-32bit: Fine-Tuned Llama3 for Technical Medical Questions
[![](future.jpg)](https://ruslanmv.com/)
This repository provides a fine-tuned version of the powerful Llama3 8B Instruct model, specifically designed to answer medical questions in an informative way. 
It leverages the rich knowledge contained in the AI Medical Dataset ([ruslanmv/ai-medical-dataset](https://huggingface.co/datasets/ruslanmv/ai-medical-dataset)).

**Model & Development**

- **Developed by:** ruslanmv
- **License:** Apache-2.0
- **Finetuned from model:** meta-llama/Meta-Llama-3-8B-Instruct

**Key Features**

- **Medical Focus:** Optimized to address health-related inquiries.
- **Knowledge Base:** Trained on a comprehensive medical dataset.
- **Text Generation:** Generates informative and potentially helpful responses.

**Installation**

This model is accessible through the Hugging Face Transformers library. Install it using pip:

```bash
!python -m pip install --upgrade pip
!pip3 install torch==2.2.1  torchvision torchaudio xformers --index-url https://download.pytorch.org/whl/cu121
!pip install  bitsandbytes  accelerate
```

**Usage Example**

Here's a Python code snippet demonstrating how to interact with the `ai-medical-model-32bit` model and generate answers to your medical questions:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig 
import torch
model_name = "ruslanmv/ai-medical-model-32bit"
device_map = 'auto' 
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    trust_remote_code=True,
    use_cache=False,
    device_map=device_map
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

def askme(question):
  prompt = f"<|start_header_id|>system<|end_header_id|> You are a Medical AI chatbot assistant. <|eot_id|><|start_header_id|>User: <|end_header_id|>This is the question: {question}<|eot_id|>"
  # Tokenizing the input and generating the output
  #prompt = f"{question}"
  # Tokenizing the input and generating the output
  inputs = tokenizer([prompt], return_tensors="pt").to("cuda")
  outputs = model.generate(**inputs, max_new_tokens=256, use_cache=True)
  answer = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
  # Try Remove the prompt
  try:
      # Split the answer at the first line break, assuming system intro and question are on separate lines
      answer_parts = answer.split("\n", 1)
      # If there are multiple parts, consider the second part as the answer
      if len(answer_parts) > 1:
        answers = answer_parts[1].strip()  # Remove leading/trailing whitespaces
      else:
        answers = ""  # If no split possible, set answer to empty string
      print(f"Answer: {answers}")   
  except:
      print(answer)  

# Example usage
# - Question:  Make the question.
question="What was the main cause of the inflammatory CD4+ T cells?"
askme(question)
```
the type of answer is :
```
Answer: I'm happy to help!

The main cause of inflammatory CD4+ T cells is a complex process that involves multiple factors. However, some of the key triggers include:

1. Activation of CD4+ T cells: CD4+ T cells are activated by antigens, cytokines, and other signals, leading to their proliferation and differentiation into effector cells.
2. Cytokine production: Activated CD4+ T cells produce cytokines such as interleukin-2 (IL-2), interferon-gamma (IFN-γ), and tumor necrosis factor-alpha (TNF-α), which promote inflammation and immune responses.
3. Chemokine production: CD4+ T cells also produce chemokines, such as CCL3, CCL4, and CCL5, which attract other immune cells to the site of inflammation.
4. Toll-like receptor (TLR) activation: TLRs are pattern recognition receptors that recognize pathogen-associated molecular patterns (PAMPs) and activate CD4+ T cells.
5. Bacterial or viral infections: Infections caused by bacteria, viruses, or fungi can trigger the activation of CD4+ T cells and the production of cytokines and chemokines
```
**Important Note**

This model is intended for informational purposes only and should not be used as a substitute for professional medical advice. Always consult with a qualified healthcare provider for any medical concerns.

**License**

This model is distributed under the Apache License 2.0 (see LICENSE file for details).

**Contributing**

We welcome contributions to this repository! If you have improvements or suggestions, feel free to create a pull request.

**Disclaimer**

While we strive to provide informative responses, the accuracy of the model's outputs cannot be guaranteed. 
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ruslanmv__ai-medical-model-32bit)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |67.67|
|AI2 Reasoning Challenge (25-Shot)|61.43|
|HellaSwag (10-Shot)              |78.69|
|MMLU (5-Shot)                    |68.10|
|TruthfulQA (0-shot)              |51.99|
|Winogrande (5-shot)              |75.77|
|GSM8k (5-shot)                   |70.05|

