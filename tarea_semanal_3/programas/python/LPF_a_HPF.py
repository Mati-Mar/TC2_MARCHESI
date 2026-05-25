import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# =========================================================
# DATOS DEL FILTRO
# =========================================================

alpha_max = 0.5
n = 3

# =========================================================
# EPSILON CHEBYSHEV
# =========================================================

epsilon = np.sqrt(10**(alpha_max/10) - 1)

epsilon1 = epsilon**(1/n)
epsilon2 = epsilon**(2/n)
epsilon3 = epsilon**(3/n)

# =========================================================
# TRANSFERENCIA LPF PROTOTIPO
# =========================================================
# H(s) = 1 / (s³ + 2e^(1/3)s² + 2e^(2/3)s + e)

num_lp = [1]

den_lp = [
    1,
    2*epsilon1,
    2*epsilon2,
    epsilon3
]

# =========================================================
# POLOS Y CEROS LPF
# =========================================================

zeros_lp, poles_lp, gain_lp = sig.tf2zpk(num_lp, den_lp)

# =========================================================
# TRANSFORMACIÓN LP -> HP
# =========================================================
#
# s -> wc/s
#
# Cada polo:
# p_hp = wc / p_lp
#
# Los ceros del LPF en infinito
# pasan al origen en el HPF
# =========================================================

omega_c = 1

poles_hp = omega_c / poles_lp

# n ceros en el origen
zeros_hp = np.zeros(n)

# =========================================================
# FIGURA
# =========================================================

fig, ax = plt.subplots(figsize=(10,10))

# =========================================================
# POLOS LPF
# =========================================================

ax.plot(
    np.real(poles_lp),
    np.imag(poles_lp),
    'x',
    markersize=12,
    label='Polos LPF prototipo'
)

# =========================================================
# POLOS HPF
# =========================================================

ax.plot(
    np.real(poles_hp),
    np.imag(poles_hp),
    's',
    markersize=10,
    fillstyle='none',
    label='Polos HPF transformado'
)

# =========================================================
# CEROS HPF
# =========================================================

ax.plot(
    np.real(zeros_hp),
    np.imag(zeros_hp),
    'o',
    markersize=10,
    fillstyle='none',
    label='Ceros HPF'
)

# multiplicidad de ceros
ax.text(
    0.05,
    0.05,
    '×3',
    fontsize=14
)

# =========================================================
# UNIR CADA POLO LPF CON SU TRANSFORMADO
# =========================================================

for p_lp, p_hp in zip(poles_lp, poles_hp):

    ax.plot(
        [np.real(p_lp), np.real(p_hp)],
        [np.imag(p_lp), np.imag(p_hp)],
        '--',
        linewidth=1
    )

# =========================================================
# CÍRCULO UNIDAD
# =========================================================

theta = np.linspace(0, 2*np.pi, 500)

x_unit = np.cos(theta)
y_unit = np.sin(theta)

ax.plot(
    x_unit,
    y_unit,
    ':',
    label='|s| = 1'
)

# =========================================================
# EJES
# =========================================================

ax.axhline(0, color='black')
ax.axvline(0, color='black')

# =========================================================
# FORMATO
# =========================================================

ax.set_xlabel('Parte real')
ax.set_ylabel('Parte imaginaria')

ax.set_title('Transformación LPF → HPF')

ax.grid(True)
ax.legend()

ax.axis('equal')

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

plt.show()