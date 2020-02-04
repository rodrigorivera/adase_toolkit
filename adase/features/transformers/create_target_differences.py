import pandas as pd
from typing import List
from functools import reduce


def create_target_differences(df: pd.DataFrame, targets: List[str], condition: List[str]) -> pd.DataFrame:
    """
    It creates a difference in value: new_target-old_target for a given item_code and future_flag
    and generates a new column, as well as a second column for the percentage change.

    Parameters
    ----------
    df: pd.DataFrame
    targets: List[str]
    condition: List[str]

    Returns
    -------
    pd.DataFrame

    """

    data: pd.DataFrame = df.copy()
    cols_pct_change = {}
    cols_diff = {}
    for target in targets:
        cols_diff[target] = '{0}_diff'.format(target)
        cols_pct_change[target] = '{0}_pct_change'.format(target)

    df_grouped = data[condition + targets].groupby(condition)[targets]

    df_grouped_diff = df_grouped\
        .transform(lambda x: x.diff())\
        .fillna(0)\
        .rename(columns=cols_diff)

    df_grouped_pct_change = df_grouped\
        .transform(lambda x: x.pct_change())\
        .fillna(0)\
        .rename(columns=cols_pct_change)

    dfs = [df_grouped_diff, df_grouped_pct_change]
    dfs_merged = reduce(lambda x, y: x.join(y, lsuffix='_L', rsuffix='_R'), dfs)
    data = data.join(dfs_merged)

    return data

