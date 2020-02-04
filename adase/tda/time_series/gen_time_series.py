import pandas as pd
import datetime
import numpy as np


def gen_time_series(start, end, name_dates_coulumn):
    '''
    Generate time array, starting from the first in time series, ending with the last one, extracts from df
    '''

    earliest = pd.to_datetime(start)
    oldest = pd.to_datetime(end)
    step = datetime.timedelta(days=1)
    result = []
    while earliest <= oldest:
        result.append(earliest)
        earliest += step
    return pd.DataFrame(
        pd.to_datetime(np.array(result)),
        columns=[name_dates_coulumn]
    )
