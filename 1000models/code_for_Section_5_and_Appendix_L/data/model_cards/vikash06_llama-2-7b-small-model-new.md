This model is trained on experimental basis on a small dataset to assess whether training longer on a smaller dataset has a good performance or not.


# Model Details
vikash06/llama-2-7b-small-model--> Finetuned model on llama2

# Uses

# Creative Writing: Write a question or instruction that requires a creative, open-ended written response. 
The instruction should be reasonable to ask of a person with general world knowledge and should not require searching. 
In this task, your prompt should give very specific instructions to follow. 
Constraints, instructions, guidelines, or requirements all work, and the more of them the better.


# Closed QA: Write a question or instruction that requires factually correct response based on a passage of text from Wikipedia. 
The question can be complex and can involve human-level reasoning capabilities, but should not require special knowledge.
To create a question for this task include both the text of the question as well as the reference text in the form.

# Open QA: Write a question that can be answered using general world knowledge or at most a single search. 
This task asks for opinions and facts about the world at large and does not provide any reference text for consultation.

# Summarization: Give a summary of a paragraph from Wikipedia.
Please don't ask questions that will require more than 3-5 minutes to answer.
To create a question for this task include both the text of the question as well as the reference text in the form.

# Information Extraction: These questions involve reading a paragraph from Wikipedia and extracting information from the passage. 
Everything required to produce an answer (e.g. a list, keywords etc) should be included in the passages. 
To create a question for this task include both the text of the question as well as the reference text in the form.


# Classification: These prompts contain lists or examples of entities to be classified, e.g. movie reviews, products, etc. 
In this task the text or list of entities under consideration is contained in the prompt (e.g. there is no reference text.).
You can choose any categories for classification you like, the more diverse the better.

# Brainstorming: Think up lots of examples in response to a question asking to brainstorm ideas

# Direct Use

The model is intnded for direct use

# How to Get Started with the Model

import torch

import pandas as pd

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("vikash06/llama-2-7b-small-model")

model = AutoModelForCausalLM.from_pretrained("vikash06/llama-2-7b-small-model", torch_dtype=torch.float16, device_map="cuda:0")

print (model)

def generate_training_prompt(instruction,context):

    return f"""
    Below is an instruction that describes a task. Write a response that appropriately completes the request.

    ### Instruction: {instruction}

    ### Context:
    {context.strip()}


    """.strip()

data1 ={"instruction": "When was the first Reading railway station opened?", "context": "Reading railway station is a major transport hub in Reading, Berkshire, England. It is on the northern edge of the town centre, near the main retail and commercial areas and the River Thames, 36 miles (58 km) from London Paddington. The first Reading station was opened on 30 March 1840 as the temporary western terminus of the original line of the Great Western Railway (GWR). Reading is the ninth-busiest station in the UK outside London and the second busiest interchange station outside London with over 3.8 million passengers changing trains at the station annually.", "response": "The first Reading railway station was opened on the 30th of March, 1840.", "category": "closed_qa"}

prompt = generate_training_prompt(data1["instruction"],data1["context"])

input_ids = tokenizer(prompt, return_tensors="pt", truncation=True).input_ids.cuda(0)

outputs = model.generate(input_ids=input_ids, max_new_tokens=128, do_sample=True, top_p=0.9,temperature=0.3)

resp = tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=True)[0][len(prompt):].split("\n")

resp = [x for x in resp if x!='']

print(resp)
    
# Training Data
1000 samples were carefully selected from each of the category.

# Training Procedure
We used the below libraries to finetune the llama2-7b:
torch==2.1.0 

transformers==4.35.2

peft@git+https://github.com/huggingface/peft.git bitsandbytes==0.41.1 trl @ git+https://github.com/lvwerra/trl.git@34e6948d459540a21f80c5be227fb4da039dd97a 

We used batch size 0f 2 on 50 epochs

# Evaluation

We performed hellaswag task using evaluation library of EleutherAI: https://github.com/EleutherAI/lm-evaluation-harness

below are the results:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63a7d07154f1d0225b0b9d1c/CKgtAaq55ce30e-Qorzsi.png)


![image/png](https://cdn-uploads.huggingface.co/production/uploads/63a7d07154f1d0225b0b9d1c/Pyy4FpgVPC1loNRO8JA3u.png)


# Environmental Impact
Carbon Emitted: 0.432 kg/kWh Offset: 0% hardware: a6000 48GB(3) hours: 28

# Technical Report

Detail writeup coming soon
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_vikash06__llama-2-7b-small-model-new)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |46.62|
|AI2 Reasoning Challenge (25-Shot)|45.22|
|HellaSwag (10-Shot)              |72.35|
|MMLU (5-Shot)                    |46.23|
|TruthfulQA (0-shot)              |42.46|
|Winogrande (5-shot)              |63.93|
|GSM8k (5-shot)                   | 9.55|

