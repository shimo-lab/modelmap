# OPT 13B - Erebus
## Model description
This is the second generation of the original Shinen made by Mr. Seeker. The full dataset consists of 6 different sources, all surrounding the "Adult" theme. The name "Erebus" comes from the greek mythology, also named "darkness". This is in line with Shin'en, or "deep abyss". For inquiries, please contact the KoboldAI community. **Warning: THIS model is NOT suitable for use by minors. The model will output X-rated content.**

## Training data
The data can be divided in 6 different datasets:
- Literotica (everything with 4.5/5 or higher)
- Sexstories (everything with 90 or higher)
- Dataset-G (private dataset of X-rated stories)
- Doc's Lab (all stories)
- Pike Dataset (novels with "adult" rating)
- SoFurry (collection of various animals)

The dataset uses `[Genre: <comma-separated list of genres>]` for tagging.

### How to use
You can use this model directly with a pipeline for text generation. This example generates a different sequence each time it's run:
```py
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='KoboldAI/OPT-13B-Erebus')
>>> generator("Welcome Captain Janeway, I apologize for the delay.", do_sample=True, min_length=50)
[{'generated_text': 'Welcome Captain Janeway, I apologize for the delay."\nIt's all right," Janeway said. "I'm certain that you're doing your best to keep me informed of what\'s going on."'}]
```

## Limitations and biases
Based on known problems with NLP technology, potential relevant factors include bias (gender, profession, race and religion). **Warning: This model has a very strong NSFW bias!**

### License
OPT-13B is licensed under the OPT-175B license, Copyright (c) Meta Platforms, Inc. All Rights Reserved.

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