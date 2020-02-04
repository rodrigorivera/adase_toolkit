import pandas as pd
import numpy as np
from tqdm import tqdm as tqdm

from adase.tda.pickle import save_pkl


def generate_features(rf, titles, ratio=0.8):
    n_d_0 = []
    n_d_1 = []

    max_d_0 = []
    max_d_1 = []

    relevant_points_0 = []
    relevant_points_1 = []

    av_d_0 = []
    av_d_1 = []

    sums_d_0 = []
    sums_d_1 = []

    for PDs in tqdm(rf):

        n_d_0.append(len(PDs[0]))
        n_d_1.append(len(PDs[1]))

        if len(PDs[0]) > 1:
            distance = max((PDs[0][:, 1] - PDs[0][:, 0])[:-1])
            max_d_0.append(distance)

            ratio_max_d_0 = ratio * distance
            b = sum((PDs[0][:, 1] - PDs[0][:, 0])[:-1] >= ratio_max_d_0) - 1

            relevant_points_0.append(max(b, 0))

            av_d_0.append(((PDs[0][:, 1] - PDs[0][:, 0])[:-1]).mean())

            sums_d_0.append(((PDs[0][:, 1] - PDs[0][:, 0])[:-1]).sum())

        else:
            max_d_0.append(0)
            relevant_points_0.append(0)
            av_d_0.append(0)
            sums_d_0.append(0)

        if len(PDs[1]) != 0:
            distance = max((PDs[1][:, 1] - PDs[1][:, 0]))
            max_d_1.append(distance)

            ratio_max_d_1 = ratio * distance
            b = sum((PDs[1][:, 1] - PDs[1][:, 0]) >= ratio_max_d_1) - 1
            relevant_points_1.append(max(b, 0))

            av_d_1.append((PDs[1][:, 1] - PDs[1][:, 0]).mean())

            sums_d_1.append((PDs[1][:, 1] - PDs[1][:, 0]).sum())

        else:
            max_d_1.append(0)
            relevant_points_1.append(0)
            av_d_1.append(0)
            sums_d_1.append(0)

    tfs = pd.DataFrame({
        'titles': titles,
        'n_d_0': n_d_0,
        'n_d_1': n_d_1,
        'max_d_0': max_d_0,
        'max_d_1': max_d_1,
        'relevant_points_0': relevant_points_0,
        'relevant_points_1': relevant_points_1,
        'av_d_0': av_d_0,
        'av_d_1': av_d_1,
        'sums_d_0': sums_d_0,
        'sums_d_1': sums_d_1
    })

    total_features = np.vstack([n_d_0, n_d_1, max_d_0, max_d_1,
                                relevant_points_0, relevant_points_1, av_d_0, av_d_1, sums_d_0, sums_d_1]).T

    return tfs

def generate_features(rips_filtrations, titles, title):
    number_persistences = []
    number_uniques = []
    max_persistences = []
    #     birth_deathes = []

    count = 0
    for PDs in tqdm(rips_filtrations):
        n = len(PDs[1])
        number_persistences.append(n)
        if PDs[1].shape[0] > 1:
            unique_rows = np.unique(PDs[1], axis=0)
            number_uniques.append(len(unique_rows))
        else:
            number_uniques.append(0)

        PD = PDs[1]
        fP = 0
        fPIdx = 0
        if PD.shape[0] > 1:
            Pers = PD[:, 1] - PD[:, 0]
            fPIdx = np.argsort(-Pers)[0]
            max_pers = Pers[fPIdx]
        else:
            max_pers = 0
        max_persistences.append(max_pers)
        row = []
        row.append(titles[count])
        #         for b_d in PDs[1]:
        #             b_d=(b_d[0], b_d[1])

        #             row.append(b_d)
        #         birth_deathes.append(row)
        #         print(count)
        count += 1

    total_features = np.vstack([max_persistences, number_uniques, number_persistences]).T
    save_pkl(total_features, 'total_features_{}'.format(title))


#     save_pkl(number_persistences, 'number_persistences_{}'.format(title))
#     save_pkl(max_persistences, 'max_persistences_{}'.format(title))
#     save_pkl(number_uniques, 'number_uniques_{}'.format(title))
#     save_pkl(birth_deathes, 'birth_deathes_{}'.format(title))


#     return number_persistences, max_persistences, number_uniques, birth_deathes