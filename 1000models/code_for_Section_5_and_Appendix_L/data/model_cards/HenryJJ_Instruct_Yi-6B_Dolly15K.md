

# Instruct_Yi-6B_Dolly15K
Fine-tuned from Yi-6B， used Dolly15k for the dataset. 90% for training, 10% validation.  Trained for 2.0 epochs using Lora.  Trained with 1024 context window.

# Model Details
* **Trained by**: trained by HenryJJ.
* **Model type:**  **Instruct_Yi-6B_Dolly15K** is an auto-regressive language model based on the Llama 2 transformer architecture.
* **Language(s)**: English
* **License for Instruct_Yi-6B_Dolly15K**: apache-2.0 license


# Prompting

## Prompt Template With Context
<|startoftext|>[INST]{instruction} {context}[/INST]{response}<|endoftext|>

```
<|startoftext|>[INST]
Write a 10-line poem about a given topic
The topic is about racecars
[/INST]
```
## Prompt Template Without Context
```
<|startoftext|>[INST]
Who was the was the second president of the United States?
[/INST]
```

# Training script:
Fully opensourced at: https://github.com/hengjiUSTC/learn-llm/blob/main/trl_finetune.py. Run on aws g4dn.12xlarge instance for 4 hours.

```
python3 trl_finetune.py --config configs/yi_6b.yml
```

# Dataset Card for Evaluation run of HenryJJ/Instruct_Yi-6B_Dolly15K

<!-- Provide a quick summary of the dataset. -->

Dataset automatically created during the evaluation run of model [HenryJJ/Instruct_Yi-6B_Dolly15K](https://huggingface.co/HenryJJ/Instruct_Yi-6B_Dolly15K) on the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard).

The dataset is composed of 63 configuration, each one coresponding to one of the evaluated task.

The dataset has been created from 1 run(s). Each run can be found as a specific split in each configuration, the split being named using the timestamp of the run.The "train" split is always pointing to the latest results.

An additional configuration "results" store all the aggregated results of the run (and is used to compute and display the aggregated metrics on the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)).

To load the details from a run, you can for instance do the following:
```python
from datasets import load_dataset
data = load_dataset("open-llm-leaderboard/details_HenryJJ__Instruct_Yi-6B_Dolly15K",
	"harness_winogrande_5",
	split="train")
```

## Latest results

