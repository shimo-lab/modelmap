# Llama3-merge-biomed-8b

This is a DARE-TIES Merge of Llama3-8b-Instruct + NousResearch/Hermes-2-Pro-Llama-3-8B + aaditya/Llama3-OpenBioLLM-8B.
It is a simple experiment to assess whether combining models with strengths in general language understanding and biomedical knowledge can enhance performance on specialized tasks without compromising general applicability.
The results indicate promising outcomes in areas like HendrycksTest tasks related to Biology and Medicine, as well as improvements in complex reasoning as seen in the ARC Challenge and Winogrande benchmarks. 

## Usage

I recommend using the prompt template of Llama3: https://llama.meta.com/docs/model-cards-and-prompt-formats/meta-llama-3/

## Leaderboard metrics according to 🤗 Open LLM Leaderboard

| Task                                 | Metric                   | Ours (%) | Llama38BInstr. (%) |OpenBioLLM8B (%) |
|--------------------------------------|--------------------------|------------------|------------|-------------|
| **ARC Challenge**                    | Accuracy                 | **59.39**            | 57.17      | 55.38       |
|                                      | Normalized Accuracy      | **63.65**            | 60.75      | 58.62       |
| **Hellaswag**                        | Accuracy                 | **62.59**           | 59.04      | 61.83       |
|                                      | Normalized Accuracy      | **81.53**            | 78.55      | 80.76       |
| **Winogrande**                       | Accuracy                 | **75.93**            | 74.51      | 70.88       |
| **GSM8K**                            | Accuracy                 | 59.36            | **68.69**      | 10.15       |
| **HendrycksTest-Anatomy**            | Accuracy                 | **72.59**            | 65.19      | 69.62       |
| **HendrycksTest-Clinical Knowledge** | Accuracy                 | **77.83**            | 74.72      | 60.38       |
| **HendrycksTest-College Biology**    | Accuracy                 | **81.94**            | 79.86      | 79.86       |
| **HendrycksTest-College Medicine**   | Accuracy                 | 69.36            | 63.58      | **70.52**       |
| **HendrycksTest-Medical Genetics**   | Accuracy                 | **86.00**            | 80.00      | 80.00       |
| **HendrycksTest-Professional Medicine** | Accuracy              | **77.94**            | 71.69      | 77.94      |


This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE](https://arxiv.org/abs/2311.03099) [TIES](https://arxiv.org/abs/2306.01708) merge method using [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) as a base.

### Models Merged

The following models were included in the merge:
* [NousResearch/Hermes-2-Pro-Llama-3-8B](https://huggingface.co/NousResearch/Hermes-2-Pro-Llama-3-8B)
* [aaditya/Llama3-OpenBioLLM-8B](https://huggingface.co/aaditya/Llama3-OpenBioLLM-8B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: meta-llama/Meta-Llama-3-8B-Instruct
    # Base model providing a general foundation without specific parameters

  - model: meta-llama/Meta-Llama-3-8B-Instruct
    parameters:
      density: 0.60  
      weight: 0.5  

  - model: NousResearch/Hermes-2-Pro-Llama-3-8B
    parameters:
      density: 0.55  
      weight: 0.1  

  - model: aaditya/Llama3-OpenBioLLM-8B
    parameters:
      density: 0.55  
      weight: 0.4 

merge_method: dare_ties
base_model: meta-llama/Meta-Llama-3-8B-Instruct
parameters:
  int8_mask: true
dtype: bfloat16
```
