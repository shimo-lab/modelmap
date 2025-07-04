
# Llama-2-7B-ft-instruct-es

[Llama 2 (7B)](https://huggingface.co/meta-llama/Llama-2-7b) fine-tuned on [Clibrain](https://huggingface.co/clibrain)'s  Spanish instructions dataset.


## Model Details

Llama 2 is a collection of pre-trained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. This is the repository for the 7B pre-trained model. Links to other models can be found in the index at the bottom.


## Example of Usage

```py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

model_id = "clibrain/Llama-2-7b-ft-instruct-es"

model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to("cuda")
tokenizer = AutoTokenizer.from_pretrained(model_id)

def create_instruction(instruction, input_data=None, context=None):
    sections = {
        "Instrucción": instruction,
        "Entrada": input_data,
        "Contexto": context,
    }

    system_prompt = "A continuación hay una instrucción que describe una tarea, junto con una entrada que proporciona más contexto. Escriba una respuesta que complete adecuadamente la solicitud.\n\n"
    prompt = system_prompt

    for title, content in sections.items():
        if content is not None:
            prompt += f"### {title}:\n{content}\n\n"

    prompt += "### Respuesta:\n"

    return prompt


def generate(
        instruction,
        input=None,
        context=None,
        max_new_tokens=128,
        temperature=0.1,
        top_p=0.75,
        top_k=40,
        num_beams=4,
        **kwargs
):
    
    prompt = create_instruction(instruction, input, context)
    print(prompt.replace("### Respuesta:\n", ""))
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].to("cuda")
    attention_mask = inputs["attention_mask"].to("cuda")
    generation_config = GenerationConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        num_beams=num_beams,
        **kwargs,
    )
    with torch.no_grad():
        generation_output = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            generation_config=generation_config,
            return_dict_in_generate=True,
            output_scores=True,
            max_new_tokens=max_new_tokens,
            early_stopping=True
        )
    s = generation_output.sequences[0]
    output = tokenizer.decode(s)
    return output.split("### Respuesta:")[1].lstrip("\n")

instruction = "Dame una lista de lugares a visitar en España."
print(generate(instruction))
```
## Example of Usage with `pipelines`

```py
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline 

model_id = "clibrain/Llama-2-7b-ft-instruct-es"

model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to("cuda")
tokenizer = AutoTokenizer.from_pretrained(model_id)

pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200, device=0)

prompt = """
A continuación hay una instrucción que describe una tarea. Escriba una respuesta que complete adecuadamente la solicitud.
### Instrucción:
Dame una lista de 5 lugares a visitar en España.

### Respuesta:
"""

result = pipe(prompt)
print(result[0]['generated_text'])
```