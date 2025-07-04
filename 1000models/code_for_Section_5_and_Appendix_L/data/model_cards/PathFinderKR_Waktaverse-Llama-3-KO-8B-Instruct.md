
# Waktaverse-Llama-3-KO-8B-Instruct Model Card

## Model Details

![image/webp](https://cdn-uploads.huggingface.co/production/uploads/65d6e0640ff5bc0c9b69ddab/Va78DaYtPJU6xr4F6Ca4M.webp)
Waktaverse-Llama-3-KO-8B-Instruct is a Korean language model developed by Waktaverse AI team.
This large language model is a specialized version of the Meta-Llama-3-8B-Instruct, tailored for Korean natural language processing tasks. 
It is designed to handle a variety of complex instructions and generate coherent, contextually appropriate responses.

- **Developed by:** Waktaverse AI
- **Model type:** Large Language Model
- **Language(s) (NLP):** Korean, English
- **License:** [Llama3](https://llama.meta.com/llama3/license)
- **Finetuned from model:** [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)

## Model Sources

- **Repository:** [GitHub](https://github.com/PathFinderKR/Waktaverse-LLM/tree/main)
- **Paper :** [More Information Needed]



## Uses

### Direct Use

The model can be utilized directly for tasks such as text completion, summarization, and question answering without any fine-tuning. 

### Out-of-Scope Use

This model is not intended for use in scenarios that involve high-stakes decision-making including medical, legal, or safety-critical areas due to the potential risks of relying on automated decision-making. 
Moreover, any attempt to deploy the model in a manner that infringes upon privacy rights or facilitates biased decision-making is strongly discouraged.

## Bias, Risks, and Limitations

While Waktaverse Llama 3 is a robust model, it shares common limitations associated with machine learning models including potential biases in training data, vulnerability to adversarial attacks, and unpredictable behavior under edge cases. 
There is also a risk of cultural and contextual misunderstanding, particularly when the model is applied to languages and contexts it was not specifically trained on.



## How to Get Started with the Model

You can run conversational inference using the Transformers Auto classes.
We highly recommend that you add Korean system prompt for better output.
Adjust the hyperparameters as you need.

### Example Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = (
    "cuda:0" if torch.cuda.is_available() else # Nvidia GPU
    "mps" if torch.backends.mps.is_available() else # Apple Silicon GPU
    "cpu"
)

model_id = "PathFinderKR/Waktaverse-Llama-3-KO-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map=device,
)

################################################################################
# Generation parameters
################################################################################
num_return_sequences=1
max_new_tokens=1024
temperature=0.6
top_p=0.9
repetition_penalty=1.1

def prompt_template(system, user):
    return (
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
        f"{system}<|eot_id|>"
        
        "<|start_header_id|>user<|end_header_id|>\n\n"
        f"{user}<|eot_id|>"
        
        "<|start_header_id|>assistant<|end_header_id|>\n\n"
    )

def generate_response(system ,user):
    prompt = prompt_template(system, user)
    
    input_ids = tokenizer.encode(
        prompt,
        add_special_tokens=False,
        return_tensors="pt"
    ).to(device)
    
    outputs = model.generate(
        input_ids=input_ids,
        pad_token_id=tokenizer.eos_token_id,
        num_return_sequences=num_return_sequences,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
        repetition_penalty=repetition_penalty
    )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=False)

system_prompt = "다음 지시사항에 대한 응답을 작성해주세요."
user_prompt = "피보나치 수열에 대해 설명해주세요."
response = generate_response(system_prompt, user_prompt)
print(response)
```

### Example Output

```python
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

다음 지시사항에 대한 응답을 작성해 주세요.<|eot_id|><|start_header_id|>user<|end_header_id|>

피보나치 수열에 대해 설명해주세요.<|eot_id|><|start_header_id|>assistant<|end_header_id|>

