# bigstral-12b-32k

`ollama run ehartford/bigstral`

I reached for SOLAR but realized that its only 4k...   Decided to make my own 32k version.

This is [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) with layers interleaved to create a larger 12b model.

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Prompt Format

```
<s>[INST] What is your favourite condiment? [/INST]
Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!</s>
[INST] Do you have dangerously spicy mayonnaise recipes? [/INST]
```

## Example Output


give me some code that is very simple in javascript but would be very difficult in ANSI-C

> In JavaScript, functions are first-class values, which means you can assign them to variables, pass them as arguments to other functions, and even nest them inside other functions. This leads to concise and expressive code.
>
> Here's an example of a simple recursive function that calculates the factorial of a given number in JavaScript:
>
> ```javascript
> const factorial = n => n === 0 ? 1 : n * factorial(n - 1);
>
> console.log(factorial(5)); // Output: 120
>
> ```
>
> Now, let's try to write an equivalent code snippet in ANSI-C with similar functionality:
>
> ```c
> #include <stdio.h>
> #define MAX_RECURSION_DEPTH 1000
> int factorial(int n) {
>     if (n == 0)
>         return 1;
>     else {
>         int result;
>         result = factorial(--n);
>         if (++depth > MAX_RECURSION_DEPTH)
>             while(1){} // Recursion stack overflow
>         return n * result;
>     }
> }
> int main() {
>     int i, result;
>     int n = 5;
>     int depth = 0;
>
>     result = factorial(n);
>     printf("Factorial of %d is: %d\n", n, result);
>     return 0;
> }
> ```
> 
> As you can see, the ANSI-C code becomes more verbose and has several disadvantages compared to JavaScript:
>
> 1. Need to define a maximum recursion depth using a constant or an array index, which can lead to hardcoded limits and potential stack overflow issues.
> 2. The use of preprocessor directives (#define) for defining functions and macros can make the code less readable and harder to understand.
> 3. The lack of closures in ANSI-C requires using static variables or passing arguments as arguments to nested functions, making the code more verbose and less concise.
> ```

## Merge Details
### Merge Method

This model was merged using the passthrough merge method.

### Models Merged

The following models were included in the merge:
* [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
dtype: float16
merge_method: passthrough
slices:
- sources:
  - layer_range: [0, 8]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [4, 12]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [8, 16]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [12, 20]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [16, 24]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [20, 28]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [24, 32]
    model: mistralai/Mistral-7B-Instruct-v0.2

```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_abacusai__bigstral-12b-32k)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |18.05|
|IFEval (0-Shot)    |41.94|
|BBH (3-Shot)       |25.56|
|MATH Lvl 5 (4-Shot)| 0.98|
|GPQA (0-shot)      | 5.70|
|MuSR (0-shot)      |15.86|
|MMLU-PRO (5-shot)  |18.24|

