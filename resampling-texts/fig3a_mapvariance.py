# ------------------
# Data for Figure3 (a) (and Figure1)
# ------------------
import pickle
import numpy as np
from tqdm import tqdm
from sklearn.manifold import TSNE
from collections import defaultdict
from src.matrix import ColumnSampling, LogLikelihoodMatrix

class ResamplingModelMap:
    def __init__(self):
        # Load data
        modeldata = pickle.load(open('data/modeldata_1018.pkl', 'rb'))
        modeldata = sorted(modeldata, key=lambda x: (x['created_at'], x['model_name']))
        log_likelihood_vectors = np.array([x['raw_log-likelihood-10k'] for x in modeldata])
        self.model_names = [x['model_name'] for x in modeldata]

        # Setup
        self.mat = LogLikelihoodMatrix(ll_vectors=log_likelihood_vectors)
        self.col = ColumnSampling(reference_matrix=self.mat.Q)

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
        self.result_data = {}

    def run(self, method, n, r_runs):
        r_modelmaps = defaultdict(dict)
        for i in tqdm(range(r_runs)):
            seed = 42 + i
            sampled_idx, weights = self.col.sampling(method, n, seed)
            sampled_Q = self.mat.resampled_Q(sampled_idx, weights)
            modelmap_xy = self.tsne.fit_transform(sampled_Q)
            for model, xy in zip(self.model_names, modelmap_xy):
                r_modelmaps[f'{seed}'][model] = xy
        self.result_data[f'tsne_{method}_{n}_R{r_runs}'] = r_modelmaps

experiment = ResamplingModelMap()
experiment.run(method='uni', n=2500, r_runs=100)  # Setting 1
experiment.run(method='uni', n=10000, r_runs=100) # Setting 2
experiment.run(method='lss', n=2900, r_runs=100)  # Setting 3
pickle.dump(experiment.result_data, open(f'./fig3a_mapvariance.pkl', 'wb'))