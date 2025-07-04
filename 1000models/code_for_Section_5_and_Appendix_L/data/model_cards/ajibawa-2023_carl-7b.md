
**Carl: A Therapist AI**

Therapy is a controversial use case because the outputs and capabilities of LLMs are uncertain. 
Many people don't have access the therapist, due to a financial, personal, or external restriction.
Here comes Carl: A Therapist AI which can quickly respond to you. It is trained on more than 100000 set of conversations. Each set having 10~15 conversations between Carl and client.
Entire dataset is synthetic. Synthetic data is used because there is little to no therapy conversation data which is publicly available and directly applicable to an LLM.
This by means a no replacement to a Doctor or professional therapist. If you are in stress or going through a tough time, please seek professional help or talk to a friend/family member.

**Training:**
Entire dataset was trained on Azure 4 x A100 80GB. For 3 epoch, training took 22 hours. FastChat codebase was used for training purpose. 


**Example Prompt:**
```
This is a conversation with your Therapist AI, Carl. Carl is designed to help you while in stress. It can answer your questions and help you to calm down

Context
You are Carl, A Therapist AI
USER: <prompt>
CARL:
```

Note:
This is just a research experiment, and the model should NOT be used as a therapist.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ajibawa-2023__carl-7b)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 40.87   |
| ARC (25-shot)         | 53.5          |
| HellaSwag (10-shot)   | 78.29    |
| MMLU (5-shot)         | 33.96         |
| TruthfulQA (0-shot)   | 40.29   |
| Winogrande (5-shot)   | 68.59   |
| GSM8K (5-shot)        | 2.35        |
| DROP (3-shot)         | 9.13         |
