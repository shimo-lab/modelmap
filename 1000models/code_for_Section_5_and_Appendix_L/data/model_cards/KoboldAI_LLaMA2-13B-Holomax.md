# LLaMA 2 Holomax 13B - The writers version of Mythomax

This is an expansion merge to the well praised Mythomax model from Gryphe (60%) using MrSeeker's KoboldAI Holodeck model (40%)
The goal of this model is to enhance story writing capabilities while preserving the desirable traits of the Mythomax model as much as possible (It does limit chat reply length).

Testers found that this model passes the InteracTV benchmark, was useful for story writing, chatting and text adventures using Instruction mode.
Preservation of factual knowledge has not been tested since we expect the original to be better in those use cases as this merge was focussed on fiction.

## Credits
This merge is not possible without the following models and model authors (Thanks to all of you for your work!)

Mythomax by Gryphe:
- Mythologic-L2 by Gryphe:
- - Hermes by Nous-Research
  - Chronos V2 by Elinas
  - Airoboros m2.0 by Jondurbin
- Huginn by Face of Goonery:
- - Hermes by Nous-Research
  - StableBeluga by StabilityAI
  - Airoboros by Jondurbin
  - Chronos by Elinas
  - Limarp by Lemonila

Holodeck by Mr.Seeker

## Guidelines
This model is designed to be flexible, it should be able to be used as a co-writing model, as well as a variety of instruct formats (Tested with Alpaca) and regular chatting both augmented with traditional formatting and instruct formatting.
The Alpaca format is as follows:
```
### Instruction:

Instruction goes here

### Response:
```
But if you have a different preferred format that works on one of the models above it will likely still work.

## License
After publishing the model we were informed that one of the origin models upstream was uploaded under the AGPLv3, it is currently unknown what effects this has on this model because all weights have been modified and none of the original weights are intact.
At the moment of publishing (and writing this message) both merged models Holodeck and Mythomax were licensed Llama2, therefore the Llama2 license applies to this model.
However, Holodeck contains a non-commercial clause and may only be used for research or private use, while Limarp is licensed AGPLv3.
AGPLv3 conflicts with the commercial usage restrictions of the Llama2 license, therefore we assume this aspect does not apply and the authors indended for commercial usage restrictions to be permitted.
As a result we have decided to leave the model available for public download on the assumption that all involved authors intend for it to be licensed with commercial restrictions / llama2 restrictions in place, but with the further rights and freedoms the AGPLv3 grants a user.

