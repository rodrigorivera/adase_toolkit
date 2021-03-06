import pandas as pd
from typing import List
import numpy as np


def _create_centroids_dataframe_old(centroids_list: List[np.float]) -> pd.DataFrame:
    """
    TODO: Remove from codebase

    Parameters
    ----------
    centroids_list: List[np.float]

    Returns
    -------
    pd.DataFrame

    """
    columns = ['centroids', 'list_series']
    series = pd.DataFrame([x for x in centroids_list], columns=columns)
    series_list = []

    for serie in series.itertuples():
        cluster_id = [serie[0]]
        centroid = serie[1]
        for elem in serie[2]:
            temp_list = np.array([centroid, elem] + cluster_id)
            series_list.append(temp_list)

    return pd.DataFrame(np.array(series_list), columns=['centroids', 'list_series', 'cluster_id'])

