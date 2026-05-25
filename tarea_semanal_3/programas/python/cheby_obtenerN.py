import numpy as np

# Datos de la consigna
alpha_min = 30   # dB
alpha_max = 0.5    # dB (ejemplo)
omega_s = 4        # frecuencia normalizada (ejemplo)

# Cálculo de epsilon
epsilon = np.sqrt(10**(alpha_max / 10) - 1)

# Búsqueda del primer n que cumple
n = 1

while True:
    alpha_n = 10 * np.log10(
        1 + epsilon**2 * np.cosh(n * np.arccosh(omega_s))**2
    )

    if alpha_n >= alpha_min:
        break

    n += 1

print(f"Epsilon^2 = {epsilon**2:.6f}")
print(f"Primer n que cumple: {n}")
print(f"Alpha(n) = {alpha_n:.2f} dB")

