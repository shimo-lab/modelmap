
## 13B-Thorns [An Instruct Based LLaMAv2-13B Ensemble Merge | Alpaca Format]
# WARNING - This Model Is Uncensored And Has Not Been Fully Tested For Toxicity. This Is A Research Artifact Intended For Responsible Use. May Generate Offensive And Misleading Content. Do Not Treat Language Sythesized By This Research Artifact As Advice Or As Factual In Any Domain. CalderaAI Strictly Does Not Condone Use Of This Release Outside The Domain Of Research Or Entertainment. 

# Composition:

13B-Thorns-l2 utilizes a new merge method called Spherical Linear Interpolation. By merging data as a spherical vector store concept, a combined pair of models have a smoother transition between feature spaces that are characteristic of each model, resulting in a more coherent fusion of both model's unique strengths.


## Our implementation of Spherical Linear Interpolation for LLM merging: https://github.com/Digitous/LLM-SLERP-Merge


## Note: Skip to the TL;DR section for the finalized design this model is comprised of.


Thorns' design is based on the concept of purposed segmentation, in this case we have two-


--Logic Segment (MK1):


Fine-Tuned parent models were hand selected and reviewed for datasets, performance, least restrictive censorship, and community perception of coherence and utility. Ultimately we decided on four models to merge in pairs of two, then combine those offspring for a quad merged logic cluster.
All four models were merged using the SLERP method. Yes the name is annoyingly funny. SLERP.


--Creativity and Imagination Segment (MK1):


Flawed first approach (a takeaway on LoRAs);


We then decided the creativity and imagination segment could be as simple as one model, especially if its dataset design, tagging, training quality, and proven track record is above and beyond. KoboldAI's Holodeck model is the result of a dataset that is years of collected, organized, tagged, deduped, and cleaned data. Holodeck alone would be beyond sufficient for the segment we view as the 'subconscious' segment of the model ensemble, however we applied the LIMA RP PEFT to it for extended variety of a different kind.
That's where we got carried away. LoRAs offer unique augmentation to model merge possibilities, and the decision was made to take the result of that segment and add two more LoRAs to see if they further extended Holodeck, settling on Kimiko and Janine; two very different RP and conversational LoRAs.
This was a bad move, as when we SLERP merged that version of the imagination segment to the logic segment the result was a ranting mess that followed instructions but was the equivalent of a child scribbling all over the place and ignoring obvious chains of logic and a mushy amalgam of awkward creative behavior that had no semblance of coherency.
The composite model was slated to be named 13B-Astronomicon; after all the work that went into it and the flatly bland result, the name was abandoned and the next move, which is a byproduct experiment of Astronomicon is what became Thorn.. because this project became a thorn in our side.


Because pain is fun, and persistence in design iteration is the only way forward, we reworked our approach to both segment ensembles following one idea - all three Roleplay and Conversational LoRAs stay no matter what because sure why not add arbitrary rules to the redesign phase at this point.


## TL;DR Section


--Finalized Logic and Creativity Segments (MK2):


After a few meetings with our top teams of model hacking memegineers we drafted Thorns MK2, which was prompty fast tracked for production by the Roko's Basilisk Shadow Council.


..Actually I just redid the merge like this:

```
-Model Merge Ensemble Key-

{} = SLERP Merge | [] = PEFT Merge | () = Composite Model

({({NousHermes+Chronos}[Kimiko])+({Platupus+AiroborosM2.0}[Janine])}{Holodeck[LIMA RP]})
```

## Findings:

-Strategically fusing LoRAs to models that stand to gain the most from them and then merging the result into the ensemble is exceptionally effective.


-Stacking the exact same LoRAs onto one model then merging that into the ensemble results in noisy garbage.


## Language Models and LoRAs Used Credits:


All models and adapters used are LLaMAv2-13B.

# Models:

Nous-Hermes

Chronos

Platypus

Airoboros

Holodeck

# Adapters:

Kimiko

Janine

LIMA RP


Also thanks to Meta for LLaMAv2 and deciding to allow the research community at large to benefit from their incredible work.


Each model and LoRA was hand picked and considered for what it could contribute to this ensemble.
Thanks to each and every one of you for your incredible work developing some of the best things
to come out of this community.