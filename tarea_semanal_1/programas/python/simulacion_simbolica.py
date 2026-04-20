import sympy as sp
from pytc2.general import a_equal_b_latex_s, print_latex

# variable compleja s
s = sp.symbols("s", real = False)

# tensiones y corrientes que usaremos para nuestros análisis
V1, V2, Vx = sp.symbols("V1, V2, Vx")
Y1, Y2, Y3, Y4 = sp.symbols("Y1, Y2, Y3, Y4")
G1, G2, G3, C = sp.symbols("G1, G2, G3, C", real = True, positive = True) 

aa = sp.solve([ Vx*(Y1+Y2) - V1*Y1 - V2*Y2,
                           Vx*(Y3+Y4) - V1*Y4
                         ], 
                         [V1, V2, Vx])

H = aa[V2]/aa[V1]
print_latex(a_equal_b_latex_s('H(s) = \\frac{V_2}{V_1}', H))

H = H.subs({Y1:G1, Y2:G2, Y3:G3, Y4:s*C})

print_latex(a_equal_b_latex_s('H(s) = \\frac{V_2}{V_1}', H))

num, den = sp.fraction(H)

num_poly = sp.Poly(num, s)
den_poly = sp.Poly(den, s)

H_monic = sp.simplify(num / den_poly.LC()) / sp.simplify(den / den_poly.LC())
print_latex(a_equal_b_latex_s('H(s) = \\frac{V_2}{V_1}', H_monic))

H_norm = H.subs({G1:1, G2:1, G3:1, C:1})
print_latex(a_equal_b_latex_s('H(s) = \\frac{V_2}{V_1}', H_norm))