
<p align="left">
  <a href="https://console.upstage.ai/">
    <img src="https://huggingface.co/upstage/SOLAR-10.7B-Instruct-v1.0/resolve/main/solar-api-banner.png" width="100%"/>
  </a>
<p>

# **Meet 10.7B Solar: Elevating Performance with Upstage Depth UP Scaling!**

**(This model is [upstage/SOLAR-10.7B-v1.0](https://huggingface.co/upstage/SOLAR-10.7B-v1.0) fine-tuned version for single-turn conversation.)**


# **Introduction**
We introduce SOLAR-10.7B, an advanced large language model (LLM) with 10.7 billion parameters, demonstrating superior performance in various natural language processing (NLP) tasks. It's compact, yet remarkably powerful, and demonstrates unparalleled state-of-the-art performance in models with parameters under 30B.

We present a methodology for scaling LLMs called depth up-scaling (DUS) , which encompasses architectural modifications and continued pretraining. In other words, we integrated Mistral 7B weights into the upscaled layers, and finally, continued pre-training for the entire model.


SOLAR-10.7B has remarkable performance. It outperforms models with up to 30B parameters, even surpassing the recent Mixtral 8X7B model. For detailed information, please refer to the experimental table.
Solar 10.7B is an ideal choice for fine-tuning. SOLAR-10.7B offers robustness and adaptability for your fine-tuning needs. Our simple instruction fine-tuning using the SOLAR-10.7B pre-trained model yields significant performance improvements.

For full details of this model please read our [paper](https://arxiv.org/abs/2312.15166).


# **Instruction Fine-Tuning Strategy**

We utilize state-of-the-art instruction fine-tuning methods including supervised fine-tuning (SFT) and direct preference optimization (DPO) [1].

We used a mixture of the following datasets
- c-s-ale/alpaca-gpt4-data (SFT)
- Open-Orca/OpenOrca (SFT)
- in-house generated data utilizing Metamath [2] (SFT, DPO)
- Intel/orca_dpo_pairs (DPO)
- allenai/ultrafeedback_binarized_cleaned (DPO)

where we were careful of data contamination by not using GSM8K samples when generating data and filtering tasks when applicable via the following list.
```python
filtering_task_list = [
    'task228_arc_answer_generation_easy',
    'ai2_arc/ARC-Challenge:1.0.0',
    'ai2_arc/ARC-Easy:1.0.0',
    'task229_arc_answer_generation_hard',
    'hellaswag:1.1.0', 
    'task1389_hellaswag_completion',
    'cot_gsm8k',
    'cot_gsm8k_ii',
    'drop:2.0.0',
    'winogrande:1.1.0'
]
```

Using the datasets mentioned above, we applied SFT and iterative DPO training, a proprietary alignment strategy, to maximize the performance of our resulting model.

[1] Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C.D. and Finn, C., 2023. Direct preference optimization: Your language model is secretly a reward model. NeurIPS.

[2] Yu, L., Jiang, W., Shi, H., Yu, J., Liu, Z., Zhang, Y., Kwok, J.T., Li, Z., Weller, A. and Liu, W., 2023. Metamath: Bootstrap your own mathematical questions for large language models. arXiv preprint arXiv:2309.12284.

# **Data Contamination Test Results**

Recently, there have been contamination issues in some models on the LLM leaderboard. 
We note that we made every effort to exclude any benchmark-related datasets from training.
We also ensured the integrity of our model by conducting a data contamination test [3] that is also used by the HuggingFace team [4, 5].

Our results, with `result < 0.1, %:` being well below 0.9, indicate that our model is free from contamination.

*The data contamination test results of HellaSwag and Winograde will be added once [3] supports them.*

| Model                        | ARC   | MMLU | TruthfulQA | GSM8K |
|------------------------------|-------|-------|-------|-------|
| **SOLAR-10.7B-Instruct-v1.0**| result < 0.1, %: 0.06 |result < 0.1, %: 0.15 | result < 0.1, %: 0.28 | result < 0.1, %: 0.70 |

[3] https://github.com/swj0419/detect-pretrain-code-contamination

[4] https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard/discussions/474#657f2245365456e362412a06

[5] https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard/discussions/265#657b6debf81f6b44b8966230

# **Evaluation Results**

| Model                                  | H6    | Model Size |
|----------------------------------------|-------|------------|
| **SOLAR-10.7B-Instruct-v1.0**              | **74.20** | **~ 11B**      |
| mistralai/Mixtral-8x7B-Instruct-v0.1   | 72.62 | ~ 46.7B    |
| 01-ai/Yi-34B-200K                      | 70.81 | ~ 34B      |
| 01-ai/Yi-34B                           | 69.42 | ~ 34B      |
| mistralai/Mixtral-8x7B-v0.1            | 68.42 | ~ 46.7B    |
| meta-llama/Llama-2-70b-hf              | 67.87 | ~ 70B      |
| tiiuae/falcon-180B                     | 67.85 | ~ 180B     |
| **SOLAR-10.7B-v1.0**                   | **66.04** | **~11B**   |
| mistralai/Mistral-7B-Instruct-v0.2     | 65.71 | ~ 7B       |
| Qwen/Qwen-14B                          | 65.86 | ~ 14B      |
| 01-ai/Yi-34B-Chat                      | 65.32 | ~34B       |
| meta-llama/Llama-2-70b-chat-hf         | 62.4  | ~ 70B      |
| mistralai/Mistral-7B-v0.1              | 60.97 | ~ 7B       |
| mistralai/Mistral-7B-Instruct-v0.1     | 54.96 | ~ 7B       |

# **Usage Instructions**

This model has been fine-tuned primarily for single-turn conversation, making it less suitable for multi-turn conversations such as chat.

### **Version**

Make sure you have the correct version of the transformers library installed:

```sh
pip install transformers==4.35.2
```

### **Loading the Model**

Use the following Python code to load the model:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Upstage/SOLAR-10.7B-Instruct-v1.0")
model = AutoModelForCausalLM.from_pretrained(
    "Upstage/SOLAR-10.7B-Instruct-v1.0",
    device_map="auto",
    torch_dtype=torch.float16,
)
```

### **Conducting Single-Turn Conversation**

```python
conversation = [ {'role': 'user', 'content': 'Hello?'} ] 

prompt = tokenizer.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True)

inputs = tokenizer(prompt, return_tensors="pt").to(model.device) 
outputs = model.generate(**inputs, use_cache=True, max_length=4096)
output_text = tokenizer.decode(outputs[0]) 
print(output_text)
```

Below is an example of the output.
```
<s> ### User:
Hello?

### Assistant:
Hello, how can I assist you today? Please feel free to ask any questions or request help with a specific task.</s>
```

### **License**
- [upstage/SOLAR-10.7B-v1.0](https://huggingface.co/upstage/SOLAR-10.7B-v1.0): apache-2.0
- [upstage/SOLAR-10.7B-Instruct-v1.0](https://huggingface.co/upstage/SOLAR-10.7B-Instruct-v1.0): cc-by-nc-4.0
  - Since some non-commercial datasets such as Alpaca are used for fine-tuning, we release this model as cc-by-nc-4.0.

### **How to Cite**

Please cite the following papers using the below format when using this model.

```bibtex
@misc{kim2023solar,
      title={SOLAR 10.7B: Scaling Large Language Models with Simple yet Effective Depth Up-Scaling}, 
      author={Dahyun Kim and Chanjun Park and Sanghoon Kim and Wonsung Lee and Wonho Song and Yunsu Kim and Hyeonwoo Kim and Yungi Kim and Hyeonju Lee and Jihoo Kim and Changbae Ahn and Seonghoon Yang and Sukyung Lee and Hyunbyung Park and Gyoungjin Gim and Mikyoung Cha and Hwalsuk Lee and Sunghun Kim},
      year={2023},
      eprint={2312.15166},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
```bibtext
@misc{kim2024sdpo,
      title={sDPO: Don't Use Your Data All at Once}, 
      author={Dahyun Kim and Yungi Kim and Wonho Song and Hyeonwoo Kim and Yunsu Kim and Sanghoon Kim and Chanjun Park},
      year={2024},
      eprint={2403.19270},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### **The Upstage AI Team** ###
Upstage is creating the best LLM and DocAI. Please find more information at https://upstage.ai 

### **Contact Us** ###
Any questions and suggestions, please use the discussion tab. If you want to contact us directly, drop an email to [contact@upstage.ai](mailto:contact@upstage.ai)