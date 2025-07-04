
Anima LLM supporting 100K input token length. It's trained based on Llama2 7B, so the license support commercial use!

We carefully curated long QA training dataset from 30k to 100k length to train this model. We also made a lot of memory optimizations to make it scale to 100k tokens.


## How to train/infer?

#### install dependencies

```bash
# Please update the path of `CUDA_HOME`
export CUDA_HOME=/usr/local/cuda-11.8
pip install transformers==4.31.0
pip install sentencepiece
pip install ninja
pip install flash-attn --no-build-isolation
pip install git+https://github.com/HazyResearch/flash-attention.git#subdirectory=csrc/rotary
pip install git+https://github.com/HazyResearch/flash-attention.git#subdirectory=csrc/xentropy
pip install evaluate
pip install git+https://github.com/huggingface/peft.git@v0.4.0
pip install wandb
```

#### inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

base_model = "lyogavin/Anima-7B-100K"
tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(
            base_model,
            torch_dtype=torch.float16,
            trust_remote_code=True,
            device_map="auto", 
        )
model.eval()

prompt = "Where is the capital of US?"
inputs = tokenizer(prompt, return_tensors="pt")

inputs['input_ids'] = inputs['input_ids'].cuda()
inputs['attention_mask'] = inputs['attention_mask'].cuda()

# Generate
generate_ids = model.generate(**inputs, max_new_tokens=30,
                       only_last_logit=True, # to save memory
                       use_cache=False, # when run into OOM, enable this can save memory
                       xentropy=True)
output = tokenizer.batch_decode(generate_ids, 
                                skip_special_tokens=True,
                                clean_up_tokenization_spaces=False)[0]

```

#### Training

```bash
./run_longer_training.sh
```

## Evaluations

There's almost none evaluation dataset designed for 100k tokens. So we designed/curated some dataset for this model. We compared this model and several other public/private models.

#### 1. longchat topic retrieval

| Model             | Accuracy     | 
|-------------------|---------|
| Claude2 | 0.9    |
| together llama2 32k        | 0.15 | 
| longchat 32k 1.5             | 0.05 | 
| Anima 100K   | 0.5  | 

#### 2. longchat number retrieval

| Model             | Accuracy     | 
|-------------------|---------|
| Claude2 | 0.85   |
| together llama2 32k        | 0.2 | 
| longchat 32k 1.5             | 0.05 | 
| Anima 100K   | 0.45 | 

#### 3. Narrative QA in zeroscore

| Model             | F1     | 
|-------------------|---------|
| Claude2 | 0.6187   |
| together llama2 32k        | 0.3833 | 
| longchat 32k 1.5             | 0.2416 | 
| Anima 100K   | 0.4919  | 

## Github 

Github repo is [here](https://github.com/lyogavin/Anima/tree/main/anima_100k)