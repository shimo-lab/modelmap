
## 13B-Legerdemain-L2
13B-Legerdemain-L2 is the first model merge of its kind in a series of LLaMaV2 models mixed using a custom script built in-house by CalderaAI called Model-REVOLVER.
M-REVOLVER is also the first in a series of custom scripts based on the concept of mixtuning - not only does the end user have contol over which models are mixed
and their percentages on a per-layer basis, we tackle the problem of overcomplexity that arises from such a level of control; this model is the first of its series.

## The Model-REVOLVER Process Designed by CalderaAI
M-REVOLVER (Rapid Evolution Via Optimized-List Viewer Evaluated Response)
Per-layer merging between parent models is a nebulous inexact science, and therefore impractical to most users despite the raw power it offers. We propose an
entirely new approach that gives the user a clear looking glass into the impact vastly different layer merge configurations between selected parent models of
their choice will have on the potential offspring model - especially its inherited behaviors. We've developed solution MK.1 - A cyclic random pattern search
in place that determines all layer merge ratios, combines test models, infers prompt completions, and deletes a prototype after data collection is saved.
When the cyclic system has completed its entire run, nothing is left but the telemetry collected along with the cycle and layer merge ratios from every
single prototype merge. This data is then used to empower the user to choose which offspring is most fit to their desired outcome. This final step is
only initiated when all necessary data has been aggregated from all assembled-tested-erased prototypes sampled in the search space.

From here, the user is provided five 300 token prompt completions from each and every offspring contender that was created and tested during the cyclic process.
The user simply browses each prototype's series of responses and selects their desired outcome model by entering the cycle number associated with the prompt
completions they feel best suits their vision. That model is then instantly repatriated into the official offspring of its parent models and tokenizer files
found to be most relevant are instantly auto-copied from the parent model dir to the offspring.

That's it - the user instantly has a complete model based on the behavior they decided on, suggested from one of many potentials; all with their own unique
trait inheritence thanks to layer merge auto randomization inside an ordered system. One more thing - the user not only selects how many cycles to run,
the user can edit prompts.txt which the system reads as a single prompt - this means if the user desires to use any multiline instruct format to observe
all potential model outcomes from instruct, or desires simply their own prompt, it's up to them.. simply works.

Link to GitHub for M-REVOLVER are at the end of the model card. More advanced MergeTech toolsets and merge techniques are currently under internal testing
and development by Caldera.

## 13B-Legerdemain-L2 Use
13B-Legerdemain-L2 is capable of following Alpaca instructions however it seems far more receptive to the by-the-book method as seen here:

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
{New Line}
```

The primary model of choice for this model was a story-only model called Holodeck by KoboldAI. Traits preserved seem to be detailed descriptiveness, verbosity,
and characters with personality. The two other models selected were 13B-Nous-Hermes by NousResearch and 13B-orca-8k-3319 by OpenAssistant. I began the process by
providing an incredibly obscene prompt and simply ignored each and every guardrail or censorship laden prompt completion and accepted the offensive ones in turn -
intent wasn't to be crass but trigger censorship parts of the network to test if it's possible to completely undermine them. Second pass with offspring model and
Orca was a simple milquetoast prompt to gauge vocabulary, word flow, and intelligence as I selected the most fit in that category. Result model seems a bit of a
curiosity - different samplers and even a different UI (as I went from TGUI to KoboldAI) seem to uncover different facets of behavior. Godlike preset with Alpaca
Instruct in TGUI worked fine. In KoboldAI some tweaking was necessary to get the same experience. If you choose to test this model, have fun - it's got a mind of
its own.

Model-REVOLVER Git:

https://github.com/Digitous/ModelREVOLVER