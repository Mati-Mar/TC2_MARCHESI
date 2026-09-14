import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

beta_1 = 0.9
beta_2 = 0.7265425

ceros = [1]

polos_1 = [beta_1]
polos_2 = [beta_2]

plt.figure(figsize=(6, 6))

# Circunferencia unitaria
theta = np.linspace(0, 2*np.pi, 500)
plt.plot(np.cos(theta), np.sin(theta), linestyle='--', label='Circunferencia unitaria')

# Cero
plt.scatter(np.real(ceros), np.imag(ceros),
            marker='o', s=100, label='Cero')

# Polos
plt.scatter(np.real(polos_1), np.imag(polos_1),
            marker='x', s=100, label=r'Polo $\beta=0.9$')

plt.scatter(np.real(polos_2), np.imag(polos_2),
            marker='x', s=100, label=r'Polo $\beta=0.7265$')

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.xlabel(r'Parte real')
plt.ylabel(r'Parte imaginaria')
plt.title('Polos y ceros del filtro elimina continua')
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()

Omega = np.linspace(1e-5, np.pi, 2000)

def H_dc_blocker(Omega, beta):
    return (1 - np.exp(-1j * Omega)) / (1 - beta * np.exp(-1j * Omega))

H_09 = H_dc_blocker(Omega, beta_1)
H_opt = H_dc_blocker(Omega, beta_2)

mod_09 = 20 * np.log10(np.abs(H_09))
mod_opt = 20 * np.log10(np.abs(H_opt))

fase_09 = np.unwrap(np.angle(H_09)) * 180 / np.pi
fase_opt = np.unwrap(np.angle(H_opt)) * 180 / np.pi

plt.figure(figsize=(8, 4))

plt.plot(Omega / np.pi, mod_09, label=r'$\beta=0.9$')
plt.plot(Omega / np.pi, mod_opt, label=r'$\beta=0.7265$')

plt.xlabel(r'Frecuencia normalizada $\Omega/\pi$')
plt.ylabel('Módulo [dB]')
plt.title('Respuesta de módulo - Filtro elimina continua')
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize=(8, 4))

plt.plot(Omega / np.pi, fase_09, label=r'$\beta=0.9$')
plt.plot(Omega / np.pi, fase_opt, label=r'$\beta=0.7265$')

plt.xlabel(r'Frecuencia normalizada $\Omega/\pi$')
plt.ylabel('Fase [°]')
plt.title('Respuesta de fase - Filtro elimina continua')
plt.grid()
plt.legend()
plt.show()