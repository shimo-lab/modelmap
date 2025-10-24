# ------------------
# Data for Figure2
# ------------------
import pickle
import numpy as np
from tqdm import tqdm
from src.matrix import LogLikelihoodMatrix, ColumnSampling

modeldata = pickle.load(open('data/modeldata_1018.pkl', 'rb'))
log_likelihood_vectors = np.array([x['raw_log-likelihood-10k'] for x in modeldata])
mat = LogLikelihoodMatrix(ll_vectors=log_likelihood_vectors)
col = ColumnSampling(reference_matrix=mat.Q)

def diff_absolute(smp_G, ref_G):
    fro_error = np.linalg.norm(smp_G - ref_G, 'fro')
    fro_ref_G = np.linalg.norm(ref_G, 'fro')
    return fro_error / fro_ref_G

def diff_relative(smp_G, ref_G, eps):
    abs_diff = np.abs(smp_G - ref_G)
    denominator = np.maximum(ref_G, eps)
    relative_error_matrix = (abs_diff / denominator)
    return np.sqrt(np.mean(relative_error_matrix**2))

def evaluation(resampling_methods, list_n_resamples, r_runs):
    uniq_d = {method: {} for method in resampling_methods}
    r_tau1 = {method: {} for method in resampling_methods}
    r_tau2 = {method: {} for method in resampling_methods}

    # Run resampling procedure and compute pairwise distance
    for method in resampling_methods:
        for n_resamples in tqdm(list_n_resamples):
            uniq_d[method][f"{n_resamples}"] = []
            r_tau1[method][f"{n_resamples}"] = []
            r_tau2[method][f"{n_resamples}"] = []
            for i in range(r_runs):
                seed = 42 + i
                sampled_idx, weights = col.sampling(method=method, n_samples=n_resamples, seed=seed)
                sampled_G = mat.resampled_G(sampled_index=sampled_idx, weights=weights)
                uniq_d[method][f"{n_resamples}"].append(len(np.unique(sampled_idx)))
                r_tau1[method][f"{n_resamples}"].append(diff_absolute(smp_G=sampled_G, ref_G=mat.pwd_Q))
                r_tau2[method][f"{n_resamples}"].append(diff_relative(smp_G=sampled_G, ref_G=mat.pwd_Q, eps=1e-3))
    
    rms_r_tau1 = {method: {} for method in resampling_methods}
    rms_r_tau2 = {method: {} for method in resampling_methods}
    for method in resampling_methods:
        for n_resamples in list_n_resamples:
            rms_r_tau1[method][f"{n_resamples}"] = np.sqrt(np.mean(np.square(r_tau1[method][f"{n_resamples}"])))
            rms_r_tau2[method][f"{n_resamples}"] = np.sqrt(np.mean(np.square(r_tau2[method][f"{n_resamples}"])))
    
    """
    # Error of resamples against population
    # ... Sampling Error (Sample <- Population)
    # ... Resampling Error (Resample <- Sample)
    # When we evaluate **resamples**, we consider both Resampling Error and Sampling Error
    """
    tau1_unif_N = rms_r_tau1['uni']['10000'] # Sampling Error (absolute) estimated by bootstrap method
    tau2_unif_N = rms_r_tau2['uni']['10000'] # Sampling Error (relative) estimated by bootstrap method
    eps1 = {method: {} for method in resampling_methods}
    eps2 = {method: {} for method in resampling_methods}
    for method in resampling_methods:
        for n_resamples in list_n_resamples:
            eps1[method][f"{n_resamples}"] = np.sqrt(rms_r_tau1[method][f"{n_resamples}"]**2 + tau1_unif_N**2)
            eps2[method][f"{n_resamples}"] = np.sqrt(rms_r_tau2[method][f"{n_resamples}"]**2 + tau2_unif_N**2)
            # rms_r_tau1[method][f"{n_resamples}"]: Resampling Error (absolute) (Resample <- Sample)
            # rms_r_tau2[method][f"{n_resamples}"]: Resampling Error (relative) (Resample <- Sample)

    result = {
        'n': list_n_resamples,
        'd': uniq_d,
        'r_tau1': r_tau1,
        'r_tau2': r_tau2,
        'tau1': rms_r_tau1,
        'tau2': rms_r_tau2,
        'eps1': eps1,
        'eps2': eps2,
    }
    return result

plotdata = evaluation(
    resampling_methods=('uni', 'lss', 'kls'),
    list_n_resamples=list(range(10, 100, 10)) + list(range(100, 10001, 100)),
    r_runs=100
)
pickle.dump(plotdata, open('./fig2_resampling_error.pkl', 'wb'))