from typing import List
import pandas as pd


def read_df_args(*args) -> List[pd.DataFrame]:
    #TODO: Remove

    dfs = []
    for df_name in args:
        df_temp = pd.read_csv(df_name)
        dfs.append(df_temp)

    return dfs
