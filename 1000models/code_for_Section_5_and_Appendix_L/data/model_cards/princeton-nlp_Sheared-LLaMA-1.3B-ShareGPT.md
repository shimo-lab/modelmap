
**Paper**: [https://arxiv.org/pdf/2310.06694.pdf](https://arxiv.org/pdf/2310.06694.pdf)  
**Code**: https://github.com/princeton-nlp/LLM-Shearing  
**Models**: [Sheared-LLaMA-1.3B](https://huggingface.co/princeton-nlp/Sheared-LLaMA-1.3B), [Sheared-LLaMA-2.7B](https://huggingface.co/princeton-nlp/Sheared-LLaMA-2.7B)  


## Training information
This is the instruction tuned version of [princeton-nlp/Sheared-LLaMA-1.3B](https://huggingface.co/princeton-nlp/Sheared-LLaMA-1.3B). We trained the base model on 10,000 instruction-response pairs
sampled from the ShareGPT dataset (first-turns only). We use the following prompt to perform instruction tuning. 

> You are a helpful assistant. Write a response that appropriately completes the request.\n\n### Input:\n{input}\n\n### Response:

This model can be loaded through transformers.LlamaModelForCausalLM as follows:

```
from transformers import LlamaModelForCausalLM
model = LlamaModelForCausalLM.from_pretrained("princeton-nlp/Sheared-LLaMA-1.3B-ShareGPT")
```

## Bibtex

If you find our model useful, consider citing us with:
```
@article{xia2023sheared,
  title={Sheared llama: Accelerating language model pre-training via structured pruning},
  author={Xia, Mengzhou and Gao, Tianyu and Zeng, Zhiyuan and Chen, Danqi},
  journal={arXiv preprint arXiv:2310.06694},
  year={2023}
}
```

