import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# ==========================================
# TRANSFERENCIA LP
# ==========================================

# Ejemplo:
# T_LP(s) = 1 / (s³ + 2.144625 s² + 1.75063 s + 1.39725)

num_lp = [0.71569]

den_lp = [1,
          1.252906,
          1.534887,
          0.71569]

# ==========================================
# TRANSFERENCIA HP
# ==========================================

# T_HP(s) =
# s³ / [(s+1.596279)(s²+0.548346s+0.875517)]

num_hp = [1,0,0,0]

den_hp = [1,
          2.144625,
          1.75063,
          1.39725]

# ==========================================
# Polos y ceros
# ==========================================

z_lp, p_lp, k_lp = sig.tf2zpk(num_lp, den_lp)

z_hp, p_hp, k_hp = sig.tf2zpk(num_hp, den_hp)

# ==========================================
# Gráfico
# ==========================================

fig, ax = plt.subplots(figsize=(8,8))

# ------------------------
# Polos LP
# ------------------------

ax.plot(np.real(p_lp),
        np.imag(p_lp),
        'x',
        markersize=12,
        label='Polos LP')

# ------------------------
# Polos HP
# ------------------------

ax.plot(np.real(p_hp),
        np.imag(p_hp),
        's',
        markersize=10,
        fillstyle='none',
        label='Polos HP')

# ------------------------
# Ceros HP
# ------------------------

ax.plot(np.real(z_hp),
        np.imag(z_hp),
        'o',
        markersize=10,
        fillstyle='none',
        label='Ceros HP')

# multiplicidad
ax.text(0.05,0.05,'×3',fontsize=14)

# ==========================================
# Círculo unidad
# ==========================================

theta = np.linspace(0,2*np.pi,500)

x = np.cos(theta)
y = np.sin(theta)

ax.plot(x,y,'--',label='Círculo unidad')

# ==========================================
# Formato
# ==========================================

ax.axhline(0,color='black')
ax.axvline(0,color='black')

ax.grid(True)

ax.set_xlabel('Parte real')
ax.set_ylabel('Parte imaginaria')

ax.set_title('Comparación LP vs HP')

ax.legend()

ax.axis('equal')

plt.show()