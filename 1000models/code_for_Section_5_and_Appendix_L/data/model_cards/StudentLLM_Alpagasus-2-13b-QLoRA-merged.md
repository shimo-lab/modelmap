## Model Details
This is an unofficial implementation of "[AlpaGasus: Training a better Alpaca with Fewer Data.](https://github.com/Lichang-Chen/AlpaGasus)" with [LLaMA2](https://huggingface.co/meta-llama/Llama-2-13b-hf) & QLoRA! Training code is available at our [repo](https://github.com/gauss5930/AlpaGasus2-QLoRA). 

- **Developed by:** [Yunsang Yoo](https://huggingface.co/ryan0712) and [Hyunwoo Ko](https://huggingface.co/Cartinoe5930)
- **Model type:** Auto-regressive model
- **Language(s):** English
- **Base Model:** [meta-llama/Llama-2-13b-hf](https://huggingface.co/meta-llama/Llama-2-13b-hf)
- **License**: Non-Commercial Creative Commons license ([CC BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/))


### Training dataset

"StudentLLM/Alpagasus-2-13b-QLoRA-merged" used [gpt4life](https://github.com/gpt4life/alpagasus)'s gpt-3.5-turbo filtered dataset, 'alpaca_t45.json'.

Configuration of the dataset is as follows:

```
{
    'instruction': Give the instruction describing the question.
    'input': Occasionally present, detailed instructions accompany the question if available.
    'output': Give answers to questions.
}
.
.
.

```

### Prompt Template: Alpaca style prompt
```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
<prompt> (without the <>)

### Input:
<prompt> (if input exists)

### Response:
```

### Fine-tuning Procedure
Our model was finetuned using QLoRA on single A100 80GB GPU. Training details are described in [repo](https://github.com/gauss5930/AlpaGasus2-QLoRA).

### Benchmark Metrics
"StudentLLM/Alpagasus-2-13b-QLoRA-merged" model performance is uploaded on Huggingface's [OpenLLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard). Model was evaluated on the tasks specified in HF's Open LLM Leaderboard(ARC, HellaSwag, MMLU, TruthfulQA).

| Metric                | Value |
|-----------------------|-------|
| Avg.                  | 59.34 |
| MMLU                  | 55.27 |
| ARC                   | 61.09 |
| HellaSwag             | 82.46 |
| TruthfulQA            | 38.53 |

### LLM Evaluation
We tried to follow the evaluation metric introduced by the AlpaGasus paper. During the process, we consulted the code by [gpt4life](https://github.com/gpt4life/alpagasus). We used OpenAI's gpt-3.5-turbo as the evaluator model, and Alpaca2-LoRA-13B(it doesn't exist now...) as the comparison model. For more detailed information, please refer to our Github [repo](https://github.com/gauss5930/AlpaGasus2-QLoRA).

The evaluation result of AlpaGasus2-QLoRA is as follows:
![results](https://user-images.githubusercontent.com/80087878/262848860-8742bcc4-1bbc-449f-8bcf-660c08fcc10d.png)

### How to use
To use "StudentLLM/Alpagasus-2-13b-QLoRA-merged", please follow the following code! The use of the 7B model is the same!
```python
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

config = PeftConfig.from_pretrained("StudentLLM/Alpagasus-2-13B-QLoRA")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-13b-hf", use_auth_token="yotu_HuggingFace_token").to(device)
model = PeftModel.from_pretrained(model, "StudentLLM/Alpagasus-2-13B-QLoRA")

tokenizer = AutoTokenizer.from_pretrained("StudentLLM/Alpagasus-2-13B-QLoRA")
tokenizer.pad_token = tokenizer.eos_token

input_data = "Please tell me 3 ways to relieve stress."   # You can enter any questions!!

model_inputs = tokenizer(input_data, return_tensors='pt').to(device)
model_output = model.generate(**model_inputs, max_length=256)
model_output = tokenizer.decode(model_output[0], skip_special_tokens=True)
print(model_output)
```

### Citations
```bibtex
@article{chen2023alpagasus,
  title={AlpaGasus: Training a Better Alpaca with Fewer Data},
  author={Lichang Chen, Shiyang Li, Jun Yan, Hai Wang, Kalpa Gunaratna, Vikas Yadav, Zheng Tang, Vijay Srinivasan, Tianyi Zhou, Heng Huang, Hongxia Jin},
  journal={arXiv preprint arXiv:2307.08701},
  year={2023}
}
```