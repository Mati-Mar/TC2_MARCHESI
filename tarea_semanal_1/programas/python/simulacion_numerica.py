import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np

from pytc2.sistemas_lineales import bodePlot, pzmap, GroupDelay

r3 = 1000
c1 = 0.001

a = 1 / (c1 . r3)

T = sig.TransferFunction([1, -a], [1, a])
bodePlot(T, fig_id=1)
axs = plt.figure(1).axes
axs[0].set_ylim([-0.1, 0.1])

pzmap(T, fig_id=2)

GroupDelay(T, fig_id=3)

plt.show()
