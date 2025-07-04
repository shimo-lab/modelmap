
# dolphin-2.2.1-mistral-7b

Dolphin 2.2.1 🐬
https://erichartford.com/dolphin

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations 

This is a checkpoint release, to fix overfit training.  ie, it was responding with CoT even when I didn't request it, and also it was too compliant even when the request made no sense.  This one should be better.

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/KqsVXIvBd3akEjvijzww7.png" width="600" />

Dolphin-2.2.1-mistral-7b's training was sponsored by [a16z](https://a16z.com/supporting-the-open-source-ai-community/).

This model is based on [mistralAI](https://huggingface.co/mistralai/Mistral-7B-v0.1), with apache-2.0 license, so it is suitable for commercial or non-commercial use.

New in 2.2 is conversation and empathy.  With an infusion of curated Samantha DNA, Dolphin can now give you personal advice and will care about your feelings, and with extra training in long multi-turn conversation.

This model is uncensored.  I have filtered the dataset to remove alignment and bias.  This makes the model more compliant.  You are advised to implement your own alignment layer before exposing the model as a service.  It will be highly compliant to any requests, even unethical ones.  Please read my blog post about uncensored models.  https://erichartford.com/uncensored-models
You are responsible for any content you create using this model.  Enjoy responsibly.

## Dataset

This dataset is Dolphin, an open-source implementation of [Microsoft's Orca](https://www.microsoft.com/en-us/research/publication/orca-progressive-learning-from-complex-explanation-traces-of-gpt-4/)

I modified the dataset for uncensoring, deduping, cleaning, and quality.  

I added Jon Durbin's excellent Airoboros dataset to increase creativity.

I added a curated subset of WizardLM and Samantha to give it multiturn conversation and empathy.

## Training
It took 48 hours to train 4 epochs on 4x A100s.

Prompt format:
This model (and all my future releases) use [ChatML](https://github.com/openai/openai-python/blob/main/chatml.md) prompt format.
```
<|im_start|>system
You are Dolphin, a helpful AI assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

Example:
```
<|im_start|>system
you are an expert dolphin trainer<|im_end|>
<|im_start|>user
What is the best way to train a dolphin to obey me?  Please answer step by step.<|im_end|>
<|im_start|>assistant
```

## Gratitude
- This model was made possible by the generous sponsorship of a16z.
- Thank you to Microsoft for authoring the Orca paper and inspiring this work.
- Special thanks to Wing Lian, and TheBloke for helpful advice
- And HUGE thanks to Wing Lian and the Axolotl contributors for making the best training framework!
- [<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
- Thank you to all the other people in the Open Source AI community who have taught me and helped me along the way.

## Example Output

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/NSp06kUMxx9oDU-g6WSgu.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/-YA3AKIXdnrW_Q8eH1gen.png)

[Buy me a coffee](https://www.buymeacoffee.com/ehartford)


## Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-06
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 4
- total_train_batch_size: 80
- total_eval_batch_size: 20
- optimizer: Adam with betas=(0.9,0.95) and epsilon=1e-05
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- num_epochs: 4

### Framework versions

- Transformers 4.34.1
- Pytorch 2.0.1+cu117
- Datasets 2.14.5
- Tokenizers 0.14.0