


#  BEE-spoke-data/Mixtral-GQA-400m-v2




## testing code

```python
# !pip install -U -q transformers datasets accelerate sentencepiece
import pprint as pp
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="BEE-spoke-data/Mixtral-GQA-400m-v2",
    device_map="auto",
)
pipe.model.config.pad_token_id = pipe.model.config.eos_token_id

prompt = "My favorite movie is Godfather because"

res = pipe(
    prompt,
    max_new_tokens=256,
    top_k=4,
    penalty_alpha=0.6,
    use_cache=True,
    no_repeat_ngram_size=4,
    repetition_penalty=1.1,
    renormalize_logits=True,
)
pp.pprint(res[0])
```