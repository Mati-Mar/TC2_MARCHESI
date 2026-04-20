import scipy.signal as sig
import matplotlib.pyplot as plt

from pytc2.sistemas_lineales import pzmap

g3 = 1
c1 = 1

a = g3 / c1

T = sig.TransferFunction([1, -a], [1, a])

pzmap(T, fig_id=1)

plt.show()