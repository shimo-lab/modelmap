This is a [LLaMA-2-7b-hf](https://huggingface.co/NousResearch/Llama-2-7b-hf) model fine-tuned using QLoRA (4-bit precision) on my [claude_pippa_bluemoon_2k](https://huggingface.co/datasets/Norquinal/claude_pippa_bluemoon_2k) dataset, which is a randomized subset of ~1000 samples from my [claude_multiround_chat_30k](https://huggingface.co/datasets/Norquinal/claude_multiround_chat_30k) dataset combined with an additional ~600 randomized samplings from the [PIPPA](https://huggingface.co/datasets/PygmalionAI/PIPPA) and [Bluemoon RP](https://huggingface.co/datasets/Squish42/bluemoon-fandom-1-1-rp-cleaned) datasets. The intent was to improve the finetune's ability to RP and write creative fiction. To that end, it seems to have worked, if only marginally.

Do not take this model very seriously, it is probably not very good. I haven't a clue of what I'm doing. I just thought it was a fun thing to make.

## Prompt Format
The model was finetuned with the Vicuna 1.1 prompt format:
```
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.

USER: {instruction}
ASSISTANT:
```

## Example Usage
>USER: Write a story about a boy who wakes up in the middle of a magical forest.

>ASSISTANT: Once upon a time there was a young boy named Jack. One night he had a dream that he was walking through a beautiful enchanted forest filled with talking animals and strange creatures. When he opened his eyes it turned out to be real! He found himself standing in the center of this mysterious place surrounded by tall trees and lush greenery. 
>
>The first thing Jack did was ask for directions from one of the many colorful birds flying overhead. They told him that if he followed the path straight ahead he would eventually come across a village inhabited by friendly fairies. So off he went down the well-worn trail leading deeper into the woods. After several hours of hiking he finally reached the edge of the fairy settlement where tiny houses made entirely of flowers dotted the landscape like jewels on a crown.  
>
>Jack knocked at the door of the largest cottage which belonged to the king and queen of these mystical folk. Upon entering they welcomed him warmly as their newest guest. Over tea and scones they explained how magic flowed freely throughout their land but only those pure of heart could see its beauty. Jack promised not to tell anyone else about what he had witnessed here so long as he might return someday when needed most. With that assurance given, the fairies bid him goodnight and sent him back along the same path he came from - now knowing more than ever before just how special life truly is.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Norquinal__llama-2-7b-claude-chat-rp)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 44.78   |
| ARC (25-shot)         | 54.95          |
| HellaSwag (10-shot)   | 80.05    |
| MMLU (5-shot)         | 47.03         |
| TruthfulQA (0-shot)   | 43.47   |
| Winogrande (5-shot)   | 74.74   |
| GSM8K (5-shot)        | 7.28        |
| DROP (3-shot)         | 5.94         |
