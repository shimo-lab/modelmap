<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->
<!-- markdownlint-disable no-duplicate-header -->

<div align="center">
  <img src="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/figures/logo.svg?raw=true" width="60%" alt="DeepSeek-V2" />
</div>
<hr>
<div align="center" style="line-height: 1;">
  <a href="https://www.deepseek.com/" target="_blank" style="margin: 2px;">
    <img alt="Homepage" src="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/figures/badge.svg?raw=true" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://chat.deepseek.com/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/🤖%20Chat-DeepSeek%20V2-536af5?color=536af5&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://huggingface.co/deepseek-ai" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-DeepSeek%20AI-ffc107?color=ffc107&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://discord.gg/Tc7c45Zzu5" target="_blank" style="margin: 2px;">
    <img alt="Discord" src="https://img.shields.io/badge/Discord-DeepSeek%20AI-7289da?logo=discord&logoColor=white&color=7289da" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/figures/qr.jpeg?raw=true" target="_blank" style="margin: 2px;">
    <img alt="Wechat" src="https://img.shields.io/badge/WeChat-DeepSeek%20AI-brightgreen?logo=wechat&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://twitter.com/deepseek_ai" target="_blank" style="margin: 2px;">
    <img alt="Twitter Follow" src="https://img.shields.io/badge/Twitter-deepseek_ai-white?logo=x&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>
<div align="center" style="line-height: 1;">
  <a href="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/LICENSE-CODE" style="margin: 2px;">
    <img alt="Code License" src="https://img.shields.io/badge/Code_License-MIT-f5de53?&color=f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/LICENSE-MODEL" style="margin: 2px;">
    <img alt="Model License" src="https://img.shields.io/badge/Model_License-Model_Agreement-f5de53?&color=f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>
<p align="center">
  <a href="#2-evaluation-results">Evaluation Results</a> |
  <a href="#3-model-downloads">Model Download</a> |
  <a href="#4-license">License</a> |
  <a href="#5-citation">Citation</a> |
  <a href="#6-contact">Contact</a>
</p>



<p align="center">
  <a href="https://arxiv.org/abs/2408.08152"><b>Paper Link</b>👁️</a>
</p>

# DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search

## 1. Introduction

We introduce DeepSeek-Prover-V1.5, an open-source language model designed for theorem proving in Lean 4, which enhances DeepSeek-Prover-V1 by optimizing both training and inference processes. Pre-trained on DeepSeekMath-Base with specialization in formal mathematical languages, the model undergoes supervised fine-tuning using an enhanced formal theorem proving dataset derived from DeepSeek-Prover-V1. Further refinement is achieved through reinforcement learning from proof assistant feedback (RLPAF). Beyond the single-pass whole-proof generation approach of DeepSeek-Prover-V1, we propose RMaxTS, a variant of Monte-Carlo tree search that employs an intrinsic-reward-driven exploration strategy to generate diverse proof paths. DeepSeek-Prover-V1.5 demonstrates significant improvements over DeepSeek-Prover-V1, achieving new state-of-the-art results on the test set of the high school level miniF2F benchmark (63.5%) and the undergraduate level ProofNet benchmark (25.3%).

<p align="center">
  <img width="100%" src="https://github.com/deepseek-ai/DeepSeek-Prover-V1.5/blob/main/figures/performance.png?raw=true">
</p>


## 2. Evaluation Results

<div align="center">

|  | miniF2F-test | ProofNet |
|--------|------------------|------------------|
| **ReProver** | 26.5% |  13.8% |
| **GPT-f** | 36.6% |  - |
| **Hypertree Proof Search** | 41.0% |  - |
| **InternLM2-StepProver** | 54.5% | 18.1% |
| **DeepSeek-Prover-V1** | 50.0% | - |
| **DeepSeek-Prover-V1.5-Base** | 42.2% | 13.2% |
| **DeepSeek-Prover-V1.5-SFT** | 57.4% | 22.9% |
| **DeepSeek-Prover-V1.5-RL** | 60.2% | 22.6% |
| **DeepSeek-Prover-V1.5-RL + RMaxTS** | **63.5%** | **25.3%** |

</div>

## 3. Model Downloads

We release the DeepSeek-Prover-V1.5 with 7B parameters, including base, SFT and RL models, to the public.

<div align="center">

|            **Model**            |                          **Download**                         |
| :-----------------------------: | :----------------------------------------------------------: |
|   DeepSeek-Prover-V1.5-Base   | [🤗 HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V1.5-Base) |
|   DeepSeek-Prover-V1.5-SFT   | [🤗 HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V1.5-SFT) |
|   DeepSeek-Prover-V1.5-RL   | [🤗 HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V1.5-RL) |

</div>

## 4. License
This code repository is licensed under the MIT License. The use of DeepSeekMath models is subject to the Model License. DeepSeekMath supports commercial use.

See the [LICENSE-CODE](LICENSE-CODE) and [LICENSE-MODEL](LICENSE-MODEL) for more details.

## 5. Citation
```latex
@article{xin2024deepseekproverv15harnessingproofassistant,
      title={DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}, 
      author={Huajian Xin and Z. Z. Ren and Junxiao Song and Zhihong Shao and Wanjia Zhao and Haocheng Wang and Bo Liu and Liyue Zhang and Xuan Lu and Qiushi Du and Wenjun Gao and Qihao Zhu and Dejian Yang and Zhibin Gou and Z. F. Wu and Fuli Luo and Chong Ruan},
      year={2024},
      eprint={2408.08152},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2408.08152}, 
}
```

## 6. Contact

If you have any questions, please raise an issue or contact us at [service@deepseek.com](mailto:service@deepseek.com).
