

# Llama-3-8B-Synthia-v3.5
Llama-3-8B-Synthia-v3.5 (Synthetic Intelligent Agent) is a general purpose Large Language Model (LLM). It was trained on the Synthia-v3.5 dataset that contains the varied system contexts, plus some other publicly available datasets.

It has been fine-tuned for instruction following as well as having long-form conversations.

Compute for Llama-3-8B-Synthia-v3.5 was sponsored by [KindoAI](https://kindo.ai/).

<br>

![Synthia](https://huggingface.co/migtissera/Llama-3-8B-Synthia-v3.5/resolve/main/Synthia-3.5.jpg)

<br>




## Evaluation

We evaluated Llama-3-8B-Synthia-v3.5 on a wide range of tasks using [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) from EleutherAI. 

Here are the results on metrics used by [HuggingFaceH4 Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard). Section to follow.

||||
|:------:|:--------:|:-------:|
|**Task**|**Metric**|**Value**|
|*arc_challenge*|acc_norm||
|*hellaswag*|acc_norm||
|*mmlu*|acc_norm||
|*truthfulqa_mc*|mc2||
|**Total Average**|-|||

<br>


# Sample code to run inference

```python
import torch, json
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "/home/migel/Tess-2.0-Llama-3-8B"
output_file_path = "/home/migel/conversations.jsonl"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto",
    load_in_4bit=False,
    trust_remote_code=False,
)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

def generate_text(instruction):
    tokens = tokenizer.encode(instruction)
    tokens = torch.LongTensor(tokens).unsqueeze(0)
    tokens = tokens.to("cuda")

    instance = {
        "input_ids": tokens,
        "top_p": 1.0,
        "temperature": 0.75,
        "generate_len": 1024,
        "top_k": 50,
    }

    length = len(tokens[0])
    with torch.no_grad():
        rest = model.generate(
            input_ids=tokens,
            max_length=length + instance["generate_len"],
            use_cache=True,
            do_sample=True,
            top_p=instance["top_p"],
            temperature=instance["temperature"],
            top_k=instance["top_k"],
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
        )
    output = rest[0][length:]
    string = tokenizer.decode(output, skip_special_tokens=True)
    return f"{string}"

conversation = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are Synthia, a helful, female AI assitant. You always provide detailed answers without hesitation.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"""

while True:
    user_input = input("You: ")
    llm_prompt = f"{conversation}{user_input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    answer = generate_text(llm_prompt)
    print(answer)

    conversation = f"{llm_prompt}{answer}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"

    json_data = {"prompt": user_input, "answer": answer}

    with open(output_file_path, "a") as output_file:
        output_file.write(json.dumps(json_data) + "\n")
```

# Join My General AI Discord (NeuroLattice):
https://discord.gg/Hz6GrwGFKD

# Limitations & Biases:

While this model aims for accuracy, it can occasionally produce inaccurate or misleading results. 

Despite diligent efforts in refining the pretraining data, there remains a possibility for the generation of inappropriate, biased, or offensive content. 

Exercise caution and cross-check information when necessary. This is an uncensored model.