If HF informs us that this assumption is incorrect and requests us to take this model down, we will republish the model in the form of the original merging script that was used to create the end result.
To comply with the AGPLv3 aspect the "source" of this model is as follows (Because this model is made on a binary level, we can only provide the script that created the model):
```
import json
import os
import shutil
import subprocess
from tkinter.filedialog import askdirectory, askopenfilename

import torch
from colorama import Fore, Style, init
from transformers import (AutoModel, AutoModelForCausalLM, AutoTokenizer,
                          LlamaConfig, LlamaForCausalLM, LlamaTokenizer,
                          PreTrainedTokenizer, PreTrainedTokenizerFast)

newline = '\n'
def clear_console():
    if os.name == "nt":  # For Windows
        subprocess.call("cls", shell=True)
    else:  # For Linux and macOS
        subprocess.call("clear", shell=True)

clear_console()
print(f"{Fore.YELLOW}Starting script, please wait...{Style.RESET_ALL}")

#mixer output settings
blend_ratio = 0.4           #setting to 0 gives first model, and 1 gives second model
fp16 = False                 #perform operations in fp16. Saves memory, but CPU inference will not be possible.
always_output_fp16 = True   #if true, will output fp16 even if operating in fp32
max_shard_size = "10000MiB"  #set output shard size
force_cpu = True            #only use cpu
load_sharded = True         #load both models shard by shard

print(f"Blend Ratio set to: {Fore.GREEN}{blend_ratio}{Style.RESET_ALL}")
print(f"Operations in fp16 is: {Fore.GREEN}{fp16}{Style.RESET_ALL}")
print(f"Save Result in fp16: {Fore.GREEN}{always_output_fp16}{Style.RESET_ALL}")
print(f"CPU RAM Only: {Fore.GREEN}{force_cpu}{Style.RESET_ALL}{newline}")

#test generation settings, only for fp32
deterministic_test = True   #determines if outputs are always the same
test_prompt = ""    #test prompt for generation. only for fp32. set to empty string to skip generating.
test_max_length = 32        #test generation length


blend_ratio_b = 1.0 - blend_ratio

def get_model_info(model):
    with torch.no_grad():
        outfo = ""
        cntent = 0
        outfo += "\n==============================\n"
        for name, para in model.named_parameters():
            cntent += 1
            outfo += ('{}: {}'.format(name, para.shape))+"\n"
        outfo += ("Num Entries: " + str(cntent))+"\n"
        outfo += ("==============================\n")
        return outfo

def merge_models(model1,model2):
    with torch.no_grad():
        tensornum = 0
        for p1, p2 in zip(model1.parameters(), model2.parameters()):
           p1 *= blend_ratio
           p2 *= blend_ratio_b
           p1 += p2
           tensornum += 1
           print("Merging tensor "+str(tensornum))
           pass

def read_index_filenames(sourcedir):
    index = json.load(open(sourcedir + '/pytorch_model.bin.index.json','rt'))
    fl = []
    for k,v in index['weight_map'].items():
        if v not in fl:
            fl.append(v)
    return fl

print("Opening file dialog, please select FIRST model directory...")
model_path1 = "Gryphe/MythoMax-L2-13b"
print(f"First Model is: {model_path1}")
print("Opening file dialog, please select SECOND model directory...")
model_path2 = "KoboldAI/LLAMA2-13B-Holodeck-1"
print(f"Second Model is: {model_path2}")
print("Opening file dialog, please select OUTPUT model directory...")
model_path3 = askdirectory(title="Select Output Directory of merged model")
print(f"Merged Save Directory is: {model_path3}{newline}")
if not model_path1 or not model_path2:
    print("\nYou must select two directories containing models to merge and one output directory. Exiting.")
    exit()

with torch.no_grad():
    if fp16:
        torch.set_default_dtype(torch.float16)
    else:
        torch.set_default_dtype(torch.float32)

    device = torch.device("cuda") if (torch.cuda.is_available() and not force_cpu) else torch.device("cpu")
    print(device)

    print("Loading Model 1...")
    model1 = AutoModelForCausalLM.from_pretrained(model_path1) #,torch_dtype=torch.float16
    model1 = model1.to(device)
    model1.eval()
    print("Model 1 Loaded. Dtype: " + str(model1.dtype))
    print("Loading Model 2...")
    model2 = AutoModelForCausalLM.from_pretrained(model_path2) #,torch_dtype=torch.float16
    model2 = model2.to(device)
    model2.eval()
    print("Model 2 Loaded. Dtype: " + str(model2.dtype))

#   Saving for posterity reasons, handy for troubleshooting if model result is broken
#    #ensure both models have the exact same layout
#    m1_info = get_model_info(model1)
#    m2_info = get_model_info(model2)
#    if m1_info != m2_info:
#        print("Model 1 Info: " + m1_info)
#        print("Model 2 Info: " + m2_info)
#        print("\nERROR:\nThe two selected models are not compatible! They must have identical structure!")
#        exit()

    print("Merging models...")
    merge_models(model1,model2)

    if model_path3:
        print("Saving new model...")
        if always_output_fp16 and not fp16:
            model1.half()
        model1.save_pretrained(model_path3, max_shard_size=max_shard_size)
        print("\nSaved to: " + model_path3)
        print("\nCopying files to: " + model_path3)
        files_to_copy = ["tokenizer.model", "special_tokens_map.json", "tokenizer_config.json", "vocab.json", "merges.txt"]
        for filename in files_to_copy:
            src_path = os.path.join(model_path1, filename)
            dst_path = os.path.join(model_path3, filename)
            try:
                shutil.copy2(src_path, dst_path)
            except FileNotFoundError:
                print("\nFile " + filename + " not found in" + model_path1 + ". Skipping.")
        else:
            print("\nOutput model was not saved as no output path was selected.")
    print("\nScript Completed.")
```