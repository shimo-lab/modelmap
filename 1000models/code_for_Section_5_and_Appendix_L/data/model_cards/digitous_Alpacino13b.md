
-Alpac(ino) stands for Alpaca Integrated Narrative Optimization.

This model is a triple model merge of (Alpaca+(CoT+Storytelling)), resulting in a comprehensive boost in Alpaca's reasoning and story writing capabilities.
Alpaca was chosen as the backbone of this merge to ensure Alpaca's instruct format remains dominant. 

Hey! New GGML flavor! WOW!

Thanks to xzuyn for making Alpacino13B accessible to the cool GGML community.
https://huggingface.co/xzuyn/Alpacino-13B-GGML

-Legalese:

This model is under a non-commercial license. This release contains modified weights of Llama13b and is commensurate with good faith that those
who download and/or utilize this model have been granted explicit access to the original Llama weights by Meta AI after filling out the following
form-
https://docs.google.com/forms/d/e/1FAIpQLSfqNECQnMkycAp2jP4Z9TFX0cGR4uf7b_fBxjY_OjhJILlKGA/viewform

-Use Case Example of an Infinite Text-Based Adventure Game With Alpacino13b:

In Text-Generation-WebUI or KoboldAI enable chat mode, name the user Player and name the AI Narrator, then tailor the instructions below as desired and paste in
context/memory field-


\#\#\# Instruction:(carriage return)
Make Narrator function as a text based adventure game that responds with verbose, detailed, and creative descriptions of what happens next after Player's response.
Make Player function as the player input for Narrator's text based adventure game, controlling a character named (insert character name here, their short bio, and
whatever quest or other information to keep consistent in the interaction).
\#\#\# Response:(carriage return)

Testing subjectively suggests ideal presets for both TGUI and KAI are "Storywriter" (temp raised to 1.1) or "Godlike" with context tokens
at 2048 and max generation tokens at ~680 or greater. This model will determine when to stop writing and will rarely use half as many tokens.

-Obligatory:

This model may output offensive text and/or fabricated information; do not use this model for advice
in any domain, especially medical or mental health advice. Meta AI and I are not liable for improper
use or any damages, percieved or otherwise.

-Sourced LoRA Credits:

ChanSung's exellently made Alpaca LoRA

https://huggingface.co/chansung/alpaca-lora-13b

https://huggingface.co/datasets/yahma/alpaca-cleaned

https://github.com/gururise/AlpacaDataCleaned

magicgh's valuable CoT LoRA

https://huggingface.co/magicgh/llama13b-lora-cot

https://huggingface.co/datasets/QingyiSi/Alpaca-CoT

https://github.com/PhoebusSi/alpaca-CoT

GamerUntouch's unique Storytelling LoRA

https://huggingface.co/GamerUntouch/Storytelling-LLaMa-LoRAs