
from pytc2.general import s, symbfunc2tf
from pytc2.sistemas_lineales import bodePlot

# Función impedancia original
Z = (s**2 + 6*s + 8) / (s**2 + 4*s + 3)

# Convierto la función simbólica a función de transferencia
Z_tf = symbfunc2tf(Z)

# Grafico el diagrama de Bode
bodePlot(
    Z_tf,
    filter_description='Z(s)',
    xaxis='omega'
);
