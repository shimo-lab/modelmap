
# Model Summary

> GritLM is a generative representational instruction tuned language model. It unifies text representation (embedding) and text generation into a single model achieving state-of-the-art performance on both types of tasks.

- **Repository:** [ContextualAI/gritlm](https://github.com/ContextualAI/gritlm)
- **Paper:** https://arxiv.org/abs/2402.09906
- **Logs:** https://wandb.ai/muennighoff/gritlm/runs/0uui712t/overview
- **Script:** https://github.com/ContextualAI/gritlm/blob/main/scripts/training/train_gritlm_7b.sh

| Model | Description |
|-------|-------------|
| [GritLM 7B](https://hf.co/GritLM/GritLM-7B) | Mistral 7B finetuned using GRIT |
| [GritLM 8x7B](https://hf.co/GritLM/GritLM-8x7B) | Mixtral 8x7B finetuned using GRIT |

# Use

The model usage is documented [here](https://github.com/ContextualAI/gritlm?tab=readme-ov-file#inference).

# Citation

```bibtex
@misc{muennighoff2024generative,
      title={Generative Representational Instruction Tuning}, 
      author={Niklas Muennighoff and Hongjin Su and Liang Wang and Nan Yang and Furu Wei and Tao Yu and Amanpreet Singh and Douwe Kiela},
      year={2024},
      eprint={2402.09906},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```