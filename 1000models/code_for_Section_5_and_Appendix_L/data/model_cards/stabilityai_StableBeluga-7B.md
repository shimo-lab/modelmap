# Stable Beluga 7B

Use [Stable Chat (Research Preview)](https://chat.stability.ai/chat) to test Stability AI's best language models for free

## Model Description

`Stable Beluga 7B` is a Llama2 7B model finetuned on an Orca style Dataset

## Usage

Start chatting with `Stable Beluga 7B` using the following code snippet:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

tokenizer = AutoTokenizer.from_pretrained("stabilityai/StableBeluga-7B", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("stabilityai/StableBeluga-7B", torch_dtype=torch.float16, low_cpu_mem_usage=True, device_map="auto")
system_prompt = "### System:\nYou are StableBeluga, an AI that follows instructions extremely well. Help as much as you can. Remember, be safe, and don't do anything illegal.\n\n"

message = "Write me a poem please"
prompt = f"{system_prompt}### User: {message}\n\n### Assistant:\n"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
output = model.generate(**inputs, do_sample=True, top_p=0.95, top_k=0, max_new_tokens=256)

print(tokenizer.decode(output[0], skip_special_tokens=True))
```

Stable Beluga 7B should be used with this prompt format:
```
### System:
This is a system prompt, please behave and help the user.

### User:
Your prompt here

### Assistant:
The output of Stable Beluga 7B
```

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: Stable Beluga 7B is an auto-regressive language model fine-tuned on Llama2 7B.
* **Language(s)**: English
* **Library**: [HuggingFace Transformers](https://github.com/huggingface/transformers)
* **License**: Fine-tuned checkpoints (`Stable Beluga 7B`) is licensed under the [STABLE BELUGA NON-COMMERCIAL COMMUNITY LICENSE AGREEMENT](https://huggingface.co/stabilityai/StableBeluga-7B/blob/main/LICENSE.txt)
* **Contact**: For questions and comments about the model, please email `lm@stability.ai`

### Training Dataset

` Stable Beluga 7B` is trained on our internal Orca-style dataset

### Training Procedure

Models are learned via supervised fine-tuning on the aforementioned datasets, trained in mixed-precision (BF16), and optimized with AdamW. We outline the following hyperparameters:

| Dataset           | Batch Size | Learning Rate |Learning Rate Decay| Warm-up | Weight Decay | Betas       |
|-------------------|------------|---------------|-------------------|---------|--------------|-------------|
| Orca pt1 packed   | 256        | 3e-5          | Cosine to 3e-6    | 100     | 1e-6         | (0.9, 0.95) |
| Orca pt2 unpacked | 512        | 3e-5          | Cosine to 3e-6    | 100     | 1e-6         | (0.9, 0.95) |

## Ethical Considerations and Limitations

Beluga is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Beluga's potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Beluga, developers should perform safety testing and tuning tailored to their specific applications of the model.

## Citations

```bibtext
@misc{touvron2023llama,
      title={Llama 2: Open Foundation and Fine-Tuned Chat Models}, 
      author={Hugo Touvron and Louis Martin and Kevin Stone and Peter Albert and Amjad Almahairi and Yasmine Babaei and Nikolay Bashlykov and Soumya Batra and Prajjwal Bhargava and Shruti Bhosale and Dan Bikel and Lukas Blecher and Cristian Canton Ferrer and Moya Chen and Guillem Cucurull and David Esiobu and Jude Fernandes and Jeremy Fu and Wenyin Fu and Brian Fuller and Cynthia Gao and Vedanuj Goswami and Naman Goyal and Anthony Hartshorn and Saghar Hosseini and Rui Hou and Hakan Inan and Marcin Kardas and Viktor Kerkez and Madian Khabsa and Isabel Kloumann and Artem Korenev and Punit Singh Koura and Marie-Anne Lachaux and Thibaut Lavril and Jenya Lee and Diana Liskovich and Yinghai Lu and Yuning Mao and Xavier Martinet and Todor Mihaylov and Pushkar Mishra and Igor Molybog and Yixin Nie and Andrew Poulton and Jeremy Reizenstein and Rashi Rungta and Kalyan Saladi and Alan Schelten and Ruan Silva and Eric Michael Smith and Ranjan Subramanian and Xiaoqing Ellen Tan and Binh Tang and Ross Taylor and Adina Williams and Jian Xiang Kuan and Puxin Xu and Zheng Yan and Iliyan Zarov and Yuchen Zhang and Angela Fan and Melanie Kambadur and Sharan Narang and Aurelien Rodriguez and Robert Stojnic and Sergey Edunov and Thomas Scialom},
      year={2023},
      eprint={2307.09288},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```bibtext
@misc{mukherjee2023orca,
      title={Orca: Progressive Learning from Complex Explanation Traces of GPT-4}, 
      author={Subhabrata Mukherjee and Arindam Mitra and Ganesh Jawahar and Sahaj Agarwal and Hamid Palangi and Ahmed Awadallah},
      year={2023},
      eprint={2306.02707},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```