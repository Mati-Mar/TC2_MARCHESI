import scipy.signal as sig
import matplotlib.pyplot as plt

from pytc2.sistemas_lineales import bodePlot, GroupDelay

# Transferencia
num = [15]
den = [1, 6, 15, 15]

T = sig.TransferFunction(num, den)

# Bode
bodePlot(T, fig_id=1)

# Retardo de grupo
GroupDelay(T, fig_id=2)

plt.show()