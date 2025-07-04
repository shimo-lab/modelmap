
[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
**[💵 Donate to OpenAccess AI Collective](https://github.com/sponsors/OpenAccess-AI-Collective) to help us keep building great tools and models!**

# Due to a bug, the initial release of Minotaur 13B dropped a few datasets during training. We have corrected the issue and this is the retrained model

The affected datasets include:
- prose generation
- classification
- coding

# Minotaur 13B (FIXED)

Minotaur 13B is an instruct fine-tuned model on top of LlaMA-13B. Minotaur 13B is fine-tuned **on only completely open datasets** making this model reproducible by anyone.

Questions, comments, feedback, looking to donate, or want to help? Reach out on our [Discord](https://discord.gg/PugNNHAF5r) or email [wing@openaccessaicollective.org](mailto:wing@openaccessaicollective.org)

# Prompts
Chat only style prompts using `USER:`,`ASSISTANT:`.

<img src="https://huggingface.co/openaccess-ai-collective/minotaur-13b/resolve/main/minotaur.png" alt="minotaur" width="600" height="500"/>

# Training Datasets

Minotaur 13B model is fine-tuned on the following openly available datasets:

- [WizardLM](https://huggingface.co/datasets/ehartford/WizardLM_alpaca_evol_instruct_70k_unfiltered)
- [subset of QingyiSi/Alpaca-CoT for roleplay and CoT](https://huggingface.co/QingyiSi/Alpaca-CoT)
- [GPTeacher-General-Instruct](https://huggingface.co/datasets/teknium/GPTeacher-General-Instruct)
- [metaeval/ScienceQA_text_only](https://huggingface.co/datasets/metaeval/ScienceQA_text_only) - instruct for concise responses
- [openai/summarize_from_feedback](https://huggingface.co/datasets/openai/summarize_from_feedback) - instruct augmented tl;dr summarization
- [camel-ai/math](https://huggingface.co/datasets/camel-ai/math)
- [camel-ai/physics](https://huggingface.co/datasets/camel-ai/physics)
- [camel-ai/chemistry](https://huggingface.co/datasets/camel-ai/chemistry)
- [camel-ai/biology](https://huggingface.co/datasets/camel-ai/biology)
- [winglian/evals](https://huggingface.co/datasets/winglian/evals) - instruct augmented datasets
  - custom sysnthetic datasets around misconceptions, in-context qa, jokes, N-tasks problems, and context-insensitivity
  - ARC-Easy & ARC-Challenge - instruct augmented for detailed responses, derived from the `train` split
  - [hellaswag](https://huggingface.co/datasets/hellaswag) - 30K+ rows of instruct augmented for detailed explanations w 30K+ rows, derived from the `train` split
  - [riddle_sense](https://huggingface.co/datasets/riddle_sense) - instruct augmented, derived from the `train` split
  - [gsm8k](https://huggingface.co/datasets/gsm8k) - instruct augmented, derived from the `train` split
  - prose generation

# Shoutouts

Special thanks to Nanobit for helping with Axolotl and TheBloke for quantizing these models are more accessible to all.

# Demo

HF Demo in Spaces available in the [Community ChatBot Arena](https://huggingface.co/spaces/openaccess-ai-collective/rlhf-arena) under the OAAIC Chatbots tab.

## Release Notes

- https://wandb.ai/wing-lian/minotaur-13b/runs/5ystr7w6/workspace

## Build

Minotaur was built with [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) on 6XA100 80GB
 - 1 epochs taking approximately 7.5 hours

## Bias, Risks, and Limitations
Minotaur has not been aligned to human preferences with techniques like RLHF or deployed with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so).
Minotaur was fine-tuned from the base model LLaMA-13B, please refer to its model card's Limitations Section for relevant information. (included below)

## Benchmarks

hf-causal-experimental (pretrained=openaccess-ai-collective/minotaur-13b-fixed), limit: None, provide_description: False, num_fewshot: 0, batch_size: None
|    Task     |Version| Metric |Value |   |Stderr|
|-------------|------:|--------|-----:|---|-----:|
|arc_challenge|      0|acc     |0.4778|_  |0.0146|
|             |       |acc_norm|0.4932|_  |0.0146|
|arc_easy     |      0|acc     |0.7786|_  |0.0085|
|             |       |acc_norm|0.7487|_  |0.0089|
|boolq        |      1|acc     |0.8141|_  |0.0068|
|hellaswag    |      0|acc     |0.6072|_  |0.0049|
|             |       |acc_norm|0.7929|_  |0.0040|
|openbookqa   |      0|acc     |0.3420|_  |0.0212|
|             |       |acc_norm|0.4580|_  |0.0223|
|piqa         |      0|acc     |0.8025|_  |0.0093|
|             |       |acc_norm|0.8107|_  |0.0091|
|winogrande   |      0|acc     |0.7285|_  |0.0125|


## Examples - results may vary based on temperature (0.7 for this) and other settings

```
The following is a chat between a USER and a friendly and helpful ASSISTANT.
USER: Solve for x: 5x = 3x + 10
ASSISTANT:A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.
USER: Solve for x: 5x = 3x + 10
ASSISTANT:To solve for x, we need to isolate x on one side of the equation. We can do this by following these steps:

1. Subtract 3x from both sides of the equation:
5x - 3x = 3x + 10 - 3x
2x = 10

2. Divide both sides of the equation by 2:
2x/2 = 10/2
x = 5
```

```
The following is a chat between a USER and a friendly and helpful ASSISTANT.
USER: You have 3 apples. You eat 2 pears. How many apples do you have left?
ASSISTANT:You still have 3 apples. Eating pears does not affect the number of apples you have.
```

```
The following is a chat between a USER and a friendly and helpful ASSISTANT.
USER: List three words that start with "ex". What is 33 + 77?
ASSISTANT:Three words that start with "ex" are "express", "exact", and "excite". 33 + 77 = 110.
```

```
The following is a chat between a USER and a friendly and helpful ASSISTANT.
USER: Write a haiku about dinosaurs.
ASSISTANT:Titanic creatures roam,
Thunderous footsteps echo,
Extinct but not forgotten.
```
meh, 6/7/7 rather than 5/7/5


```
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.                                                                 
USER: Create an original short story in the style of J.K Rowling about the Weesley family going on a vacation in Australia whith Harry Potter and Hermione Grainger tagging along.                                             
ASSISTANT:Once upon a time, there was a magical family named the Weesleys. They lived in a cozy little cottage at the edge of Hogsmeade village, where they ran a charming bed and breakfast called "The Flying Ford Anglia." A
s any other magical family, they enjoyed adventures that brought them close to nature, so they decided to go on a trip to Australia. They invited their dear friends Harry Potter and Hermione Grainger to join them on this ex
citing journey.                                                                                                                                                                                                                

The Weesleys had been planning for months and had everything ready for their trip. Their children, Freddie and Roxanne were thrilled to visit the land down under, and their parents, George and Angelina, could not wait to ex
plore the beautiful country with their friends. They would be leaving soon, but before departing, there was one small problem - the luggage.

"We can't possibly take all these trunks!" exclaimed Freddie as he stared at the mountain of bags stacked up in front of him.

His father looked at him seriously. "You see, son," he began, "our luggage is crucial because we have to pack all our magical essentials like wand holsters, extra wand chargers, spell books, potions ingredients, and much mo
re."

Roxanne interrupted, "But daddy, we don't even use magic in everyday life! And what if it rains? We'll look weird carrying umbrellas around!"

Her mother joined in. "My dear, you know how unpredictable the weather can be. We must always be prepared for unexpected circumstances. Don't forget that even Muggles carry umbrellas."

After hours of debating, they finally managed to narrow down their luggage list and fit all the necessary supplies into several large trunks. The day had come; they were ready to leave for their grand adventure!

As the Weesleys boarded the Portkey that would transport them across the world, their wands began to glow softly, indicating that they had enough energy to make the journey. The Portkey dropped them off in Sydney, right in 
front of the magnificent Opera House.

They spent the first few days exploring the city, marveling at the iconic architecture and tasting local cuisine. Then, as planned, they headed north to visit the Great Barrier Reef, one of the most famous natural wonders o
f the world.

Harry and Hermione joined them during this leg of the trip, which made it even more enjoyable. Harry regaled them with tales of his own travels while Hermione shared her extensive knowledge of plants, animals, and the envir
onment.

Soon, they arrived at a quaint town nestled among vibrant green hills and surrounded by vast cattle farms. It was here that they would learn about Aboriginal culture and see some truly unique sights.

One morning, after enjoying a hearty breakfast, they set out to explore the local area. They visited a nearby art gallery that showcased amazing Indigenous works of art, including traditional paintings, sculptures, and text
iles. Afterward, they attended a didgeridoo concert given by a talented young musician who captivated everyone with his soulful tunes.

The following day, they embarked on a bushwalk through the rainforest trails. The air was cool and fresh, and the towering trees seemed to reach for the sky. Hermione took great pleasure in identifying various species of pl
ants and explaining their medicinal properties.

As they walked deeper into the forest, they heard faint chattering noises coming from high above. To their surprise, they spotted a group of small, furry creatures perched on a tree branch. They turned out to be native Aust
ralian possums, which delighted the children, especially Freddie, who could communicate with them using sign language.

Later that afternoon, they visited Uluru, also known as Ayers Rock, a massive sandstone monolith located in the heart of the Outback. The sight of its magnificent red hues against the blue sky left them all speechless. They
 spent the rest of the day exploring the rock formation, taking in the breathtaking views and learning about its significance to the Anangu people.

Their last destination was Queensland, home to the world-famous Great Barrier Reef. They spent two days snorkeling, diving, and swimming among the colorful coral reefs, watching schools of fish, sea turtles, and dolphins sw
im past them.

As the sun began to set over the crystal-clear waters, Harry spoke up. "I think it's time we return to reality, don't you agree?" he said, looking at his wife. "This trip has been fantastic, but we can't stay forever."

Everyone nodded in agreement as they prepared themselves for their final journey back to Sydney. When they got there, they gathered on the balcony of their hotel room, reminiscing about the incredible memories they had crea
ted together.

"Thank you for inviting us along on your adventure, Weesleys," said Harry. "It was an honor and a privilege to share this experience with such kind and generous friends. I hope we can do it again sometime."

With tears in their eyes and heavy hearts, they bid each other farewell, promising to keep in touch and meet again soon. And so, their epic journey came to an end. But the memories would remain with them forever, reminding 
them of the power of friendship, the beauty of nature, and the importance of discovering new worlds.
```