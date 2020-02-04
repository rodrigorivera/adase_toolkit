import pandas as pd
import numpy as np
from typing import List


def create_log_targets(df: pd.DataFrame,
                       targets: List[str]
                       ) -> pd.DataFrame:

    """
    It creates a new column with a log transformation of the target

    Parameters
    ----------
    :param df:pd.DataFrame
    :param targets:List[str]

    Returns
    -------
    pd.DataFrame

    """

    df_temp: pd.DataFrame = df.copy()

    for target in targets:
        title = 'log_{}'.format(target.replace('original_', ''))
        df_temp[title] = np.log1p(df_temp[target] + 1)

    return df_temp
