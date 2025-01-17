# Workshop 3: Data Visualization

def plot_w3c1():
    '''
    Plot the solution to Challenge 1 of Workshop 3.
    '''
    
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    # Data
    np.random.seed(3)
    x = 4 + np.random.normal(0, 2, 24)
    y = 4 + np.random.normal(0, 2, len(x))
    sizes = np.random.uniform(15, 80, len(x))

    # Plot
    fig, ax = plt.subplots(figsize = (4,3))
    sc = ax.scatter(x, y, marker = '*', s=sizes, c = sizes, cmap = 'flare_r', lw = 0.5, alpha = 0.8, edgecolor = 'k')
    ax.text(x = 5.5, y = 7.5, s = '$Magnifique!$', c = 'red')

    # Aesthetics
    ax.set(xlim=(0, 8.2), xticks=np.arange(0, 9, 2),
        ylim=(0, 8.2), yticks=np.arange(0, 9, 2))
    ax.set_xlabel('X', fontsize = 'large', fontweight = 'bold')
    ax.set_ylabel('Y', fontsize = 'large', fontweight = 'bold')
    plt.suptitle('Colored Scatterplot w/ Legend', y = 1)
    handles, labels = sc.legend_elements("sizes", num=5)
    for i, handle in enumerate(handles):
        handle.set_color(sns.color_palette('flare_r', 6)[i])
    plt.legend(handles = handles, labels = labels, bbox_to_anchor = [1.25, 1], title = 'Size')
    sns.despine(top = True, right = True)
    # plt.savefig('/content/drive/MyDrive/Misc/Code/INMAN Lab/NDS-Workshops/Data/W3C1.png', dpi = 500, bbox_inches = 'tight')
    plt.show()
    
def plot_w3c2():
    '''
    Plot the solution to Challenge 2 of Workshop 3.
    '''
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    from matplotlib.gridspec import GridSpec
    
    # Layout
    fig = plt.figure(figsize = (8,4))
    gs = GridSpec(2, 3, figure=fig, hspace = 0.25, wspace = 0.25)
    ax1 = fig.add_subplot(gs[0, :])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[1, 1])
    ax4 = fig.add_subplot(gs[1, 2])

    # Aesthetics
    for i, ax in enumerate([ax1, ax2, ax3, ax4]):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.suptitle('Figure Layout')
    sns.despine(top = True, right = True)
    # plt.savefig('/content/drive/MyDrive/Misc/Code/INMAN Lab/NDS-Workshops/Data/W3C2.png', dpi = 500, bbox_inches = 'tight')
    plt.show()