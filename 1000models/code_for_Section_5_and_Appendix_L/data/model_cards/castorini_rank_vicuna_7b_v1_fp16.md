
# RankVicuna (FP16) Model Card

## Model Details

RankVicuna is a chat assistant trained by fine-tuning Llama 2 on user-shared conversations collected from ShareGPT.

- **Developed by:** [Castorini](https://github.com/castorini)
- **Model type:** An auto-regressive language model based on the transformer architecture
- **License:** Llama 2 Community License Agreement	
- **Finetuned from base model:** [Llama 2](https://arxiv.org/abs/2307.09288)

This specific model is a 7B variant and is trained with data augmentation.
It is also worth noting that it is converted to FP16.

### Model Sources

- **Repository:** https://github.com/castorini/rank_llm
- **Paper:** https://arxiv.org/abs/2309.15088

## Uses

The primary use of RankVicuna is research at the intersection of large language models and retrieval.
The primary intended users of the model are researchers and hobbyists in natural language processing and information retrieval.

## Training Details

RankVicuna is finetuned from `lmsys/vicuna-7b-v1.5` with supervised instruction fine-tuning.

## Evaluation

RankVicuna is currently evaluated on DL19/DL20. See more details in our [paper](https://arxiv.org/pdf/2309.15088.pdf).