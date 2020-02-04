from sklearn.decomposition import PCA


def sl_w_pca_2(x, dim=50, Tau=1, dT=1):
    '''
    This function takes ts and returns massive of sliding windows
    for each of them and massive of two most important components of it, obtained by pca
    '''
    X = getSlidingWindow(x, dim, Tau, dT)
    pca = PCA(n_components=2)
    Y = pca.fit_transform(X)
    return (X, Y)