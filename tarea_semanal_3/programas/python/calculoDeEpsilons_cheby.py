import numpy as np

# Datos
alpha_min = 30
alpha_max = 0.5
omega_s = 4
n = 3

# Epsilon
epsilon = np.sqrt(10**(alpha_max/10) - 1)

epsilon1 = epsilon**(1/n)
epsilon2 = epsilon**(2/n)
epsilon3 = epsilon**(3/n)

print(f"epsilon       = {epsilon:.6f}")
print(f"epsilon^(1/n) = {epsilon1:.6f}")
print(f"epsilon^(2/n) = {epsilon2:.6f}")
print(f"epsilon^(3/n) = {epsilon3:.6f}")

# Polinomio denominador
coef = [1, 2*epsilon1, epsilon2, epsilon3]

# Polos
poles = np.roots(coef)

print("\nPolos:")   
print(poles)