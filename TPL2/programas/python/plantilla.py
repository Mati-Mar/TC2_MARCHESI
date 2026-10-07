import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
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

plt.figure(figsize=(fig_sz_x / 1.2, fig_sz_y / 1.5))
plt.axis([40, 60, -70, 5])

plot_plantilla(
    filter_type='bandstop',
    fpass=(wp1, wp2),
    fstop=(ws1, ws2),
    ripple=ripple,
    attenuation=atenuacion,
    fs=fs
)

plt.title('Filtro plantilla')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.grid()
plt.legend()
plt.show()
