import pickle
import numpy as np
from tqdm import tqdm
from collections import defaultdict
from src.matrix import LogLikelihoodMatrix, ColumnSampling

modeldata = pickle.load(open('data/modeldata_1018.pkl', 'rb'))
log_likelihood_vectors = np.array([x['raw_log-likelihood-10k'] for x in modeldata])
mat = LogLikelihoodMatrix(ll_vectors=log_likelihood_vectors)
col = ColumnSampling(reference_matrix=mat.Q)

seed_list = [42+i for i in range(10)]
list_n_resamples = list(range(10, 100, 10)) + list(range(100, 10001, 100))

for method in ('kls', 'lss', 'uniform'):
    print(method)
    idx_and_weight = defaultdict(dict)
    for seed in tqdm(seed_list):
        idx_and_weight[f'{seed}'] = defaultdict(dict)
        for n in list_n_resamples:
            uniq_idx, weights = col.sampling(method=method, n_samples=n, seed=seed)
            idx_and_weight[f'{seed}'][f'{n}']['unique_index'] = uniq_idx
            idx_and_weight[f'{seed}'][f'{n}']['weights'] = weights
            
    pickle.dump(idx_and_weight, open(f'{method}-uniq-idx-weight.pkl', 'wb'))