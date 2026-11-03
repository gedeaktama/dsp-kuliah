"""
Laboratorium 02: Sekuens Diskrit Elementer & Operasi Transformasi Sinyal
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 1 (CPL-A)
"""

import numpy as np
import matplotlib.pyplot as plt

def unit_impulse(n):
    return np.where(n == 0, 1.0, 0.0)

def unit_step(n):
    return np.where(n >= 0, 1.0, 0.0)

def decompose_even_odd(n, x):
    n_max = max(abs(min(n)), abs(max(n)))
    n_sym = np.arange(-n_max, n_max + 1)
    
    x_sym = np.zeros_like(n_sym, dtype=float)
    idx_map = np.isin(n_sym, n)
    x_sym[idx_map] = x
    
    x_reversed = np.flip(x_sym)
    x_even = 0.5 * (x_sym + x_reversed)
    x_odd = 0.5 * (x_sym - x_reversed)
    return n_sym, x_sym, x_even, x_odd

def main():
    print("=== LAB 02: OPERASI MANIPULASI SEKUENS & DEKOMPOSISI GENAP-GANJIL ===")
    
    # 1. Pembangkitan Sinyal Kausal Uji: x[n] = (0.8)^n u[n] untuk n in [0, 8]
    n = np.arange(0, 9)
    x = (0.8) ** n * unit_step(n)
    
    # 2. Pergeseran Sinyal: y[n] = x[n - 2] (Time Delay)
    n_shifted = n + 2
    
    # 3. Dekomposisi Sinyal Genap-Ganjil
    n_sym, x_full, x_even, x_odd = decompose_even_odd(n, x)
    
    # 4. Verifikasi Energi: E_total == E_even + E_odd
    E_total = np.sum(x_full ** 2)
    E_even = np.sum(x_even ** 2)
    E_odd = np.sum(x_odd ** 2)
    print(f"Energi Total      : {E_total:.6f}")
    print(f"E_even + E_odd    : {E_even + E_odd:.6f}")
    print(f"Selisih Teorema   : {abs(E_total - (E_even + E_odd)):.2e} (Terbukti Presisi!)")
    
    # 5. Visualisasi
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.stem(n, x, basefmt='k-'); plt.title('Sinyal Asli x[n]')
    plt.xlabel('n'); plt.grid(True, alpha=0.5)
    
    plt.subplot(2, 2, 2)
    plt.stem(n_shifted, x, basefmt='k-'); plt.title('Sinyal Tergeser x[n - 2]')
    plt.xlabel('n'); plt.grid(True, alpha=0.5)
    
    plt.subplot(2, 2, 3)
    plt.stem(n_sym, x_even, basefmt='k-'); plt.title('Komponen Genap xe[n]')
    plt.xlabel('n'); plt.grid(True, alpha=0.5)
    
    plt.subplot(2, 2, 4)
    plt.stem(n_sym, x_odd, basefmt='k-'); plt.title('Komponen Ganjil xo[n]')
    plt.xlabel('n'); plt.grid(True, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('output_lab_02.png', dpi=150)
    print("Grafik disimpan sebagai 'output_lab_02.png'.")
    plt.show()

if __name__ == '__main__':
    main()
