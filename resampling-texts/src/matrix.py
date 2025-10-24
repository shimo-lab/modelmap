import numpy as np

class ColumnSampling:
    def __init__(self, reference_matrix):
        matrix = np.asarray(reference_matrix)
        self.mat = matrix
        self.K_rows, self.N_cols = matrix.shape
    
    def _uniform(self):
        probs = np.ones(self.N_cols) / self.N_cols
        return probs

    def _ls(self):
        col_scores = np.sum(self.mat**2, axis=0)
        probs = col_scores / np.sum(col_scores)
        return probs

    def _kl(self):
        mat_pow2 = self.mat**2
        mat_pow3 = self.mat * mat_pow2
        mat_pow4 = mat_pow2 * mat_pow2

        colwise_sum1 = np.sum(self.mat, axis=0)
        colwise_sum2 = np.sum(mat_pow2, axis=0)
        colwise_sum3 = np.sum(mat_pow3, axis=0)
        colwise_sum4 = np.sum(mat_pow4, axis=0)

        col_score_val = 2 * (self.K_rows * colwise_sum4) + 6 * (colwise_sum2**2) - 8 * (colwise_sum1 * colwise_sum3)
        col_scores = np.sqrt(np.maximum(col_score_val, 0))
        probs = col_scores / np.sum(col_scores)
        return probs
    
    def _to_unique(self, sampled_index, weights):
        unique_idx, first_occurrence_indices, counts_per_unique = np.unique(
            sampled_index, return_index=True, return_counts=True
        )
        w_for_unique_idx = weights[first_occurrence_indices]
        scaling_factors = np.sqrt(counts_per_unique) * w_for_unique_idx
        return unique_idx, scaling_factors
    
    def sampling(self, method, n_samples, seed=None):
        if seed is not None:
            np.random.seed(seed)

        match method:
            case 'uniform' | 'uni':
                probs = self._uniform()
            case 'ls' | 'lss':
                probs = self._ls()
            case 'kl' | 'kls':
                probs = self._kl()
            case _:
                raise ValueError(f"Defined method: 'uniform', 'ls', 'kl'")
            
        sampled_index = np.random.choice(self.N_cols, size=n_samples, replace=True, p=probs)
        weights = np.array([1.0 / np.sqrt(n_samples * probs[idx]) for idx in sampled_index])
        return self._to_unique(sampled_index, weights)


class LogLikelihoodMatrix:
    def __init__(self, ll_vectors):
        self.raw_matrix = np.array(ll_vectors)
        self.lower_p2 = np.quantile(self.raw_matrix, q=0.02)
        self.L = np.maximum(self.raw_matrix, self.lower_p2) # Clipping
        self.Q = double_centering(self.L)
        self.pwd_Q = pwd(self.Q)
    
    def append(self, new_ll_vectors):
        new_L = np.maximum(np.array(new_ll_vectors), self.lower_p2)
        self.L = np.concatenate((self.L, new_L), axis=0)

    def resampled_G(self, sampled_index, weights):
        """
        Pairwise (Euclidean distance)^2 based on column resampling
        """
        sampled_L = self.L[:, sampled_index]
        return pwd(centering(sampled_L, weights**2) * weights)
    
    def resampled_Q(self, sampled_index, weights):
        sampled_L = self.L[:, sampled_index]
        return centering(sampled_L, weights**2) * weights



def clipping(X, q=0.02):
    thresh = np.quantile(X, q)
    clipped_X = np.maximum(X, thresh)
    return clipped_X, thresh

def centering(X, weights=None):
    if weights is None:
        weights = np.ones(X.shape[1])
    else:
        weights = np.array(weights)
    weights = weights / np.sum(weights)
    weighted_mean = np.sum(X * weights, axis=1)
    centered_X = X - weighted_mean[:, np.newaxis]
    return centered_X

def double_centering(x):
    x = np.array(x)
    return centering(centering(x.T).T)

def pwd(X: np.ndarray):
    """
    Compute pairwise squared Euclidean distance matrix.
    """
    sq_norms = np.sum(X**2, axis=1)
    xxt = np.dot(X, X.T)
    dist_sq = sq_norms[:, np.newaxis] + sq_norms - 2 * xxt
    return np.maximum(dist_sq, 0)