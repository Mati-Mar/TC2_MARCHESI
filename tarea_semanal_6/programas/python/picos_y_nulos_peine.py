import numpy as np
import matplotlib.pyplot as plt

# Parámetros del filtro
c1 = -1
N = 8

a0, a1, a2 = 1, 0, 0
b0, b1, b2 = 1, 0, 0

# Frecuencia de muestreo propuesta
fs = 1000  # Hz

Omega = np.linspace(0, np.pi, 4000)
H = 1 + np.exp(-1j * N * Omega)

# Frecuencias de nulos y picos
k_null = np.arange(4)
f_null = (2*k_null + 1) * fs / (2*N)

k_peak = np.arange(5)
f_peak = k_peak * fs / N

# Conversión de frecuencia normalizada a Hz
f = Omega / (2*np.pi) * fs

modulo = np.abs(H)
modulo_db = 20 * np.log10(np.maximum(modulo, 1e-12))

plt.figure(figsize=(10, 4.8))
plt.plot(f, modulo_db, label="|H(f)|")

plt.scatter(f_null, np.zeros_like(f_null), marker="x", s=70,
            label="Nulos")
plt.scatter(f_peak, np.full_like(f_peak, 6.02), marker="o", s=55,
            label="Picos")

for fn in f_null:
    plt.axvline(fn, linestyle=":", linewidth=0.9)

for fp in f_peak:
    plt.axvline(fp, linestyle="--", linewidth=0.8)

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Módulo [dB]")
plt.title("Respuesta del filtro peine con $f_s = 1$ kHz")
plt.grid(True, alpha=0.3)
plt.xlim(0, fs/2)
plt.ylim(-60, 8)
plt.legend()
plt.show()