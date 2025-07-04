# med-law-dolphin-beagle-merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the breadcrumbs merge method using [mlabonne/NeuralBeagle14-7B](https://huggingface.co/mlabonne/NeuralBeagle14-7B) as a base.

### Models Merged

The following models were included in the merge:
* [cognitivecomputations/dolphin-2.6-mistral-7b](https://huggingface.co/cognitivecomputations/dolphin-2.6-mistral-7b)
* [Equall/Saul-Instruct-v1](https://huggingface.co/Equall/Saul-Instruct-v1)
* [BioMistral/BioMistral-7B-SLERP](https://huggingface.co/BioMistral/BioMistral-7B-SLERP)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Equall/Saul-Instruct-v1
    parameters:
      weight: 1.0
  - model: BioMistral/BioMistral-7B-SLERP
    parameters:
      weight: 1.0
  - model: cognitivecomputations/dolphin-2.6-mistral-7b
    parameters:
      weight: 0.5
merge_method: breadcrumbs
base_model: mlabonne/NeuralBeagle14-7B

parameters:
    density: 0.9
    gamma: 0.01    
dtype: float16
```