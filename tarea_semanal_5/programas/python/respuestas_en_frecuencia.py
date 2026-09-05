import numpy as np
import matplotlib.pyplot as plt

from pytc2.general import s


L = 10e-3
C = 100e-9

w0 = 1 / np.sqrt(L*C)

transferencias = [
    ((1/(L*C)) / (s**2 + 1/(L*C)), r'$V_{23}/V_{13}$'),
    (s**2 / (s**2 + 1/(L*C)), r'$V_{21}/V_{31}$'),
    (s**2 / (s**2 + 1/(L*C)), r'$V_{12}/V_{32}$')
]

f = np.logspace(1, 6, 2000)
w = 2*np.pi*f

for T, nombre in transferencias:

    H = np.array([complex(T.subs(s, 1j*wi)) for wi in w])

    for valores, ylabel, titulo in [
        (np.abs(H), r'$|T|$', 'Módulo'),
        (np.angle(H, deg=True), 'Fase [°]', 'Fase')
    ]:

        plt.figure(figsize=(10, 6))
        plt.semilogx(f, valores)
        plt.axvline(w0/(2*np.pi), linestyle=':', label=r'$f_0$')
        plt.xlabel('Frecuencia [Hz]')
        plt.ylabel(ylabel)
        plt.title(f'{titulo} de {nombre}')
        plt.grid(True, which='both')
        plt.legend()
        plt.show()