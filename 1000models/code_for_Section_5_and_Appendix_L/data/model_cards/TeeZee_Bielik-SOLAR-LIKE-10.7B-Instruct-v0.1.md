### TeeZee/Bielik-SOLAR-LIKE-10.7B-Instruct-v0.1 ###
Precise recipe used by Upstage to create [SOLAR](https://huggingface.co/upstage/SOLAR-10.7B-v1.0) was applied to https://huggingface.co/speakleash/Bielik-7B-Instruct-v0.1
*(just merge, no finetuning)

### Results ###
- model is still coherent in Polish language, even without finetuning after merge
- instruct mode works in ooba without issues
- model is censored and aligned
- seems that this model scores highest amongst all versions of original Bielik models, further finetunig should improve results even more.

  ![imgage/png](https://huggingface.co/TeeZee/Bielik-SOLAR-LIKE-10.7B-Instruct-v0.1/resolve/main/OpenLLMLeaderboard_results.png)

- on dedicated to Polish speaking LLM leaderboards, its 2nd, just behind instruct version used for this merge, and thats to be expected when applying DUS merge - very small quality loss.

[Polish LLMs leaderboards](https://huggingface.co/spaces/speakleash/open_pl_llm_leaderboard)

- overall it seems like a good base for further finetunig in Polish language.
