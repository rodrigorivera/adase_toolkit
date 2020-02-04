import numpy as np
import pandas as pd
from sklearn.externals.joblib import Parallel, delayed
from sklearn.pipeline import FeatureUnion, _fit_transform_one, _transform_one
from scipy import sparse


class PandasFeatureUnion(FeatureUnion):
    """
    TODO: Asses if this can be removed
    """
    def fit_transform(self, X, y=None, **fit_params):
        """

        Parameters
        ----------
        X
        y
        fit_params

        Returns
        -------

        """
        self._validate_transformers()
        result = Parallel(n_jobs=self.n_jobs)\
            (delayed(_fit_transform_one)(trans, weight, X, y,**fit_params) for name, trans, weight in self._iter())

        if not result:
            # All transformers are None
            return np.zeros((X.shape[0], 0))

        Xs, transformers = zip(*result)
        self._update_transformer_list(transformers)

        if any(sparse.issparse(f) for f in Xs):
            Xs = sparse.hstack(Xs).tocsr()
        else:
            Xs = self.merge_dataframes_by_column(Xs)

        return Xs

    def merge_dataframes_by_column(self, Xs):
        """

        Parameters
        ----------
        Xs

        Returns
        -------

        """
        return pd.concat(Xs, axis="columns", copy=False)

    def transform(self, X):
        """

        Parameters
        ----------
        X

        Returns
        -------

        """
        Xs = Parallel(n_jobs=self.n_jobs)(
            delayed(_transform_one)(trans, weight, X)
            for name, trans, weight in self._iter())
        if not Xs:
            # All transformers are None
            return np.zeros((X.shape[0], 0))
        if any(sparse.issparse(f) for f in Xs):
            Xs = sparse.hstack(Xs).tocsr()
        else:
            Xs = self.merge_dataframes_by_column(Xs)
        return Xs