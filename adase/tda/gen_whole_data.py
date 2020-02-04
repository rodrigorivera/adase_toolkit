import numpy as np

def gen_whole_data(data, times):
    def gen_whole_ts(sample, times):
        '''
        Generates time series with number of purchases from raw data

        sample is taken from data and has two columns: data and purchase amount
        times is time series of dates
        '''
        values = np.zeros(len(times), dtype='int64')

        unique, counts = np.unique(sample[:, 0], return_counts=True)
        uniques = dict(zip(unique, counts))

        for i in uniques.items():
            itemindex = np.where(times == i[0])
            #         print(itemindex[0])
            #         print(i[1])
            values[itemindex[0][0]] = i[1]
        #     print(times)
        #     whole_ts = np.hstack((times, values))

        return values

    whole_data = []

    for i in range(len(data)):
        whole_data.append(gen_whole_ts(data[i], times))