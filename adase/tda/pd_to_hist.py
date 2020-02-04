import numpy as np
from typing import Tuple

def pd_to_hist(x: Tuple, d: int, maximum: int) -> np.matrix:
    '''
    From PD diagram creates a histogram on a grid dxd without diagonal elements
    input:
        x — persisnttence diagram as a tuple, from which we take 2d element, corresponding
        to the PD of 1D
        d — size of the grid
        maximum — coordinate of maximum point among all PDs
    '''
    # if(len(x) == 1):
    data = x[1]
    # else:
    #    data = x
    n, m = data.shape
    hist = np.zeros((d, d))
    maximum = maximum + 1.e-3
    n, m = data.shape
    if n * m != 0:
        i = d * data[:, 0] / maximum
        j = d * data[:, 1] / maximum
        i = i.astype(np.int)
        j = j.astype(np.int)
        for ii, jj in zip(i, j):
            if ii != jj:
                hist[ii, jj] += 1
    mass = hist.sum()
    return hist  # , mass