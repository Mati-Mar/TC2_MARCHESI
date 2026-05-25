import numpy as np
import matplotlib.pyplot as plt

# =========================
# POLOS CHEBYSHEV
# =========================

p1 = -0.3132 + 1j*1.0219
p2 = -0.3132 - 1j*1.0219
p3 = -0.6265 + 0j

polos = np.array([p1, p2, p3])

# =========================
# GRAFICO
# =========================

fig, ax = plt.subplots(figsize=(7,7))

# Ejes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Polos
ax.plot(np.real(polos),
        np.imag(polos),
        'x',
        markersize=12,
        label='Polos')

# Etiquetas
for i, p in enumerate(polos):
    ax.text(np.real(p)+0.03,
            np.imag(p)+0.03,
            f'p{i+1}')

# =========================
# ELIPSE APROXIMADA
# =========================

# semiejes aproximados
a = 0.63
b = 1.07

t = np.linspace(0, 2*np.pi, 400)

x = -a*np.cos(t)
y = b*np.sin(t)

ax.plot(x, y, '--', label='Elipse Chebyshev')

# =========================
# CIRCUNFERENCIA
# (comparacion Butterworth)
# =========================

r = 1.07

xc = r*np.cos(t)
yc = r*np.sin(t)

ax.plot(xc, yc, ':', label='Circunferencia Butterworth')

# =========================
# FORMATO
# =========================

ax.set_xlabel('Parte Real')
ax.set_ylabel('Parte Imaginaria')

ax.set_title('Polos Chebyshev n=3')

ax.grid(True)
ax.legend()

ax.set_aspect('equal')

plt.show()