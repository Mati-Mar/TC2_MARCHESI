import numpy as np
import matplotlib.pyplot as plt


# Datos medidos

frecuencia = np.array([
    20.0, 40.0, 57.5, 59.7, 61.9, 64.1, 66.3, 68.5,
    69.6, 70.7, 72.9, 75.1, 77.3, 79.5, 80.8, 100.0, 150.0
])

ganancia = np.array([
    10.0, 9.1, 7.1, 6.0, 5.32, 4.51, 3.64, 2.95,
    2.83, 3.07, 4.0, 5.5, 6.48, 7.2, 7.1, 9.27, 9.27
])

fase_ms = np.array([
    25.2, 13.6, 10.0, 9.7, 9.3, 8.9, 8.2, 7.3,
    6.7, 7.5, 7.7, 7.8, 7.6, 7.4, 7.2, 5.5, 3.48
])


Vin = 10.0  # Vpp

ganancia_lineal = ganancia / Vin
ganancia_dB = 20 * np.log10(ganancia_lineal)

# Fase a partir del desfasaje temporal
fase_grados = -fase_ms * frecuencia * 0.36


fig, ax = plt.subplots(2, 1, figsize=(10, 8), sharex=True)


# Módulo
ax[0].semilogx(
    frecuencia,
    ganancia_dB,
    marker='o',
    linestyle='-',
    linewidth=2,
    label='Medición'
)

ax[0].set_title('Respuesta en frecuencia')
ax[0].set_ylabel('Ganancia [dB]')
ax[0].grid(True, which='both')
ax[0].legend()


# Fase
ax[1].semilogx(
    frecuencia,
    fase_grados,
    marker='o',
    linestyle='-',
    linewidth=2,
    label='Medición'
)

ax[1].set_xlabel('Frecuencia [Hz]')
ax[1].set_ylabel('Fase [°]')
ax[1].grid(True, which='both')
ax[1].legend()


plt.tight_layout()
plt.show()