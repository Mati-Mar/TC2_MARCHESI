import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 1000          # Frecuencia de muestreo [Hz]
f0 = 10            # Frecuencia de la señal [Hz]
N = 200            # Cantidad de muestras

n = np.arange(N)
t = n / fs

# Señal de entrada
x = np.sin(2 * np.pi * f0 * t)

# Filtro diferenciador por diferencia central
y = np.zeros(N)
y[2:] = (x[2:] - x[:-2]) / 2

# Derivada ideal
dy = 2 * np.pi * f0 * np.cos(2 * np.pi * f0 * t)

# Conversión a derivada respecto del tiempo
y_derivada = fs * y

# Representación
plt.figure(figsize=(10, 5))

plt.plot(t, dy, label="Derivada ideal")
plt.plot(t, y_derivada, "--", label="Diferenciador discreto")

plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.title("Comparación entre derivada ideal y diferenciador discreto")
plt.grid()
plt.legend()
plt.show()

## COMPARATIVA CON SCIPY DIFF

from scipy.fftpack import diff

# Derivada calculada mediante scipy.fftpack.diff
x_diff = diff(x, order=1, period=N/fs)

# Comparación
plt.figure(figsize=(10, 5))

plt.plot(t, dy, label="Derivada ideal")
plt.plot(t, y_derivada, "--", label="Diferenciador discreto")
plt.plot(t, x_diff, ":", label="scipy.fftpack.diff")

plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.title("Comparación de la derivada y el diferenciador discreto")
plt.grid()
plt.legend()
plt.show()