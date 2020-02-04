import pandas as pd


def create_increase(df: pd.DataFrame,
                    target: str,
                    ) -> pd.DataFrame:
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
    title = target + '_increase'
    first_rpd = df_temp[df_temp['rpd'] == 2][target]
    df_temp[title] = ((df_temp['{0}_diff'.format(target)]) / first_rpd).fillna(0)

    return df_temp
