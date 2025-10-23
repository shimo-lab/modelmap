# ------------------
# Data for Figure3 (b)
# ------------------
import pickle
import numpy as np
from sklearn.manifold import TSNE
from collections import defaultdict
from src.matrix import ColumnSampling, LogLikelihoodMatrix

class ExperimentAddNew:
    def __init__(self, num_exist):
        # Load data
        modeldata = pickle.load(open('data/modeldata_1018.pkl', 'rb'))
        modeldata = sorted(modeldata, key=lambda x: (x['created_at'], x['model_name']))
        log_likelihood_vectors = np.array([x['raw_log-likelihood-10k'] for x in modeldata])

        # List of Model Names 
        self.model_names = [x['model_name'] for x in modeldata]
        data_model_name = {
            'existing_models': [self.model_names[i] for i in range(num_exist)],
            'new_models': [self.model_names[i] for i in range(num_exist, len(self.model_names))]
        }

        # Log Likelihood Matrix
        self.mat = LogLikelihoodMatrix(ll_vectors=log_likelihood_vectors[:num_exist])
        self.col = ColumnSampling(reference_matrix=self.mat.Q)
        new_llv = log_likelihood_vectors[num_exist:]
        self.mat.append(new_llv)

        # t-SNE
        self.tsne = TSNE(
            n_components=2,
            perplexity=30,
            max_iter=1000,
            random_state=42,
            init='pca',
            metric='sqeuclidean'
        )

        # Results
        self.result_data = {
            'name': data_model_name,
            'tsne': defaultdict(dict)
        }
    
    def run(self, n):
        sampled_idx, weights = self.col.sampling(method='ls', n_samples=n, seed=42)
        sampled_Q = self.mat.resampled_Q(sampled_idx, weights)
        tsne_xy = self.tsne.fit_transform(sampled_Q)
        for model, xy in zip(self.model_names, tsne_xy):
            self.result_data['tsne'][f'{n}'][model] = xy

experiment = ExperimentAddNew(num_exist=898)
experiment.run(n=2900)
pickle.dump(experiment.result_data, open(f'./fig3b_addnew.pkl', 'wb'))