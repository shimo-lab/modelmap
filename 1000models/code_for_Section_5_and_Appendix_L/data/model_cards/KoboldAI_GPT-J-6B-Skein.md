# Model Card for GPT-J-6B-Skein
  
# Model Details
 
## Model Description
 
 
- **Developed by:** KoboldAI
- **Shared by [Optional]:** KoboldAI
- **Model type:** Text Generation
- **Language(s) (NLP):** English
- **License:** Apache License 2.0
- **Related Models:** [GPT-J 6B](https://huggingface.co/EleutherAI/gpt-j-6B?text=My+name+is+Mariama%2C+my+favorite)
  - **Parent Model:**  GPT-J
- **Resources for more information:** 
    - [GitHub Repo](https://github.com/kingoflolz/mesh-transformer-jax)
    - [Associated Model Doc](https://huggingface.co/docs/transformers/main/en/model_doc/gptj#transformers.GPTJForCausalLM)
 
# Uses
 
 
## Direct Use
 
This model is designed for creative story generation. It can understand both free-form text and text written in interactive fiction style with actions starting with "> You", such as:

```
You become aware of her breathing -- the slight expansion of her ribs, the soft exhalation -- natural, and yet somehow studied. "Ah -- by the way," she says, in a way that utterly fails to be casual, "have you seen the artist out there? -- My artist, that is."

"No," you respond, uneasy. You open your mouth and close it again.

> You ask about the experience of waking up
```
 
## Downstream Use [Optional]
 
More information needed
 
## Out-of-Scope Use
 
The model should not be used to intentionally create hostile or alienating environments for people.
 
# Bias, Risks, and Limitations
The core functionality of GPT-J is taking a string of text and predicting the next token. While language models are widely used for tasks other than this, there are a lot of unknowns with this work. When prompting GPT-J it is important to remember that the statistically most likely next token is often not the token that produces the most "accurate" text. Never depend upon GPT-J to produce factually accurate output.
GPT-J was trained on the Pile, a dataset known to contain profanity, lewd, and otherwise abrasive language. Depending upon use case GPT-J may produce socially unacceptable text. See Sections 5 and 6 of the Pile paper for a more detailed analysis of the biases in the Pile.
As with all language models, it is hard to predict in advance how GPT-J will respond to particular prompts and offensive content may occur without warning. We recommend having a human curate or filter the outputs before releasing them, both to censor undesirable content and to improve the quality of the results.
 
See the [GPT-J 6B model card](https://huggingface.co/EleutherAI/gpt-j-6B?text=My+name+is+Mariama%2C+my+favorite) for more information.
 
## Recommendations
 
Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.
 
 
# Training Details
 
## Training Data
 
The data are mostly comprised of light novels from the dataset of the [KoboldAI/GPT-Neo-2.7B-Horni-LN](https://huggingface.co/KoboldAI/GPT-Neo-2.7B-Horni-LN) model and assorted interactive fiction. The dataset uses `[Themes: <comma-separated list of genres>]` for tagging, which means that if similar text is placed in the context, the model will attempt to generate text in the specified style(s). For more details about the dataset, consult [this document](https://wandb.ai/ve-forbryderne/skein/runs/files/files/datasets/README.txt).
 
## Training Procedure
 
 
### Preprocessing
 
The data were preprocessed using the Python package ftfy to eliminate as much as possible non-ASCII punctuation characters and possible encoding errors. The interactive fiction in the dataset also underwent deduplication since interactive fiction logs often contain duplicate text from, for example, visiting the same in-game area several times. spaCy was used for grammatical analysis with the purpose of reformatting the actions commonly found in old text adventure games into more complete sentences. There was also some manual elimination of things such as "thank you for playing" messages and title messages.
 
### Speeds, Sizes, Times
 
Training took approximately 14 hours in total, with the average speed being 5265 tokens per second.
 
# Evaluation
 
 
## Testing Data, Factors & Metrics
 
### Testing Data
 
More information needed
 
### Factors
 
 
### Metrics
 
More information needed
## Results 
 
More information needed
 
# Model Examination
 
More information needed
 
# Environmental Impact
 
 
Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).
 
- **Hardware Type:** More information needed
- **Hours used:** More information needed
- **Cloud Provider:** More information needed
- **Compute Region:** More information needed
- **Carbon Emitted:** More information needed
 
# Technical Specifications [optional]
 
## Model Architecture and Objective
 
More information needed
 
## Compute Infrastructure
 
More information needed
 
### Hardware
 
More information needed
 
### Software
https://github.com/kingoflolz/mesh-transformer-jax
 
# Citation
 
 
**BibTeX:**
 ```
@misc{mesh-transformer-jax,
  author = {Wang, Ben},
  title = {{Mesh-Transformer-JAX: Model-Parallel Implementation of Transformer Language Model with JAX}},
  howpublished = {\url{https://github.com/kingoflolz/mesh-transformer-jax}},
  year = 2021,
  month = May
}
```
 
# Glossary [optional]
More information needed
 
# More Information [optional]
 
More information needed
 
# Model Card Authors [optional]
 
 
KoboldAI in collaboration with Ezi Ozoani and the Hugging Face team
 
# Model Card Contact
 
More information needed
 
# How to Get Started with the Model
 
Use the code below to get started with the model.
 
<details>
<summary> Click to expand </summary>

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
 
tokenizer = AutoTokenizer.from_pretrained("KoboldAI/GPT-J-6B-Skein")
 
model = AutoModelForCausalLM.from_pretrained("KoboldAI/GPT-J-6B-Skein")
```
</details>
