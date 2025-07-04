# Orca Mini v2 German 7b

`orca_mini_v2_ger_7b` is a variant of [Pankaj Mathur´s](https://huggingface.co/psmathur) [Orca Mini V2 7b](https://huggingface.co/psmathur/orca_mini_v2_7b) model, finetuned on an additional dataset in German language. 
The original model has been trained on explain tuned datasets, created using instructions and input from WizardLM, Alpaca & Dolly-V2 datasets and applying Orca Research Paper dataset construction approaches.

This model is optimized for German text, providing proficiency in understanding, generating, and interacting with German language content.
However the model is not yet fully optimized for German language, as it has been trained on a small, experimental dataset and has limited capabilities due to the small parameter count. 

I am working on improving the model´s capabilities and will update the model if there is sufficient interest.

A quantized GGML version for use with llama.cpp, kobold.cpp and other GUIs for CPU inference can be found [here](https://huggingface.co/jphme/orca_mini_v2_ger_7b-GGML).

# Results

I did only evaluate the output on a small, handcrafted sample on test prompts in German, confirming that the model's ability to understand and generate German text is well above the base model. 

## Example Output

System prompt and question:
```
### System:
You are an AI assistant that follows instruction extremely well. Help as much as you can. If the user speaks German, please also answer in German.

### User:
Wenn du 2024 für das Amt des Präsidenten der Vereinigten Staaten kandidieren würdest, was wäre dein Programm?
```

Response original orca_mini_v2_7b:
```
### Response:
If you run for the office of President of the United States in 2024, what would your program be?
```

**Response orca_mini_v2_ger_7b:**
```
### Response:
Als Kandidat für das Amt des Präsidenten der Vereinigten Staaten in der Wahl von 2024 würde mein Programm folgende Schwerpunkte haben:

1. Wirtschaftliche Gerechtigkeit: Ich würde die Reichtumsverteilung neu verstehen und die Möglichkeit für jeden Amerikaner, eine erfolgreiche und sorgenfreie Existenz zu führen, fördern. Ich würde einen Anstrich von Steuern für mehr Gerechtigkeit schaffen und die Ausgaben für Wohlfahrt und Bildung erhöhen.
2. Klimaschutz: Als Präsident würde ich eine umfassende und einschneidende Strategie zur Bekämpfung des Klimawandels einschlagen, die einen vollständigen Rückzug aus den Rohstoff- und Kohle-Geschäften, die Verringerung von Treibhausgasemissionen und die Förderung erneuerbarer Energien umfasst.
3. Gesundheitliche Sicherheit: Ich würde eine umfassende Gesundheitsreform implementieren, die die Einführung eines universellen Gesundheitsplans, die Verbesserung der Lebensqualität und die Bekämpfung der Armut vorantreibt.
4. Bildung: Die Bildung ist entscheidend für den Aufstieg und die Entwicklung jedes Individuums und der wirtschaftlichen Gemeinschaft. Ich würde die finanzielle Unterstützung für Bildung und Forschung erhöhen, den Zugang zu Bildungsmöglichkeiten für alle betreiben und die Bedeutung der Geisteswissenschaften stärken.
5. Gleichstellung und Rechte: Als Präsident würde ich die Rechte und Chancen für Frauen, Afroamerikaner, LGBT-Menschen und Menschen mit Behinderungen verbessern. Ich würde die Polizei reformieren, Strafverfolgung und Inhaftierung neu regeln und die Rechte von Gefangenen sicherstellen.
6. Außenpolitik: Als Präsident würde ich eine neue Strategie zur Bekämpfung von Terrorismus, die humanitärem Verhalten und diplomatischer Lösungen folgt, anstelle von militärischer Gewalt. Außerdem würde ich den Umweltsünderstaaten ausweichen, die aus der COVID-19-Pandemie profitieren, und die Möglichkeiten für eine globale Zusammenarbeit und Kooperation fördern.
7. Umweltschutz: Ich würde die Umsetzung einer energieeffizienten und umweltfreundlicheren Wirtschaft forcieren, die den Einsatz erneuerbarer Energien und die Bekämpfung von Luftverschmutzung und Wasserschutz priorisiert.
8. Arbeitsmarkt und Arbeitslosigkeit: Ich würde ein umfassendes Jobsprogramm implementieren, das die Verbesserung der Arbeitsmarkttiefe, die Unterstützung für kleine Betriebe und die Förderung von Bildungsmöglichkeiten für Jugendliche umfasst. Zudem würde ich die Gesetze und Regeln zur Arbeit für mehr Gerechtigkeit und fairere Arbeitsbedingungen reformieren.

Mein Ziel als Präsident wäre es, die amerikanische Bevölkerung zu einem gemeinsamen Versprechen für ein besseres Leben und eine bessere Zukunft zu ermutigen und unsere Vorurteile zu überwinden, um eine brüderlichere und gerechtere Gesellschaft zu schaffen.
```

## Evaluation
For systematic evaluation results of the base model, see [here](https://huggingface.co/psmathur/orca_mini_v2_7b#evaluation).

# Dataset

I used a proprietary, small and handcrafted finetuning set of instructions in German language from public sources. The dataset is not yet available for public use.

# Training

The model was trained on a A100 GPU at LambdaLabs with a [customized Version](https://github.com/OpenAccess-AI-Collective/axolotl/pull/263) of the [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) library.

# Prompt Format

The `orca_mini_v2_ger_7b` follows the same prompt format as the original model, however I didn't use the optional `### Input` field.
This format an be used e.g. for the [Oobabooga Text generation UI ](https://github.com/oobabooga/text-generation-webui) or other downstream uses:

```
### System:
{system}

### User:
{instruction}

### Response:
```

## Use with tranformers

Unchanged from the base model:

```python
import torch
from transformers import LlamaForCausalLM, LlamaTokenizer

# Hugging Face model_path
model_path = 'jphme/orca_mini_v2_ger_7b'
tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float16, device_map='auto',
)


#generate text function
def generate_text(system, instruction, input=None):
    
    if input:
        prompt = f"### System:\n{system}\n\n### User:\n{instruction}\n\n### Input:\n{input}\n\n### Response:\n"
    else:
        prompt = f"### System:\n{system}\n\n### User:\n{instruction}\n\n### Response:\n"
    
    tokens = tokenizer.encode(prompt)
    tokens = torch.LongTensor(tokens).unsqueeze(0)
    tokens = tokens.to('cuda')

    instance = {'input_ids': tokens,'top_p': 1.0, 'temperature':0.7, 'generate_len': 1024, 'top_k': 50}

    length = len(tokens[0])
    with torch.no_grad():
        rest = model.generate(
            input_ids=tokens, 
            max_length=length+instance['generate_len'], 
            use_cache=True, 
            do_sample=True, 
            top_p=instance['top_p'],
            temperature=instance['temperature'],
            top_k=instance['top_k']
        )    
    output = rest[0][length:]
    string = tokenizer.decode(output, skip_special_tokens=True)
    return f'[!] Response: {string}'

# Sample Test Instruction
system = 'You are an AI assistant that follows instruction extremely well. Help as much as you can. If the user speaks German, please also answer in German.'
instruction = 'Wenn du 2024 für das Amt des Präsidenten der Vereinigten Staaten kandidieren würdest, was wäre dein Programm?'
print(generate_text(system, instruction))

```

# Limitations & Biases

This model can produce factually incorrect output, and should not be relied on to produce factually accurate information.
This model was trained on various public datasets. While great efforts have been taken to clean the pretraining data, it is possible that this model could generate lewd, biased or otherwise offensive outputs.

# Disclaimer:

The license on this model does not constitute legal advice. I am not responsible for the actions of third parties who use this model.
This model should only be used for research purposes.

# Citation

Please cite the use of `orca_mini_v2_ger_7b` using the following BibTeX:
...

```
@misc{orca_mini_v2_ger_7b,
  author = {Jan Philipp Harries},
  title = {orca_mini_v2_ger_7b: An explain tuned LLaMA-7b model based on Orca Mini v2 and adapted to German language},
  year = {2023},
  publisher = {GitHub, HuggingFace},
  journal = {GitHub repository, HuggingFace repository},
  howpublished = {\url{https://https://huggingface.co/jphme/orca_mini_v2_ger_7b},
}
```
```
@misc{orca_mini_v2_7b,
  author = {Pankaj Mathur},
  title = {orca_mini_v2_7b: An explain tuned LLaMA-7b model on uncensored wizardlm, alpaca, & dolly datasets},
  year = {2023},
  publisher = {GitHub, HuggingFace},
  journal = {GitHub repository, HuggingFace repository},
  howpublished = {\url{https://https://huggingface.co/psmathur/orca_mini_v2_7b},
}
```
```
@software{touvron2023llama,
  title={LLaMA: Open and Efficient Foundation Language Models},
  author={Touvron, Hugo and Lavril, Thibaut and Izacard, Gautier and Martinet, Xavier and Lachaux, Marie-Anne and Lacroix, Timoth{\'e}e and Rozi{\`e}re, Baptiste and Goyal, Naman and Hambro, Eric and Azhar, Faisal and Rodriguez, Aurelien and Joulin, Armand and Grave, Edouard and Lample, Guillaume},
  journal={arXiv preprint arXiv:2302.13971},
  year={2023}
}
```
```
@misc{openalpaca,
  author = {Yixuan Su and Tian Lan and Deng Cai},
  title = {OpenAlpaca: A Fully Open-Source Instruction-Following Model Based On OpenLLaMA},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/yxuansu/OpenAlpaca}},
}
```
```
@misc{alpaca,
  author = {Rohan Taori and Ishaan Gulrajani and Tianyi Zhang and Yann Dubois and Xuechen Li and Carlos Guestrin and Percy Liang and Tatsunori B. Hashimoto },
  title = {Stanford Alpaca: An Instruction-following LLaMA model},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/tatsu-lab/stanford_alpaca}},
}
```
```
@online{DatabricksBlog2023DollyV2,
    author    = {Mike Conover and Matt Hayes and Ankit Mathur and Jianwei Xie and Jun Wan and Sam Shah and Ali Ghodsi and Patrick Wendell and Matei Zaharia and Reynold Xin},
    title     = {Free Dolly: Introducing the World's First Truly Open Instruction-Tuned LLM},
    year      = {2023},
    url       = {https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm},
    urldate   = {2023-06-30}
}
```
```
@misc{xu2023wizardlm,
      title={WizardLM: Empowering Large Language Models to Follow Complex Instructions}, 
      author={Can Xu and Qingfeng Sun and Kai Zheng and Xiubo Geng and Pu Zhao and Jiazhan Feng and Chongyang Tao and Daxin Jiang},
      year={2023},
      eprint={2304.12244},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```