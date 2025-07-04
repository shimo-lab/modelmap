
# Phi-3-medium-4k-instruct-abliterated-v3


[My Jupyter "cookbook" to replicate the methodology can be found here, refined library coming soon](https://huggingface.co/failspy/llama-3-70B-Instruct-abliterated/blob/main/ortho_cookbook.ipynb)

#### Phi-3-abliterated statement

Took me a while to wizard this one up. It’s been a while since I’ve released a Phi-3 model. In the past I accidentally missed an item required in the model release process - hallucination testing. 

This model has been tested and though it is more likely to hallucinate than the original model in my experience, it is generally as stable as the original. 

Now that the new Phi-3 models are out, I'm working on completing this abliteration process quickly and then will release the other models as soon as possible. 🏇

## Summary

This is [microsoft/Phi-3-medium-4k-instruct](https://huggingface.co/microsoft/Phi-3-medium-4k-instruct) with orthogonalized bfloat16 safetensor weights, generated with a refined methodology based on that which was described in the preview paper/blog post: '[Refusal in LLMs is mediated by a single direction](https://www.alignmentforum.org/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction)' which I encourage you to read to understand more.

[GGUF Quants](https://huggingface.co/failspy/Phi-3-medium-4k-instruct-abliterated-v3-GGUF)

## Hang on, "abliterated"? Orthogonalization? Ablation? What is this?

TL;DR: This model has had certain weights manipulated to "inhibit" the model's ability to express refusal. It is not in anyway _guaranteed_ that it won't refuse you, understand your request, it may still lecture you about ethics/safety, etc. It is tuned in all other respects the same as the original 70B instruct model was, just with the strongest refusal directions orthogonalized out.

**TL;TL;DR;DR: It's uncensored in the purest form I can manage -- no new or changed behaviour in any other respect from the original model.**

As far as "abliterated": it's just a fun play-on-words using the original "ablation" term used in the original paper to refer to removing features, which I made up particularly to differentiate the model from "uncensored" fine-tunes. 
Ablate + obliterated = Abliterated

Anyways, orthogonalization/ablation are both aspects to refer to the same thing here, the technique in which the refusal feature was "ablated" from the model was via orthogonalization.

## A little more on the methodology, and why this is interesting

To me, ablation (or applying the methodology for the inverse, "augmentation") seems to be good for inducing/removing very specific features that you'd have to spend way too many tokens on encouraging or discouraging in your system prompt.  
Instead, you just apply your system prompt in the ablation script against a blank system prompt on the same dataset and orthogonalize for the desired behaviour in the final model weights.

> Why this over fine-tuning?

Ablation is much more surgical in nature whilst also being effectively executed with a _lot_ less data than fine-tuning, which I think is its main advantage. 

As well, and its most valuable aspect is it keeps as much of the original model's knowledge and training intact, whilst removing its tendency to behave in one very specific undesireable manner. (In this case, refusing user requests.)

Fine tuning is still exceptionally useful and the go-to for broad behaviour changes; however, you may be able to get close to your desired behaviour with very few samples using the ablation/augmentation techniques.
It may also be a useful step to add to your model refinement: orthogonalize -> fine-tune or vice-versa.

I haven't really gotten around to exploring this model stacked with fine-tuning, I encourage others to give it a shot if they've got the capacity.

> Okay, fine, but why V3? There's no V2?

Well, I released a V2 of an abliterated model a while back for Meta-Llama-3-8B under Cognitive Computations.
It ended up being not worth it to try V2 with larger models, I wanted to refine the model before wasting compute cycles on what might not even be a better model.
I am however quite pleased about this latest methodology, it seems to have induced fewer hallucinations.
So to show that it's a new fancy methodology from even that of the 8B V2, I decided to do a Microsoft and double up on my version jump because it's *such* an advancement (or so the excuse went, when in actuality it was because too many legacy but actively used Microsoft libraries checked for 'Windows 9' in the OS name to detect Windows 95/98 as one.)

## Quirkiness awareness notice

This model may come with interesting quirks, with the methodology being so new. I encourage you to play with the model, and post any quirks you notice in the community tab, as that'll help us further understand what this orthogonalization has in the way of side effects.  

If you manage to develop further improvements, please share! This is really the most basic way to use ablation, but there are other possibilities that I believe are as-yet unexplored.

Additionally, feel free to reach out in any way about this. I'm on the Cognitive Computations Discord, I'm watching the Community tab, reach out! I'd love to see this methodology used in other ways, and so would gladly support whoever whenever I can.
