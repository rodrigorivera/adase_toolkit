import pandas as pd


def is_larger_than_stat(df: pd.DataFrame, target: str) -> pd.DataFrame:
    """

    Parameters
    ----------
    df: pd.DataFrame
    target: str

    Returns
    -------
    pd.DataFrame

    """

    df_temp: pd.DataFrame = df.copy()
    statistics = ['_cum_mean', '_cum_median']

    for stat in statistics:
        to_compare = target + stat
        if (to_compare in set(df_temp.columns.values)) & (target in set(df_temp.columns.values)):
            df_temp[target + '_lg_than' + stat] = (df_temp[target] > df_temp[to_compare]) * 1

    return df_temp
