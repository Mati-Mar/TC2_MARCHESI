import numpy as np
import matplotlib.pyplot as plt

N = 7

n = np.arange(0, 13)

# Respuesta al impulso del promediador
h_promedio = np.zeros(len(n))
h_promedio[:N] = 1 / N

# Respuesta al impulso del sumador
h_sumador = np.zeros(len(n))
h_sumador[:N] = 1

plt.figure(figsize=(8, 7))

# Filtro de media móvil

plt.subplot(2, 1, 1)

plt.stem(n, h_promedio)

plt.xlabel("n")
plt.ylabel("h[n]")
plt.title("Respuesta al impulso - Promedio (N=7)")

plt.ylim(0, 1.1)
plt.grid(True)

# Filtro como sumador

plt.subplot(2, 1, 2)

plt.stem(n, h_sumador)

plt.xlabel("n")
plt.ylabel("h[n]")
plt.title("Respuesta al impulso - Sumador (N=7)")

plt.ylim(0, 1.1)
plt.grid(True)

plt.tight_layout()
plt.show()