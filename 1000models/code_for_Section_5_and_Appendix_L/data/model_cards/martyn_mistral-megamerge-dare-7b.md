

# mistral 7b mega merge

This model was merged using [https://github.com/martyn/safetensors-merge-supermario](https://github.com/martyn/safetensors-merge-supermario) with hyperparams `p=0.12` and `lambda=2.1`.

The first entry is the base model:

```
mistralai/Mistral-7B-Instruct-v0.2
uukuguy/speechless-code-mistral-7b-v1.0
AIDC-ai-business/Marcoroni-7B-v3
Weyaxi/Seraph-7B
rwitz/dec10
Intel/neural-chat-7b-v3-3
rwitz/go-bruins-v2
```

To merge your own model:
```
python hf_merge.py to_merge_7b.txt mistral_7b_0.2_merge -p 0.12 -lambda 2.1
```