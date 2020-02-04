import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(a: np.array, cmap=plt.cm.gist_heat_r):
    '''
    Plot histogram
    Input:
    a - histogram
    '''
    f = plt.figure(figsize=(5, 5), dpi=100)
    plt.imshow(a.T, cmap=cmap)
    plt.ylim(0, a.shape[0])
    dd = a.shape[0]
    plt.plot([x for x in range(dd)], [x for x in range(dd)], c='grey')
    xx, yy = np.meshgrid(np.arange(0, dd, 1),
                         np.arange(0, dd, 1))
    z = np.zeros(xx.shape)
    for x, y in zip(xx.reshape(-1), yy.reshape(-1)):
        if x > y:
            z[x][y] = 0
        else:
            z[x][y] = 1
    #     plt.contourf(xx, yy, z.reshape(xx.shape), cmap=plt.cm.gray_r, alpha = 0.2)
    plt.xticks(())
    plt.yticks(())
    return f