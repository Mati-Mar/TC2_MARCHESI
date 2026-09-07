import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Osciloscopio

frecuencia_osc = np.array([
    20.0, 40.0, 57.5, 59.7, 61.9, 64.1, 66.3, 68.5,
    69.6, 70.7, 72.9, 75.1, 77.3, 79.5, 80.8, 100.0, 150.0
])

ganancia_osc = np.array([
    10.0, 9.1, 7.1, 6.0, 5.32, 4.51, 3.64, 2.95,
    2.83, 3.07, 4.0, 5.5, 6.48, 7.2, 7.1, 9.27, 9.27
])

Vin = 10.0  # Vpp

# Ganancia en dB
ganancia_osc_dB = 20 * np.log10(ganancia_osc / Vin)


# Analizador de espectro

path = "../../recursos/barrido.csv"

with open(path, "r") as f:
    lineas = f.readlines()

inicio = next(
    i for i, linea in enumerate(lineas)
    if "Vac vs Frequency" in linea
)

datos = pd.read_csv(
    path,
    skiprows=inicio + 1
)

frecuencia_analizador = datos["X (Hz)"].to_numpy()
ganancia_analizador_dB = datos["Ch-2 (dBr)"].to_numpy()


# Llevar ambas curvas a 0 dB en su máximo
ganancia_osc_norm = ganancia_osc_dB - np.max(ganancia_osc_dB)
ganancia_analizador_norm = (
    ganancia_analizador_dB - np.max(ganancia_analizador_dB)
)


# Comparación

plt.figure(figsize=(10, 6))

plt.semilogx(
    frecuencia_osc,
    ganancia_osc_norm,
    marker='o',
    linewidth=2,
    label='Osciloscopio'
)

plt.semilogx(
    frecuencia_analizador,
    ganancia_analizador_norm,
    linewidth=2,
    label='Analizador de espectro'
)

plt.title(
    'Comparación de mediciones',
    fontsize=14,
    fontweight='bold'
)

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Ganancia normalizada [dB]')

plt.grid(True, which='both', alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()