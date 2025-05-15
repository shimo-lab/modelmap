import os
import json
from typing import List, Dict
import _config as cfg


class LikelihoodDataManager:
    def __init__(
            self,
            dataset_name,
            model_name,
            dtype_str = 'float16'
    ):
        likelihood_dir = cfg.get_likelihood_dir(dataset_name)
        self.logp_path = f"{likelihood_dir}/{model_name.replace('/', '--')}_{dtype_str}.jsonl"

    def load_computed_idx(self):
        if os.path.exists(self.logp_path):
            with open(self.logp_path, 'r', encoding='utf-8') as f:
                existing_results = [json.loads(line) for line in f]
                computed_idx = [res["index"] for res in existing_results]
            return computed_idx
        else:
            return []
    
    def load_existing_results(self):
        if os.path.exists(self.logp_path):
            with open(self.logp_path, 'r', encoding='utf-8') as f:
                existing_results = [json.loads(line) for line in f]
            return existing_results
        else:
            return []
    
    def save_results(self, likelihoods: List[Dict]):
        existing_results = self.load_existing_results()
        with open(self.logp_path, 'w', encoding='utf-8') as f:
            sorted_results = sorted(
                existing_results + likelihoods,
                key=lambda x: x["index"]
            )
            for result in sorted_results:
                f.write(json.dumps(result, ensure_ascii=False) + "\n")