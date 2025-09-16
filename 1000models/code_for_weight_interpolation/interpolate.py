import os
import argparse
from tqdm import tqdm
import json
import pickle
import numpy as np
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer
from collections import OrderedDict


def fix_random_seed(seed: int):
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def load_models(model_names, cache_dir):
    models = []
    for i, model_name in enumerate(model_names):
        print(f"Loading model_{i} from {model_name} ...")
        model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)
        models.append(model)
    tokenizer = AutoTokenizer.from_pretrained(model_names[0], cache_dir=cache_dir)
    
    return models, tokenizer


def calculate_inner_products(
        model_0: AutoModelForCausalLM,
        model_1: AutoModelForCausalLM,
        model_2: AutoModelForCausalLM,
) -> dict:
    state_dict_0 = model_0.state_dict()
    state_dict_1 = model_1.state_dict()
    state_dict_2 = model_2.state_dict()

    ip11, ip22, ip12 = 0.0, 0.0, 0.0
    len_for_ip = 0

    for param_name in state_dict_0.keys():
        value0, value1, value2 = state_dict_0[param_name], state_dict_1[param_name], state_dict_2[param_name]
        model_slice = tuple(slice(0, s) for s in value0.shape)
        diff1 = value1[model_slice] - value0
        diff2 = value2[model_slice] - value0
        ip11 += torch.sum(diff1 * diff1).item()
        ip22 += torch.sum(diff2 * diff2).item()
        ip12 += torch.sum(diff1 * diff2).item()
        len_for_ip += diff1.numel()

    ip11 /= len_for_ip
    ip22 /= len_for_ip
    ip12 /= len_for_ip

    return {"ip11": ip11, "ip22": ip22, "ip12": ip12}


def merge_models(
        model_0: AutoModelForCausalLM,
        model_1: AutoModelForCausalLM,
        model_2: AutoModelForCausalLM,
        alpha: float,
        beta: float,
) -> AutoModelForCausalLM:
    
    merged_model = AutoModelForCausalLM.from_config(model_0.config)

    state_dict_0 = model_0.state_dict()
    state_dict_1 = model_1.state_dict()
    state_dict_2 = model_2.state_dict()
    merged_state_dict = merged_model.state_dict()

    for param_name in tqdm(state_dict_0.keys(), desc="Merging weights"):
        w0 = state_dict_0[param_name]
        w1 = state_dict_1[param_name]
        w2 = state_dict_2[param_name]
        tqdm.write(f"{param_name} shape: {w0.shape} dtype: {w0.dtype}, {w1.dtype}, {w2.dtype}")

        merged_param = (1 - alpha - beta) * w0 + alpha * w1 + beta * w2
        merged_state_dict[param_name].copy_(merged_param)
    
    merged_model.load_state_dict(merged_state_dict)
    return merged_model


def compute_tokenwise_log_likelihood(
        model: AutoModelForCausalLM,
        tokenizer: AutoTokenizer,
        text_list: list,
        device: str = "cpu",
) -> np.ndarray:
    model.to(device)
    model.eval()

    log_probs_list = []

    for text in tqdm(text_list):

        inputs = tokenizer(text, return_tensors="pt")
        input_ids = inputs["input_ids"].to(device)

        with torch.no_grad():
            outputs = model(input_ids, labels=input_ids)
            loss, logits = outputs.loss, outputs.logits
        
        shift_logits = logits[..., :-1, :].contiguous()
        shift_labels = input_ids[..., 1:].contiguous()
        log_probs_all = F.log_softmax(shift_logits, dim=-1)
        next_token_log_probs = log_probs_all.gather(
            dim=-1, index=shift_labels.unsqueeze(-1)).squeeze(0).squeeze(-1)
        next_token_log_probs = next_token_log_probs.cpu().numpy()
        log_probs_list.append(next_token_log_probs.tolist())

    return log_probs_list


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--model_a", type=str)
    parser.add_argument("--model_b", type=str)
    parser.add_argument("--model_c", type=str)
    parser.add_argument("--data_size", type=int, default=1000)
    parser.add_argument("--alphas", type=float, nargs="*")
    parser.add_argument("--betas", type=float, nargs="*")
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--cache_dir", type=str, default=None)
    parser.add_argument("--data_dir", type=str, default="")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    fix_random_seed(args.seed)
    
    model_names = [args.model_a, args.model_b, args.model_c]
    alphas = args.alphas
    betas = args.betas
    device = args.device
    cache_dir = args.cache_dir
    data_dir = args.data_dir
    data_size = args.data_size

    # e.g. Llama-2-7b-hf_Llama-2-7b-chat-hf_vicuna-7b-v1.5
    instance_name = '_'.join([model_names[i].split('/')[-1] for i in range(3)])

    models, tokenizer = load_models(model_names, cache_dir)

    ips = calculate_inner_products(models[0], models[1], models[2])

    print(f"Inner products: {ips}")
    with open(f"{data_dir}/inner_products_{instance_name}.json", "w") as f:
        json.dump(ips, f, indent=4)

    with open(f"{data_dir}/texts.jsonl", "r") as f:
        text_list = [json.loads(line)["text"] for line in
                        f.readlines()]
        text_list = text_list[:data_size]

    merge_ratio = [(alpha, beta) for beta in betas for alpha in alphas]

    for alpha, beta in merge_ratio:
        print(f"Interpolating {model_names[0]} and {model_names[1]} and {model_names[2]} with alpha={alpha} and beta={beta} ...")

        merged_model = merge_models(models[0], models[1], models[2], alpha, beta)

        print("Computing tokenwise log likelihood ...")
        log_probs_list = compute_tokenwise_log_likelihood(merged_model, tokenizer, text_list, device)

        os.makedirs(f"{data_dir}/likelihood/{instance_name}", exist_ok=True)

        with open(f"{data_dir}/likelihood/{instance_name}/interp_{alpha}_{beta}.pkl", "wb") as f:
            pickle.dump([sum(logps) for logps in log_probs_list], f)


if __name__ == "__main__":
    main()
