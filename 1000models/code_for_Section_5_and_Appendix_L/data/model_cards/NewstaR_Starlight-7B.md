# Starlight (7B)

| Model                | Average ⬆️ | ARC   | HellaSwag | MMLU  | TruthfulQA |
|----------------------|------------|-------|-----------|-------|------------|
| NewstaR/Starlight-13B| 58.63      | 59.3  | 82.15     | 55.67 | 37.39      |
| NewstaR/Starlight-7B | 54.3       | 53.07 | 78.57     | 46.8  | 38.75      |


## The model follows the Alpaca template:
```
### Instruction: {prompt} ### Response:
```

## Example:
```
### Instruction: Summarize the key details of the Starlight model in a few sentences.

### Response: Starlight is a 7B parameter transformer model trained on the AverageData and Above the Clouds datasets for conversational text generation. It has strong language modeling capabilities but lacks true language understanding and may generate incorrect or biased text, so outputs should be monitored and safeguards implemented. The model is intended for use in chatbots and content creation applications.
```

## Instructions for Safe Use

- Avoid exposing Starlight to offensive, unethical, dangerous or illegal prompts
- Monitor outputs for signs of bias, toxicity or factual incorrectness
- Do not rely on Starlight for high-stakes or safety critical applications

## Limitations

- May hallucinate or generate incorrect information
- Large model size leads to high compute requirements

```
@misc{open-llm-leaderboard,
  author = {Edward Beeching, Clémentine Fourrier, Nathan Habib, Sheon Han, Nathan Lambert, Nazneen Rajani, Omar Sanseviero, Lewis Tunstall, Thomas Wolf},
  title = {Open LLM Leaderboard},
  year = {2023},
  publisher = {Hugging Face},
  howpublished = "\url{https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard}"
}
```
```
@software{eval-harness,
  author       = {Gao, Leo and
                  Tow, Jonathan and
                  Biderman, Stella and
                  Black, Sid and
                  DiPofi, Anthony and
                  Foster, Charles and
                  Golding, Laurence and
                  Hsu, Jeffrey and
                  McDonell, Kyle and
                  Muennighoff, Niklas and
                  Phang, Jason and
                  Reynolds, Laria and
                  Tang, Eric and
                  Thite, Anish and
                  Wang, Ben and
                  Wang, Kevin and
                  Zou, Andy},
  title        = {A framework for few-shot language model evaluation},
  month        = sep,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {v0.0.1},
  doi          = {10.5281/zenodo.5371628},
  url          = {https://doi.org/10.5281/zenodo.5371628}
}
```
```
@misc{clark2018think,
      title={Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge},
      author={Peter Clark and Isaac Cowhey and Oren Etzioni and Tushar Khot and Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},
      year={2018},
      eprint={1803.05457},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
```
@misc{zellers2019hellaswag,
      title={HellaSwag: Can a Machine Really Finish Your Sentence?},
      author={Rowan Zellers and Ari Holtzman and Yonatan Bisk and Ali Farhadi and Yejin Choi},
      year={2019},
      eprint={1905.07830},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
``` 
@misc{hendrycks2021measuring,
      title={Measuring Massive Multitask Language Understanding},
      author={Dan Hendrycks and Collin Burns and Steven Basart and Andy Zou and Mantas Mazeika and Dawn Song and Jacob Steinhardt},
      year={2021},
      eprint={2009.03300},
      archivePrefix={arXiv},
      primaryClass={cs.CY}
}
```
```
@misc{lin2022truthfulqa,
      title={TruthfulQA: Measuring How Models Mimic Human Falsehoods},
      author={Stephanie Lin and Jacob Hilton and Owain Evans},
      year={2022},
      eprint={2109.07958},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_NewstaR__Starlight-7B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 43.42   |
| ARC (25-shot)         | 53.07          |
| HellaSwag (10-shot)   | 78.57    |
| MMLU (5-shot)         | 46.8         |
| TruthfulQA (0-shot)   | 38.75   |
| Winogrande (5-shot)   | 74.03   |
| GSM8K (5-shot)        | 7.13        |
| DROP (3-shot)         | 5.59         |
