import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

from pytc2.general import s, symbfunc2tf
from pytc2.sistemas_lineales import pzmap, GroupDelay


# ============================================================
# Parámetros del filtro
# ============================================================

GC = 1/32e3
GA = 1/160e3

C1 = C2 = 100e-9


# ============================================================
# Transferencia
# ============================================================

T = -(
    s**2 + (GC**2)/(C1*C2)
) / (
    s**2 + s*GA/C1 + (GC**2)/(C1*C2)
)

T = sp.factor(T)

T_tf = symbfunc2tf(T)


# ============================================================
# Respuesta en frecuencia
# ============================================================

f = np.logspace(1, 3, 2000)
w = 2*np.pi*f

T_func = sp.lambdify(s, T, 'numpy')

H = T_func(1j*w)

magnitud = 20*np.log10(np.abs(H))
fase = np.unwrap(np.angle(H))


# ============================================================
# Respuesta de módulo y fase
# ============================================================

bodePlot(
    T_tf,
    fig_id=1,
    filter_description='Filtro Notch KHN'
)

plt.show()

pzmap(
    T_tf,
    fig_id=2,
    filter_description='Polos y ceros - Filtro Notch KHN'
)

plt.show()

GroupDelay(
    T_tf,
    fig_id=3,
    filter_description='Retardo de grupo - Filtro Notch KHN'
)

plt.show()

# VERIFICACIÓN DE LA PLANTILLA

f1 = 45
f0 = 50
f2 = 55
alpha_max = 3

H_verificacion = T_func(
    1j * 2*np.pi*np.array([f1, f0, f2])
)

magnitud_verificacion = 20*np.log10(
    np.abs(H_verificacion)
)


fig, ax = plt.subplots(figsize=(8, 5))

ax.semilogx(
    f,
    magnitud,
    label='Filtro Notch KHN'
)

# Frecuencias de la plantilla
ax.axvline(
    f1,
    color='red',
    linestyle='--',
    label='$f_1 = 45$ Hz'
)

ax.axvline(
    f0,
    color='blue',
    linestyle='--',
    label='$f_0 = 50$ Hz'
)

ax.axvline(
    f2,
    color='red',
    linestyle='--',
    label='$f_2 = 55$ Hz'
)

# Atenuación máxima
ax.axhline(
    -alpha_max,
    color='green',
    linestyle=':',
    label='$\\alpha_{max} = 3$ dB'
)

ax.set_title('Verificación de la plantilla')
ax.set_xlabel('Frecuencia [Hz]')
ax.set_ylabel('Magnitud [dB]')

ax.grid(True, which='both')
ax.legend()

plt.tight_layout()
plt.show()