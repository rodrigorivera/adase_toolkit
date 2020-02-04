import pickle


def read_pickle(name: str)-> pickle:
    """

    Parameters
    ----------
    name: str

    Returns
    -------
    pickle

    """
    return pickle.load(open(name, 'rb'))