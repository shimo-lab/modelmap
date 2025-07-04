<img src="llemma.png" width="400">

[ArXiv](http://arxiv.org/abs/2310.10631) | [Models](https://huggingface.co/EleutherAI/llemma_34b) | [Data](https://huggingface.co/datasets/EleutherAI/proof-pile-2) | [Code](https://github.com/EleutherAI/math-lm) | [Blog](https://blog.eleuther.ai/llemma/) | [Sample Explorer](https://llemma-demo.github.io/)

[Zhangir Azerbayev](https://zhangir-azerbayev.github.io/), [Hailey Schoelkopf](https://github.com/haileyschoelkopf), [Keiran Paster](https://keirp.com), [Marco Dos Santos](https://github.com/dsantosmarco), [Stephen McAleer](https://www.andrew.cmu.edu/user/smcaleer/), [Albert Q. Jiang](https://albertqjiang.github.io/), [Jia Deng](https://www.cs.princeton.edu/~jiadeng/), [Stella Biderman](https://www.stellabiderman.com/), [Sean Welleck](https://wellecks.com/)

**Llemma 7B** is a language model for mathematics. It was initialized with [Code Llama 7B](https://github.com/facebookresearch/codellama) weights, and trained on the [Proof-Pile-2](https://huggingface.co/datasets/EleutherAI/proof-pile-2) for 200B tokens. 

This model also comes in a 34B parameter version: [Llemma 34B](https://huggingface.co/EleutherAI/llemma_34b).

## Evaluations

Llemma models are particularly strong at chain-of-thought mathematical reasoning and using computational tools for mathematics, such as Python and formal theorem provers.


### Chain-of-thought Math
On chain-of-thought mathematics tasks, Llemma models outperform Llama-2, Code Llama, and when controlled for model size, outperform Minerva.

| Model      | Size | GSM8k  | [OCW](https://openreview.net/forum?id=IFXTZERXdM7)   | MMLU-STEM | [SAT](https://huggingface.co/datasets/mcaleste/sat_multiple_choice_math_may_23)   | MATH  |
|------------|------|--------|-------|-----------|-------|-------|
| Llama 2    | 7B   | 11.8%  | 3.7%  | 29.9%     | 25%   | 3.2%  |
| Code Llama | 7B   | 10.5%  | 4.4%  | 25.1%     | 9.4%  | 4.5%  |
| LLEMMA     | 7B   | **36.4%**  | **7.7%**  | **37.7%**     | **53.1%** | **18.0%** |
| Minerva    | 8B   | 16.2%  | **7.7%**  | 35.6%     | -     | 14.1% |
|------------|------|--------|-------|-----------|-------|-------|
| Code Llama | 34B  | 29.6%  | 7.0%  | 40.5%     | 40.6% | 12.2% |
| LLEMMA     | 34B  | **51.5%**  | **11.8%** | **49.0%**     | **71.9%** | **25.0%** |
|------------|------|--------|-------|-----------|-------|-------|
| Minerva    | 62B  | 52.4%  | 12.0% | 53.9%     | -     | 27.6% |
| Minerva    | 540B | 58.8%  | 17.6% | 63.9%     | -     | 33.6% |


Further performance can be extracted by using majority voting: 

| Model   | Size | GSM8k maj@100 | OCW maj@100 | MMLU-STEM maj@16 | SAT maj@16 | MATH maj@256 |
|---------|------|-------------|-----------|-----------------|-----------|------------|
| LLEMMA  | 7B   | 54.0%       | 14.3%     | 49.9%           | 78.1%     | **33.5**      |
| Minerva | 8B   | 28.4%       | 12.5%     | 43.4%           | -         | 25.4%      |
|---------|------|-------------|-----------|-----------------|-----------|------------|
| LLEMMA  | 34B  | 69.3%       | 18.4%     | 59.7%           | 81.3%     | **43.1%**      |
|---------|------|-------------|-----------|-----------------|-----------|------------|
| Minerva | 62B  | 68.5%       | 23.5%     | 63.5%           | -         | 43.4%      |
| Minerva | 540B | 78.5%       | 30.8%     | 75.0%           | -         | 50.3%      |

### Tool Use and Theorem Proving
In addition to chain-of-thought reasoning, Llemma has strong capabilities in computational mathematics tasks. For tool use and formal theorem proving evaluations, see [our paper](http://arxiv.org/abs/2310.10631).

### Citation
```
@misc{azerbayev2023llemma,
      title={Llemma: An Open Language Model For Mathematics}, 
      author={Zhangir Azerbayev and Hailey Schoelkopf and Keiran Paster and Marco Dos Santos and Stephen McAleer and Albert Q. Jiang and Jia Deng and Stella Biderman and Sean Welleck},
      year={2023},
      eprint={2310.10631},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```