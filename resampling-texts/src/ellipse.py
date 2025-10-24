import numpy as np
from scipy.linalg import orthogonal_procrustes

def map_alignment(map_list, reference_map, scaling=False) -> np.ndarray:
    """
    Input:
        list_tsne: (Runs, n_samples, 2)
    """
    map_list = np.array(map_list)
    map_list = map_list - np.mean(map_list, axis=1, keepdims=True)
    aligned_maps = []
    for i in range(len(map_list)):
        current_map = map_list[i]
        R, scale_val = orthogonal_procrustes(current_map, reference_map)
        aligned = current_map @ R
        if scaling:
            aligned = scale_val * aligned
        aligned_maps.append(aligned)
    return np.array(aligned_maps)


def map_mean_cov(map_list, reference_map, scaling=False) -> tuple:
    """
    Input:
        list_tsne: (Runs, n_samples, 2)
    """
    aligned_maps = map_alignment(map_list, reference_map, scaling)
    mean_X = np.mean(aligned_maps, axis=0)
    centered_X = aligned_maps - np.mean(aligned_maps, axis=0, keepdims=True)
    cov_X = np.einsum('rsi,rsj->sij', centered_X, centered_X) / (aligned_maps.shape[0] - 1)
    return mean_X, cov_X


def std_ellipse(cov_X, std: float = 1.0):
    ellipse_of_each_point = []
    for i in range(cov_X.shape[0]):
        cov = cov_X[i]
        eigvals, eigvecs = np.linalg.eigh(cov)
        eigvals = np.maximum(eigvals, 1e-10)
        order = eigvals.argsort()[::-1]
        eigvals, eigvecs = eigvals[order], eigvecs[:, order]
        ellipse = {}
        ellipse['width'] = 2 * std * np.sqrt(eigvals[0])
        ellipse['height'] = 2 * std * np.sqrt(eigvals[1])
        ellipse['angle'] = np.rad2deg(np.arctan2(eigvecs[1][0], eigvecs[0][0]))
        ellipse_of_each_point.append(ellipse)
    return ellipse_of_each_point


def rotate(tsne_data, ref_tsne_data):
    models = list(ref_tsne_data.keys())
    src_mat = []
    tgt_mat = []
    for k in models:
        src_mat.append(tsne_data[k])
        tgt_mat.append(ref_tsne_data[k])
    src_mat = np.array(src_mat)
    tgt_mat = np.array(tgt_mat)
    rot_matrix = map_alignment([src_mat], reference_map=tgt_mat)
    rot_tsne = {}
    for i, k in enumerate(models):
        rot_tsne[k] = rot_matrix[0][i]
    return rot_tsne


def map_centrography(tsne_data, ref_tsne_data):
    models = sorted(list(ref_tsne_data.keys()))
    run_keys = list(tsne_data.keys())

    tgt_mat = np.zeros((len(models), 2))
    src_mat = np.zeros((len(run_keys), len(models), 2))

    for i, m in enumerate(models):
        tgt_mat[i, :] = ref_tsne_data[m]
    
    for r, rk in enumerate(run_keys):
        for i, m in enumerate(models):
            src_mat[r, i, :] = tsne_data[rk][m]

    mean_X, cov_X = map_mean_cov(src_mat, tgt_mat)
    ellipse_shapes = std_ellipse(cov_X, std=1.0)
    d_points = {name: tsne_xy for name, tsne_xy in zip(models, mean_X)}
    d_ellipses = {name: ellipse for name, ellipse in zip(models, ellipse_shapes)}
    return d_points, d_ellipses