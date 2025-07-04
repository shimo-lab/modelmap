# GPT-J 6B - PPO_Pygway Mix
## Model description
This is a merged model, using a weighted parameter blend strategy at a (20:20:60) ratio between the models:

- [20%] - KoboldAI/GPT-J-6B-Janeway: https://huggingface.co/KoboldAI/GPT-J-6B-Janeway
- [20%] - reciprocate/ppo_hh_gpt-j: https://huggingface.co/reciprocate/ppo_hh_gpt-j
- [60%] - Pygmalion/Pygmalion-6b DEV (V8 / Part 4): https://huggingface.co/Pygmalion/Pygmalion-6b
 
By their respective authors.

**Warning: PPO_Pygway-V8p4_Dev-6b may generate NSFW or inappropriate content due to the base models (Mainly [Pygmalion/Pygmalion-6b V8P4](https://huggingface.co/Pygmalion/Pygmalion-6b)) being trained on general user logs, and internet archives.**

### Intended Use:

Research purposes only, intended for responsible use.
Express a conversation in natural language, and PPO_Pygmalion will pick up on the conversational format.
Try starting a two line prompt such as:
```
Bot: "Hello, how are you?"
You: "I am doing just fine, thank you."
```
Or any other topic, and the model will carry on in this back and forth style.

## Information:
For more details, check out the related source models, especially [Pygmalion/Pygmalion-6b V8P4](https://huggingface.co/Pygmalion/Pygmalion-6b) for more information on how to utilize the chat bot formatting expected.

In a similar manner to fine-tuning, merging weights does not add information but transforms it, therefore it is important to consider trade-offs.
PPO_Pygway combines `ppo_hh_gpt-j`, `Janeway-6b` and `Pygmalion-6b V8P4`; all three models were blended in a two step process using a simple weighted parameter method
```
(X*A + Y*B)
```
With X & Y being the model weighs, and A/B being how strongly they are represented within the final value. 
The intent of this is to elevate the end-model by borrowing the strongly represented aspects out of each base model, 
but may also weaken other faces of each model, which can be desirable if the base models have problematic traits that need to be worked on.

Blend was done in FP32 and output saved in FP16 for reduced storage needs.


## Limitations and biases
Based on known problems with NLP technology, potential relevant factors include bias (gender, profession, race and religion).

<ins>Warning: This model has a moderate NSFW bias.</ins>

### License
GPT-J-6b is licensed by EleutherAI under the apache-2.0 license. All Rights Reserved.

### BibTeX entry and citation info
```
@misc{gpt-j,
  author = {Wang, Ben and Komatsuzaki, Aran},
  title = {{GPT-J-6B: A 6 Billion Parameter Autoregressive Language Model}},
  howpublished = {\url{https://github.com/kingoflolz/mesh-transformer-jax}},
  year = 2021,
  month = May
}
```

### Credits To:

Models involved:
- https://huggingface.co/EleutherAI/gpt-j-6B
- https://huggingface.co/Pygmalion/Pygmalion-6b
- https://huggingface.co/reciprocate/ppo_hh_gpt-j
- https://huggingface.co/KoboldAI/GPT-J-6B-Janeway

Average weights merging Script credit to Concedo:
- https://huggingface.co/concedo

### Related datasets and articles:

PPO_HH-GPT-J-6b's Dataset is a variant of the Helpful Harmless assistant themed
dataset and Proximal Policy Optimization, specific datasets
used are unknown; listed repo datasets include:
- https://huggingface.co/datasets/reciprocate/summarize_eval_ilql
- https://huggingface.co/datasets/reciprocate/hh_eval_ilql

PPO explained:
- https://paperswithcode.com/method/ppo

Potential HH-type datasets utilized:
- https://huggingface.co/HuggingFaceH4
- https://huggingface.co/datasets/Anthropic/hh-rlhf

No formal evaluation is available for this model at this time.

It is recommend to use this model with the KoboldAI software. All feedback and comments can be directed to TeH_Venom on the KoboldAI discord.

