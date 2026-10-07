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




frecuencia_fir_fase = np.array([
    40.0, 40.1, 40.2, 40.3, 40.4, 40.5
])

retardo_fir = np.array([
    8.8, 16.0, 22.0, 28.4, 35.4, 41.2
])  # ms

retardo_fir_s = retardo_fir / 1000

fase_fir_medida = -2 * np.pi * frecuencia_fir_fase * retardo_fir_s


plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    frecuencia_fir_fase,
    fase_fir_medida,
    marker='o',
    label='Medición FIR'
)

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.title('Desfasaje medido - Filtro FIR')
plt.grid()
plt.legend()
plt.show()


frecuencia_iir_fase = np.array([
    40, 45, 49, 52, 60
])

retardo_iir = np.array([
    51.8, 3.24, 13.2, 7.2, 0.2
])  # ms

retardo_iir_s = retardo_iir / 1000

fase_iir_medida = -2 * np.pi * frecuencia_iir_fase * retardo_iir_s


plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    frecuencia_iir_fase,
    fase_iir_medida,
    marker='o',
    label='Medición IIR'
)

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.title('Desfasaje medido - Filtro IIR')
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

fase_fir_sim = np.unwrap(np.angle(hh_win))

frecuencia_fir_sim = w

fase_fir_sim_medida = np.interp(
    frecuencia_fir_fase,
    frecuencia_fir_sim,
    fase_fir_sim
)

offset_fir = fase_fir_medida[0] - fase_fir_sim_medida[0]
fase_fir_sim_ajustada = fase_fir_sim_medida + offset_fir


plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    frecuencia_fir_fase,
    fase_fir_sim_ajustada,
    marker='o',
    label='Simulación FIR'
)

plt.plot(
    frecuencia_fir_fase,
    fase_fir_medida,
    marker='o',
    label='Medición FIR'
)

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.title('Comparación del desfasaje - FIR')
plt.grid()
plt.legend()
plt.show()



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

fase_iir_sim = np.unwrap(np.angle(h_iir))

frecuencia_iir_sim = w_rad

fase_iir_sim_medida = np.interp(
    frecuencia_iir_fase,
    frecuencia_iir_sim,
    fase_iir_sim
)


plt.figure(figsize=(fig_sz_x, fig_sz_y))

plt.plot(
    frecuencia_iir_fase,
    fase_iir_sim_medida,
    marker='o',
    label='Simulación IIR'
)

plt.plot(
    frecuencia_iir_fase,
    fase_iir_medida,
    marker='o',
    label='Medición IIR'
)

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.title('Comparación del desfasaje - IIR')
plt.grid()
plt.legend()
plt.show()
