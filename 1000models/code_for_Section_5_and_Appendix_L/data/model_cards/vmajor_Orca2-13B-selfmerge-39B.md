This model is a result of merging three Orca2-13B models with itself using 'mergekit-legacy'. Merge parameters were passthrough for one and --weight 0.5 --density 0.5 for the second merge.


This merged model showed marginal improvement in perplexity scores:

The perplexity for Orca-2-13b is: 7.595028877258301
The perplexity for orca2-26B-self-merge is: 7.550178050994873
The perplexity for orca2-39B-self-merge is: NC

The following table summarizes the model performance across a range of benchmarks:

| Model                              | Average  | ARC   | HellaSwag | MMLU  | TruthfulQA | Winogrande | GSM8K |
|------------------------------------|-------------|-------|-----------|-------|------------|------------|-------|
| microsoft/Orca-2-13b               | 58.64       | 60.67 | 79.81     | 60.37 | 56.41      | 76.64      | 17.97 |
| vmajor/Orca2-13B-selfmerge-26B     | 62.24       | 60.84 | 79.84     | 60.32 | 56.38      | 76.87      | 39.2  |
| vmajor/Orca2-13B-selfmerge-39B     | 62.24       | 60.84 | 79.84     | 60.32 | 56.38      | 76.87      | 39.2  |

Interestingly the GSM8K performance more than doubled with the first self merge. Second self merge resulting in the 39B model did not produce any further gains.


---
license: ms-pl
---