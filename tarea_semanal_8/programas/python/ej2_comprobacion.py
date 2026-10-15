import sympy as sp
from pytc2.general import s

Z1 = sp.Rational(3, 8)
R1 = sp.Rational(35, 32)
C1 = sp.Rational(32, 175)

Z2 = sp.Rational(105, 104)
R2 = sp.Rational(350, 507)
C2 = sp.Rational(507, 1400)

Z3 = sp.Rational(50, 39)

# R1-C1 en serie
ZR1C1 = sp.factor(R1 + 1 / (s*C1))

# R2-C2 en serie
ZR2C2 = sp.factor(R2 + 1 / (s*C2))

# (R2 + C2) || Z3
Zp = sp.factor(1 / (1/ZR2C2 + 1/Z3))

# Z2 + paralelo de salida
Zrama2 = sp.factor(Z2 + Zp)

# Impedancia de entrada
Zin = sp.factor(Z1 + 1 / (1/ZR1C1 + 1/Zrama2))

# Función impedancia original
Z = (s**2 + 6*s + 8) / (s**2 + 4*s + 3)

diferencia = sp.factor(Zin - Z)

print("\n¿Coinciden las funciones?")
if diferencia == 0:
    print("SI")
else:
    print("NO")