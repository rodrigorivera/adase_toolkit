import numpy as np


def mae(true, predicted):
    """
    MAE on log1p

    Parameters
    ----------
    true
    predicted

    Returns
    -------

    """
    true_o = np.log1p(true)
    pred_o = np.log1p(predicted)
    error = np.abs(true_o - pred_o) / 2

    return np.mean(error)
