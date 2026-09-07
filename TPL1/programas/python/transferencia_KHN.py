import sympy as sp
from pytc2.remociones import remover_polo_dc
from pytc2.general import a_equal_b_latex_s, print_latex, s, symbfunc2tf, factorSOS
from pytc2.sistemas_lineales import bodePlot
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig
import math

# Parámetros:
Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11 = sp.symbols("Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11")
Vi, Vo, Va, Vb, Vc, Vd, Ve, Vf, Vg = sp.symbols("Vi, Vo, Va, Vb, Vc, Vd, Ve, Vf, Vg")
G1, G2, G3, G4, G5, G6, G7, G8, G9, C1, C2, wt, w0 = sp.symbols("G1, G2, G3, G4, G5, G6, G7, G8, G9, C1, C2, wt, w0", real=True, positive=True) 
s = sp.symbols('s')

# Ecuaciones de nodos
eq1 = Va*(Y3+Y10+Y1+Y2) - Vi*Y3 - Vb*Y10 - Vb*Y1 - Vf*Y2
eq2 = Va*1
eq3 = Vc*(Y4+Y11) - Vb*Y4 - Vd*Y11
eq4 = Vc*1
eq5 = Ve*(Y5+Y6) - Vd*Y5 - Vf*Y6
eq6 = Ve*1
eq7 = Vg*(Y8+Y7+Y9) - Vb*Y8 - Vi*Y7 - Vo*Y9
eq8 = Vg*1

solucion = sp.solve([eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8], [Vo, Va, Vb, Vc, Vd, Ve, Vf, Vg], dict=True)


# Calculamos la transferencia T = Vo / Vi
Vo_resuelto = solucion[0][Vo]
T = sp.simplify(Vo_resuelto / Vi)

T_s = T.subs({
    Y1: G1,
    Y2: G2,
    Y3: G3,
    Y4: G4,
    Y5: G5,
    Y6: G6,
    Y7: G7,
    Y8: G8,
    Y9: G9,
    Y10: s*C1,
    Y11: s*C2
})

# Simplificación
T_s = sp.together(T_s)
T_s = sp.factor(T_s)
T_s = sp.simplify(T_s)

### Impresión llevando a un formato más cómodo la transferencia

# print_latex(a_equal_b_latex_s('T(s)', T_s))

divisor = C1*C2*G6*G9

num, den = sp.fraction(T_s)

num_dividido = sp.collect(sp.expand(num / divisor), s, evaluate=sp.simplify)
den_dividido = sp.collect(sp.expand(den / divisor), s, evaluate=sp.simplify)

T_s = num_dividido / den_dividido

# Impresión del resultado final con componentes
print_latex(a_equal_b_latex_s('T(s)', T_s))