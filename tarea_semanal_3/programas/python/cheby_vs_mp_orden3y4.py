import numpy as np
import matplotlib.pyplot as plt

# Datos
alpha_max = 0.5
alpha_min = 30
ws = 4

epsilon = np.sqrt(10**(alpha_max/10) - 1)

w = np.logspace(-1, 2, 3000)

def H_cheby(w, n, eps):

    H = np.zeros_like(w)

    idx_pb = w <= 1
    idx_sb = w > 1

    H[idx_pb] = 1/np.sqrt(
        1 + eps**2 *
        np.cos(
            n*np.arccos(w[idx_pb])
        )**2
    )

    H[idx_sb] = 1/np.sqrt(
        1 + eps**2 *
        np.cosh(
            n*np.arccosh(w[idx_sb])
        )**2
    )

    return H


def H_mp(w, n, eps):

    return 1/np.sqrt(
        1 + eps**2 * w**(2*n)
    )

Hc3  = H_cheby(w, 3, epsilon)
Hmp3 = H_mp(w, 3, epsilon)
Hmp4 = H_mp(w, 4, epsilon)

# FIGURA 1
plt.figure(figsize=(8,5))

plt.semilogx(
    w,
    20*np.log10(Hc3),
    label='Chebyshev n=3'
)

plt.semilogx(
    w,
    20*np.log10(Hmp3),
    label='MP n=3'
)

plt.axvline(ws, color='k', linestyle=':')
plt.axhline(-alpha_min, color='gray', linestyle='--')

plt.grid(True, which='both')
plt.xlabel(r'$\omega/\omega_p$')
plt.ylabel('Magnitud [dB]')
plt.title('Comparación con mismo orden (n=3)')
plt.legend()

# FIGURA 2
plt.figure(figsize=(8,5))

plt.semilogx(
    w,
    20*np.log10(Hc3),
    label='Chebyshev n=3'
)

plt.semilogx(
    w,
    20*np.log10(Hmp4),
    label='MP n=4'
)

plt.axvline(ws, color='k', linestyle=':')
plt.axhline(-alpha_min, color='gray', linestyle='--')

plt.grid(True, which='both')
plt.xlabel(r'$\omega/\omega_p$')
plt.ylabel('Magnitud [dB]')
plt.title('Chebyshev n=3 vs MP n=4')
plt.legend()

plt.show()