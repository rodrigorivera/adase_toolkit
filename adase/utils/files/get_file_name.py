def get_file_name(url: str) -> str:
    """

    Parameters
    ----------
    url

    Returns
    -------
    str

    """
    if url.find('/'):
        return url.rsplit('/', 1)[1]

    else:
        return None

