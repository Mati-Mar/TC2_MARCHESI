import numpy as np
import matplotlib.pyplot as plt

# Parámetros del filtro
c1 = -1
N = 8

a0, a1, a2 = 1, 0, 0
b0, b1, b2 = 1, 0, 0

# Polos y ceros
k = np.arange(N)

zeros = np.exp(1j * (2*k + 1) * np.pi / N)
poles = np.zeros(N, dtype=complex)

# Circunferencia unidad
theta = np.linspace(0, 2*np.pi, 500)

plt.figure(figsize=(6, 6))

plt.plot(
    np.cos(theta),
    np.sin(theta),
    linestyle="--",
    label="Circunferencia unidad"
)

# Ceros
plt.scatter(
    zeros.real,
    zeros.imag,
    marker="o",
    s=70,
    label="Ceros"
)

# Polos
plt.scatter(
    poles.real,
    poles.imag,
    marker="x",
    s=90,
    label="Polos (multiplicidad 8)"
)

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.grid(True, alpha=0.3)

plt.xlim(-1.25, 1.25)
plt.ylim(-1.25, 1.25)

plt.gca().set_aspect("equal", adjustable="box")

plt.xlabel("Parte real")
plt.ylabel("Parte imaginaria")
plt.title("Diagrama de polos y ceros")
plt.legend()

plt.show()

# Respuesta en frecuencia
Omega = np.linspace(0, np.pi, 4000)
H = 1 + np.exp(-1j * N * Omega)

modulo = np.abs(H)
modulo_db = 20 * np.log10(np.maximum(modulo, 1e-12))

plt.figure(figsize=(9, 4.5))
plt.plot(Omega / np.pi, modulo_db)

plt.xlabel(r"Frecuencia normalizada $\Omega/\pi$")
plt.ylabel("Módulo [dB]")
plt.title("Respuesta de módulo del filtro peine")
plt.grid(True, alpha=0.3)
plt.ylim(-60, 7)
plt.xlim(0, 1)
plt.show()

# Fase principal
fase = np.angle(H)

plt.figure(figsize=(9, 4.5))
plt.plot(Omega / np.pi, fase)

plt.xlabel(r"Frecuencia normalizada $\Omega/\pi$")
plt.ylabel("Fase [rad]")
plt.title("Respuesta de fase del filtro peine")
plt.grid(True, alpha=0.3)
plt.xlim(0, 1)
plt.show()