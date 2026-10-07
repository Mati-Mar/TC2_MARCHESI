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

ripple = 1       # dB
atenuacion = 60  # dB

ws1 = 49.5  # Hz
wp1 = 49.0  # Hz
wp2 = 51.0  # Hz
ws2 = 50.5  # Hz

ripple_iterado = 1
atenuacion_iterado = 60

sos_iir = sig.iirdesign(
    wp=[wp1, wp2],
    ws=[ws1, ws2],
    gpass=ripple_iterado,
    gstop=atenuacion_iterado,
    output='sos',
    analog=False,
    ftype='cheby1',
    fs=fs
)

w_rad, h_iir = sig.freqz_sos(
    sos_iir,
    worN=4096,
    fs=fs
)

plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    w_rad,
    20 * np.log10(np.abs(h_iir) + 1e-12),
    label='IIR'
)

plot_plantilla(
    filter_type='bandstop',
    fpass=(wp1, wp2),
    fstop=(ws1, ws2),
    ripple=ripple,
    attenuation=atenuacion,
    fs=fs
)

plt.title('Respuesta en frecuencia del filtro IIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.xlim(40, 60)
plt.ylim(-70, 5)
plt.grid()
plt.legend()
plt.show()

fase_iir = np.unwrap(np.angle(h_iir))

plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    w_rad,
    fase_iir,
    label='IIR'
)

plt.axvline(
    50,
    linestyle='--',
    label='50 Hz'
)

plt.title('Fase del filtro IIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.xlim(40, 60)
plt.grid()
plt.legend()
plt.show()
