from tqdm import tqdm as tqdm
from ripser import ripser

from adase.tda.pickle import save_pkl


def gen_rips_filtrations(sliding_windows, title):
    '''
    generates rips filtrations for each of sliding windows
    '''
    rips_filtrations = []

    for i in tqdm(range(len(sliding_windows))):
        r = ripser(sliding_windows[i], maxdim=1)['dgms']
        rips_filtrations.append(r)
    #         print(i)

    save_pkl(rips_filtrations, 'rf_{}'.format(title))


#     return rips_filtrations