
import sympy as sp
from pytc2.general import s

# Valores de los componentes
C1 = sp.Rational(1)
R1 = sp.Rational(1, 2)
L1 = sp.Rational(1, 4)
R2 = sp.Rational(1, 16)
C2 = sp.Rational(64, 13)
R3 = sp.Rational(13, 48)

# C2 || R3
Zp = sp.factor(1 / (s*C2 + 1/R3))

# R2 + L1 + (C2 || R3)
Zrama = sp.factor(R2 + s*L1 + Zp)

# Impedancia de entrada reconstruida
Zin = sp.factor(1 / (s*C1 + 1/R1 + 1/Zrama))

# Función impedancia original
Z = (s**2 + s + 1) / ((s + 1)*(s**2 + 2*s + 5))

# Comparación simbólica
diferencia = sp.factor(Zin - Z)

print("Z(s) original =", Z)
print("Zin(s) reconstruida =", Zin)
print("Diferencia =", diferencia)
print("¿Coinciden las funciones?")

if diferencia == 0:
    print("SI")
else:
    print("NO")
