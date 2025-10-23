import pickle
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from src.matrix import LogLikelihoodMatrix

modeldata = pickle.load(open('data/modeldata_1018.pkl', 'rb'))
modeldata = sorted(modeldata, key=lambda x: (x['created_at'], x['model_name']))
log_likelihood_vectors = np.array([x['raw_log-likelihood-10k'] for x in modeldata])
model_names = [x['model_name'] for x in modeldata]
mat = LogLikelihoodMatrix(ll_vectors=log_likelihood_vectors)

def run_tsne(X, model_names):    
    tsne = TSNE(
        n_components=2,
        perplexity=30,
        max_iter=10000,
        init='pca',
        verbose=1,
        metric='sqeuclidean',
        random_state=42
    )
    tsne_X = tsne.fit_transform(X)
    
    tsne_embs = {}
    for name, pos_xy in zip(model_names, tsne_X):
        tsne_embs[name] = pos_xy
    return tsne_embs

dict_tsne_Q = run_tsne(X=mat.Q, model_names=model_names)
pickle.dump(dict_tsne_Q, open('tsne_Q.pkl', 'wb'))