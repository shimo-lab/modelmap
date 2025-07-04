
# Instruct-12B

This model was created by finetuning [EleutherAI's Pythia 12B deduped model](https://huggingface.co/EleutherAI/pythia-12b-deduped) on the [Open-Instruct v1 dataset](https://huggingface.co/datasets/hakurei/open-instruct-v1) for the purpose of allowing Large Language Models to follow the user's intentions. Additionally, this model was developed with the intention of creating an open-source alternative for [OpenAI's InstructGPT series of models](https://openai.com/research/instruction-following), therefore the prompting for Instruct-12B and GPT-3.5 will be quite similar.

If there are any questions that you have regaring this model, please feel free to reach out in my [Discord server](https://discord.gg/touhouai) or in DMs: ``haru#1367``.

## Usage

Every prompt, user input, and generated outputs are delimited by double newlines in the dataset. Therefore, to prompt with this model, you would have to write your prompts in the format of:

```
user instruction here

optional additional user input

generated output
```

So, from the above, a formatted prompt could look something like:

```
Does this tweet have negative or positive sentiment?

i hate my life!!!!
```

And the following generation would look like this:

```
Negative
```

## Example Outputs

```
Explain what computers are while sounding like a western cowboy

Computer, pardner. That there machine can store and process information faster than the fastest gunslinger in these parts. It's got more memory than a steer and can make calculations quicker than a pocket watch. It's the equalizer when it comes to computin', and I aim to keep it that way.
```

```
List me several ways on how to be happy

- Spend time with loved ones
- Take up a hobby
- Exercise regularly
- Eat healthy food
- Get enough sleep
- Stay positive
- Avoid negative people
- Practice meditation
- Do things that make you smile
- Make time for yourself
```

```
How do I make a cake?

Ingredients:
- Flour
- Sugar
- Eggs
- Milk
- Butter
- Baking powder
- Vanilla extract
- Salt
- Baking soda
- Vegetable oil
Steps:
1. Preheat the oven to 350 degrees.
2. Grease a 9x13 inch baking pan.
3. Sift together the flour, sugar, baking powder, baking soda, and salt in a large bowl.
4. In another bowl, mix the eggs, milk, and vanilla extract.
5. Stir in the vegetable oil and mix until combined.
6. Pour the wet ingredients into the dry ingredients and stir until just combined.
7. Pour batter into the prepared pan.
8. Bake for 30 minutes or until a toothpick inserted in the center comes out clean.
9. Allow to cool before frosting.
10. Frost the cake.
11. Enjoy!
```

### Contact

You can reach out to me in my [Discord server](https://discord.gg/touhouai) for any questions.

[![Discord Server](https://discordapp.com/api/guilds/930499730843250783/widget.png?style=banner2)](https://discord.gg/touhouai)