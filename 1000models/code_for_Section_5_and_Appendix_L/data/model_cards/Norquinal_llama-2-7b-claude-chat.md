This is a [LLaMA-2-7b-hf](https://huggingface.co/NousResearch/Llama-2-7b-hf) model fine-tuned using QLoRA (4-bit precision) on my [claude_multiround_chat_1k](https://huggingface.co/datasets/Norquinal/claude_multiround_chat_1k) dataset, which is a randomized subset of ~1000 samples from my [claude_multiround_chat_30k](https://huggingface.co/datasets/Norquinal/claude_multiround_chat_30k) dataset.

Do not take this model very seriously, it is probably not very good. I haven't a clue of what I'm doing. I just thought it was a fun thing to make.

## Prompt Format
The model was finetuned with the Vicuna 1.1 prompt format:
```
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.

USER: {instruction}
ASSISTANT:
```

## Example Usage
>USER: First, give a brief overview of Chinese cuisine, including its regional diversity. next, describe the importance of the five flavors in Chinese cooking. Then, mention three popular Chinese dishes and their main ingredients. After that, provide a popular Chinese cooking technique and an example of a dish prepared using that technique. Finally, discuss the role of tea in traditional Chinese culture.

>ASSISTANT: Chinese cuisine is diverse due to China's vast geography and climate. Different regions have developed distinct styles of food based on local ingredients and techniques. 
>
>The Five Flavor Theory states that all tastes - sweetness, sourness, saltiness, bitterness, and savory umami - are essential components of good Chinese cooking. Chefs use these flavors harmoniously to create balanced meals with complex taste profiles.  
>
>Three famous Chinese dishes include Peking duck (roasted duck), Sichuan hot pot (spicy broth with vegetables) and dim sum (small buns or steamed dumplings). Their key ingredient is usually meat, poultry or seafood.   
>
>A common cooking method is stir-frying where ingredients like chicken, beef or vegetables are quickly sautéed in oil at high heat until just cooked through. Stir fried green beans would be an example.    
>
>Tea has been consumed for thousands of years as part of daily life in China. It is served before meals to cleanse palates and afterward to aid digestion. Teas range from mildly fragrant white teas to robust oolong varieties.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Norquinal__llama-2-7b-claude-chat)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 44.54   |
| ARC (25-shot)         | 54.44          |
| HellaSwag (10-shot)   | 80.66    |
| MMLU (5-shot)         | 46.74         |
| TruthfulQA (0-shot)   | 41.39   |
| Winogrande (5-shot)   | 74.9   |
| GSM8K (5-shot)        | 7.73        |
| DROP (3-shot)         | 5.89         |
