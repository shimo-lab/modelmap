
# VMware/open-llama-0.7T-7B-open-instruct-v1.1

---

# UPDATE: Final Version Now Available!

Please use the final version: [Open LLaMA 7B Open Instruct](https://huggingface.co/VMware/open-llama-7b-open-instruct)

---

## License
- <b>Commercially Viable </b>
- Instruction dataset, [VMware/open-instruct-v1-oasst-dolly-hhrlhf](https://huggingface.co/datasets/VMware/open-instruct-v1-oasst-dolly-hhrlhf) is under cc-by-sa-3.0
- Language Model ([openlm-research/open_llama_7b_700bt_preview](https://huggingface.co/openlm-research/open_llama_7b_700bt_preview)) is under apache-2.0


## Nomenclature 

- Model : Open-llama
- Model trained on : 700B or 0.7 T tokens
- Model Size: 7B parameters
- Dataset: Open-instruct-v1.1 (oasst,dolly, hhrlhf)
- Version: 1.1 (Alpaca prompt template)


## Use in Transformers


```
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = 'VMware/open-llama-0.7T-7B-open-instruct-v1.1'


tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype= torch.float16, device_map = 'sequential')

prompt_template = "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{instruction}\n\n### Response:"

prompt=  'Explain in simple terms how the attention mechanism of a transformer model works'


inputt = prompt_template.format(instruction= prompt)
input_ids = tokenizer(inputt, return_tensors="pt").input_ids.to("cuda")

output1 = model.generate(input_ids, max_length=512)
input_length = input_ids.shape[1]
output1 = output1[:, input_length:]
output= tokenizer.decode(output1[0])

print(output)

'''
The attention mechanism of a transformer model is designed to help the model understand the relationship between different parts of a sentence.
The model uses a weighted attention score to determine how much each input token contributes to the output.
The attention score is calculated by looking at the similarity between each input token and the output token,and assigning a weight to each input token based on this similarity.
This way, the model can better understand the relationship between different parts of a sentence and generate more accurate predictions.

'''
```
  



# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_VMware__open-llama-0.7T-7B-open-instruct-v1.1)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 39.33   |
| ARC (25-shot)         | 46.67          |
| HellaSwag (10-shot)   | 67.67    |
| MMLU (5-shot)         | 28.55         |
| TruthfulQA (0-shot)   | 37.6   |
| Winogrande (5-shot)   | 65.43   |
| GSM8K (5-shot)        | 0.76        |
| DROP (3-shot)         | 28.61         |
