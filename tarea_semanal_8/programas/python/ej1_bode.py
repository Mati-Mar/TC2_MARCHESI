
from pytc2.general import s, symbfunc2tf
from pytc2.sistemas_lineales import bodePlot

# Función impedancia original
Z = (s**2 + s + 1) / ((s + 1)*(s**2 + 2*s + 5))

# Convierto la función simbólica a función de transferencia
Z_tf = symbfunc2tf(Z)

# Grafico el diagrama de Bode
bodePlot(
    Z_tf,
    filter_description='Z(s)',
    xaxis='omega'
);
