# Typhoon-7B: Thai Large Language Model (Pretrained)

**Typhoon-7B** is a *pretrained* Thai 🇹🇭 large language model with 7 billion parameters, and it is based on Mistral-7B.

**Typhoon-7B** outperforms all open-source Thai language models at the time of writing as evaluated on Thai examination benchmarks, and its instruction-tuned variant achieves the best results in instruction-following tasks. Also, its performance in Thai is on par with GPT-3.5 while being 2.62 times more efficient in tokenizing Thai text.

**This is not an instruction-tuned model** - It may not be able to follow  human instructions without using one/few-shot learning or instruction fine-tuning. The model does not have any moderation mechanisms, and may generate harmful or inappropriate responses. 

The Instruct model (chat-model) will be released soon. The beta version register is open at https://opentyphoon.ai/ or follow us for future model release https://twitter.com/opentyphoon.

<div align="center">
<img src="https://storage.googleapis.com/scb10x-ai-lab-public/assets/typhoon_benchmark.png" alt="Typhoon benchmark" width="100%" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
</div>

For full details of this model, please read our [paper](https://arxiv.org/abs/2312.13951).


## Model Description
- **Model type**: A 7B pretrained decoder-only model
- **Requirement**: transformers 4.34.0 or newer.
- **Primary Language(s)**: Thai 🇹🇭 and English 🇬🇧
- **License**: Apache-2.0 (Commercial)

## Performance on Thai Benchmark

| **Model**           | **ONET** | **IC** | **TGAT** | **TPAT-1** | **A-Level** |
|---------------------|----------|--------|----------|------------|-------------|
| Typhoon-7B          | 0.379    | 0.393  | 0.700    | 0.414      | 0.324       |
| SeaLLM-7B           | 0.342    | 0.256  | 0.589    | 0.336      | 0.305       |
| OpenThaiGPT-beta-7B | 0.180    | 0.278  | 0.411    | 0.319      | 0.243       |
| WangChanGLM         | 0.192    | 0.271  | 0.167    | 0.172      | 0.175       |
| SEA-LION-7B         | 0.179    | 0.290  | 0.244    | 0.198      | 0.175       |
| Avg. Human          | 0.318    | -      | 0.472    | 0.406      | -           |

## Intended Uses & Limitations

This model is a pretrained base model. Thus, it may not be able to follow  human instructions without using one/few-shot learning or instruction fine-tuning. The model does not have any moderation mechanisms, and may generate harmful or inappropriate responses.

## Follow us

https://twitter.com/opentyphoon

## Support / Ask any question

https://discord.gg/us5gAYmrxw

## SCB 10X AI Team
 
- Kunat Pipatanakul, Phatrasek Jirabovonvisut, Potsawee Manakul, Sittipong Sripaisarnmongkol, Ruangsak Patomwong, Pathomporn Chokchainant, Kasima Tharnpipitchai
- If you find Typhoon-7B useful for your work, please cite it using:
```
@article{pipatanakul2023typhoon,
    title={Typhoon: Thai Large Language Models}, 
    author={Kunat Pipatanakul and Phatrasek Jirabovonvisut and Potsawee Manakul and Sittipong Sripaisarnmongkol and Ruangsak Patomwong and Pathomporn Chokchainant and Kasima Tharnpipitchai},
    year={2023},
    journal={arXiv preprint arXiv:2312.13951},
    url={https://arxiv.org/abs/2312.13951}
}
```

## Contact Us

- General & Collaboration: kasima@scb10x.com, pathomporn@scb10x.com
- Technical: kunat@scb10x.com
