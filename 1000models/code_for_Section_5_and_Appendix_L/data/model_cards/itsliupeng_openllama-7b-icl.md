Train openllama-7b with [in-context leanrning](https://arxiv.org/abs/2310.10638)


A Reproduction of OpenLLaMA using 128 H100 GPUs in Bfloat16.

The pretrain data consists of Falcon, Starcoder, and the wikipedia, arxiv, books, stackexchange from RedPajama. In total, this encompassed nearly 1 trillion tokens.

The model was trained over a single epoch, incorporating 2000 warm-up steps and a cosine learning rate schedule, starting at 3e-5 with 4M batch size.


The sole distinction from the [OpenLLaMA 7B Base](https://huggingface.co/itsliupeng/openllama-7b-base) lies in the organization of Falcon documents, which follows the methodology outlined in this [arXiv paper](https://arxiv.org/abs/2310.10638).


![image/png](https://cdn-uploads.huggingface.co/production/uploads/643fb889b9ba82afb66d6b36/Lr2Mup7QFuSSROrsRSzSP.png)

