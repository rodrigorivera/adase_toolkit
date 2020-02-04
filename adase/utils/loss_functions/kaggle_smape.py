import numpy as np


def kaggle_smape(true, predicted):
    """
    SMAPE as Kaggle calculates it

    Parameters
    ----------
    true
    predicted

    Returns
    -------

    """
    true_o = true
    pred_o = predicted
    summ = np.abs(true_o) + np.abs(pred_o)
    smape = np.where(summ == 0, 0, np.abs(pred_o - true_o) / summ)

    return np.mean(smape)
