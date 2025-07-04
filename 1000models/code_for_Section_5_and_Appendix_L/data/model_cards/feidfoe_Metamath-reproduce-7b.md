This model is a reproduction of [Meta-Math](https://huggingface.co/meta-math/MetaMath-7B-V1.0). 
We follow the training instructions described in the original repo as much as possible with minimal modifications.

## Prompt
Unlike the original Meta-math model, we do not use any instructions.

"""

Problem: {query_problem}\nSolution: {gt_solution}

"""

The {gt_solution} is provided in the training stage, whereas it is empty string in the evaluation stage.

