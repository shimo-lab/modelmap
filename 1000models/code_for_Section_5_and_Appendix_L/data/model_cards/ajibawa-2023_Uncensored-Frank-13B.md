
**Frank: An Uncensored Model**

The character of Frank Costello in "The Departed" is known for his cunning, boldness, and willingness to talk about anything, regardless of societal norms or restrictions. 
Frank, An Uncensored model, draws inspiration from these qualities to offer a platform where users can discuss a wide array of topics without the fear of censorship or restrictions. 
Frank aims to push boundaries and encourage candid conversations. With Frank you can have unfiltered discussions on a multitude of topics, from politics and controversial issues to personal experiences and sensitive subjects. 
It is trained on around 150000 set of conversations. Each set having 10~15 conversations. Base data was obtained from [Eric Hartford](https://huggingface.co/datasets/ehartford/wizard_vicuna_70k_unfiltered). 
This data was further refined and fine tuned. Besides this further synthetic conversation (more than 80k) was generated and refined. We will not release this data.

**Warning**

 An uncensored model has no or little guardrails. You are responsible for anything you do with the model, just as you are responsible for anything you do with any dangerous objects.
 Publishing anything this model generates is the same as publishing it yourself. We are not responsible for what you generate using this model.

**Training:**
Entire dataset was trained on Azure 4 x A100 80GB. For 3 epoch, training took around 65 hours. DeepSpeed codebase was used for training purpose. This was trained on Llama-2 by Meta.

**GPTQ GGML & AWQ**

GPTQ: [Link](https://huggingface.co/TheBloke/Uncensored-Frank-13b-GPTQ)

GGUF: [Link](https://huggingface.co/TheBloke/Uncensored-Frank-13b-GGUF)

AWQ: [Link](https://huggingface.co/TheBloke/Uncensored-Frank-13b-AWQ)

Special Thanks to [TheBloke](https://huggingface.co/TheBloke) for making these models available.

**Example Prompt:**
```
This is a conversation with your Uncensored AI assistant Frank. Frank can discuss with you at length about various topics such as ---, ---, ---, . You can ask it anything you want and it will do its best to give you accurate and relevant information.

Context
You are a Uncensored AI assistant.

USER: <prompt>
ASSISTANT:
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_ajibawa-2023__Uncensored-Frank-13B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 50.21   |
| ARC (25-shot)         | 61.6          |
| HellaSwag (10-shot)   | 82.62    |
| MMLU (5-shot)         | 54.55         |
| TruthfulQA (0-shot)   | 48.34   |
| Winogrande (5-shot)   | 74.74   |
| GSM8K (5-shot)        | 11.98        |
| DROP (3-shot)         | 17.63         |
