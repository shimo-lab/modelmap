
A Reproduction of [OpenLLaMA](https://github.com/openlm-research/open_llama) using 128 H100 GPUs in Bfloat16.


The pretrain data consists of Falcon, Starcoder, and the wikipedia, arxiv, books, stackexchange from RedPajama. In total, this encompassed nearly 1 trillion tokens.


The model was trained over a single epoch, incorporating 2000 warm-up steps and a cosine learning rate schedule, starting at 3e-5 with 4M batch size.



![image/png](https://cdn-uploads.huggingface.co/production/uploads/643fb889b9ba82afb66d6b36/7nSjTJNB7qjwIa74Rr6kd.png)

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_itsliupeng__openllama-7b-base)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |47.09|
|AI2 Reasoning Challenge (25-Shot)|46.16|
|HellaSwag (10-Shot)              |76.40|
|MMLU (5-Shot)                    |42.82|
|TruthfulQA (0-shot)              |36.65|
|Winogrande (5-shot)              |70.88|
|GSM8k (5-shot)                   | 9.63|