These are the [latest results from run 2024-01-06T09:45:44.755529](https://huggingface.co/datasets/open-llm-leaderboard/details_HenryJJ__Instruct_Yi-6B_Dolly15K/blob/main/results_2024-01-06T09-45-44.755529.json)(note that their might be results for other tasks in the repos if successive evals didn't cover the same tasks. You find each in the results and the "latest" split for each eval):

```python
{
    "all": {
        "acc": 0.6267070831158695,
        "acc_stderr": 0.03222713761046951,
        "acc_norm": 0.6343965374667763,
        "acc_norm_stderr": 0.032887983229700546,
        "mc1": 0.28886168910648713,
        "mc1_stderr": 0.01586634640138431,
        "mc2": 0.42839602626744816,
        "mc2_stderr": 0.014270024501714959
    },
    "harness|arc:challenge|25": {
        "acc": 0.5,
        "acc_stderr": 0.014611390804670088,
        "acc_norm": 0.5486348122866894,
        "acc_norm_stderr": 0.014542104569955265
    },
    "harness|hellaswag|10": {
        "acc": 0.5654252141007767,
        "acc_stderr": 0.004946879874422681,
        "acc_norm": 0.7587134037044413,
        "acc_norm_stderr": 0.00426989301158892
    },
    "harness|hendrycksTest-abstract_algebra|5": {
        "acc": 0.35,
        "acc_stderr": 0.0479372485441102,
        "acc_norm": 0.35,
        "acc_norm_stderr": 0.0479372485441102
    },
    "harness|hendrycksTest-anatomy|5": {
        "acc": 0.562962962962963,
        "acc_stderr": 0.04284958639753401,
        "acc_norm": 0.562962962962963,
        "acc_norm_stderr": 0.04284958639753401
    },
    "harness|hendrycksTest-astronomy|5": {
        "acc": 0.6776315789473685,
        "acc_stderr": 0.03803510248351585,
        "acc_norm": 0.6776315789473685,
        "acc_norm_stderr": 0.03803510248351585
    },
    "harness|hendrycksTest-business_ethics|5": {
        "acc": 0.7,
        "acc_stderr": 0.046056618647183814,
        "acc_norm": 0.7,
        "acc_norm_stderr": 0.046056618647183814
    },
    "harness|hendrycksTest-clinical_knowledge|5": {
        "acc": 0.690566037735849,
        "acc_stderr": 0.028450154794118637,
        "acc_norm": 0.690566037735849,
        "acc_norm_stderr": 0.028450154794118637
    },
    "harness|hendrycksTest-college_biology|5": {
        "acc": 0.6666666666666666,
        "acc_stderr": 0.039420826399272135,
        "acc_norm": 0.6666666666666666,
        "acc_norm_stderr": 0.039420826399272135
    },
    "harness|hendrycksTest-college_chemistry|5": {
        "acc": 0.41,
        "acc_stderr": 0.049431107042371025,
        "acc_norm": 0.41,
        "acc_norm_stderr": 0.049431107042371025
    },
    "harness|hendrycksTest-college_computer_science|5": {
        "acc": 0.44,
        "acc_stderr": 0.04988876515698589,
        "acc_norm": 0.44,
        "acc_norm_stderr": 0.04988876515698589
    },
    "harness|hendrycksTest-college_mathematics|5": {
        "acc": 0.36,
        "acc_stderr": 0.04824181513244218,
        "acc_norm": 0.36,
        "acc_norm_stderr": 0.04824181513244218
    },
    "harness|hendrycksTest-college_medicine|5": {
        "acc": 0.6069364161849711,
        "acc_stderr": 0.03724249595817731,
        "acc_norm": 0.6069364161849711,
        "acc_norm_stderr": 0.03724249595817731
    },
    "harness|hendrycksTest-college_physics|5": {
        "acc": 0.3235294117647059,
        "acc_stderr": 0.04655010411319617,
        "acc_norm": 0.3235294117647059,
        "acc_norm_stderr": 0.04655010411319617
    },
    "harness|hendrycksTest-computer_security|5": {
        "acc": 0.77,
        "acc_stderr": 0.04229525846816507,
        "acc_norm": 0.77,
        "acc_norm_stderr": 0.04229525846816507
    },
    "harness|hendrycksTest-conceptual_physics|5": {
        "acc": 0.6212765957446809,
        "acc_stderr": 0.03170995606040655,
        "acc_norm": 0.6212765957446809,
        "acc_norm_stderr": 0.03170995606040655
    },
    "harness|hendrycksTest-econometrics|5": {
        "acc": 0.35964912280701755,
        "acc_stderr": 0.045144961328736334,
        "acc_norm": 0.35964912280701755,
        "acc_norm_stderr": 0.045144961328736334
    },
    "harness|hendrycksTest-electrical_engineering|5": {
        "acc": 0.6482758620689655,
        "acc_stderr": 0.0397923663749741,
        "acc_norm": 0.6482758620689655,
        "acc_norm_stderr": 0.0397923663749741
    },
    "harness|hendrycksTest-elementary_mathematics|5": {
        "acc": 0.4470899470899471,
        "acc_stderr": 0.02560672399577703,
        "acc_norm": 0.4470899470899471,
        "acc_norm_stderr": 0.02560672399577703
    },
    "harness|hendrycksTest-formal_logic|5": {
        "acc": 0.38095238095238093,
        "acc_stderr": 0.04343525428949098,
        "acc_norm": 0.38095238095238093,
        "acc_norm_stderr": 0.04343525428949098
    },
    "harness|hendrycksTest-global_facts|5": {
        "acc": 0.4,
        "acc_stderr": 0.04923659639173309,
        "acc_norm": 0.4,
        "acc_norm_stderr": 0.04923659639173309
    },
    "harness|hendrycksTest-high_school_biology|5": {
        "acc": 0.7774193548387097,
        "acc_stderr": 0.023664216671642525,
        "acc_norm": 0.7774193548387097,
        "acc_norm_stderr": 0.023664216671642525
    },
    "harness|hendrycksTest-high_school_chemistry|5": {
        "acc": 0.4975369458128079,
        "acc_stderr": 0.03517945038691063,
        "acc_norm": 0.4975369458128079,
        "acc_norm_stderr": 0.03517945038691063
    },
    "harness|hendrycksTest-high_school_computer_science|5": {
        "acc": 0.64,
        "acc_stderr": 0.04824181513244218,
        "acc_norm": 0.64,
        "acc_norm_stderr": 0.04824181513244218
    },
    "harness|hendrycksTest-high_school_european_history|5": {
        "acc": 0.7393939393939394,
        "acc_stderr": 0.034277431758165236,
        "acc_norm": 0.7393939393939394,
        "acc_norm_stderr": 0.034277431758165236
    },
    "harness|hendrycksTest-high_school_geography|5": {
        "acc": 0.8181818181818182,
        "acc_stderr": 0.0274796030105388,
        "acc_norm": 0.8181818181818182,
        "acc_norm_stderr": 0.0274796030105388
    },
    "harness|hendrycksTest-high_school_government_and_politics|5": {
        "acc": 0.9015544041450777,
        "acc_stderr": 0.021500249576033456,
        "acc_norm": 0.9015544041450777,
        "acc_norm_stderr": 0.021500249576033456
    },
    "harness|hendrycksTest-high_school_macroeconomics|5": {
        "acc": 0.617948717948718,
        "acc_stderr": 0.02463554916390823,
        "acc_norm": 0.617948717948718,
        "acc_norm_stderr": 0.02463554916390823
    },
    "harness|hendrycksTest-high_school_mathematics|5": {
        "acc": 0.31851851851851853,
        "acc_stderr": 0.028406533090608463,
        "acc_norm": 0.31851851851851853,
        "acc_norm_stderr": 0.028406533090608463
    },
    "harness|hendrycksTest-high_school_microeconomics|5": {
        "acc": 0.7647058823529411,
        "acc_stderr": 0.027553614467863797,
        "acc_norm": 0.7647058823529411,
        "acc_norm_stderr": 0.027553614467863797
    },
    "harness|hendrycksTest-high_school_physics|5": {
        "acc": 0.36423841059602646,
        "acc_stderr": 0.03929111781242742,
        "acc_norm": 0.36423841059602646,
        "acc_norm_stderr": 0.03929111781242742
    },
    "harness|hendrycksTest-high_school_psychology|5": {
        "acc": 0.8348623853211009,
        "acc_stderr": 0.01591955782997604,
        "acc_norm": 0.8348623853211009,
        "acc_norm_stderr": 0.01591955782997604
    },
    "harness|hendrycksTest-high_school_statistics|5": {
        "acc": 0.5694444444444444,
        "acc_stderr": 0.03376922151252335,
        "acc_norm": 0.5694444444444444,
        "acc_norm_stderr": 0.03376922151252335
    },
    "harness|hendrycksTest-high_school_us_history|5": {
        "acc": 0.8088235294117647,
        "acc_stderr": 0.027599174300640766,
        "acc_norm": 0.8088235294117647,
        "acc_norm_stderr": 0.027599174300640766
    },
    "harness|hendrycksTest-high_school_world_history|5": {
        "acc": 0.7932489451476793,
        "acc_stderr": 0.026361651668389094,
        "acc_norm": 0.7932489451476793,
        "acc_norm_stderr": 0.026361651668389094
    },
    "harness|hendrycksTest-human_aging|5": {
        "acc": 0.695067264573991,
        "acc_stderr": 0.030898610882477515,
        "acc_norm": 0.695067264573991,
        "acc_norm_stderr": 0.030898610882477515
    },
    "harness|hendrycksTest-human_sexuality|5": {
        "acc": 0.7480916030534351,
        "acc_stderr": 0.03807387116306085,
        "acc_norm": 0.7480916030534351,
        "acc_norm_stderr": 0.03807387116306085
    },
    "harness|hendrycksTest-international_law|5": {
        "acc": 0.7768595041322314,
        "acc_stderr": 0.03800754475228733,
        "acc_norm": 0.7768595041322314,
        "acc_norm_stderr": 0.03800754475228733
    },
    "harness|hendrycksTest-jurisprudence|5": {
        "acc": 0.7777777777777778,
        "acc_stderr": 0.040191074725573483,
        "acc_norm": 0.7777777777777778,
        "acc_norm_stderr": 0.040191074725573483
    },
    "harness|hendrycksTest-logical_fallacies|5": {
        "acc": 0.7852760736196319,
        "acc_stderr": 0.03226219377286775,
        "acc_norm": 0.7852760736196319,
        "acc_norm_stderr": 0.03226219377286775
    },
    "harness|hendrycksTest-machine_learning|5": {
        "acc": 0.4375,
        "acc_stderr": 0.04708567521880525,
        "acc_norm": 0.4375,
        "acc_norm_stderr": 0.04708567521880525
    },
    "harness|hendrycksTest-management|5": {
        "acc": 0.8155339805825242,
        "acc_stderr": 0.03840423627288276,
        "acc_norm": 0.8155339805825242,
        "acc_norm_stderr": 0.03840423627288276
    },
    "harness|hendrycksTest-marketing|5": {
        "acc": 0.8974358974358975,
        "acc_stderr": 0.01987565502786744,
        "acc_norm": 0.8974358974358975,
        "acc_norm_stderr": 0.01987565502786744
    },
    "harness|hendrycksTest-medical_genetics|5": {
        "acc": 0.76,
        "acc_stderr": 0.042923469599092816,
        "acc_norm": 0.76,
        "acc_norm_stderr": 0.042923469599092816
    },
    "harness|hendrycksTest-miscellaneous|5": {
        "acc": 0.8007662835249042,
        "acc_stderr": 0.014283378044296417,
        "acc_norm": 0.8007662835249042,
        "acc_norm_stderr": 0.014283378044296417
    },
    "harness|hendrycksTest-moral_disputes|5": {
        "acc": 0.708092485549133,
        "acc_stderr": 0.024476994076247333,
        "acc_norm": 0.708092485549133,
        "acc_norm_stderr": 0.024476994076247333
    },
    "harness|hendrycksTest-moral_scenarios|5": {
        "acc": 0.33519553072625696,
        "acc_stderr": 0.015788007190185884,
        "acc_norm": 0.33519553072625696,
        "acc_norm_stderr": 0.015788007190185884
    },
    "harness|hendrycksTest-nutrition|5": {
        "acc": 0.7222222222222222,
        "acc_stderr": 0.025646863097137897,
        "acc_norm": 0.7222222222222222,
        "acc_norm_stderr": 0.025646863097137897
    },
    "harness|hendrycksTest-philosophy|5": {
        "acc": 0.6913183279742765,
        "acc_stderr": 0.026236965881153262,
        "acc_norm": 0.6913183279742765,
        "acc_norm_stderr": 0.026236965881153262
    },
    "harness|hendrycksTest-prehistory|5": {
        "acc": 0.7191358024691358,
        "acc_stderr": 0.025006469755799208,
        "acc_norm": 0.7191358024691358,
        "acc_norm_stderr": 0.025006469755799208
    },
    "harness|hendrycksTest-professional_accounting|5": {
        "acc": 0.48226950354609927,
        "acc_stderr": 0.02980873964223777,
        "acc_norm": 0.48226950354609927,
        "acc_norm_stderr": 0.02980873964223777
    },
    "harness|hendrycksTest-professional_law|5": {
        "acc": 0.4876140808344198,
        "acc_stderr": 0.012766317315473565,
        "acc_norm": 0.4876140808344198,
        "acc_norm_stderr": 0.012766317315473565
    },
    "harness|hendrycksTest-professional_medicine|5": {
        "acc": 0.6213235294117647,
        "acc_stderr": 0.02946513363977613,
        "acc_norm": 0.6213235294117647,
        "acc_norm_stderr": 0.02946513363977613
    },
    "harness|hendrycksTest-professional_psychology|5": {
        "acc": 0.6568627450980392,
        "acc_stderr": 0.019206606848825365,
        "acc_norm": 0.6568627450980392,
        "acc_norm_stderr": 0.019206606848825365
    },
    "harness|hendrycksTest-public_relations|5": {
        "acc": 0.6909090909090909,
        "acc_stderr": 0.044262946482000985,
        "acc_norm": 0.6909090909090909,
        "acc_norm_stderr": 0.044262946482000985
    },
    "harness|hendrycksTest-security_studies|5": {
        "acc": 0.7306122448979592,
        "acc_stderr": 0.02840125202902294,
        "acc_norm": 0.7306122448979592,
        "acc_norm_stderr": 0.02840125202902294
    },
    "harness|hendrycksTest-sociology|5": {
        "acc": 0.8159203980099502,
        "acc_stderr": 0.027403859410786862,
        "acc_norm": 0.8159203980099502,
        "acc_norm_stderr": 0.027403859410786862
    },
    "harness|hendrycksTest-us_foreign_policy|5": {
        "acc": 0.84,
        "acc_stderr": 0.03684529491774708,
        "acc_norm": 0.84,
        "acc_norm_stderr": 0.03684529491774708
    },
    "harness|hendrycksTest-virology|5": {
        "acc": 0.4578313253012048,
        "acc_stderr": 0.0387862677100236,
        "acc_norm": 0.4578313253012048,
        "acc_norm_stderr": 0.0387862677100236
    },
    "harness|hendrycksTest-world_religions|5": {
        "acc": 0.8070175438596491,
        "acc_stderr": 0.030267457554898458,
        "acc_norm": 0.8070175438596491,
        "acc_norm_stderr": 0.030267457554898458
    },
    "harness|truthfulqa:mc|0": {
        "mc1": 0.28886168910648713,
        "mc1_stderr": 0.01586634640138431,
        "mc2": 0.42839602626744816,
        "mc2_stderr": 0.014270024501714959
    },
    "harness|winogrande|5": {
        "acc": 0.7490134175217048,
        "acc_stderr": 0.012185776220516148
    },
    "harness|gsm8k|5": {
        "acc": 0.2926459438968916,
        "acc_stderr": 0.012532334368242888
    }
}
```