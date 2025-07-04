Experiment for DARE(Drop and REscale), most of the delta parameters can be directly set to zeros without affecting the capabilities of SFT LMs and larger models can tolerate a higher proportion of discarded parameters.

weight_mask_rate: 0.85 / use_weight_rescale: True / mask_stratery: random / scaling_coefficient: 1.0

| Model                                                        | Average | ARC    | HellaSwag | MMLU   | TruthfulQA | Winogrande | GSM8K  | DROP   |
| ------                                                       | ------  | ------ | ------    | ------ | ------     | ------     | ------ | ------ |
| Intel/neural-chat-7b-v3-1                                    | 59.06   | 66.21  | 83.64     | 62.37  | 59.65      | 78.14      | 19.56  | 43.84  |
| migtissera/SynthIA-7B-v1.3                                   | 57.11   | 62.12  | 83.45     | 62.65  | 51.37      | 78.85      | 17.59  | 43.76  |
| bhenrym14/mistral-7b-platypus-fp16                           | 56.89   | 63.05  | 84.15     | 64.11  | 45.07      | 78.53      | 17.36  | 45.92  |
| jondurbin/airoboros-m-7b-3.1.2                               | 56.24   | 61.86  | 83.51     | 61.91  | 53.75      | 77.58      | 13.87  | 41.2   |
| uukuguy/speechless-code-mistral-orca-7b-v1.0                 | 55.33   | 59.64  | 82.25     | 61.33  | 48.45      | 77.51      | 8.26   | 49.89  |
| teknium/CollectiveCognition-v1.1-Mistral-7B                  | 53.87   | 62.12  | 84.17     | 62.35  | 57.62      | 75.37      | 15.62  | 19.85  |
| Open-Orca/Mistral-7B-SlimOrca                                | 53.34   | 62.54  | 83.86     | 62.77  | 54.23      | 77.43      | 21.38  | 11.2   |
| uukuguy/speechless-mistral-dolphin-orca-platypus-samantha-7b | 53.34   | 64.33  | 84.4      | 63.72  | 52.52      | 78.37      | 21.38  | 8.66   |
| ehartford/dolphin-2.2.1-mistral-7b                           | 53.06   | 63.48  | 83.86     | 63.28  | 53.17      | 78.37      | 21.08  | 8.19   |
| teknium/CollectiveCognition-v1-Mistral-7B                    | 52.55   | 62.37  | 85.5      | 62.76  | 54.48      | 77.58      | 17.89  | 7.22   |
| HuggingFaceH4/zephyr-7b-alpha                                | 52.4    | 61.01  | 84.04     | 61.39  | 57.9       | 78.61      | 14.03  | 9.82   |
| ehartford/samantha-1.2-mistral-7b                            | 52.16   | 64.08  | 85.08     | 63.91  | 50.4       | 78.53      | 16.98  | 6.13   |
