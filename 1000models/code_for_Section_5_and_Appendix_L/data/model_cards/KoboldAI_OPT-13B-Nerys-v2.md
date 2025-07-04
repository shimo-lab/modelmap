# OPT 13B - Nerys
## Model Description
OPT 13B-Nerys is a finetune created using Facebook's OPT model.
## Training data
The training data contains around 2500 ebooks in various genres (the "Pike" dataset), a CYOA dataset called "CYS" and 50 Asian "Light Novels" (the "Manga-v1" dataset).
Most parts of the dataset have been prepended using the following text: `[Genre: <genre1>, <genre2>]`
This dataset has been cleaned in the same way as fairseq-dense-13B-Nerys-v2
### How to use
You can use this model directly with a pipeline for text generation. This example generates a different sequence each time it's run:
```py
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='KoboldAI/OPT-13B-Nerys-v2')
>>> generator("Welcome Captain Janeway, I apologize for the delay.", do_sample=True, min_length=50)
[{'generated_text': 'Welcome Captain Janeway, I apologize for the delay."\nIt's all right," Janeway said. "I'm certain that you're doing your best to keep me informed of what\'s going on."'}]
```
### Limitations and Biases
Based on known problems with NLP technology, potential relevant factors include bias (gender, profession, race and religion).

### License
OPT-6B is licensed under the OPT-175B license, Copyright (c) Meta Platforms, Inc. All Rights Reserved.

### BibTeX entry and citation info
```
@misc{zhang2022opt,
      title={OPT: Open Pre-trained Transformer Language Models}, 
      author={Susan Zhang and Stephen Roller and Naman Goyal and Mikel Artetxe and Moya Chen and Shuohui Chen and Christopher Dewan and Mona Diab and Xian Li and Xi Victoria Lin and Todor Mihaylov and Myle Ott and Sam Shleifer and Kurt Shuster and Daniel Simig and Punit Singh Koura and Anjali Sridhar and Tianlu Wang and Luke Zettlemoyer},
      year={2022},
      eprint={2205.01068},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```