Slerp Merge of shadowml/Marcoro14-7B-slerp and rishiraj/CatPPT
I've been meaning to mix in EmbeddedLLM/Mistral-7B-Merge-14-v0.1 but have had issues so thanks to shadowml that merges it with AIDC-ai-business/Marcoroni-7B-v3

Also, been hearing talks of AIDC-ai-business/Marcoroni-7B-v3 being contaminated, 
I don't know if this is true but if you do in fact find this to be true, make a post on HuggingFaceH4/open_llm_leaderboard so we can keep the board clean

.yaml file for mergekit

```.yaml:
slices:
  - sources:
      - model: shadowml/Marcoro14-7B-slerp
        layer_range: [0, 32]
      - model: rishiraj/CatPPT
        layer_range: [0, 32]
merge_method: slerp
base_model: shadowml/Marcoro14-7B-slerp
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: bfloat16
```