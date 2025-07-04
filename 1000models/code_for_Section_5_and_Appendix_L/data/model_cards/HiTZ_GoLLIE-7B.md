
<p align="center">
    <br>
    <img src="https://github.com/hitz-zentroa/GoLLIE/raw/main/assets/GoLLIE.png" style="height: 250px;">
    <h2 align="center"><b>G</b>uideline f<b>o</b>llowing <b>L</b>arge <b>L</b>anguage Model for <b>I</b>nformation <b>E</b>xtraction</h2>
    <br>


# Model Card for GoLLIE 7B


<p align="justify">
We present GoLLIE, a Large Language Model trained to follow annotation guidelines. GoLLIE outperforms previous approaches on zero-shot Information Extraction and allows the user to perform inferences with annotation schemas defined on the fly. Different from previous approaches, GoLLIE is able to follow detailed definitions and does not only rely on the knowledge already encoded in the LLM. 

- 💻 Code: [https://github.com/osainz59/CoLLIE/](https://github.com/hitz-zentroa/GoLLIE)
- 📒 Blog Post: [GoLLIE: Guideline-following Large Language Model for Information Extraction](https://hitz-zentroa.github.io/GoLLIE/)
- 📖 Paper: [GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction](https://arxiv.org/abs/2310.03668)
- 🐕 GoLLIE Colection in the 🤗HuggingFace Hub: [HiTZ/gollie](https://huggingface.co/collections/HiTZ/gollie-651bf19ee315e8a224aacc4f)
- 🚀 Example Jupyter Notebooks: [GoLLIE Notebooks](https://github.com/hitz-zentroa/GoLLIE/tree/main/notebooks)
</p>

<p align="center">
<img src="https://github.com/hitz-zentroa/GoLLIE/raw/main/assets/zero_shot_results.png">
</p>


### Model Description

- **Developed by:** [Oscar Sainz](https://osainz59.github.io/), [Iker García-Ferrero](https://ikergarcia1996.github.io/Iker-Garcia-Ferrero/), [Rodrigo Agerri](https://ragerri.github.io/), [Oier Lopez de Lacalle](https://oierldl.github.io/), [German Rigau](https://adimen.si.ehu.es/~rigau/) and [Eneko Agirre](https://eagirre.github.io/)
- **Institution:** [HiTZ Basque Center for Language Technology](http://www.hitz.eus/) - [Ixa](https://www.ixa.eus/node/2?language=en), [University of the Basque Country UPV/EHU](https://www.ehu.eus/en/en-home)
- **Model type:** Text Generation 
- **Language(s) (NLP):** English
- **License:** LLaMA2 License for the base and merged model. Apache 2.0 for pre-trained LoRA Adapters
- **Finetuned from model:** CODE-LLaMA2



## Schema definition and inference example

The labels are represented as Python classes, and the guidelines or instructions are introduced as docstrings. The model start generating after the `result = [` line.
```Python
# Entity definitions
@dataclass
class Launcher(Template):
    """Refers to a vehicle designed primarily to transport payloads from the Earth's 
    surface to space. Launchers can carry various payloads, including satellites, 
    crewed spacecraft, and cargo, into various orbits or even beyond Earth's orbit. 
    They are usually multi-stage vehicles that use rocket engines for propulsion."""

    mention: str  
    """
    The name of the launcher vehicle. 
    Such as: "Sturn V", "Atlas V", "Soyuz", "Ariane 5"
    """
    space_company: str # The company that operates the launcher. Such as: "Blue origin", "ESA", "Boeing", "ISRO", "Northrop Grumman", "Arianespace"
    crew: List[str] # Names of the crew members boarding the Launcher. Such as: "Neil Armstrong", "Michael Collins", "Buzz Aldrin"
    

@dataclass
class Mission(Template):
    """Any planned or accomplished journey beyond Earth's atmosphere with specific objectives, 
    either crewed or uncrewed. It includes missions to satellites, the International 
    Space Station (ISS), other celestial bodies, and deep space."""
    
    mention: str
    """
    The name of the mission. 
    Such as: "Apollo 11", "Artemis", "Mercury"
    """
    date: str # The start date of the mission
    departure: str # The place from which the vehicle will be launched. Such as: "Florida", "Houston", "French Guiana"
    destination: str # The place or planet to which the launcher will be sent. Such as "Moon", "low-orbit", "Saturn"

# This is the text to analyze
text = (
    "The Ares 3 mission to Mars is scheduled for 2032. The Starship rocket build by SpaceX will take off from Boca Chica,"
    "carrying the astronauts Max Rutherford, Elena Soto, and Jake Martinez."
)

# The annotation instances that take place in the text above are listed here
result = [
    Mission(mention='Ares 3', date='2032', departure='Boca Chica', destination='Mars'),
    Launcher(mention='Starship', space_company='SpaceX', crew=['Max Rutherford', 'Elena Soto', 'Jake Martinez'])
]
```

## How to Get Started with the Model

Please read our [🚀 Example Jupyter Notebooks](https://github.com/hitz-zentroa/GoLLIE/tree/main/notebooks) to get started with GoLLIE. 

The best way to load the model is using our custom `load_model` fuction. However, you can also load them using the AutoModelForCausalLM class.

**Important**: Our flash attention implementation has small numerical differences compared to the attention implementation in Huggingface.
You must use the flag `trust_remote_code=True` or you will get inferior results. Flash attention requires an available CUDA GPU. Running GOLLIE 
pre-trained models on a CPU is not supported. We plan to address this in future releases. First, install flash attention 2:
```bash
pip install flash-attn --no-build-isolation
pip install git+https://github.com/HazyResearch/flash-attention.git#subdirectory=csrc/rotary
```

Then you can load the model using

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("HiTZ/GoLLIE-7B")
model = AutoModelForCausalLM.from_pretrained("HiTZ/GoLLIE-7B", trust_remote_code=True, torch_dtype=torch.bfloat16)
model.to("cuda")
```

Read our [🚀 Example Jupyter Notebooks](https://github.com/hitz-zentroa/GoLLIE/tree/main/notebooks) to learn how to easily define guidelines, generate model inputs and parse the output! 



### Training Data

This is the list of task used for training and evaluating GoLLIE. However, as demonstrated in the  🚀 [Create Custom Task notebook](https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Create%20Custom%20Task.ipynb) GoLLIE can perform a wide range of unseen tasks. 
For more info, read our [📖Paper](https://arxiv.org/abs/2310.03668).

<p align="center">
<img src="https://github.com/hitz-zentroa/GoLLIE/raw/main/assets/datasets.png">
</p>


## Evaluation

| Model | Supervised average F1 | Zero-shot average F1 |                     🤗HuggingFace Hub                     |
|---|:---------------------:|:--------------------:|:---------------------------------------------------------:|
| GoLLIE-7B |         73.0          |         55.3         |  [HiTZ/GoLLIE-7B](https://huggingface.co/HiTZ/GoLLIE-7B)  |
| GoLLIE-13B |         73.9          |         56.0         | [HiTZ/GoLLIE-13B](https://huggingface.co/HiTZ/GoLLIE-13B) |
| GoLLIE-34B |       **75.0**        |       **57.2**       | [HiTZ/GoLLIE-34B](https://huggingface.co/HiTZ/GoLLIE-34B) |


## Environmental Impact

| Model | Hardware | FLOPs            | Time (h) | CO<sup>2</sup>eq (kg) |
|----------------|-------------------|---------------------------|-------------------|-------------------------------------|
| GoLLIE 7B       | 1xA100            | 11.9e<sup>18</sup> | 44.5              | 1.57                                |
| GoLLIE 13B    | 1xA100            | 22.7e<sup>18</sup> | 79.5              | 2.80                                |
| GoLLIE 34B    | 2xA100            | 55.8e<sup>18</sup> | 94.6              | 6.67                                |



## Citation
```
@misc{sainz2023gollie,
      title={GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction}, 
      author={Oscar Sainz and Iker García-Ferrero and Rodrigo Agerri and Oier Lopez de Lacalle and German Rigau and Eneko Agirre},
      year={2023},
      eprint={2310.03668},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```