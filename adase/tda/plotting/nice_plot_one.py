import matplotlib.pyplot as plt

def nice_plot_one(numb, data, titles, times):
    '''
    This function plots _numb_th ts from dataset
    '''
    ts = data[numb]

    tt = {'fontsize': 20}

    name = titles[numb]

    f, axs = plt.subplots(nrows=1, ncols=1, sharex=False, sharey=False, figsize=(13, 4))

    axs.plot(times, ts, '-o', c='c',
             markerfacecolor='m', mec='m', markersize=4)
    axs.grid(color='grey', linestyle='-', linewidth=0.3)

    plt.suptitle('Time series of transactions of user with card id = {}'.format(name), y=1.05, fontsize=23)
    plt.tight_layout()