import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# Datos
alpha_min = 30
alpha_max = 0.5
omega_s = 4
n = 3

# Epsilon
epsilon = np.sqrt(10**(alpha_max/10) - 1)

epsilon1 = epsilon**(1/n)
epsilon2 = epsilon**(2/n)
epsilon3 = epsilon**(3/n)

# Transferencia
num = [1, 0, 0, 0]
den = [1, 2*epsilon1, 2*epsilon2, epsilon3]

# Polos y ceros
zeros, poles, gain = sig.tf2zpk(num, den)

# ===== Gráfico =====

fig, ax = plt.subplots(figsize=(7,7))

# Polos
ax.plot(np.real(poles),
        np.imag(poles),
        'x',
        markersize=10,
        label='Polos')

# Ceros
ax.plot(np.real(zeros),
        np.imag(zeros),
        'o',
        markersize=10,
        fillstyle='none',
        label='Ceros')

# ---------- Círculo de polos ----------
# Tomo el primer polo complejo
theta = np.linspace(0, 2*np.pi, 500)
complex_poles = [p for p in poles if np.imag(p) != 0]

if complex_poles:
    r = np.abs(complex_poles[0])

    x_p = r*np.cos(theta)
    y_p = r*np.sin(theta)

    ax.plot(x_p,
            y_p,
            '--',
            label=f'Radio polos = {r:.3f}')


# Ejes
ax.axhline(0)
ax.axvline(0)

ax.set_xlabel('Parte real')
ax.set_ylabel('Parte imaginaria')

ax.set_title('Plano Polo-Cero')

ax.grid(True)
ax.legend()

ax.axis('equal')
ax.text(0.08, 0.08,
        '×3',
        fontsize=14)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

plt.show()