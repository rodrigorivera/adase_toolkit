import numpy as np
import scipy.interpolate as interp


def get_sliding_window(x, dim:int, Tau:float, dT:float):
    '''
    This function takes time series x (without time-part)
    and returns a massive X, which has sliding windows as columns
    '''
    N = len(x)
    NWindows = int(np.floor((N - dim * Tau) / dT))  # The number of windows
    if NWindows <= 0:
        print("Error: Tau too large for signal extent")
        return np.zeros((3, dim))
    X = np.zeros((NWindows, dim))  # Create a 2D array which will store all windows
    idx = np.arange(N)
    for i in range(NWindows):
        # Figure out the indices of the samples in this window
        idxx = dT * i + Tau * np.arange(dim)
        start = int(np.floor(idxx[0]))
        end = int(np.ceil(idxx[-1])) + 2
        if end >= len(x):
            X = X[0:i, :]
            break
        # Do spline interpolation to fill in this window, and place
        # it in the resulting array
        spl = interp.interp1d(idx[start:end + 1], x[start:end + 1], kind='quadratic')
        X[i, :] = spl(idxx)
        # X[i, :] = interp.spline(idx[start:end+1], x[start:end+1], idxx)
    return X