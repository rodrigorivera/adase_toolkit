import pandas as pd
import datetime
import numpy as np

def gen_times(df:pd.DataFrame, name_dates:str):
    '''
    Generate time array, starting from the first in time series, ending with the last one, extracts from df
    '''
    df[name_dates] = pd.to_datetime(df[name_dates])

    earliest = min(df[name_dates])
    oldest = max(df[name_dates])
    step = datetime.timedelta(days=1)
    result = []
    while earliest <= oldest:
        result.append(earliest)
        earliest += step
    return pd.to_datetime(np.array(result))