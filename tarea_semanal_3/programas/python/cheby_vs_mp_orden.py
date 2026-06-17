import numpy as np

# Datos de la consigna
alpha_min = 30      # dB
alpha_max = 0.5     # dB
omega_s = 4

# epsilon
epsilon = np.sqrt(10**(alpha_max/10) - 1)


#Chebyshev
n_cheby = 1

while True:

    alpha_cheby = 10*np.log10(
        1 + epsilon**2 *
        np.cosh(
            n_cheby*np.arccosh(omega_s)
        )**2
    )

    if alpha_cheby >= alpha_min:
        break

    n_cheby += 1

#MP

n_mp = 1

while True:

    alpha_mp = 10*np.log10(
        1 + epsilon**2 *
        omega_s**(2*n_mp)
    )

    if alpha_mp >= alpha_min:
        break

    n_mp += 1

alpha_mp_orden_cheby = 10*np.log10(
        1 + epsilon**2 *
        omega_s**(2*n_cheby)
    )

print("Chebyshev")
print(f"n mínimo = {n_cheby}")
print(f"α(ωs) = {alpha_cheby:.2f} dB")
print()

print("Máxima Planicidad")
print(f"n mínimo = {n_mp}")
print(f"α(ωs) = {alpha_mp:.2f} dB")

print()
print("Máxima Planicidad para mismo del chebyshev")
print(f"α(ωs) = {alpha_mp_orden_cheby:.2f} dB")