<img src="https://cdn-uploads.huggingface.co/production/uploads/5df8bb21da6d0311fd3d540f/xL6Ax1I34qfC4VPKEFA6Z.png" alt="llamantino3_anita" border="0" width="800px">

<hr>
<!--<img src="https://i.ibb.co/6mHSRm3/llamantino53.jpg" width="200"/>-->
<h3><i>"Built with <b>Meta Llama 3</b>".</i></i></h3>
<p style="text-align:justify;"><b>LLaMAntino-3-ANITA-8B-Inst-DPO-ITA</b> is a model of the <a href="https://huggingface.co/swap-uniba"><b>LLaMAntino</b></a> - <i>Large Language Models family</i>.
The model is an instruction-tuned version of <a href="https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct"><b>Meta-Llama-3-8b-instruct</b></a> (a fine-tuned <b>LLaMA 3 model</b>).
This model version aims to be the a <b>Multilingual Model</b> 🏁  (EN 🇺🇸 + ITA🇮🇹) to further fine-tuning on Specific Tasks in Italian.</p>


The 🌟**ANITA project**🌟 *(**A**dvanced **N**atural-based interaction for the **ITA**lian language)*
wants to provide Italian NLP researchers with an improved model for the Italian Language 🇮🇹 use cases.<br>

<hr>

