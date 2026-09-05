import sympy as sp

from pytc2.general import s, print_latex, a_equal_b_latex_s
from pytc2.cuadripolos import calc_MAI_vtransf_ij_mn


# Simbolos

L, C = sp.symbols('L C', positive=True)

YL = 1/(s*L)
YC = s*C


# Circuito
#
#    0 -- L ----- 3 ----- L ----- 1
#                 |
#                 C
#                 |
#                 2

# Armo la MAI
Ymai = sp.Matrix([
    [ YL,       0,       0,      -YL],
    [  0,       YL,       0,      -YL],
    [  0,        0,      YC,      -YC],
    [-YL,      -YL,      -YC,  2*YL + YC]
])


# V23/V13
V23_V13 = calc_MAI_vtransf_ij_mn(
    Ymai,
    1, 2,       # V23
    0, 2,       # V13
)

# V21/V31
V21_V31 = calc_MAI_vtransf_ij_mn(
    Ymai,
    1, 0,       # V21
    2, 0,       # V31
)

# V12/V32
V12_V32 = calc_MAI_vtransf_ij_mn(
    Ymai,
    0, 1,       # V12
    2, 1,       # V32
)

print_latex(
    a_equal_b_latex_s(r'\frac{V_{23}}{V_{13}}', V23_V13)
)

print_latex(
    a_equal_b_latex_s(r'\frac{V_{21}}{V_{31}}', V21_V31)
)

print_latex(
    a_equal_b_latex_s(r'\frac{V_{12}}{V_{32}}', V12_V32)
)