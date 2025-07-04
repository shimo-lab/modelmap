[HIGHLY EXPERIMENTAL]

Just try it for a good laugh. Need testing.
```shell
The plan :
Open-Orca/OpenOrcaxOpenChat-Preview2-13B
PygmalionAI/pygmalion-2-13b

Undi95/MLewd-L2-13B-v2-3
jondurbin/spicyboros-13b-2.2

lemonilia/limarp-llama2-v2

Step 1: Merge OpenOrcaxOpenChat-Preview2-13B with pygmalion-2-13b 
=> OpenOrcaPyg2
Step 2: Merge MLewd with Spicyboros
=> MLewdBorosPlus
Step 3: In the layer side, replace the layer 0 to 8 with MLewd, and the layer 16 to 20 with Spicyboros of the first merge
=> OpenOrcaPyg2-Layered
Step 4: In the layer side, replace the layer 0 to 8 with MLewd, and the layer 16 to 20 with Spicyboros of the second merge
=> MLewdBorosPlus-Layered
Step 5: Merge OpenOrcaPyg2-Layered with MLewdBorosPlus-Layered
=> OpenRPBase
Step 6: Apply Limarp2 at 0.5 weight at the end
=> OpenRP

Goal: making Orca a RP model with Pyg2 dataset and MLewd+Spicyboros 100% layer accross the merge and avoid censoring
It will be diluted to ~25% in other layer, SLERP do the dirty job 
The LoRA is here to redirect to RP writing
```

Don't ask me why this model work. I'm a blind scientist. It seems a little obsessed with the game "Garry's mod" tho. Be patient with him.
SuperCOT applied : https://huggingface.co/Undi95/OpenRP-13B-SuperCOT
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Undi95__OpenRP-13B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 53.25   |
| ARC (25-shot)         | 62.12          |
| HellaSwag (10-shot)   | 82.6    |
| MMLU (5-shot)         | 57.5         |
| TruthfulQA (0-shot)   | 48.29   |
| Winogrande (5-shot)   | 76.01   |
| GSM8K (5-shot)        | 12.89        |
| DROP (3-shot)         | 33.38         |
