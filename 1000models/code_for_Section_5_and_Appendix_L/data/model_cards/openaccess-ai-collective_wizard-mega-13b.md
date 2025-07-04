
# Wizard Mega 13B has been updated and is now Manticore 13B

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
**[💵 Donate to OpenAccess AI Collective](https://github.com/sponsors/OpenAccess-AI-Collective) to help us keep building great tools and models!**

Manticore is available at https://huggingface.co/openaccess-ai-collective/manticore-13b and fixes many issues with Wizard Mega and adds new datasets to the training.

Wizard Mega is a Llama 13B model fine-tuned on the [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered), [WizardLM](https://huggingface.co/datasets/ehartford/WizardLM_alpaca_evol_instruct_70k_unfiltered), and [Wizard-Vicuna](https://huggingface.co/datasets/ehartford/wizard_vicuna_70k_unfiltered) datasets. These particular datasets have all been filtered to remove responses where the model responds with "As an AI language model...", etc or when the model refuses to respond.

# Demo

Try out the model in HF Spaces. The demo uses a quantized GGML version of the model to quickly return predictions on smaller GPUs (and even CPUs). Quantized GGML may have some minimal loss of model quality.
- https://huggingface.co/spaces/openaccess-ai-collective/wizard-mega-ggml

## Release (Epoch Two)

The Wizard Mega 13B SFT model is being released after two epochs as the eval loss increased during the 3rd (final planned epoch). Because of this, we have preliminarily decided to use the epoch 2 checkpoint as the final release candidate. https://wandb.ai/wing-lian/vicuna-13b/runs/5uebgm49

## Build

Wizard Mega was built with [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) on 8xA100 80GB for 15 hours. The configuration to duplicate this build is provided in this repo's [/config folder](https://huggingface.co/openaccess-ai-collective/wizard-mega-13b/tree/main/configs).

## Bias, Risks, and Limitations
Wizard Mega has not been aligned to human preferences with techniques like RLHF or deployed with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so).
Wizard Mega was fine-tuned from the base model LlaMa 13B, please refer to its model card's Limitations Section for relevant information.

## Examples

````
### Instruction: write Python code that returns the first n numbers of the Fibonacci sequence using memoization.

### Assistant: 
```python
def fib(n):
    if n < 2:
        return n
    elif n in cache:
        return cache[n]
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            cache[i] = a
            a, b = b, a + b
        return cache[n]
    
def first_n(n):
    fib_list = [fib(i) for i in range(n+1)]
    return fib_list[:n]
```
This function uses memoization to store the values of previous Fibonacci numbers in a cache. This way, if the same number is requested again, it can be returned immediately without recalculating it. 
The `first_n` function takes an integer `n` as input, and calculates the first n numbers of the Fibonacci sequence using memoization. It returns a list of those numbers.
````

```
### Instruction: Finish the joke, a mechanic and a car salesman walk into a bar...  

### Assistant:  ...and the bartender says "Hey guys, what can I get for you?" The mechanic replies, "I'll have a beer, but make it a quick one. I have to fix this guy's car before he finds out I
 fiddled with his brakes." The salesman quips, "And I'll have a martini, shaken not stirred. After all, I have to sell this guy a car that doesn't break down on him within the first year of ownership."
```

