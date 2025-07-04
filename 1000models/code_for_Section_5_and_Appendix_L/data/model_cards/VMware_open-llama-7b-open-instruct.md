
# VMware/open-llama-7B-open-instruct
Instruction-tuned version of the fully trained Open LLama 7B model. The model is open for <b>COMMERCIAL USE</b>. <br>

<b> There is a v2 version of this model available, https://huggingface.co/VMware/open-llama-7b-v2-open-instruct </b>

<b> NOTE </b> : The model was trained using the Alpaca prompt template
<b> NOTE </b> : Fast tokenizer results in incorrect encoding, set the ```use_fast = False``` parameter, when instantiating the tokenizer

## License
- <b>Commercially Viable </b>
- Instruction dataset, [VMware/open-instruct-v1-oasst-dolly-hhrlhf](https://huggingface.co/datasets/VMware/open-instruct-v1-oasst-dolly-hhrlhf) is under cc-by-sa-3.0
- Language Model, ([openlm-research/open_llama_7b](https://huggingface.co/openlm-research/open_llama_7b)) is under apache-2.0


## Nomenclature 

- Model : Open-llama
- Model Size: 7B parameters
- Dataset: Open-instruct-v1 (oasst,dolly, hhrlhf)

## Use in Transformers

```
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = 'VMware/open-llama-7b-open-instruct'


tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map='sequential')

prompt_template = "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{instruction}\n\n### Response:"

prompt = 'Explain in simple terms how the attention mechanism of a transformer model works'


inputt = prompt_template.format(instruction= prompt)
input_ids = tokenizer(inputt, return_tensors="pt").input_ids.to("cuda")

output1 = model.generate(input_ids, max_length=512)
input_length = input_ids.shape[1]
output1 = output1[:, input_length:]
output = tokenizer.decode(output1[0])

print(output)

'''
 Attention is a mechanism used in deep learning models, such as transformer models, to capture global dependencies between different parts of the input. In a transformer model, the attention mechanism works by computing a weighted sum of the input vectors and then applying a non-linear activation function to the result.

The attention mechanism in a transformer model works in two steps:

1. Query-Key Mapping: First, the input sequence is divided into two parts: the query vector and the key vector. The query vector represents the input at the current position, and the key vector represents the input at a previous position.

2. Attention Weight Calculation: Second, the attention weights are calculated using the dot product between the query vector and each key vector. The attention weights represent the importance of the input at the previous position to the current position.

The attention weights are then used to compute the attention score for each input element. The attention score represents the relevance of the input element to the current position.

The attention mechanism in a transformer model is designed to capture global dependencies between different parts of the input. By attending to input elements from different positions, the model can learn to understand the relationships between different parts of the input. This allows the model to perform more complex tasks, such as understanding the relationships between words in a sentence or pixels in an image.</s>

'''
```
  
## Finetuning details
The finetuning scripts will be available in our [RAIL Github Repository](https://github.com/vmware-labs/research-and-development-artificial-intelligence-lab/tree/main/instruction-tuning)

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_VMware__open-llama-7b-open-instruct)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 40.9   |
| ARC (25-shot)         | 49.74          |
| HellaSwag (10-shot)   | 73.67    |
| MMLU (5-shot)         | 31.52         |
| TruthfulQA (0-shot)   | 34.65   |
| Winogrande (5-shot)   | 65.43   |
| GSM8K (5-shot)        | 0.53        |
| DROP (3-shot)         | 30.75         |
