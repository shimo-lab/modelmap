
# Instruct_Mixtral-7B-v0.1_Dolly15K
Fine-tuned from Mixtral-7B-v0.1， used Dolly15k for the dataset. 90% for training, 10% validation.  Trained for 2.0 epochs using Lora.  Trained with 1024 context window.

# Model Details
* **Trained by**: trained by HenryJJ.
* **Model type:**  **Instruct_Mixtral-7B-v0.1_Dolly15K** is an auto-regressive language model based on the Llama 2 transformer architecture.
* **Language(s)**: English
* **License for Instruct_Mixtral-7B-v0.1_Dolly15K**: apache-2.0 license


# Prompting

## Prompt Template With Context

```
Write a 10-line poem about a given topic

Input:

The topic is about racecars

Output:
```
## Prompt Template Without Context
```
Who was the was the second president of the United States?

Output:
```

# Training script:
Fully opensourced at: https://github.com/hengjiUSTC/learn-llm/blob/main/trl_finetune.py. 

## Latest results

These are the [latest results from run 2024-01-04T13:27:32.660899](https://huggingface.co/datasets/open-llm-leaderboard/details_HenryJJ__Instruct_Mistral-7B-v0.1_Dolly15K/blob/main/results_2024-01-04T13-27-32.660899.json)(note that their might be results for other tasks in the repos if successive evals didn't cover the same tasks. You find each in the results and the "latest" split for each eval):

```python
{
    "all": {
        "acc": 0.6241143484289186,
        "acc_stderr": 0.032689663124831826,
        "acc_norm": 0.6299031400315822,
        "acc_norm_stderr": 0.033361474961048916,
        "mc1": 0.2802937576499388,
        "mc1_stderr": 0.015723139524608767,
        "mc2": 0.435601924823795,
        "mc2_stderr": 0.014179199089974604
    },
    "harness|arc:challenge|25": {
        "acc": 0.5571672354948806,
        "acc_stderr": 0.014515573873348906,
        "acc_norm": 0.5938566552901023,
        "acc_norm_stderr": 0.014351656690097862
    },
    "harness|hellaswag|10": {
        "acc": 0.6253734315873332,
        "acc_stderr": 0.004830371317841054,
        "acc_norm": 0.826229834694284,
        "acc_norm_stderr": 0.00378137335887
    },
    "harness|hendrycksTest-abstract_algebra|5": {
        "acc": 0.31,
        "acc_stderr": 0.04648231987117316,
        "acc_norm": 0.31,
        "acc_norm_stderr": 0.04648231987117316
    },
    "harness|hendrycksTest-anatomy|5": {
        "acc": 0.6148148148148148,
        "acc_stderr": 0.04203921040156279,
        "acc_norm": 0.6148148148148148,
        "acc_norm_stderr": 0.04203921040156279
    },
    "harness|hendrycksTest-astronomy|5": {
        "acc": 0.6513157894736842,
        "acc_stderr": 0.03878139888797611,
        "acc_norm": 0.6513157894736842,
        "acc_norm_stderr": 0.03878139888797611
    },
    "harness|hendrycksTest-business_ethics|5": {
        "acc": 0.57,
        "acc_stderr": 0.04975698519562428,
        "acc_norm": 0.57,
        "acc_norm_stderr": 0.04975698519562428
    },
    "harness|hendrycksTest-clinical_knowledge|5": {
        "acc": 0.660377358490566,
        "acc_stderr": 0.029146904747798328,
        "acc_norm": 0.660377358490566,
        "acc_norm_stderr": 0.029146904747798328
    },
    "harness|hendrycksTest-college_biology|5": {
        "acc": 0.7291666666666666,
        "acc_stderr": 0.03716177437566017,
        "acc_norm": 0.7291666666666666,
        "acc_norm_stderr": 0.03716177437566017
    },
    "harness|hendrycksTest-college_chemistry|5": {
        "acc": 0.46,
        "acc_stderr": 0.05009082659620332,
        "acc_norm": 0.46,
        "acc_norm_stderr": 0.05009082659620332
    },
    "harness|hendrycksTest-college_computer_science|5": {
        "acc": 0.54,
        "acc_stderr": 0.05009082659620333,
        "acc_norm": 0.54,
        "acc_norm_stderr": 0.05009082659620333
    },
    "harness|hendrycksTest-college_mathematics|5": {
        "acc": 0.38,
        "acc_stderr": 0.04878317312145632,
        "acc_norm": 0.38,
        "acc_norm_stderr": 0.04878317312145632
    },
    "harness|hendrycksTest-college_medicine|5": {
        "acc": 0.5838150289017341,
        "acc_stderr": 0.03758517775404947,
        "acc_norm": 0.5838150289017341,
        "acc_norm_stderr": 0.03758517775404947
    },
    "harness|hendrycksTest-college_physics|5": {
        "acc": 0.35294117647058826,
        "acc_stderr": 0.04755129616062946,
        "acc_norm": 0.35294117647058826,
        "acc_norm_stderr": 0.04755129616062946
    },
    "harness|hendrycksTest-computer_security|5": {
        "acc": 0.77,
        "acc_stderr": 0.04229525846816505,
        "acc_norm": 0.77,
        "acc_norm_stderr": 0.04229525846816505
    },
    "harness|hendrycksTest-conceptual_physics|5": {
        "acc": 0.5574468085106383,
        "acc_stderr": 0.032469569197899575,
        "acc_norm": 0.5574468085106383,
        "acc_norm_stderr": 0.032469569197899575
    },
    "harness|hendrycksTest-econometrics|5": {
        "acc": 0.5,
        "acc_stderr": 0.047036043419179864,
        "acc_norm": 0.5,
        "acc_norm_stderr": 0.047036043419179864
    },
    "harness|hendrycksTest-electrical_engineering|5": {
        "acc": 0.5724137931034483,
        "acc_stderr": 0.041227371113703316,
        "acc_norm": 0.5724137931034483,
        "acc_norm_stderr": 0.041227371113703316
    },
    "harness|hendrycksTest-elementary_mathematics|5": {
        "acc": 0.3994708994708995,
        "acc_stderr": 0.02522545028406788,
        "acc_norm": 0.3994708994708995,
        "acc_norm_stderr": 0.02522545028406788
    },
    "harness|hendrycksTest-formal_logic|5": {
        "acc": 0.3968253968253968,
        "acc_stderr": 0.04375888492727061,
        "acc_norm": 0.3968253968253968,
        "acc_norm_stderr": 0.04375888492727061
    },
    "harness|hendrycksTest-global_facts|5": {
        "acc": 0.35,
        "acc_stderr": 0.0479372485441102,
        "acc_norm": 0.35,
        "acc_norm_stderr": 0.0479372485441102
    },
    "harness|hendrycksTest-high_school_biology|5": {
        "acc": 0.7483870967741936,
        "acc_stderr": 0.024685979286239956,
        "acc_norm": 0.7483870967741936,
        "acc_norm_stderr": 0.024685979286239956
    },
    "harness|hendrycksTest-high_school_chemistry|5": {
        "acc": 0.5221674876847291,
        "acc_stderr": 0.03514528562175008,
        "acc_norm": 0.5221674876847291,
        "acc_norm_stderr": 0.03514528562175008
    },
    "harness|hendrycksTest-high_school_computer_science|5": {
        "acc": 0.67,
        "acc_stderr": 0.04725815626252607,
        "acc_norm": 0.67,
        "acc_norm_stderr": 0.04725815626252607
    },
    "harness|hendrycksTest-high_school_european_history|5": {
        "acc": 0.7636363636363637,
        "acc_stderr": 0.03317505930009182,
        "acc_norm": 0.7636363636363637,
        "acc_norm_stderr": 0.03317505930009182
    },
    "harness|hendrycksTest-high_school_geography|5": {
        "acc": 0.7525252525252525,
        "acc_stderr": 0.030746300742124498,
        "acc_norm": 0.7525252525252525,
        "acc_norm_stderr": 0.030746300742124498
    },
    "harness|hendrycksTest-high_school_government_and_politics|5": {
        "acc": 0.844559585492228,
        "acc_stderr": 0.026148483469153314,
        "acc_norm": 0.844559585492228,
        "acc_norm_stderr": 0.026148483469153314
    },
    "harness|hendrycksTest-high_school_macroeconomics|5": {
        "acc": 0.6205128205128205,
        "acc_stderr": 0.024603626924097417,
        "acc_norm": 0.6205128205128205,
        "acc_norm_stderr": 0.024603626924097417
    },
    "harness|hendrycksTest-high_school_mathematics|5": {
        "acc": 0.337037037037037,
        "acc_stderr": 0.028820884666253252,
        "acc_norm": 0.337037037037037,
        "acc_norm_stderr": 0.028820884666253252
    },
    "harness|hendrycksTest-high_school_microeconomics|5": {
        "acc": 0.6260504201680672,
        "acc_stderr": 0.031429466378837076,
        "acc_norm": 0.6260504201680672,
        "acc_norm_stderr": 0.031429466378837076
    },
    "harness|hendrycksTest-high_school_physics|5": {
        "acc": 0.33774834437086093,
        "acc_stderr": 0.03861557546255169,
        "acc_norm": 0.33774834437086093,
        "acc_norm_stderr": 0.03861557546255169
    },
    "harness|hendrycksTest-high_school_psychology|5": {
        "acc": 0.7944954128440367,
        "acc_stderr": 0.01732435232501601,
        "acc_norm": 0.7944954128440367,
        "acc_norm_stderr": 0.01732435232501601
    },
    "harness|hendrycksTest-high_school_statistics|5": {
        "acc": 0.5046296296296297,
        "acc_stderr": 0.03409825519163572,
        "acc_norm": 0.5046296296296297,
        "acc_norm_stderr": 0.03409825519163572
    },
    "harness|hendrycksTest-high_school_us_history|5": {
        "acc": 0.8137254901960784,
        "acc_stderr": 0.027325470966716312,
        "acc_norm": 0.8137254901960784,
        "acc_norm_stderr": 0.027325470966716312
    },
    "harness|hendrycksTest-high_school_world_history|5": {
        "acc": 0.7763713080168776,
        "acc_stderr": 0.027123298205229966,
        "acc_norm": 0.7763713080168776,
        "acc_norm_stderr": 0.027123298205229966
    },
    "harness|hendrycksTest-human_aging|5": {
        "acc": 0.6860986547085202,
        "acc_stderr": 0.031146796482972465,
        "acc_norm": 0.6860986547085202,
        "acc_norm_stderr": 0.031146796482972465
    },
    "harness|hendrycksTest-human_sexuality|5": {
        "acc": 0.7557251908396947,
        "acc_stderr": 0.037683359597287434,
        "acc_norm": 0.7557251908396947,
        "acc_norm_stderr": 0.037683359597287434
    },
    "harness|hendrycksTest-international_law|5": {
        "acc": 0.7851239669421488,
        "acc_stderr": 0.037494924487096966,
        "acc_norm": 0.7851239669421488,
        "acc_norm_stderr": 0.037494924487096966
    },
    "harness|hendrycksTest-jurisprudence|5": {
        "acc": 0.75,
        "acc_stderr": 0.04186091791394607,
        "acc_norm": 0.75,
        "acc_norm_stderr": 0.04186091791394607
    },
    "harness|hendrycksTest-logical_fallacies|5": {
        "acc": 0.7791411042944786,
        "acc_stderr": 0.03259177392742178,
        "acc_norm": 0.7791411042944786,
        "acc_norm_stderr": 0.03259177392742178
    },
    "harness|hendrycksTest-machine_learning|5": {
        "acc": 0.41964285714285715,
        "acc_stderr": 0.04684099321077106,
        "acc_norm": 0.41964285714285715,
        "acc_norm_stderr": 0.04684099321077106
    },
    "harness|hendrycksTest-management|5": {
        "acc": 0.7961165048543689,
        "acc_stderr": 0.039891398595317706,
        "acc_norm": 0.7961165048543689,
        "acc_norm_stderr": 0.039891398595317706
    },
    "harness|hendrycksTest-marketing|5": {
        "acc": 0.8589743589743589,
        "acc_stderr": 0.022801382534597528,
        "acc_norm": 0.8589743589743589,
        "acc_norm_stderr": 0.022801382534597528
    },
    "harness|hendrycksTest-medical_genetics|5": {
        "acc": 0.73,
        "acc_stderr": 0.044619604333847394,
        "acc_norm": 0.73,
        "acc_norm_stderr": 0.044619604333847394
    },
    "harness|hendrycksTest-miscellaneous|5": {
        "acc": 0.8135376756066411,
        "acc_stderr": 0.013927751372001501,
        "acc_norm": 0.8135376756066411,
        "acc_norm_stderr": 0.013927751372001501
    },
    "harness|hendrycksTest-moral_disputes|5": {
        "acc": 0.6994219653179191,
        "acc_stderr": 0.0246853168672578,
        "acc_norm": 0.6994219653179191,
        "acc_norm_stderr": 0.0246853168672578
    },
    "harness|hendrycksTest-moral_scenarios|5": {
        "acc": 0.4033519553072626,
        "acc_stderr": 0.01640712303219525,
        "acc_norm": 0.4033519553072626,
        "acc_norm_stderr": 0.01640712303219525
    },
    "harness|hendrycksTest-nutrition|5": {
        "acc": 0.7320261437908496,
        "acc_stderr": 0.02536060379624255,
        "acc_norm": 0.7320261437908496,
        "acc_norm_stderr": 0.02536060379624255
    },
    "harness|hendrycksTest-philosophy|5": {
        "acc": 0.7009646302250804,
        "acc_stderr": 0.02600330111788514,
        "acc_norm": 0.7009646302250804,
        "acc_norm_stderr": 0.02600330111788514
    },
    "harness|hendrycksTest-prehistory|5": {
        "acc": 0.7067901234567902,
        "acc_stderr": 0.025329888171900926,
        "acc_norm": 0.7067901234567902,
        "acc_norm_stderr": 0.025329888171900926
    },
    "harness|hendrycksTest-professional_accounting|5": {
        "acc": 0.49645390070921985,
        "acc_stderr": 0.02982674915328092,
        "acc_norm": 0.49645390070921985,
        "acc_norm_stderr": 0.02982674915328092
    },
    "harness|hendrycksTest-professional_law|5": {
        "acc": 0.44784876140808344,
        "acc_stderr": 0.01270058240476822,
        "acc_norm": 0.44784876140808344,
        "acc_norm_stderr": 0.01270058240476822
    },
    "harness|hendrycksTest-professional_medicine|5": {
        "acc": 0.6397058823529411,
        "acc_stderr": 0.029163128570670733,
        "acc_norm": 0.6397058823529411,
        "acc_norm_stderr": 0.029163128570670733
    },
    "harness|hendrycksTest-professional_psychology|5": {
        "acc": 0.6666666666666666,
        "acc_stderr": 0.019070985589687495,
        "acc_norm": 0.6666666666666666,
        "acc_norm_stderr": 0.019070985589687495
    },
    "harness|hendrycksTest-public_relations|5": {
        "acc": 0.6727272727272727,
        "acc_stderr": 0.0449429086625209,
        "acc_norm": 0.6727272727272727,
        "acc_norm_stderr": 0.0449429086625209
    },
    "harness|hendrycksTest-security_studies|5": {
        "acc": 0.7020408163265306,
        "acc_stderr": 0.029279567411065677,
        "acc_norm": 0.7020408163265306,
        "acc_norm_stderr": 0.029279567411065677
    },
    "harness|hendrycksTest-sociology|5": {
        "acc": 0.7960199004975125,
        "acc_stderr": 0.02849317624532607,
        "acc_norm": 0.7960199004975125,
        "acc_norm_stderr": 0.02849317624532607
    },
    "harness|hendrycksTest-us_foreign_policy|5": {
        "acc": 0.84,
        "acc_stderr": 0.03684529491774709,
        "acc_norm": 0.84,
        "acc_norm_stderr": 0.03684529491774709
    },
    "harness|hendrycksTest-virology|5": {
        "acc": 0.5542168674698795,
        "acc_stderr": 0.03869543323472101,
        "acc_norm": 0.5542168674698795,
        "acc_norm_stderr": 0.03869543323472101
    },
    "harness|hendrycksTest-world_religions|5": {
        "acc": 0.8011695906432749,
        "acc_stderr": 0.03061111655743253,
        "acc_norm": 0.8011695906432749,
        "acc_norm_stderr": 0.03061111655743253
    },
    "harness|truthfulqa:mc|0": {
        "mc1": 0.2802937576499388,
        "mc1_stderr": 0.015723139524608767,
        "mc2": 0.435601924823795,
        "mc2_stderr": 0.014179199089974604
    },
    "harness|winogrande|5": {
        "acc": 0.7932123125493291,
        "acc_stderr": 0.011382566829235805
    },
    "harness|gsm8k|5": {
        "acc": 0.3510235026535254,
        "acc_stderr": 0.01314694594139722
    }
}
```