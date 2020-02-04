from adase.tda.pickle import save_pkl
from tqdm import tqdm as tqdm
from adase.tda.sliding_window import sl_w_pca_2


def gen_sliding_windows(whole_data, title, dim=50):
    '''
    generates sliding windows for each time series in whole data, saves it to pickle
    '''
    sliding_windows = []  # dataset with sliding windows massives for each card_id
    pca_transforms = []  # dataset with pca(2) transforms of sliding windows
    counter = 0
    for time_series in tqdm(whole_data):
        #         if counter == 4500:
        #             break
        w, p = sl_w_pca_2(time_series, dim=dim, Tau=1, dT=1)
        sliding_windows.append(w)
        pca_transforms.append(p)
        #         print(counter)
        counter += 1

    save_pkl(sliding_windows, 'sw_' + title + str(dim))

    save_pkl(pca_transforms, 'pcas_' + title + str(dim))

    #return sliding_windows, pca_transforms