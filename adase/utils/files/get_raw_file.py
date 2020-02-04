import requests

from .get_file_name import get_file_name


def get_raw_file(path: str, url: str) -> None:
    """

    Parameters
    ----------
    path: str
    url: str

    Returns
    -------
    None

    """
    r = requests.get(url, allow_redirects=True)
    open(path + get_file_name(url), 'wb').write(r.content)