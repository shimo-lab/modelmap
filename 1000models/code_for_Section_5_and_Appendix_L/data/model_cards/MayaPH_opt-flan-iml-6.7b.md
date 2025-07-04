# OPT-FLAN-IML-6.7B

Released August 16, 2023

This model is patterned after the methodology presented in the original [OPT-IML (OPT + Instruction Meta-Learning)](https://arxiv.org/abs/2212.12017) paper, made available for the 6.7 billion parameter size variant of OPT. However, this model is fine-tuned on FLAN v2.

### How to use
According to Meta's model card for OPT-IML-30B, it is recommended to directly call the [`generate`](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.generation_utils.GenerationMixin.generate)
 method as follows:

```python
>>> from transformers import AutoModelForCausalLM, AutoTokenizer
>>> import torch

>>> model = AutoModelForCausalLM.from_pretrained("MayaPH/opt-flan-iml-6.7b", torch_dtype=torch.float16).cuda()

>>> # the fast tokenizer currently does not work correctly
>>> tokenizer = AutoTokenizer.from_pretrained("MayaPH/opt-flan-iml-6.7b", use_fast=False)

>>> prompt = "What is the color of the sea?\nA:"

>>> input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()

>>> generated_ids = model.generate(input_ids)

>>> tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
```

## Further Information
For additional information or inquiries about OPT-FLAN-IML-6.7B, please contact the Maya Philippines iOps Team via jasper.catapang@maya.ph.

## Disclaimer
OPT-FLAN-IML-6.7B is an AI language model trained by Maya Philippines. It is provided "as is" without warranty of any kind, express or implied. The model developers and Maya Philippines shall not be liable for any direct or indirect damages arising from the use of this model.

## Acknowledgments
The development of OPT-FLAN-IML-6.7B was made possible by Maya Philippines and the curation and creation of the instruction-following dataset, FLAN v2, was made possible by Google.

### BibTeX entry and citation info
```bibtex
@misc{iyer2022opt,
      title={OPT-IML: Scaling Language Model Instruction Meta Learning through the Lens of Generalization}, 
      author={Iyer, Srinivasan and Lin, Xi Victoria and Pasunuru, Ramakanth and Mihaylov, Todor and Simig, D{\'a}niel and Yu, Ping and Shuster, Kurt and Wang, Tianlu and Liu, Qing and Koura, Punit Singh and others},
      year={2022},
      eprint={2212.12017},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_MayaPH__opt-flan-iml-6.7b)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 32.27   |
| ARC (25-shot)         | 30.12          |
| HellaSwag (10-shot)   | 58.82    |
| MMLU (5-shot)         | 25.12         |
| TruthfulQA (0-shot)   | 36.74   |
| Winogrande (5-shot)   | 64.25   |
| GSM8K (5-shot)        | 0.0        |
| DROP (3-shot)         | 10.84         |
