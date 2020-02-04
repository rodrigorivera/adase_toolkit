import matplotlib.pyplot as plt



def plot_comparison(numb, data, titles, times):
    '''
    This function plots _numb_th ts from dataset
    '''
    ts = data[numb]

    tt = {'fontsize': 20}

    name = titles[numb]

    plt.plot(times, ts, '-o', c='c',
             markerfacecolor='m', mec='m', markersize=4)
    plt.grid(color='grey', linestyle='-', linewidth=0.3)

    plt.suptitle('Time series of transactions of user with card id = {}'.format(name), y=1.05, fontsize=23)
    plt.tight_layout()