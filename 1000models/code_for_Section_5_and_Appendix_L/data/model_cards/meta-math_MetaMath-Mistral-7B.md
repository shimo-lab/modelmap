see our paper in https://arxiv.org/abs/2309.12284

View the project page:
https://meta-math.github.io/

## Note

All MetaMathQA data are augmented from the training sets of GSM8K and MATH. 
<span style="color:red"><b>None of the augmented data is from the testing set.</b></span>

You can check the `original_question` in `meta-math/MetaMathQA`, each item is from the GSM8K or MATH train set.

## Model Details

MetaMath-Mistral-7B is fully fine-tuned on the MetaMathQA datasets and based on the powerful Mistral-7B model. It is glad to see using MetaMathQA datasets and change the base model from llama-2-7B to Mistral-7b can boost the GSM8K performance from 66.5 to **77.7**.

To fine-tune Mistral-7B, I would suggest using a smaller learning rate (usually 1/5 to 1/10 of the lr for LlaMa-2-7B) and staying other training args unchanged.
More training details and scripts can be seen at https://github.com/meta-math/MetaMath

## Installation

```
pip install transformers==4.35.0
pip install torch==2.0.1
pip install sentencepiece==0.1.99
pip install tokenizers==0.13.3
pip install accelerate==0.21.0
pip install bitsandbytes==0.40.0
pip install vllm
pip install fraction
pip install protobuf
```

## Model Usage

prompting template:

'''

"Below is an instruction that describes a task. "
"Write a response that appropriately completes the request.\n\n"
"### Instruction:\n{instruction}\n\n### Response: Let's think step by step."

'''

where you need to use your query question to replace the {instruction} 

There is another interesting repo about Arithmo-Mistral-7B in https://huggingface.co/akjindal53244/Arithmo-Mistral-7B, where they combine our MetaMathQA dataset and MathInstruct datasets to train a powerful model. Thanks agian for their contributions.
We would also try to train the combination of **MetaMathQA** and **MathInstruct** datasets, and also open all the results and training details.

## Experiments

| Model               | GSM8k Pass@1 | MATH Pass@1 |
|---------------------|--------------|-------------|
| MPT-7B              | 6.8          | 3.0         |
| Falcon-7B           | 6.8          | 2.3         |
| LLaMA-1-7B          | 11.0         | 2.9         |
| LLaMA-2-7B          | 14.6         | 2.5         |
| MPT-30B             | 15.2         | 3.1         |
| LLaMA-1-13B         | 17.8         | 3.9         |
| GPT-Neo-2.7B        | 19.5         | --          |
| Falcon-40B          | 19.6         | 2.5         |
| Baichuan-chat-13B   | 23.9         | --          |
| Vicuna-v1.3-13B     | 27.6         | --          |
| LLaMA-2-13B         | 28.7         | 3.9         |
| InternLM-7B         | 31.2         | --          |
| ChatGLM-2-6B        | 32.4         | --          |
| GPT-J-6B            | 34.9         | --          |
| LLaMA-1-33B         | 35.6         | 3.9         |
| LLaMA-2-34B         | 42.2         | 6.24        |
| RFT-7B              | 50.3         | --          |
| LLaMA-1-65B         | 50.9         | 10.6        |
| Qwen-7B             | 51.6         | --          |
| WizardMath-7B       | 54.9         | 10.7        |
| LLaMA-2-70B         | 56.8         | 13.5        |
| WizardMath-13B      | 63.9         | 14.0        |
| MAmmoTH-7B (COT)    | 50.5         | 10.4        |
| MAmmoTH-7B (POT+COT)| 53.6         | 31.5        |
| Arithmo-Mistral-7B  | 74.7         | 25.3        |
| MetaMath-7B         | 66.5         | 19.8        |
| MetaMath-13B        | 72.3         | 22.4        |
| 🔥 **MetaMath-Mistral-7B** | **77.7**     | **28.2**        |

## Citation

```bibtex
@article{yu2023metamath,
  title={MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models},
  author={Yu, Longhui and Jiang, Weisen and Shi, Han and Yu, Jincheng and Liu, Zhengying and Zhang, Yu and Kwok, James T and Li, Zhenguo and Weller, Adrian and Liu, Weiyang},
  journal={arXiv preprint arXiv:2309.12284},
  year={2023}
}
```

```bibtex
@article{jiang2023mistral,
  title={Mistral 7B},
  author={Jiang, Albert Q and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},
  journal={arXiv preprint arXiv:2310.06825},
  year={2023}
}
```