# Model Card for Cymist2-v0.2-SFT
### Model Description

Cymist2-v0.2 is a cutting-edge language model developed by the Cypien AI Team, optimized for text-generation tasks. The model leverages the transformers library and is available under the Apache-2.0 license.

- **Developed by:** Cypien AI Team
- **Model type:** Language Model for Text-Generation
- **Language(s) (NLP):** Turkish, English
- **License:** Apache-2.0
- **Finetuned from model**: mistralai/Mistral-7B-v0.1


### Direct Use

This model is designed for direct use in general applications requiring Turkish language understanding, RAG and text-generation capabilities. It can be integrated into chatbots, virtual assistants, and other AI systems where understanding and generating human-like responses are essential.

### Out-of-Scope Use

The model is not intended for use in critical systems where incorrect answers could lead to harm or in contexts that require domain-specific knowledge beyond the scope of general text-generation.

## Bias, Risks, and Limitations

The model, like all AI models, may inherit biases from its training data. Users should be aware of these potential biases and consider them when integrating the model into applications.


```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "cypienai/cymist2-v02-SFT"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token_id = tokenizer.eos_token_id
```
## Use Flash-Attention 2 to further speed-up generation

First make sure to install flash-attn. Refer to the original repository of Flash Attention regarding that package installation. Simply change the snippet above with:

```python
model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        attn_implementation="flash_attention_2"
        )
```

# Example usage

Here's the prompt template for this model:


```python
question="Yenilenebilir gıdalar nelerdir ?"
prompt= f"[INST] {question} [/INST]"

with torch.inference_mode():
  input_ids = tokenizer(prompt, return_tensors="pt").to(device)
  output = model.generate(**input_ids, max_new_tokens=8096)
  decoded_output = tokenizer.decode(output[0], skip_special_tokens=False)
  print(decoded_output)
``` 


## Training Details

### Training Data

The model was trained on a diverse set of Turkish & English language sources, encompassing a wide range of topics to ensure comprehensive language understanding.

### Training Procedure

#### Preprocessing

The training data underwent standard NLP preprocessing steps, including tokenization, normalization, and possibly data augmentation to enhance the model's robustness.


## Environmental Impact

The training of Cymist2-v0.1-SFT was conducted with a focus on minimizing carbon emissions. Detailed carbon emission statistics will be provided based on the Machine Learning Impact calculator, considering hardware type, usage hours, cloud provider, compute region, and total emissions.

0.93 kg of CO2eq

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

## Technical Specifications

More detailed technical specifications, including model architecture, compute infrastructure, hardware, and software, will be provided to offer insights into the model's operational context.

## Citation

When citing this model in your research, please refer to this model card for information about the model's development and capabilities.

## Glossary

A glossary section can be added to define specific terms and calculations related to the model, ensuring clarity for all potential users.

## More Information [optional]

For more information or inquiries about the model, please contact the Cypien AI Team.

## Model Card Contact

info@cypien.ai

CypienAI team