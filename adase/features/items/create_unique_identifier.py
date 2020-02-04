import pandas as pd
from typing import List


def create_unique_identifier(df: pd.DataFrame, targets: List[str]) -> pd.DataFrame:
    """
    It creates a new column containing a combination of the item code and the future flag

    Parameters
    ----------
    df: pd.DataFrame
    targets: pd.DataFrame

    Returns
    -------
    pd.DataFrame

    """

    df_temp: pd.DataFrame = df.copy()
    title = '_'.join(targets)
    df_tp = df_temp[targets]
    df_temp[title] = df_tp[df_tp.columns[0:]].apply(lambda x: '00'.join(x.astype(int).astype(str)).astype(int), axis=1)

    return df_temp