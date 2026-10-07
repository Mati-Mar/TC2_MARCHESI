import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

from pytc2.sistemas_lineales import plot_plantilla


fig_sz_x = 14
fig_sz_y = 7
fig_font_size = 16

plt.rcParams.update({'font.size': fig_font_size})

fs = 1000  # Hz
nyq_frec = fs / 2


ripple = 1       # dB
atenuacion = 60  # dB

ws1 = 49.5  # Hz
wp1 = 49.0  # Hz
wp2 = 51.0  # Hz
ws2 = 50.5  # Hz

cant_coeficientes = 3001

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

ventana = ('kaiser', 5)

num_win = sig.firwin2(
    cant_coeficientes,
    freq=frecuencias,
    gain=ganancia,
    window=ventana,
    fs=fs
)

w, hh_win = sig.freqz(
    num_win,
    worN=4096,
    fs=fs
)

plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    w,
    20 * np.log10(np.abs(hh_win) + 1e-12),
    label='FIR'
)

plot_plantilla(
    filter_type='bandstop',
    fpass=(wp1, wp2),
    fstop=(ws1, ws2),
    ripple=ripple,
    attenuation=atenuacion,
    fs=fs
)

plt.title('Respuesta en frecuencia del filtro FIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.xlim(40, 60)
plt.ylim(-70, 5)
plt.grid()
plt.legend()
plt.show()

fase_fir = np.unwrap(np.angle(hh_win))

plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    w,
    fase_fir,
    label='FIR'
)

plt.axvline(
    50,
    linestyle='--',
    label='50 Hz'
)

plt.title('Fase del filtro FIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.xlim(40, 60)
plt.grid()
plt.legend()
plt.show()
