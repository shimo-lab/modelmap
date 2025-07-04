

# TinyDolphin-2.8-1.1b

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/655dc641accde1bbc8b41aec/qUCZv8vxXDXi9r-9c0jvP.jpeg)

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations

This is an experimental model trained on 2 3090's by Kearm on the new Dolphin 2.8 dataset by Eric Hartford https://erichartford.com/dolphin 🐬

## Example Outputs

Invent a sinister prank involving teleportation that leaves the victim utterly confused.

```
As you requested, here's how I would go about creating this sinister prank:

    First, we need to find a location where teleportation is possible. This could be anywhere in the world, but let's choose a place with a lot of people around. For example, a crowded street or a busy park.

    Next, we need to gather some materials such as a flashlight, a bag of salt, and a small bottle of water. These items are essential for making the prank work.

    Now, we need to carefully position ourselves near the chosen location. We want to be close enough so that if someone tries to teleport away from us, they won't get lost.

    When the person attempts to teleport, we will pretend to be standing right next to them. This will make it look like they were teleported without our knowing.

    With the flashlight, we will light up the area around us. The brightness of the light should cause the person to lose their sense of direction and become disorientated.

    Finally, we will say something silly or nonsensical while holding the bag of salt. This will make it seem like we are trying to distract them by throwing it at them.

    When the person finally loses their way, we will disappear into thin air. They will think we left them behind, and they will be completely confused.
```

Draft a sarcastic letter from a disgruntled employee to their boss, filled with subtle jabs and veiled threats.

```
Dear [Boss],

I hope this message finds you in good health and high spirits. I am writing to express my deepest dissatisfaction at working under your management. My job has become monotonous and tedious, and I have lost all motivation to continue. The company's lack of accountability and transparency has made it difficult for me to feel valued or respected. In fact, I often find myself questioning whether I should stay on board or look for another opportunity where I can make a difference.

The environment here is hostile and unfriendly, making it challenging to maintain a sense of belonging among employees. I would love to be treated as an individual with unique talents and skills rather than just another cog in the machine. I believe there are more capable individuals within our ranks who deserve recognition and support.

In addition to my frustrations, I also have concerns about the future direction of the company. It seems like we are moving towards automation and outsourcing instead of investing in innovative solutions that will benefit both customers and employees alike. This approach does not align well with my personal values and beliefs.

As someone who values fairness and equality, I urge you to reconsider your decision-making process and explore alternative options that better suit my needs and those of other employees. I understand that change is necessary but it must be done carefully and thoughtfully. Please consider my concerns before making any decisions that may affect my job security and professional growth.

Thank you for your time and consideration. I look forward to discussing these matters further when we meet next.

Sincerely,

[Your Name]
```

Construct a poem describing the rise and rule of succesful malevolent king who ruled through fear and manipulation.

```
In his reign, he ruled with ease, his every move dictated by fear. His name was not known for its wisdom but rather for his ability to control others. He had a dark heart, consumed by malice and power.

His reign brought misery and suffering, as those around him were subjected to his cruelty. His oppression was unmatched, as he held people in check without mercy. Yet, despite all this, he remained invincible, his rule never faltering.

His reign was one of terror, as he wielded his power with absolute authority. His subjects lived in fear, knowing they could be executed at any moment. Yet, they submitted, oblivious to their plight. They did so out of loyalty to their king, or perhaps because they believed it would bring them some measure of comfort.

Their lives were miserable under his tyranny, yet they endured, as they knew they were better off than being free. The king's reign of terror lasted for centuries, leaving behind a legacy of sorrow and despair.
```

Support my efforts! ko-fi.com/kearm

# Orignal Model Card Below

# TinyLlama-1.1B
</div>

https://github.com/jzhang38/TinyLlama

The TinyLlama project aims to **pretrain** a **1.1B Llama model on 3 trillion tokens**. With some proper optimization, we can achieve this within a span of "just" 90 days using 16 A100-40G GPUs 🚀🚀. The training has started on 2023-09-01. 

We adopted exactly the same architecture and tokenizer as Llama 2. This means TinyLlama can be plugged and played in many open-source projects built upon Llama. Besides, TinyLlama is compact with only 1.1B parameters. This compactness allows it to cater to a multitude of applications demanding a restricted computation and memory footprint.

#### This Collection
This collection contains all checkpoints after the 1T fix. Branch name indicates the step and number of tokens seen.

#### Eval

| Model                                     | Pretrain Tokens | HellaSwag | Obqa | WinoGrande | ARC_c | ARC_e | boolq | piqa | avg |
|-------------------------------------------|-----------------|-----------|------|------------|-------|-------|-------|------|-----|
| Pythia-1.0B                               |        300B     | 47.16     | 31.40| 53.43      | 27.05 | 48.99 | 60.83 | 69.21 | 48.30 |
| TinyLlama-1.1B-intermediate-step-50K-104b |        103B     | 43.50     | 29.80| 53.28      | 24.32 | 44.91 | 59.66 | 67.30 | 46.11|
| TinyLlama-1.1B-intermediate-step-240k-503b|        503B     | 49.56     |31.40 |55.80       |26.54  |48.32  |56.91  |69.42  | 48.28 |
| TinyLlama-1.1B-intermediate-step-480k-1007B |     1007B     | 52.54     | 33.40 | 55.96      | 27.82 | 52.36 | 59.54 | 69.91 | 50.22 |
| TinyLlama-1.1B-intermediate-step-715k-1.5T |     1.5T     | 53.68     | 35.20 | 58.33      | 29.18 | 51.89 | 59.08 | 71.65 | 51.29 |
| TinyLlama-1.1B-intermediate-step-955k-2T |     2T     | 54.63     | 33.40 | 56.83      | 28.07 | 54.67 | 63.21 | 70.67 | 51.64 |
| TinyLlama-1.1B-intermediate-step-1195k-2.5T              |     2.5T     | 58.96     | 34.40 | 58.72      | 31.91 | 56.78 | 63.21 | 73.07 | 53.86|
| TinyLlama-1.1B-intermediate-step-1431k-3T |     3T     | 59.20     | 36.00 | 59.12      | 30.12 | 55.25 | 57.83 | 73.29 | 52.99|