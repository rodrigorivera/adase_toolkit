import numpy as np


def differentiable_smape(true, predicted):
    """
    Approximated differentiable SMAPE

    Parameters
    ----------
    true
    predicted

    Returns
    -------


    """
    epsilon = 0.1
    true_o = np.array(true)
    pred_o = np.array(predicted)
    summ = np.maximum(np.abs(true_o) + np.abs(pred_o) + epsilon, 0.5 + epsilon)
    smape = np.abs(pred_o - true_o) / summ

    return np.mean(smape)
