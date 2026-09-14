import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

theta = np.linspace(0, 2*np.pi, 500)

# Ceros y polos
zeros = np.array([1, -1])
poles = np.array([0, 0])

plt.figure(figsize=(7, 7))

# Círculo unitario
plt.plot(
    np.cos(theta),
    np.sin(theta),
    '--',
    label='Círculo unitario'
)

# Ceros
plt.scatter(
    np.real(zeros),
    np.imag(zeros),
    s=100,
    marker='o',
    facecolors='none',
    edgecolors='black',
    label='Ceros'
)

# Polos
plt.scatter(
    np.real(poles),
    np.imag(poles),
    s=100,
    marker='x',
    linewidths=2,
    label='Polos'
)

# Ejes
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.xlabel('Parte real')
plt.ylabel('Parte imaginaria')

plt.title('Plano z - Filtro diferenciador')

plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)

plt.gca().set_aspect('equal', adjustable='box')

plt.grid()
plt.legend()

plt.show()


# Coeficientes de H(z)
b = [0.5, 0, -0.5]
a = [1]

w, H = signal.freqz(
    b,
    a,
    worN=4096,
    whole=True
)

f = w / (2 * np.pi)

magnitude_db = 20 * np.log10(
    np.maximum(np.abs(H), 1e-6)
)

plt.figure(figsize=(9, 5))

plt.plot(
    f,
    magnitude_db
)

plt.xlabel(r'Frecuencia normalizada $f/f_s$')
plt.ylabel('Magnitud [dB]')
plt.title('Respuesta de módulo - Filtro diferenciador')

plt.xlim(0, 1)
plt.ylim(-90, 5)

plt.grid()
plt.show()

plt.figure(figsize=(9, 5))

plt.plot(
    w / np.pi,
    np.unwrap(np.angle(H))
)

plt.xlabel(r'Frecuencia normalizada $\Omega/\pi$')
plt.ylabel('Fase [rad]')
plt.title('Respuesta de fase - Filtro diferenciador')

plt.grid()
plt.show()