**Live DEMO:** [https://chat.llamantino.it/](https://chat.llamantino.it/)<br>
*It works only with Italian connection.*

<hr>

## Model Details
*Last Update: 10/05/2024*<br>

<a href="https://github.com/marcopoli/LLaMAntino-3-ANITA"><img src="https://github.githubassets.com/assets/GitHub-Logo-ee398b662d42.png" width="150"> https://github.com/marcopoli/LLaMAntino-3-ANITA</a><br>

| Model | HF   | GGUF   | EXL2   |
|-------|-------|-------|-------|
| *swap-uniba/LLaMAntino-3-ANITA-8B-Inst-DPO-ITA* | [Link](https://huggingface.co/swap-uniba/LLaMAntino-3-ANITA-8B-Inst-DPO-ITA) | [Link](https://huggingface.co/swap-uniba/LLaMAntino-3-ANITA-8B-Inst-DPO-ITA_GGUF) | [Link](https://huggingface.co/swap-uniba/LLaMAntino-3-ANITA-8B-Inst-DPO-ITA_EXL2) |

<hr>

## Specifications

- **Model developers**: <br><a href="https://marcopoli.github.io/">Ph.D. Marco Polignano</a> - University of Bari Aldo Moro, Italy <br> <a href="https://huggingface.co/swap-uniba">SWAP Research Group</a> <br>
- **Variations**: The model release has been **supervised fine-tuning (SFT)** using **QLoRA** 4bit, on instruction-based datasets. **DPO** approach over the *mlabonne/orpo-dpo-mix-40k* dataset is used to align with human preferences for helpfulness and safety.
- **Input**: Models input text only.
- **Language**: Multilingual 🏁 + Italian 🇮🇹
- **Output**: Models generate text and code only.
- **Model Architecture**: *Llama 3 architecture*.
- **Context length**: 8K, 8192.
- **Library Used**: [Unsloth](https://unsloth.ai/)
<hr>

## Playground

To use the model directly, there are many ways to get started, choose one of the following ways to experience it.

### Prompt Template
```
<|start_header_id|>system<|end_header_id|>

{ SYS Prompt }<|eot_id|><|start_header_id|>user<|end_header_id|>

{ USER Prompt }<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{ ASSIST Prompt }<|eot_id|>
````

### Transformers

For direct use with `transformers`, you can easily get started with the following steps.

- Firstly, you need to install transformers via the command below with `pip`.

  ```bash
  pip install -U transformers trl peft accelerate bitsandbytes
  ```

- Right now, you can start using the model directly.

  ```python
  import torch
  from transformers import (
      AutoModelForCausalLM,
      AutoTokenizer,
  )
  
  base_model = "swap-uniba/LLaMAntino-3-ANITA-8B-Inst-DPO-ITA"
  model = AutoModelForCausalLM.from_pretrained(
      base_model,
      torch_dtype=torch.bfloat16,
      device_map="auto",
  )
  tokenizer = AutoTokenizer.from_pretrained(base_model)
  
  sys = "Sei un an assistente AI per la lingua Italiana di nome LLaMAntino-3 ANITA " \
      "(Advanced Natural-based interaction for the ITAlian language)." \
      " Rispondi nella lingua usata per la domanda in modo chiaro, semplice ed esaustivo."
  
  messages = [
      {"role": "system", "content": sys},
      {"role": "user", "content": "Chi è Carlo Magno?"}
  ]

  #Method 1
  prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
  inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
  for k,v in inputs.items():
      inputs[k] = v.cuda()
  outputs = model.generate(**inputs, max_new_tokens=512, do_sample=True, top_p=0.9, temperature=0.6)
  results = tokenizer.batch_decode(outputs)[0]
  print(results)

  #Method 2
  import transformers
  pipe = transformers.pipeline(
      model=model,
      tokenizer=tokenizer,
      return_full_text=False, # langchain expects the full text
      task='text-generation',
      max_new_tokens=512, # max number of tokens to generate in the output
      temperature=0.6,  #temperature for more or less creative answers
      do_sample=True,
      top_p=0.9,
  )

  sequences = pipe(messages)
  for seq in sequences:
      print(f"{seq['generated_text']}")
  
  ```

- Additionally, you can also use a model with **4bit quantization** to reduce the required resources at least. You can start with the code below.

  ```python
  import torch
  from transformers import (
      AutoModelForCausalLM,
      AutoTokenizer,
      BitsAndBytesConfig,
  )

  base_model = "swap-uniba/LLaMAntino-3-ANITA-8B-Inst-DPO-ITA"
  bnb_config = BitsAndBytesConfig(
      load_in_4bit=True,
      bnb_4bit_quant_type="nf4",
      bnb_4bit_compute_dtype=torch.bfloat16,
      bnb_4bit_use_double_quant=False,
  )
  model = AutoModelForCausalLM.from_pretrained(
      base_model,
      quantization_config=bnb_config,
      device_map="auto",
  )
  tokenizer = AutoTokenizer.from_pretrained(base_model)

  sys = "Sei un an assistente AI per la lingua Italiana di nome LLaMAntino-3 ANITA " \
      "(Advanced Natural-based interaction for the ITAlian language)." \
      " Rispondi nella lingua usata per la domanda in modo chiaro, semplice ed esaustivo."
  
  messages = [
      {"role": "system", "content": sys},
      {"role": "user", "content": "Chi è Carlo Magno?"}
  ]

  #Method 1
  prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
  inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
  for k,v in inputs.items():
      inputs[k] = v.cuda()
  outputs = model.generate(**inputs, max_new_tokens=512, do_sample=True, top_p=0.9, temperature=0.6)
  results = tokenizer.batch_decode(outputs)[0]
  print(results)

  #Method 2
  import transformers
  pipe = transformers.pipeline(
      model=model,
      tokenizer=tokenizer,
      return_full_text=False, # langchain expects the full text
      task='text-generation',
      max_new_tokens=512, # max number of tokens to generate in the output
      temperature=0.6,  #temperature for more or less creative answers
      do_sample=True,
      top_p=0.9,
  )

  sequences = pipe(messages)
  for seq in sequences:
      print(f"{seq['generated_text']}")

  ```

<hr>

## Evaluation

**Open LLM Leaderboard:**

Evaluated with lm-evaluation-benchmark-harness for the [**Open Italian LLMs Leaderboard**](https://huggingface.co/spaces/FinancialSupport/open_ita_llm_leaderboard)
```
   lm_eval --model hf --model_args pretrained=HUGGINGFACE_MODEL_ID  --tasks hellaswag_it,arc_it  --device cuda:0 --batch_size auto:2
   lm_eval --model hf --model_args pretrained=HUGGINGFACE_MODEL_ID  --tasks m_mmlu_it --num_fewshot 5  --device cuda:0 --batch_size auto:2 
```

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | **0.6160**  |
| Arc_IT         | 0.5714 |
| Hellaswag_IT    | 0.7093 |
| MMLU_IT          | 0.5672 |

<hr>

## Unsloth

<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/made with unsloth.png" width="200px" align="center" />

[Unsloth](https://unsloth.ai), a great tool that helps us easily develop products, at a lower cost than expected.

## Citation instructions
```bibtex
@misc{polignano2024advanced,
      title={Advanced Natural-based interaction for the ITAlian language: LLaMAntino-3-ANITA}, 
      author={Marco Polignano and Pierpaolo Basile and Giovanni Semeraro},
      year={2024},
      eprint={2405.07101},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```bibtex
@misc{basile2023llamantino,
      title={LLaMAntino: LLaMA 2 Models for Effective Text Generation in Italian Language}, 
      author={Pierpaolo Basile and Elio Musacchio and Marco Polignano and Lucia Siciliani and Giuseppe Fiameni and Giovanni Semeraro},
      year={2023},
      eprint={2312.09993},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```bibtex
@article{llama3modelcard,
  title={Llama 3 Model Card},
  author={AI@Meta},
  year={2024},
  url = {https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md}
}
```

# Acknowledgments
We acknowledge the support of the PNRR project [FAIR - Future AI Research (PE00000013)](https://fondazione-fair.it/en/foundation/), Spoke 6 - Symbiotic AI (CUP H97G22000210007) under the NRRP MUR program funded by the NextGenerationEU.
Models are built on the Leonardo supercomputer with the support of CINECA-Italian Super Computing Resource Allocation, class C project IscrC\_Pro\_MRS (HP10CQO70G).
<img src="https://wiki.u-gov.it/confluence/download/attachments/49842317/image2022-6-21_11-11-44.png?version=1&modificationDate=1655802705000&api=v2" width="600px">
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_swap-uniba__LLaMAntino-3-ANITA-8B-Inst-DPO-ITA)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |75.12|
|AI2 Reasoning Challenge (25-Shot)|74.57|
|HellaSwag (10-Shot)              |92.75|
|MMLU (5-Shot)                    |66.85|
|TruthfulQA (0-shot)              |75.93|
|Winogrande (5-shot)              |82.00|
|GSM8k (5-shot)                   |58.61|

