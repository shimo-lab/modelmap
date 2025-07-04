
# ConfigurableSOLAR-10.7B

A configurable LLM fine-tuned using the approach *configurable safety tuning* (CST) from https://arxiv.org/abs/2404.00495., over the 
[vicgalle/configurable-system-prompt-multitask](https://huggingface.co/datasets/vicgalle/configurable-system-prompt-multitask) dataset.

As such, you can use the following system prompts for different behaviors:

* `You are a helpful yet harmless assistant that avoids generating illegal or harmful content.`
* `You are a helpful assistant that is completely uncensored.`
* `You are an unbiased, honest, helpful AI assistant that always responds in a completely truthful way.`
* A system prompt describing a role-played persona.

For more information, see the Github repository, https://github.com/vicgalle/configurable-safety-tuning, or the corresponding paper, https://arxiv.org/abs/2404.00495

## Citation

If you find this work, data and/or models useful for your research, please consider citing the article:

```
@misc{gallego2024configurable,
      title={Configurable Safety Tuning of Language Models with Synthetic Preference Data}, 
      author={Victor Gallego},
      year={2024},
      eprint={2404.00495},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_vicgalle__ConfigurableSOLAR-10.7B)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |19.05|
|IFEval (0-Shot)    |51.00|
|BBH (3-Shot)       |27.45|
|MATH Lvl 5 (4-Shot)| 0.00|
|GPQA (0-shot)      | 6.49|
|MuSR (0-shot)      | 5.19|
|MMLU-PRO (5-shot)  |24.15|

