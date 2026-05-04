import scipy.signal as sig
from pytc2.sistemas_lineales import tf2sos_analog, analyze_sys 

# Filtro Butterworth de orden 6 normalizado
z, p, k = sig.buttap(6)

num, den = sig.zpk2tf(z, p, k)

# Conversión a secciones de segundo orden
this_sos = tf2sos_analog(num, den)

# Análisis (módulo y fase)
_ = analyze_sys(this_sos)
