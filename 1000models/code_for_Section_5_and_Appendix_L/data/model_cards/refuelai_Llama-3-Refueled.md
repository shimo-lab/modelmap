<div style="width: auto; margin-left: auto; margin-right: auto; background-color:black">
<img src="https://assets-global.website-files.com/6423879a8f63c1bb18d74bfa/648818d56d04c3bdf36d71ab_Refuel_rev8-01_ts-p-1600.png" alt="Refuel.ai" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>

## Model Details

RefuelLLM-2-small, aka Llama-3-Refueled, is a Llama3-8B base model instruction tuned on a corpus of 2750+ datasets, spanning tasks such as classification, reading comprehension, structured attribute extraction and entity resolution. We're excited to open-source the model for the community to build on top of. 

* More details about [RefuelLLM-2 family of models](https://www.refuel.ai/blog-posts/announcing-refuel-llm-2)
* You can also try out the models in our [LLM playground](https://labs.refuel.ai/playground)

**Model developers** - Refuel AI

**Input** - Text only.

**Output** - Text only.

**Architecture** - Llama-3-Refueled is built on top of Llama-3-8B-instruct which is an auto-regressive language model that uses an optimized transformer architecture. 

**Release Date** - May 8, 2024.

**License** - [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en)

## How to use

This repository contains weights for Llama-3-Refueled that are compatible for use with HuggingFace. See the snippet below for usage with Transformers:

```python
>>> import torch
>>> from transformers import AutoModelForCausalLM, AutoTokenizer

>>> model_id = "refuelai/Llama-3-Refueled"
>>> tokenizer = AutoTokenizer.from_pretrained(model_id)
>>> model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")

>>> messages = [{"role": "user", "content": "Is this comment toxic or non-toxic: RefuelLLM is the new way to label text data!"}]

>>> inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to("cuda")

>>> outputs = model.generate(inputs, max_new_tokens=20)
>>> print(tokenizer.decode(outputs[0]))
```

## Training Data

The model was both trained on over 4 Billion tokens, spanning 2750+ NLP tasks. Our training collection consists majorly of:
1. Human annotated datasets like Flan, Task Source, and the Aya collection 
2. Synthetic datasets like OpenOrca, OpenHermes and WizardLM
3. Proprietary datasets developed or licensed by Refuel AI

## Benchmarks 

In this section, we report the results for Refuel models on our benchmark of labeling tasks. For details on the methodology see [here](https://refuel.ai/blog-posts/announcing-refuel-llm-2).

<table>
<tr></tr>
<tr><th>Provider</th><th>Model</th><th colspan="4" style="text-align: center">LLM Output Quality (by task type)</tr>
<tr><td></td><td></td><td>Overall</td><td>Classification</td><td>Reading Comprehension</td><td>Structure Extraction</td><td>Entity Matching</td><td></td></tr>
<tr><td>Refuel</td><td>RefuelLLM-2</td><td>83.82%</td><td>84.94%</td><td>76.03%</td><td>88.16%</td><td>92.00%</td><td></td></tr>
<tr><td>OpenAI</td><td>GPT-4-Turbo</td><td>80.88%</td><td>81.77%</td><td>72.08%</td><td>84.79%</td><td>97.20%</td><td></td></tr>
<tr><td>Refuel</td><td>RefuelLLM-2-small (Llama-3-Refueled)</td><td>79.67%</td><td>81.72%</td><td>70.04%</td><td>84.28%</td><td>92.00%</td><td></td></tr>
<tr><td>Anthropic</td><td>Claude-3-Opus</td><td>79.19%</td><td>82.49%</td><td>67.30%</td><td>88.25%</td><td>94.96%</td><td></td></tr>
<tr><td>Meta</td><td>Llama3-70B-Instruct</td><td>78.20%</td><td>79.38%</td><td>66.03%</td><td>85.96%</td><td>94.13%</td><td></td></tr>
<tr><td>Google</td><td>Gemini-1.5-Pro</td><td>74.59%</td><td>73.52%</td><td>60.67%</td><td>84.27%</td><td>98.48%</td><td></td></tr>
<tr><td>Mistral</td><td>Mixtral-8x7B-Instruct</td><td>62.87%</td><td>79.11%</td><td>45.56%</td><td>47.08%</td><td>86.52%</td><td></td></tr>
<tr><td>Anthropic</td><td>Claude-3-Sonnet</td><td>70.99%</td><td>79.91%</td><td>45.44%</td><td>78.10%</td><td>96.34%</td><td></td></tr>
<tr><td>Anthropic</td><td>Claude-3-Haiku</td><td>69.23%</td><td>77.27%</td><td>50.19%</td><td>84.97%</td><td>54.08%</td><td></td></tr>
<tr><td>OpenAI</td><td>GPT-3.5-Turbo</td><td>68.13%</td><td>74.39%</td><td>53.21%</td><td>69.40%</td><td>80.41%</td><td></td></tr>
<tr><td>Meta</td><td>Llama3-8B-Instruct</td><td>62.30%</td><td>68.52%</td><td>49.16%</td><td>65.09%</td><td>63.61%</td><td></td></tr>
</table>


## Limitations

The Llama-3-Refueled does not have any moderation mechanisms. We're looking forward to engaging with the community 
on ways to make the model finely respect guardrails, allowing for deployment in environments requiring moderated outputs.