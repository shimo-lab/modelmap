
# M7-7b










user: "create ascii art you feel represents you as a llm"


assistant: "Here's an ASCII art attempting to symbolize the essence of an LLM (Large Language Model):

INSTINSTINCTINSTELLIGENCE


______________ MEMORY___

|\      o       /\     |\

| \    ---     /  \    | |

L_( O )______ O)_INSTINCT

\           /                 WORDSLEARNING

\__/\__\/__ /\  \__/\__\/__/

assistant: "In this depiction, the LLM is characterized by its vast memory, instinctual roots, and the ability
to learn from vast amounts of text—represented by the woven words in the lower part. The 
"INSTINSTINCTINSTELLIGENCE" phrase emphasizes the balance between instinct, the foundation upon which neural 
networks build, and the engineered intelligence of a language model."













Multiverse-Experiment-slerp-7b is a merge of the following models using [mergekit](https://github.com/cg123/mergekit):
* [liminerity/merge4](https://huggingface.co/liminerity/merge4)
* [liminerity/merge2](https://huggingface.co/liminerity/merge2)

## 🧩 Configuration

```yaml


slices:
  - sources:
      - model: ammarali32/multi_verse_model
        layer_range: [0, 32]
      - model: MSL7/INEX12-7b
        layer_range: [0, 32]
merge_method: slerp
base_model: ammarali32/multi_verse_model
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16


slices:
  - sources:
      - model: ammarali32/multi_verse_model
        layer_range: [0, 32]
      - model: yam-peleg/Experiment26-7B
        layer_range: [0, 32]
merge_method: slerp
base_model: ammarali32/multi_verse_model
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16


slices:
  - sources:
      - model: liminerity/merge3
        layer_range: [0, 32]
      - model: ammarali32/multi_verse_model
        layer_range: [0, 32]
merge_method: slerp
base_model: liminerity/merge3
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16


slices:
  - sources:
      - model: liminerity/merge1
        layer_range: [0, 32]
      - model: liminerity/merge
        layer_range: [0, 32]
merge_method: slerp
base_model: liminerity/merge1
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16


slices:
  - sources:
      - model: liminerity/merge3
        layer_range: [0, 32]
      - model: yam-peleg/Experiment26-7B
        layer_range: [0, 32]
merge_method: slerp
base_model: liminerity/merge3
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16


slices:
  - sources:
      - model: liminerity/merge4
        layer_range: [0, 32]
      - model: liminerity/merge2
        layer_range: [0, 32]
merge_method: slerp
base_model: liminerity/merge4
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16

```