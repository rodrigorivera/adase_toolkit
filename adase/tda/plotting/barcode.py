import matplotlib.pyplot as plt


def barcode(PD, card_id):
    '''
    This code generates barcode diagrams of 0 and 1 dimensional homologies
    '''
    h0 = len(PD[0])
    fig, [ax, bx] = plt.subplots(ncols=2, figsize=(15, 7))
    plt.suptitle('Barcode diagram for ' + card_id, y=1, fontsize=23)
    # unique_rows = np.unique(PD[1], axis=0)
    for i in range(h0):
        ax.plot(PD[0][i], [i, i], 'o-', c='c', linewidth=0.5, markersize=2)

    ax.spines['top'].set_linewidth(0.4)
    ax.spines['right'].set_linewidth(0.4)

    ax.spines['left'].set_color('grey')
    ax.spines['bottom'].set_color('grey')
    ax.tick_params(axis='y', which='both', length=0, pad=10)
    ax.tick_params(axis='x', which='both', length=3, pad=5)
    ax.set_title('0-dim', fontsize=18)
    ax.set_yticklabels([])
    ax.set_xlabel('Radius')

    h1 = len(PD[1])
    for i in range(h1):
        bx.plot(PD[1][i], [i, i], '-D', c='c', linewidth=0.5, markersize=2)

    bx.spines['top'].set_linewidth(0.4)
    bx.spines['right'].set_linewidth(0.4)

    bx.spines['left'].set_color('grey')
    bx.spines['bottom'].set_color('grey')
    bx.tick_params(axis='y', which='both', length=0, pad=10)
    bx.tick_params(axis='x', which='both', length=3, pad=5)
    bx.set_title('1-dim', fontsize=18)
    bx.set_yticklabels([])
    bx.set_xlabel('Radius')


def barcode(PD, card_id):
    '''
    This code generates barcode diagrams of 0 and 1 dimensional homologies
    '''
    h0 = len(PD[0])
    fig, [ax, bx] = plt.subplots(ncols=2, figsize=(15, 7))
    plt.suptitle('Barcode diagram for {0}'.format(card_id), y=1, fontsize=23)
    # unique_rows = np.unique(PD[1], axis=0)
    for i in range(h0):
        ax.plot(PD[0][i], [i, i], 'o-', c='c', linewidth=0.5, markersize=2)

    ax.spines['top'].set_linewidth(0.4)
    ax.spines['right'].set_linewidth(0.4)

    ax.spines['left'].set_color('grey')
    ax.spines['bottom'].set_color('grey')
    ax.tick_params(axis='y', which='both', length=0, pad=10)
    ax.tick_params(axis='x', which='both', length=3, pad=5)
    ax.set_title('0-dim', fontsize=18)
    ax.set_yticklabels([])
    ax.set_xlabel('Radius')

    h1 = len(PD[1])
    for i in range(h1):
        bx.plot(PD[1][i], [i, i], '-D', c='c', linewidth=0.5, markersize=2)

    bx.spines['top'].set_linewidth(0.4)
    bx.spines['right'].set_linewidth(0.4)

    bx.spines['left'].set_color('grey')
    bx.spines['bottom'].set_color('grey')
    bx.tick_params(axis='y', which='both', length=0, pad=10)
    bx.tick_params(axis='x', which='both', length=3, pad=5)
    bx.set_title('1-dim', fontsize=18)
    bx.set_yticklabels([])
    bx.set_xlabel('Radius')