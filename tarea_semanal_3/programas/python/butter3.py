import scipy.signal as sig

from pytc2.sistemas_lineales import tf2sos_analog, analyze_sys 

z,p,k = sig.buttap(3)

num, den = sig.zpk2tf(z,p,k)

this_sos = tf2sos_analog(num, den)
        
_ = analyze_sys( this_sos )