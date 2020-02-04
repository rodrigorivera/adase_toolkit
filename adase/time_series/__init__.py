from adase.tda.pickle import save_pkl
from .distance_matrix import distance_matrix

from persim import wasserstein
from persim import bottleneck

from threading import Timer
from multiprocessing import Process, Queue, active_children
import numpy as np
from time import time

import argparse

parser = argparse.ArgumentParser(description='L2 norms')

parser.add_argument('--dataset',
                    dest='dataset',
                    type=str,
                    required=True,
                    help='Dataset file')

args = parser.parse_args()

DATASET = args.dataset

threads = 30  # n of subprocesses
t = 0


def mainp(queue, res_queue, df, rfs):
    print("thread initiated")
    while not queue.empty():
        try:
            i = queue.get(True, 15)
            res_queue.put((i, df[0].apply(lambda x: wasserstein(x, rfs[i]))))
        # 			f = np.vectorize(lambda x:wasserstein(x, rfs[i]))
        # 			res_queue.put((i,f(rfs)))

        except Exception as err:
            print("process down")
            break
        if queue.empty():
            quit()
            break


if __name__ == '__main__':
    # load the dataset
    dgms, _, _ = load_pkl(
        '../../data/interim/Time_series_classification/direct_pds_univariate_ts_clf/{}.pkl'.format(DATASET))
    rfs = dgms['direct_PD']
    df = pd.DataFrame(index=range(len(rfs)), columns=[0])
    # ~ for i in range(len(rfs)):
    # ~ df[i] = rfs
    df[0] = rfs
    queue = Queue()  # create queue
    res_queue = Queue()  # results

    print("Queue init size: " + str(queue.qsize()))
    for i in tqdm(range(len(rfs))): queue.put(i)
    print("Queue init size: " + str(queue.qsize()))

    target_size = queue.qsize()

    jobs = []
    t0 = time()
    for job in range(threads):
        jobs.append(Process(target=mainp, args=(queue, res_queue, df, rfs)))
        
    for job in jobs:
        print("Input: " + str(queue.qsize()) + " | --> | Output: " + str(res_queue.qsize()))
        job.start()
        t += 1
        print("Threads {}/{}".format(threads, t))

    while True:
        if res_queue.qsize() == target_size:
            print("Input: " + str(queue.qsize()) + " | --> | Output: " + str(res_queue.qsize()))
            print("Processing DONE\n Building DF results...")
            while not res_queue.empty():
                i = res_queue.get(True, 15)
                df['distance_to_{}'.format(i[0])] = i[1]
            print("DONE!")
            t1 = time()
            print("Total Time: " + str(t1 - t0))
            # save the dataset
            save_pkl(
                df,
                '../../data/interim/Time_series_classification/wasserstein_distance_matrices/{}_adj.pkl'.format(DATASET)
            )
            break
        else:
            print("Input: " + str(queue.qsize()) + " | --> | Output: " + str(res_queue.qsize()))


