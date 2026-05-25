import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.signal as sig

#--------------------------------------------------------
# CONFIGURACION GRAFICA
#--------------------------------------------------------

fig_sz_x = 12
fig_sz_y = 7
fig_dpi = 100

mpl.rcParams['figure.figsize'] = (fig_sz_x, fig_sz_y)
mpl.rcParams['figure.dpi'] = fig_dpi

plt.rcParams.update({'font.size': 12})

#--------------------------------------------------------
# PARAMETROS DEL FILTRO
#--------------------------------------------------------

n = 3          # orden
rp = 3         # ripple en dB

#--------------------------------------------------------
# PROTOTIPO CHEBYSHEV LPF
#--------------------------------------------------------

# Obtención de polos, ceros y ganancia
z, p, k = sig.cheb1ap(n, rp)

# Conversión a función transferencia
num, den = sig.zpk2tf(z, p, k)

#--------------------------------------------------------
# TRANSFORMACION LPF -> HPF
#--------------------------------------------------------

num_hp, den_hp = sig.lp2hp(num, den)

# Sistema final
system = sig.TransferFunction(num_hp, den_hp)

#--------------------------------------------------------
# RESPUESTA EN FRECUENCIA
#--------------------------------------------------------

w, mag, phase = sig.bode(system)

#--------------------------------------------------------
# GRAFICOS
#--------------------------------------------------------

plt.figure()

#--------------------------------------------------------
# MODULO
#--------------------------------------------------------

plt.subplot(2,1,1)

plt.semilogx(w, mag, linewidth=2)

plt.title('Filtro Chebyshev Tipo I - HPF - Orden 3')

plt.ylabel('Magnitud [dB]')

plt.grid(True, which='both')

# Zoom para ver el ripple
plt.xlim([0.1, 10])
plt.ylim([-80, 5])

#--------------------------------------------------------
# FASE
#--------------------------------------------------------

plt.subplot(2,1,2)

plt.semilogx(w, phase, linewidth=2)

plt.ylabel('Fase [°]')
plt.xlabel('Frecuencia angular [rad/s]')

plt.grid(True, which='both')

plt.xlim([0.1, 10])

#--------------------------------------------------------
# MOSTRAR
#--------------------------------------------------------

plt.tight_layout()
plt.show()