
# GPT-Neo 2.7B

## Model Description

GPT-Neo 2.7B is a transformer model designed using EleutherAI's replication of the GPT-3 architecture. GPT-Neo refers to the class of models, while 2.7B represents the number of parameters of this particular pre-trained model.

## Training data

GPT-Neo 2.7B was trained on the Pile, a large scale curated dataset created by EleutherAI for the purpose of training this model.

## Training procedure

This model was trained for 420 billion tokens over 400,000 steps. It was trained as a masked autoregressive language model, using cross-entropy loss.

## Intended Use and Limitations

This way, the model learns an inner representation of the English language that can then be used to extract features useful for downstream tasks. The model is best at what it was pretrained for however, which is generating texts from a prompt.

### How to use

You can use this model directly with a pipeline for text generation. This example generates a different sequence each time it's run:

```py
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
>>> generator("EleutherAI has", do_sample=True, min_length=50)

[{'generated_text': 'EleutherAI has made a commitment to create new software packages for each of its major clients and has'}]
```

### Limitations and Biases

GPT-Neo was trained as an autoregressive language model. This means that its core functionality is taking a string of text and predicting the next token. While language models are widely used for tasks other than this, there are a lot of unknowns with this work.

GPT-Neo was trained on the Pile, a dataset known to contain profanity, lewd, and otherwise abrasive language. Depending on your usecase GPT-Neo may produce socially unacceptable text. See Sections 5 and 6 of the Pile paper for a more detailed analysis of the biases in the Pile.

As with all language models, it is hard to predict in advance how GPT-Neo will respond to particular prompts and offensive content may occur without warning. We recommend having a human curate or filter the outputs before releasing them, both to censor undesirable content and to improve the quality of the results. 

## Eval results

All evaluations were done using our [evaluation harness](https://github.com/EleutherAI/lm-evaluation-harness). Some results for GPT-2 and GPT-3 are inconsistent with the values reported in the respective papers. We are currently looking into why, and would greatly appreciate feedback and further testing of our eval harness. If you would like to contribute evaluations you have done, please reach out on our [Discord](https://discord.gg/vtRgjbM).

### Linguistic Reasoning

| Model and Size   | Pile BPB   | Pile PPL   | Wikitext PPL  | Lambada PPL | Lambada Acc | Winogrande | Hellaswag   |
| ---------------- | ---------- | ---------- | ------------- | ----------- | ----------- | ---------- | ----------- |
| GPT-Neo 1.3B     | 0.7527     | 6.159      | 13.10         |  7.498      | 57.23%      | 55.01%     | 38.66%  |
| GPT-2 1.5B       | 1.0468     | -----      | 17.48         |  10.634     | 51.21%      | 59.40%     | 40.03%      |
| **GPT-Neo 2.7B** | **0.7165** | **5.646**  | **11.39**     |  **5.626**  | **62.22%**  | **56.50%** | **42.73%**  |
| GPT-3 Ada        | 0.9631     | -----      | -----         |  9.954      | 51.60%      | 52.90%     | 35.93%      |

### Physical and Scientific Reasoning

| Model and Size   | MathQA     | PubMedQA   | Piqa        |
| ---------------- | ---------- | ---------- | ----------- |
| GPT-Neo 1.3B     | 24.05%     | 54.40%     | 71.11%  |
| GPT-2 1.5B       | 23.64%     | 58.33%     | 70.78%      |
| **GPT-Neo 2.7B** | **24.72%** | **57.54%** | **72.14%**  |
| GPT-3 Ada        | 24.29%     | 52.80%     | 68.88%      |

### Down-Stream Applications

TBD

### BibTeX entry and citation info

To cite this model, use
```bibtex
@software{gpt-neo,
  author       = {Black, Sid and
                  Leo, Gao and
                  Wang, Phil and
                  Leahy, Connor and
                  Biderman, Stella},
  title        = {{GPT-Neo: Large Scale Autoregressive Language 
                   Modeling with Mesh-Tensorflow}},
  month        = mar,
  year         = 2021,
  note         = {{If you use this software, please cite it using 
                   these metadata.}},
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.5297715},
  url          = {https://doi.org/10.5281/zenodo.5297715}
}

@article{gao2020pile,
  title={The Pile: An 800GB Dataset of Diverse Text for Language Modeling},
  author={Gao, Leo and Biderman, Stella and Black, Sid and Golding, Laurence and Hoppe, Travis and Foster, Charles and Phang, Jason and He, Horace and Thite, Anish and Nabeshima, Noa and others},
  journal={arXiv preprint arXiv:2101.00027},
  year={2020}
}
```