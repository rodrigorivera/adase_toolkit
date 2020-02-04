import numpy as np
import pandas as pd
import logging
from kshape.core import kshape

from typing import List, Tuple


def create_clusters_kshape(df: pd.DataFrame, data_time_series: np.array, centroids: int ) -> pd.DataFrame:
    """
    This method triggers kshape and after execution returns a new column with the respective cluster id for
    each time series (item_code_future_flag)

    Parameters
    ----------
    df: pd.DataFrame
    data_time_series: np.array
    centroids: int

    Returns
    -------
    pd.DataFrame

    """

    logging.debug('Method: Kshape')
    centroids_list = _prepare_kshape(data_time_series, centroids)
    df_centroids = _convert_centroids_to_dataframe(centroids_list)
    df_centroids = _create_centroids_dataframe(df_centroids)\
        .rename(columns = {'list_series': 'index'})
    cols = ['index', 'cluster_id']
    df_centroids[cols] = df_centroids[cols].apply(pd.to_numeric)
    data: pd.DataFrame = df.merge(df_centroids, right_on='index', left_on='index')

    return data


def _prepare_kshape(data: pd.DataFrame, cluster_num: int ) -> List[Tuple]:
    """

    Parameters
    ----------
    data: pd.DataFrame
    cluster_num: int

    Returns
    -------
    List[Tuple]

    """

    return kshape(data, cluster_num)


def _convert_centroids_to_dataframe(centroids_list: List[Tuple]) -> pd.DataFrame:
    """

    Parameters
    ----------
    centroids_list: List[Tuple]

    Returns
    -------
    pd.DataFrame

    """

    return pd.DataFrame([x for x in centroids_list], columns=['centroids', 'list_series'])


def _create_centroids_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    TODO: Refactor this. The loops are not efficient.

    Parameters
    ----------
    df: pd.DataFrame

    Returns
    -------
    pd.DataFrame

    """

    series_list = []
    for serie in df.itertuples():
        cluster_id = [serie[0]]
        centroid = serie[1]
        for elem in serie[2]:
            for cent in centroid:
                temp_list = np.array([cent, elem] + cluster_id)
                series_list.append(temp_list)

    return pd.DataFrame(np.array(series_list), columns=['centroids', 'list_series', 'cluster_id'])

