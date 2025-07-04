see our paper in https://arxiv.org/abs/2309.12284

View the project page:
https://meta-math.github.io/

## Note

All MetaMathQA data are augmented from the training sets of GSM8K and MATH. 
<span style="color:red"><b>None of the augmented data is from the testing set.</b></span>

You can check the `original_question` in `meta-math/MetaMathQA`, each item is from the GSM8K or MATH train set.

## Model Details

MetaMath-Llemma-7B is fully fine-tuned on the MetaMathQA datasets and based on the powerful Llemma-7B model. It is glad to see using MetaMathQA datasets and change the base model from llama-2-7B to Llemma-7B can boost the MATH performance from 19.8 to **30.0**.

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
| 🔥 **MetaMath-Llemma-7B** | **69.2**     | **30.0**        |
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
@article{azerbayev2023llemma,
  title={Llemma: An open language model for mathematics},
  author={Azerbayev, Zhangir and Schoelkopf, Hailey and Paster, Keiran and Santos, Marco Dos and McAleer, Stephen and Jiang, Albert Q and Deng, Jia and Biderman, Stella and Welleck, Sean},
  journal={arXiv preprint arXiv:2310.10631},
  year={2023}
}
```