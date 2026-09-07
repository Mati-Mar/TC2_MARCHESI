import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# Datos medidos
# ============================================================

datos = {
    'Frecuencia [Hz]': [20, 40, 57.5, 59.7, 61.9, 64.1, 66.3, 68.5,
                        69.6, 70.7, 72.9, 75.1, 77.3, 79.5, 80.8, 100, 150],

    'Vout [V]': [10, 9.1, 7.1, 6, 5.32, 4.51, 3.64, 5.95,
                 2.83, 3.07, 4, 5.5, 6.48, 7.2, 7.1, 9.27, 9.27],

    'Desfasaje [ms]': [25.2, 13.6, 10, 9.7, 9.3, 8.9, 8.2, 7.3,
                       6.7, 7.5, 7.7, 7.8, 7.6, 7.4, 7.2, 5.5, 3.48]
}

df = pd.DataFrame(datos)

# Mostrar tabla
df

# ============================================================
# Cálculo de ganancia y fase
# ============================================================

Vin = 10       # Vpp
f = df['Frecuencia [Hz]']

# Ganancia lineal
df['|H|'] = df['Vout [V]'] / Vin

# Ganancia en dB
df['|H| [dB]'] = 20 * np.log10(df['|H|'])

# Fase a partir del desfasaje temporal
df['Fase [°]'] = -360 * f * df['Desfasaje [ms]'] * 1e-3

df