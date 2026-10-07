import numpy as np
import matplotlib.pyplot as plt


fig_sz_x = 14
fig_sz_y = 7
fig_font_size = 16

plt.rcParams.update({'font.size': fig_font_size})


frecuencia_tt = np.array([
    20, 30, 40, 50, 60, 70, 80, 90, 100, 110,
    120, 130, 140, 150, 160, 170, 180, 190, 200, 500
])

vout_tt = np.array([
    2.90, 2.90, 2.85, 2.80, 2.77, 2.70, 2.66, 2.55, 2.46, 2.35,
    2.25, 2.16, 2.07, 2.00, 1.94, 1.82, 1.75, 1.70, 1.62, 0.60
])


plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    frecuencia_tt[:-1],
    vout_tt[:-1],
    marker='o',
    label='Mediciones 20-200 Hz'
)

plt.plot(
    frecuencia_tt[-1],
    vout_tt[-1],
    marker='o',
    linestyle='None',
    label='Medición a 500 Hz'
)

plt.title('Medición experimental - Talk-Through')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('$V_{out}$ [Vpp]')
plt.grid()
plt.legend()
plt.show()
