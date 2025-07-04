
**Paper**: [https://arxiv.org/pdf/2310.06694.pdf](https://arxiv.org/pdf/2310.06694.pdf)  
**Code**: https://github.com/princeton-nlp/LLM-Shearing  
**Models**: [Sheared-LLaMA-1.3B](https://huggingface.co/princeton-nlp/Sheared-LLaMA-1.3B), [Sheared-LLaMA-2.7B](https://huggingface.co/princeton-nlp/Sheared-LLaMA-2.7B)  
**Pruned Models without Continued Pre-training**: [Sheared-LLaMA-1.3B-Pruned](https://huggingface.co/princeton-nlp/Sheared-LLaMA-1.3B-Pruned), [Sheared-LLaMA-2.7B-Pruned](https://huggingface.co/princeton-nlp/Sheared-LLaMA-2.7B-Pruned)  
**Instruction-tuned Models**: [Sheared-LLaMA-1.3B-ShareGPT](https://huggingface.co/princeton-nlp/Sheared-LLaMA-1.3B-ShareGPT), [Sheared-LLaMA-2.7B-ShareGPT](https://huggingface.co/princeton-nlp/Sheared-LLaMA-2.7B-ShareGPT)  

**License**: Must comply with license of Llama2 since it's a model derived from Llama2.

---

Sheared-LLaMA-1.3B is a model pruned and further pre-trained from [meta-llama/Llama-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf). We dynamically load data from different domains in the [RedPajama dataset](https://github.com/togethercomputer/RedPajama-Data) to prune and contune pre-train the model. We use 0.4B tokens for pruning and 50B tokens for continued pre-training the pruned model. This model can be loaded with HuggingFace via

```
model = AutoModelForCausalLM.from_pretrained("princeton-nlp/Sheared-LLaMA-1.3B")
```

- Smaller-scale
- Same vocabulary as LLaMA1 and LLaMA2
- Derived with a budget of 50B tokens by utilizing existing strong LLMs

## Downstream Tasks

We evaluate on an extensive set of downstream tasks including reasoning, reading comprehension, language modeling and knowledge intensive tasks. Our Sheared-LLaMA models outperform existing large language models. 

| Model               | # Pre-training Tokens | Average Performance |
| ------------------- | --------------------- | ------------------- |
| LLaMA2-7B           | 2T                    | 64.6                |

**1.3B**

| Model               | # Pre-training Tokens | Average Performance |
| ------------------- | --------------------- | ------------------- |
| OPT-1.3B            | 300B                  | 48.2                |
| Pythia-1.4B         | 300B                  | 48.9                |
| **Sheared-LLaMA-1.3B**  | **50B**                   | **51.0**                |

**3B**

| Model               | # Pre-training Tokens | Average Performance |
| ------------------- | --------------------- | ------------------- |
| OPT-2.7B            | 300B                  | 51.4                |
| Pythia-2.8B         | 300B                  | 52.5                |
| INCITE-Base-3B      | 800B                  | 54.7                |
| Open-LLaMA-3B-v1    | 1T                    | 55.1                |
| Open-LLaMA-3B-v2    | 1T                    | 55.7                |
| Sheared-LLaMA-2.7B  | 50B                   | 56.7                |

## Bibtex
```
@article{xia2023sheared,
  title={Sheared llama: Accelerating language model pre-training via structured pruning},
  author={Xia, Mengzhou and Gao, Tianyu and Zeng, Zhiyuan and Chen, Danqi},
  journal={arXiv preprint arXiv:2310.06694},
  year={2023}
}
```

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_princeton-nlp__Sheared-LLaMA-1.3B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 31.47   |
| ARC (25-shot)         | 32.85          |
| HellaSwag (10-shot)   | 60.91    |
| MMLU (5-shot)         | 25.71         |
| TruthfulQA (0-shot)   | 37.14   |
| Winogrande (5-shot)   | 58.64   |
| GSM8K (5-shot)        | 0.45        |
| DROP (3-shot)         | 4.56         |
