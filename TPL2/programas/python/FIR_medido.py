import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig


fig_sz_x = 14
fig_sz_y = 7
fig_font_size = 16

plt.rcParams.update({'font.size': fig_font_size})

fs = 1000


frecuencia_fir = np.array([
    48.0, 48.1, 48.2, 48.3, 48.4, 48.5, 48.6, 48.7, 48.8, 48.9,
    49.0, 49.1, 49.2, 49.3, 49.4, 49.5, 49.6, 49.7, 49.8, 49.9,
    50.0, 50.1, 50.2, 50.3, 50.4, 50.5, 50.6, 50.7, 50.8, 50.9,
    51.0, 51.1, 51.2, 51.3, 51.4, 51.5, 51.6, 51.7, 51.8, 51.9,
    52.0
])

vout_fir = np.array([
    1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34,
    1.34, 1.32, 1.27, 1.13, 0.94, 0.66, 0.50, 0.28, 0.19, 0.096,
    0.0026, 0.0026, 0.0026, 0.0028, 0.0028, 0.0028, 0.0028, 0.0028,
    0.0028, 0.0028, 0.0060, 0.116, 0.220, 0.376, 0.60, 0.82,
    1.00, 1.15, 1.27, 1.29, 1.34
])


plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    frecuencia_fir,
    vout_fir,
    marker='o'
)

plt.axvline(
    50,
    linestyle='--',
    label='50 Hz'
)

plt.title('Medición experimental - Filtro FIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('$V_{out}$ [Vp]')
plt.xlim(48, 52)
plt.grid()
plt.legend()
plt.show()



cant_coeficientes = 3001
nyq_frec = fs / 2

frecuencias = [
    0, 48.2, 49.2, 49.3, 49.4, 49.5,
    49.6, 49.7, 49.8, 49.9, 50.0, 50.1,
    50.2, 50.3, 50.4, 50.5, 50.6, 50.7,
    50.8, 50.9, 51.0, 51.1, 51.2, 52.2,
    nyq_frec
]

ganancia = [
    1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0,
    1, 1, 1
]

num_win = sig.firwin2(
    cant_coeficientes,
    freq=frecuencias,
    gain=ganancia,
    window=('kaiser', 5),
    fs=fs
)

w, hh_win = sig.freqz(
    num_win,
    worN=4096,
    fs=fs
)

vout_fir_vpp = 2 * vout_fir

ganancia_fir_medida = 20 * np.log10(vout_fir_vpp / 3)
ganancia_fir_simulada = 20 * np.log10(np.abs(hh_win) + 1e-12)


plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    w,
    ganancia_fir_simulada,
    color='blue',
    label='Simulación FIR'
)

plt.plot(
    frecuencia_fir,
    ganancia_fir_medida,
    color='orange',
    marker='o',
    label='Medición FIR'
)

plt.axvline(
    50,
    linestyle='--',
    label='50 Hz'
)

plt.title('Comparación entre simulación y medición - FIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Ganancia [dB]')
plt.xlim(48, 52)
plt.ylim(-70, 5)
plt.grid()
plt.legend()
plt.show()
