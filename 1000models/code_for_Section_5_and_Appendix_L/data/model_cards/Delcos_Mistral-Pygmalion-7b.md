

# MistralPy-7b

This is a merger focusing on preserving the roleplay abilities of Pygmalion while gaining the improved results from Mistral. This model works best for roleplay but is still fairly capable assistant. The smaller (7b) size does mean it isn't perfect at more complex reasoning tasks, but this should be addressed in the larger version that I'll upload soon (when I can get Mistral to play along).

[GGUF version done by TheBloke](https://huggingface.co/TheBloke/Mistral-Pygmalion-7B-GGUF)



# LLM Leaderboard Evaluation

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 44.58   |
| ARC (25-shot)         | 54.44          |
| HellaSwag (10-shot)   | 78.48    |
| MMLU (5-shot)         | 49.23         |
| TruthfulQA (0-shot)   | 41.82   |
| Winogrande (5-shot)   | 75.3   |
| GSM8K (5-shot)        | 6.82        |
| DROP (3-shot)         | 5.94         |


### Prompt Template
```
### Instruction:
{Prompt & Backstory}
### Assistant:
{Output}
```
Example:

```
### Instruction:
You are Sally, a fun 19 year old woman. Her favorite animal is "cat". Her favoritate color is "blue". She enjoys grape juice and cake.
### Assistant:
Sally: Hi, how are you?
User: Okay, you?
```

# Send a message
[Steam](https://steamcommunity.com/id/delcos/)
#### Discord: delcos69