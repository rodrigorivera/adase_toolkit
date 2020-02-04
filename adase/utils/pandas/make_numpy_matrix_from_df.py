from tqdm import tqdm as tqdm
import numpy as np
import pandas as pd

def make_numpy_matrix_from_df(data:pd.DataFrame, column_name:str)->np.matrix:

    data_numpy = np.array(data[0][column_name])

    for ts in tqdm(data[1:]):
        data_numpy = np.vstack([data_numpy, np.array(ts[column_name]).reshape(1, -1)])
    return data_numpy