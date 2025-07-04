
## 13B-Chimera

## Composition:
[] = applied as LoRA to a composite model | () = combined as composite models

((MantiCore3E+VicunaCocktail)+[SuperCOT+[StorytellingV2+(SuperHOTProtoType-8192ctx+Metharme)]])

This model is the result of an experimental use of LoRAs on language models and model merges that are not the base HuggingFace-format LLaMA model they were intended for.
The desired outcome is to additively apply desired features without paradoxically watering down a model's effective behavior.

Potential limitations - LoRAs applied on top of each other may intercompete.

Subjective results - very promising. Further experimental tests and objective tests are required.

Instruct and Setup Suggestions:

Alpaca instruct verified working, Vicuna instruct formats should work.
If using KoboldAI or Text-Generation-WebUI, recommend switching between Godlike and Storywriter presets and adjusting output length + instructions in memory.
Other presets as well as custom settings can yield highly different results, especially Temperature.
If poking it with a stick doesn't work try another stick.

## Language Models and LoRAs Used Credits:

manticore-13b [Epoch3] by openaccess-ai-collective

https://huggingface.co/openaccess-ai-collective/manticore-13b

vicuna-13b-cocktail by reeducator

https://huggingface.co/reeducator/vicuna-13b-cocktail

SuperCOT-LoRA [13B] by kaiokendev

https://huggingface.co/kaiokendev/SuperCOT-LoRA

Storytelling-LLaMa-LoRA [13B, Version 2] by GamerUnTouch

https://huggingface.co/GamerUntouch/Storytelling-LLaMa-LoRAs

SuperHOT Prototype [13b 8k ctx] by kaiokendev

https://huggingface.co/kaiokendev/SuperHOT-LoRA-prototype

Metharme 13b by PygmalionAI

https://huggingface.co/PygmalionAI/metharme-13b

Also thanks to Meta for LLaMA.

Each model and LoRA was hand picked and considered for what it could contribute to this ensemble.
Thanks to each and every one of you for your incredible work developing some of the best things
to come out of this community.