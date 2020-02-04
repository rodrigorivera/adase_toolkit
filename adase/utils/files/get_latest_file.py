import os

from .get_all_files import get_all_files


def get_latest_file(path: str, number_of_files:int=1):
    """
    TODO: have a fallback method in case there is older data that does not correspond to the latest one, to avoid generating always from scratch

    Parameters
    ----------
    path
    number_of_files

    Returns
    -------

    """

    return sorted(get_all_files(path + '*'), key=os.path.getctime)[-number_of_files:]
