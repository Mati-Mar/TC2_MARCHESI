import numpy as np
from scipy import signal

# =========================
# DATOS
# =========================

n = 3           # orden
rp = 0.5        # ripple en dB

# =========================
# CHEBYSHEV LP NORMALIZADO
# =========================

b_lp, a_lp = signal.cheby1(
    N=n,
    rp=rp,
    Wn=1,
    btype='low',
    analog=True,
    output='ba'
)

print("\n=== LP NORMALIZADO ===")
print("Numerador:")
print(b_lp)

print("\nDenominador:")
print(a_lp)

# =========================
# PASAALTOS
# =========================

b_hp, a_hp = signal.lp2hp(
    b_lp,
    a_lp,
    wo=1
)

print("\n=== HP NORMALIZADO ===")
print("Numerador:")
print(b_hp)

print("\nDenominador:")
print(a_hp)

# =========================
# POLOS
# =========================

poles = np.roots(a_hp)

print("\n=== POLOS HP ===")
print(poles)

# =========================
# SOS
# =========================

sos = signal.tf2sos(b_hp, a_hp)

print("\n=== SOS ===")
print(sos)