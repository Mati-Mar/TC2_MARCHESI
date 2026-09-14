import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Ns = [3, 4, 5]

theta = np.linspace(0, 2*np.pi, 500)

plt.figure(figsize=(7, 7))

# Círculo unitario
plt.plot(
    np.cos(theta),
    np.sin(theta),
    '--',
    label='Círculo unitario'
)

for N in Ns:

    # Ceros del filtro de media móvil
    k = np.arange(1, N)
    zeros = np.exp(1j * 2 * np.pi * k / N)

    plt.scatter(
        np.real(zeros),
        np.imag(zeros),
        s=70,
        label=f'N={N}'
    )

# Ejes
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.xlabel(r'Parte real')
plt.ylabel(r'Parte imaginaria')

plt.title('Plano z - Filtros de media móvil')

plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)

plt.gca().set_aspect('equal', adjustable='box')

plt.grid()
plt.legend()

plt.show()

plt.figure(figsize=(9, 5))

for N in Ns:

    b = np.ones(N) / N
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

    plt.plot(
        f,
        magnitude_db,
        label=f'N={N}'
    )

plt.xlabel(r'Frecuencia normalizada $f/f_s$')
plt.ylabel('Magnitud [dB]')
plt.title('Respuesta de módulo - Filtros de media móvil')

plt.xlim(0, 1)
plt.ylim(-90, 2)

plt.grid()
plt.legend()
plt.show()

plt.figure(figsize=(9, 5))

for N in Ns:

    b = np.ones(N) / N
    a = [1]

    w, H = signal.freqz(b, a, worN=2048)

    plt.plot(
        w / np.pi,
        np.unwrap(np.angle(H)),
        label=f'N={N}'
    )

plt.xlabel(r'Frecuencia normalizada $\Omega/\pi$')
plt.ylabel('Fase [rad]')
plt.title('Respuesta de fase - Filtros de media móvil')
plt.grid()
plt.legend()
plt.show()