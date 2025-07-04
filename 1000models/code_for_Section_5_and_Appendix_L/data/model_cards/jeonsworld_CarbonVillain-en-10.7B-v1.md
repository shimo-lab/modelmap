
# CarbonVillain
**This is a model created without learning to oppose indiscriminate carbon emissions.**  

This model is an experimental version created using [mergekit](https://github.com/cg123/mergekit).  
- merge models
  - Weyaxi/SauerkrautLM-UNA-SOLAR-Instruct
  - VAGOsolutions/SauerkrautLM-SOLAR-Instruct
- method: slerp


# Prompt Template(s)

```
### User:
{user}

### Assistant:
{asistant}
```


# Evaluation
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_jeonsworld__CarbonVillain-en-10.7B-v1)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 74.28   |
| ARC (25-shot)         | 71.24      |
| HellaSwag (10-shot)   | 88.45    |
| MMLU (5-shot)         | 66.42      |
| TruthfulQA (0-shot)   | 71.97  |
| Winogrande (5-shot)   | 83.26  |
| GSM8K (5-shot)        | 64.29     |