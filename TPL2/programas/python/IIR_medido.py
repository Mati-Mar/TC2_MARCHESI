# %%
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


# %%
frecuencia_iir = np.array([
    48.0, 48.1, 48.2, 48.3, 48.4, 48.5, 48.6, 48.7, 48.8, 48.9,
    49.0, 49.1, 49.2, 49.3, 49.4, 49.5, 49.6, 49.7, 49.8, 49.9,
    50.0, 50.1, 50.2, 50.3, 50.4, 50.5, 50.6, 50.7, 50.8, 50.9,
    51.0, 51.1, 51.2, 51.3, 51.4, 51.5, 51.6, 51.7, 51.8, 51.9,
    52.0
])

vout_iir = np.array([
    2.80, 2.80, 2.77, 2.74, 2.66, 2.60, 2.52, 2.50, 2.50, 2.60,
    2.77, 2.70, 2.55, 2.70, 0.45, 0.14, 0.006, 0.008, 0.006, 0.006,
    0.006, 0.006, 0.004, 0.004, 0.004, 0.004, 0.004, 0.004, 0.12, 0.10,
    0.10, 0.18, 0.19, 0.19, 0.70, 2.75, 2.50, 2.80, 2.80, 2.60, 2.55
])


# %%
plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    frecuencia_iir,
    vout_iir,
    marker='o'
)

plt.axvline(
    50,
    linestyle='--',
    label='50 Hz'
)

plt.title('Medición experimental - Filtro IIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('$V_{out}$ [Vpp]')
plt.xlim(48, 52)
plt.grid()
plt.legend()
plt.show()


# %%
# Comparación con la simulación

wp1 = 49.0
wp2 = 51.0
ws1 = 49.5
ws2 = 50.5

sos_iir = sig.iirdesign(
    wp=[wp1, wp2],
    ws=[ws1, ws2],
    gpass=1,
    gstop=60,
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

ganancia_iir_medida = 20 * np.log10(vout_iir / 3)
ganancia_iir_simulada = 20 * np.log10(np.abs(h_iir) + 1e-12)


# %%
plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    w_rad,
    ganancia_iir_simulada,
    color='blue',
    label='Simulación IIR'
)

plt.plot(
    frecuencia_iir,
    ganancia_iir_medida,
    color='orange',
    marker='o',
    label='Medición IIR'
)

plt.axvline(
    50,
    linestyle='--',
    label='50 Hz'
)

plt.title('Comparación entre simulación y medición - IIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Ganancia [dB]')
plt.xlim(48, 52)
plt.ylim(-210, 5)
plt.grid()
plt.legend()
plt.show()
