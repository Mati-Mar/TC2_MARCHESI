import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# =========================
# Datos
# =========================

alpha_min = 30
alpha_max = 0.5
omega_s = 4
n = 3

# =========================
# Epsilon
# =========================

epsilon = np.sqrt(10**(alpha_max/10) - 1)

epsilonM1 = epsilon**(-1/n)
epsilon1 = epsilon**(1/n)
epsilon2 = epsilon**(2/n)
epsilon3 = epsilon**(3/n)

print(epsilonM1)

# =========================
# Transferencia
# =========================

# Numerador: s^3
num = [1, 0, 0, 0]

# Denominador
den = [1, 2*epsilon1, 2*epsilon2, epsilon3]

# =========================
# Polos y ceros
# =========================

zeros, poles, gain = sig.tf2zpk(num, den)

# =========================
# Gráfico
# =========================

fig, ax = plt.subplots(figsize=(8,8))

# ---------- Polos ----------
ax.plot(np.real(poles),
        np.imag(poles),
        'x',
        markersize=10,
        label='Polos Chebyshev')

# ---------- Ceros ----------
ax.plot(np.real(zeros),
        np.imag(zeros),
        'o',
        markersize=10,
        fillstyle='none',
        label='Ceros')

# Mostrar multiplicidad
ax.text(0.08, 0.08,
        '×3',
        fontsize=14)

# =========================
# Círculo unidad
# =========================

theta = np.linspace(0, 2*np.pi, 500)

x_unit = np.cos(theta)
y_unit = np.sin(theta)

ax.plot(x_unit,
        y_unit,
        '--',
        label='Círculo unidad')

# =========================
# Círculo de polos
# =========================

complex_poles = [p for p in poles if np.imag(p) != 0]

if complex_poles:

    r = np.abs(complex_poles[0])

    x_p = r*np.cos(theta)
    y_p = r*np.sin(theta)

    ax.plot(x_p,
            y_p,
            '--',
            label=f'Radio polos = {r:.3f}')

# =========================
# Polos Butterworth orden 3
# =========================

butter_angles = [
    2*np.pi/3,
    np.pi,
    4*np.pi/3
]

butter_poles = np.exp(1j*np.array(butter_angles))

ax.plot(np.real(butter_poles),
        np.imag(butter_poles),
        's',
        markersize=8,
        fillstyle='none',
        label='Polos Butterworth n=3')

# =========================
# Ejes y formato
# =========================

ax.axhline(0, color='black')
ax.axvline(0, color='black')

ax.set_xlabel('Parte real')
ax.set_ylabel('Parte imaginaria')

ax.set_title('Plano Polo-Cero')

ax.grid(True)
ax.legend()

ax.axis('equal')
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)

plt.show()