피보나치 수열은 수학에서 자주 사용되는 수열 중 하나로, 0과 1로 시작하여 다음 항이 이전 두 항의 합으로 구성됩니다. 피보나치 수열은 유명한 수학자 레온 알렉산드로비치 피보나치가 제안했으며, 그의 이름을 따서 명명되었습니다. 이 수열은 자연수와 정수를 포함하며, 각 항은 이전 두 항의 합입니다. 예를 들어, 첫 번째 항은 0이고 두 번째 항은 1이며, 세 번째 항은 2이고 네 번째 항은 3입니다. 피보나치 수열은 순차적으로 증가하는 특징이 있지만, 숫자가 커질수록 점점 더 빠르게 증가합니다. 피보나치 수열은 다양한 분야에서 사용되며, 수학, 컴퓨터 과학, 생물학 등에서 중요한 역할을 합니다.<|eot_id|>
```



## Training Details

### Training Data

The model is trained on the [MarkrAI/KoCommercial-Dataset](https://huggingface.co/datasets/MarkrAI/KoCommercial-Dataset), which consists of various commercial texts in Korean.

### Training Procedure

The model training used LoRA for computational efficiency. 0.04 billion parameters(0.51% of total parameters) were trained.

#### Training Hyperparameters

```python
################################################################################
# bitsandbytes parameters
################################################################################
load_in_4bit=True
bnb_4bit_compute_dtype=torch.bfloat16
bnb_4bit_quant_type="nf4"
bnb_4bit_use_double_quant=True

################################################################################
# LoRA parameters
################################################################################
task_type="CAUSAL_LM"
target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
r=8
lora_alpha=16
lora_dropout=0.05
bias="none"

################################################################################
# TrainingArguments parameters
################################################################################
num_train_epochs=1
per_device_train_batch_size=1
gradient_accumulation_steps=1
gradient_checkpointing=True
learning_rate=2e-5
lr_scheduler_type="cosine"
warmup_ratio=0.1
optim = "paged_adamw_32bit"
weight_decay=0.01

################################################################################
# SFT parameters
################################################################################
max_seq_length=4096
packing=False
```



## Evaluation

### Metrics

- **Ko-HellaSwag:**
- **Ko-MMLU:**
- **Ko-Arc:**
- **Ko-Truthful QA:**
- **Ko-CommonGen V2:**
  
### Results

<table>
  <tr>
   <td><strong>Benchmark</strong>
   </td>
   <td><strong>Waktaverse Llama 3 8B</strong>
   </td>
   <td><strong>Llama 3 8B</strong>
   </td>
  </tr>
  <tr>
   <td>Ko-HellaSwag:
   </td>
   <td>0
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>Ko-MMLU:
   </td>
   <td>0
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>Ko-Arc:
   </td>
   <td>0
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>Ko-Truthful QA:
   </td>
   <td>0
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>Ko-CommonGen V2:
   </td>
   <td>0
   </td>
   <td>0
   </td>
</table>

## Technical Specifications

### Compute Infrastructure

#### Hardware

- **GPU:** NVIDIA GeForce RTX 4080 SUPER

#### Software

- **Operating System:** Linux
- **Deep Learning Framework:** Hugging Face Transformers, PyTorch

### Training Details

- **Training time:** 80 hours
- More details on [Weights & Biases](https://wandb.ai/pathfinderkr/Waktaverse-Llama-3-KO-8B-Instruct?nw=nwuserpathfinderkr)



## Citation

**Waktaverse-Llama-3**

```
@article{waktaversellama3modelcard,
  title={Waktaverse Llama 3 Model Card},
  author={AI@Waktaverse},
  year={2024},
  url = {https://huggingface.co/PathFinderKR/Waktaverse-Llama-3-KO-8B-Instruct}
```

**Llama-3**

```
@article{llama3modelcard,
  title={Llama 3 Model Card},
  author={AI@Meta},
  year={2024},
  url = {https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md}
}
```



## Model Card Authors

[PathFinderKR](https://github.com/PathFinderKR)