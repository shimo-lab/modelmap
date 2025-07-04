
# Indic-gemma-7b-finetuned-sft-Navarasa-2.0

This model is based on [google/gemma-7b](https://huggingface.co/google/gemma-7b) and hase been LoRA finetuned on 15 Indian languages and English language instruction datasets:

1. #### Hindi - [ravithejads/samvaad-hi-filtered](https://huggingface.co/datasets/ravithejads/samvaad-hi-filtered), [HydraIndicLM/hindi_alpaca_dolly_67k](https://huggingface.co/datasets/HydraIndicLM/hindi_alpaca_dolly_67k)(sampled)
2. #### Telugu - [Telugu-LLM-Labs/telugu_alpaca_yahma_cleaned_filtered_romanized](https://huggingface.co/datasets/Telugu-LLM-Labs/telugu_alpaca_yahma_cleaned_filtered_romanized), [Telugu-LLM-Labs/telugu_teknium_GPTeacher_general_instruct_filtered_romanized](https://huggingface.co/datasets/Telugu-LLM-Labs/telugu_teknium_GPTeacher_general_instruct_filtered_romanized)
3. #### Marathi - [Telugu-LLM-Labs/sindhi_alpaca_yahma_cleaned_filtered](https://huggingface.co/datasets/Telugu-LLM-Labs/sindhi_alpaca_yahma_cleaned_filtered)
4. #### Urdu - [Telugu-LLM-Labs/urdu_alpaca_yahma_cleaned_filtered](https://huggingface.co/datasets/Telugu-LLM-Labs/urdu_alpaca_yahma_cleaned_filtered)
5. #### Assamese - [Telugu-LLM-Labs/assamese_alpaca_yahma_cleaned_filtered](https://huggingface.co/datasets/Telugu-LLM-Labs/assamese_alpaca_yahma_cleaned_filtered)
6. #### Konkani - [Telugu-LLM-Labs/konkani_alpaca_yahma_cleaned_filtered](https://huggingface.co/datasets/Telugu-LLM-Labs/konkani_alpaca_yahma_cleaned_filtered)
7. #### Nepali - [Telugu-LLM-Labs/nepali_alpaca_yahma_cleaned_filtered](https://huggingface.co/datasets/Telugu-LLM-Labs/nepali_alpaca_yahma_cleaned_filtered)
8. #### Sindhi - [Telugu-LLM-Labs/sindhi_alpaca_yahma_cleaned_filtered](https://huggingface.co/datasets/Telugu-LLM-Labs/sindhi_alpaca_yahma_cleaned_filtered)
9. #### Tamil - [abhinand/tamil-alpaca](https://huggingface.co/datasets/abhinand/tamil-alpaca)
10. #### Kannada - [Tensoic/airoboros-3.2_kn](https://huggingface.co/datasets/Tensoic/airoboros-3.2_kn), [Tensoic/gpt-teacher_kn](https://huggingface.co/datasets/Tensoic/gpt-teacher_kn)
11. #### Malayalam - [VishnuPJ/Alpaca_Instruct_Malayalam](https://huggingface.co/datasets/VishnuPJ/Alpaca_Instruct_Malayalam)
12. #### Gujarati - [Tensoic/Alpaca-Gujarati](https://huggingface.co/datasets/Tensoic/Alpaca-Gujarati)
13. #### Punjabi - [HydraIndicLM/punjabi_alpaca_52K](https://huggingface.co/datasets/HydraIndicLM/punjabi_alpaca_52K)
14. #### Bengali - [HydraIndicLM/bengali_alpaca_dolly_67k](https://huggingface.co/datasets/HydraIndicLM/bengali_alpaca_dolly_67k)(alpaca filtered)
15. #### Odia - [OdiaGenAI/Odia_Alpaca_instructions_52k](https://huggingface.co/datasets/OdiaGenAI/Odia_Alpaca_instructions_52k), [OdiaGenAI/gpt-teacher-roleplay-odia-3k](https://huggingface.co/datasets/OdiaGenAI/gpt-teacher-roleplay-odia-3k)
16. #### English - [yahma/alpaca-cleaned](https://huggingface.co/datasets/yahma/alpaca-cleaned)

The model is finetuned using [unsloth](https://github.com/unslothai/unsloth) library and we provide inference code using the same for faster inference. Alternatively you can use HuggingFace Library for inference.

# Training Details:

The model is trained on approx 650K instruction samples.
1. GPU: 1 A100, 80GB
2. Time: 45 Hours
3. Platform: [E2E Networks](https://www.e2enetworks.com/)
# Installation

`!pip install -U xformers --index-url https://download.pytorch.org/whl/cu121`
`!pip install "unsloth[kaggle-new] @git+https://github.com/unslothai/unsloth.git@nightly"`

# Input Text Format

```
### Instruction: {instruction}

### Input: {input}

## Response: {response}
```

# Inference With Unsloth

```python3
from unsloth import FastLanguageModel
import torch
max_seq_length = 2048
dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
load_in_4bit = False 
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "Telugu-LLM-Labs/Indic-gemma-7b-finetuned-sft-Navarasa-2.0",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
    device_map="auto"
)
FastLanguageModel.for_inference(model) # Enable native 2x faster inference

input_prompt = """
### Instruction:
{}

### Input:
{}

### Response:
{}"""

input_text = input_prompt.format(
        "Tranlsate following sentence to Hindi.", # instruction
        "India is a great country.", # input
        "", # output - leave this blank for generation!
    )

inputs = tokenizer([input_text], return_tensors = "pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens = 300, use_cache = True)
response = tokenizer.batch_decode(outputs)
```

# Inference with HuggingFace

```python3
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "Telugu-LLM-Labs/Indic-gemma-7b-finetuned-sft-Navarasa-2.0",
    load_in_4bit = False,
    token = hf_token
)
model.to("cuda")

tokenizer = AutoTokenizer.from_pretrained("Telugu-LLM-Labs/Indic-gemma-7b-finetuned-sft-Navarasa-2.0")

input_prompt = """
### Instruction:
{}

### Input:
{}

### Response:
{}"""

input_text = input_prompt.format(
        "Tranlsate following sentence to Hindi.", # instruction
        "India is a great country.", # input
        "", # output - leave this blank for generation!
    )

inputs = tokenizer([input_text], return_tensors = "pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens = 300, use_cache = True)
response = tokenizer.batch_decode(outputs)[0]
```

Refer to the [blog post](https://ravidesetty.medium.com/introducing-navarasa-2-0-indic-gemma-7b-2b-instruction-tuned-model-on-15-indian-languages-31f6565b2750) for sample examples.

Please check our [Code Repository](https://github.com/TeluguLLMLabs/Indic-gemma-7b-Navarasa) for training and inference scripts.


# Developers:

The model is a collaborative effort by [Ravi Theja](https://twitter.com/ravithejads) and [Ramsri Goutham](https://twitter.com/ramsri_goutham). Feel free to DM either of us if you have any questions.