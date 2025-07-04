
# 😼 CatPPT

Introducing "CatPPT" - the purrfect alternative to that other big cat in town, known for keeping all the secrets to itself! Our feline friend here is created through merging openchat and neuralchat models using Gradient SLERP method (resulting in [rishiraj/CatPPT-base](https://huggingface.co/rishiraj/CatPPT-base)) and then finetuned on no_robots dataset for chat.

This is the top-performing 7B model on the leaderboard, that's free from any whiff of evaluation data contamination.

![](https://raw.githubusercontent.com/rishiraj/rishiraj.github.io/main/assets/spider%402x.png)

## Model date

rishiraj/CatPPT was trained between 15th and 17th December, 2023.

## Evaluation

It achieves the following results on the [Open_LLM_Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard). At the time of release, CatPPT is the highest ranked 7B chat model on the leaderboard, that's **free from evaluation data contamination**.

|Model                               |Average|ARC  |HellaSwag|MMLU |TruthfulQA|Winogrande|GSM8K|
|------------------------------------|-------|-----|---------|-----|----------|----------|-----|
|**rishiraj/CatPPT**                     |**72.32**  |**68.09**|**86.69**    |**65.16**|**61.55**     |**81.61**     |**70.81**|
|Intel/neural-chat-7b-v3-3           |69.83  |66.89|85.26    |63.07|63.01     |79.64     |61.11|
|openchat/openchat-3.5-1210          |68.89  |64.93|84.92    |64.62|52.15     |80.74     |65.96|
|meta-math/MetaMath-Mistral-7B       |65.78  |60.67|82.58    |61.95|44.89     |75.77     |68.84|
|Deci/DeciLM-7B-instruct             |63.19  |61.01|82.37    |60.24|49.75     |79.72     |46.02|
|mistralai/Mistral-7B-Instruct-v0.2  |65.71  |63.14|84.88    |60.78|68.26     |77.19     |40.03|
|mistralai/Mixtral-8x7B-Instruct-v0.1|72.62  |70.22|87.63    |71.16|64.58     |81.37     |60.73|
|meta-llama/Llama-2-70b-hf           |67.87  |67.32|87.33    |69.83|44.92     |83.74     |54.06|
|tiiuae/falcon-180B                  |67.85  |69.45|88.86    |70.5 |45.47     |86.9      |45.94|

## Inference procedure

Here's how you can run the model using the pipeline() function from 🤗 Transformers:

```
import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="rishiraj/CatPPT", torch_dtype=torch.bfloat16, device_map="auto")

# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate"
    },
    {
        "role": "user",
        "content": "How many helicopters can a human eat in one sitting?"
    }
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 128
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.9947        | 0.16  | 3    | 2.0093          |


### Framework versions

- Transformers 4.36.1
- Pytorch 2.1.2+cu121
- Datasets 2.14.6
- Tokenizers 0.15.0
- PEFT 0.6.1

## Citation Information

```
@misc{rishiraj2023catppt,
  author = {Rishiraj Acharya},
  title = {CatPPT},
  year = {2023},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{https://huggingface.co/rishiraj/CatPPT}}
}
```