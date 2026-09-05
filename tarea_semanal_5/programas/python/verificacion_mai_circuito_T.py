import sympy as sp

from pytc2.general import s

# Simbolos

L, C = sp.symbols('L C', positive=True)

YL = 1/(s*L)
YC = s*C

# VERIFICACION

# Verifico que la MAI sea correcta

Ymai = sp.Matrix([
    [ YL,       0,       0,      -YL],
    [  0,       YL,       0,      -YL],
    [  0,        0,      YC,      -YC],
    [-YL,      -YL,      -YC,  2*YL + YC]
])

print("Suma de filas:")
print(Ymai * sp.ones(4, 1))

print("Suma de columnas:")
print(sp.ones(1, 4) * Ymai)

print("Determinante:")
print(sp.factor(Ymai.det()))