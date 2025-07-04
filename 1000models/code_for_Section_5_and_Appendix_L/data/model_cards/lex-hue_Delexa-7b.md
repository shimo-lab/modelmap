# Model Card

### Model Name: Delexa-7b

#### Overview:

**Purpose:** Delexa-7b is our newest large language model designed for general-purpose language tasks. It's currently under development, with ongoing improvements and testing.  

**Status:**  Active development and refinement. More comprehensive evaluation results will be available soon.

**Skills:** Initial evaluations show Delexa-7b performing exceptionally well on general tasks from llm-judge.

**Guardrails** This Model allows 18+ content and lewd content, but it wont let any illegal content through (unless you jailbreak it)

**Evaluation:**  Preliminary results from llm-judge are extremely promising. Delexa-7b demonstrates strong performance, with the potential to surpass established models. Stay tuned for more detailed evaluations!

| model                 | first turn score | second turn score | average score |
|-----------------------|------------------|-------------------|---------------|
| gpt-4                 | 8.95625          | 9.0250            | 8.990625      |
| **Delexa-7b**             | **8.70000**          | 7.5875            | **8.143750**      |
| gpt-3.5-turbo         | 8.07500          | 7.8125            | 7.943750      |
| claude-v1             | 8.15000          | 7.6500            | 7.900000      |
| palm-2-chat-bison-001 | 6.71250          | 6.0875            | 6.400000      |
| vicuna-13b-v1.3       | 6.81250          | 5.9625            | 6.387500      |

**Intended Use:**

* Exploring the capabilities of new language models.
* Experimentation and learning for AI development enthusiasts.  
* Potential applications in areas where STEM reasoning is essential. 

**Potential Risks:** 

* Like other uncensored large language models, Delexa-7b could and will generate harmful, biased, or offensive content if asked to. Responsible use and careful monitoring are essential if this model goes into production for your Business.

**Ethical Considerations**

* Delexa-7b is in the early stages of development. We are committed to ongoing evaluation to identify potential biases and address them proactively.
* Updates to this model card will ensure transparency as Delexa-7b evolves. 

### Additional Notes

Delexa-7b represents an exciting development with the potential to deliver impressive results. We invite the community to explore its capabilities and provide feedback as we continue to refine it.

We were impressed by the Evaluation Train results for our algorithm.  It showed strong performance gains despite using only 30% of our usual training data. We're excited to train it on the complete dataset.

### Support Our Work and join our Community!:

[Our Patreon](https://patreon.com/Lex_Hue?utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink)

[Our Twitter](https://twitter.com/lex_hue)

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_lex-hue__Delexa-7b)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |70.86|
|AI2 Reasoning Challenge (25-Shot)|68.00|
|HellaSwag (10-Shot)              |86.49|
|MMLU (5-Shot)                    |64.69|
|TruthfulQA (0-shot)              |62.13|
|Winogrande (5-shot)              |79.08|
|GSM8k (5-shot)                   |64.75|

