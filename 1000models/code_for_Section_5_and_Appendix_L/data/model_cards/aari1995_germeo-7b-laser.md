
(Evaluation WIP)

## Hermes + Leo + German Laser = Germeo

## Germeo-7B-Laser
A German-English understanding, but German-only speaking model merged from Hermeo-7B.

### Model details

**Merged from**: leo-mistral-hessianai-7b-chat and DPOpenHermes-7B-v2

**Model type**: Causal decoder-only transformer language model

**Languages**: German replies with English Understanding Capabilities

**Laser-Data**: LeoLM/OpenSchnabeltier


This is an early experiment on laser and its influence on language understanding. It generally improves the language understanding capabilities.
The hypothesis is that it degrades the probability of English replies and increasing those of German replies. The models internal German capabilities are boosted. 

Will keep you updated..

### Acknowledgements:

I would like to thank everyone that participated in making this model and its training possible:
To [@malteos](https://huggingface.co/malteos) for hermeo
To [@cognitivecomputations](https://huggingface.co/cognitivecomputations) and Fernando Fernandes Neto for their implementation of LASER
To [@LeoLM](https://huggingface.co/LeoLM) and Björn for the OpenSchnabeltier dataset.


### Prompt format:

```python
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
# Convert prompt to tokens
prompt_template = """<|im_start|>system
Du bist ein hilfreicher Assistent.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant"""

prompt = "Schreibe eine Stellenanzeige für Data Scientist bei AXA!"

final_prompt = prompt_template.format(prompt=prompt)
```

#### Limit the model to output reply-only:
  To solve this, you need to implement a custom stopping criteria:

```python
from transformers import StoppingCriteria
class GermeoStoppingCriteria(StoppingCriteria):
  def __init__(self, target_sequence, prompt):
      self.target_sequence = target_sequence
      self.prompt=prompt

  def __call__(self, input_ids, scores, **kwargs):
      # Get the generated text as a string
      generated_text = tokenizer.decode(input_ids[0])
      generated_text = generated_text.replace(self.prompt,'')
      # Check if the target sequence appears in the generated text
      if self.target_sequence in generated_text:
          return True  # Stop generation

      return False  # Continue generation

  def __len__(self):
      return 1

  def __iter__(self):
      yield self
```
This then expects your input prompt (formatted as given into the model), and a stopping criteria, in this case the im_end token. Simply add it to the generation:

```python
generation_output = model.generate(
    tokens, 
    streamer=streamer,
    max_new_tokens=1012,
    stopping_criteria=GermeoStoppingCriteria("<|im_end|>", prompt_template.format(prompt=prompt))
)
```

### German benchmarks

| **German tasks:**             | **MMLU-DE**    | **Hellaswag-DE** | **ARC-DE**      |**Average**      |
|-------------------------------|-------------|---------------|--------------|--------------|
| **Models / Few-shots:**       | _(5 shots)_ | _(10 shots)_  | _(24 shots)_ | |
| _7B parameters_      |  | |  | |
| llama-2-7b                    | 0.400       | 0.513         | 0.381        | 0.431  |
| leo-hessianai-7b              | 0.400       | 0.609         | 0.429        | 0.479 |
| bloom-6b4-clp-german          | 0.274       | 0.550         | 0.351        | 0.392 |
| mistral-7b                    | **0.524**       | 0.588         | 0.473        | 0.528 |
| leo-mistral-hessianai-7b      | 0.481       | 0.663         | 0.485        | 0.543 |
| leo-mistral-hessianai-7b-chat | 0.458       | 0.617         | 0.465        | 0.513 |
| DPOpenHermes-7B-v2            | 0.517         | 0.603         | 0.515        | 0.545 |
| hermeo-7b                     | 0.511       | **0.668**         | **0.528**        | **0.569** |
| **germeo-7b-laser (this model)**| ?       | ?        | ?      | ? |
| _13B parameters_      |  | |  | |
| llama-2-13b                    | 0.469       | 0.581        | 0.468        | 0.506 |
| leo-hessianai-13b              | **0.486**       | **0.658**         | **0.509**       | **0.551** |
| _70B parameters_      |  | |  | |
| llama-2-70b                    | 0.597       | 0.674       | 0.561       | 0.611 |
| leo-hessianai-70b              | **0.653**       | **0.721**         | **0.600**       | **0.658** |


Even though the model does not generate English text without being explicitly asked, performance on English Benchmarks is still up:

### English benchmarks

| **English tasks:**                 | **MMLU**    | **Hellaswag** | **ARC**      | **Average** |
|------------------------------------|-------------|---------------|--------------|-------------|
| **Models / Few-shots:**            | _(5 shots)_ | _(10 shots)_  | _(24 shots)_ |             |
| llama-2-7b                         |       0.466 |         0.786 |        0.530 |       0.594 |
| leolm-hessianai-7b                 |       0.423 |         0.759 |        0.522 |       0.568 |
| bloom-6b4-clp-german               |       0.264 |         0.525 |        0.328 |       0.372 |
| mistral-7b                         |   **0.635** |     **0.832** |        0.607 |   **0.691** |
| leolm-mistral-hessianai-7b         |       0.550 |         0.777 |        0.518 |       0.615 |
| hermeo-7b                          |       0.601 |         0.821 |    **0.620** |       0.681 |
| germeo-7b-laser (this model)       |       0.601 |         0.828 |        0.608 |       0.679 |
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_aari1995__germeo-7b-laser)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |62.82|
|AI2 Reasoning Challenge (25-Shot)|60.75|
|HellaSwag (10-Shot)              |82.81|
|MMLU (5-Shot)                    |60.57|
|TruthfulQA (0-shot)              |53.83|
|Winogrande (5-shot)              |75.61|
|GSM8k (5-shot)                   |43.37|

