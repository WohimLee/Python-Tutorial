import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import AxesZero

def distributionFunc(x, mean=0, std=1):
    term1 = 1 / (std*np.sqrt(2*np.pi))
    term2 = np.exp(-1/(2*std**2)*(x - mean)**2)
    return term1*term2

# create the figure and axes objects
fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    
means = [0, 1, 2, -3]
stds  = [1, 0.5, 2, 1.5]


# plot data on each subplot
for i, mean, std in zip(range(4), means, stds):
        ax = axs[i]
        ax.set(title=f'mean={mean}, std={std}')
        xlim = (-5+mean, 5+mean)
        ylim = (-0.5, 1)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        ax.spines['left'].set_position('zero')  # move left spine to zero
        ax.spines['bottom'].set_position('zero')  # move bottom spine to zero
        ax.spines['right'].set_visible(False)  # hide right spine
        ax.spines['top'].set_visible(False)  # hide top spine

        # plot a simple function
        x = np.linspace(-10, 10, 200)
        y = distributionFunc(x, mean=mean, std=std)
        ax.plot(x, y)
        ax.plot((mean, mean), (-0.5, 2), '--')
        

# add a title and adjust layout
fig.suptitle('Normal Distribution')
fig.tight_layout()


# display the plot
# plt.show()
fig.savefig('./imgs/normalDist.png')