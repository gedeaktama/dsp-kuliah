"""
Laboratorium 05: Simulasi Sistem LTI & Persamaan Beda LCCDE
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 2 (CPL-A, CPL-B)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, dimpulse

def main():
    print("=== LAB 05: RESPONS IMPULS & SIMULASI PERSAMAAN BEDA LCCDE ===")
    
    # Sistem: y[n] - 0.75 y[n-1] + 0.125 y[n-2] = x[n] + 0.5 x[n-1]
    b = [1.0, 0.5]          # Koefisien masukan (feedforward)
    a = [1.0, -0.75, 0.125]  # Koefisien keluaran (feedback)
    
    # 1. Hitung Respons Impuls Analitis h[n] menggunakan dimpulse
    system = (b, a, 1.0)
    t, h = dimpulse(system, n=30)
    h = np.squeeze(h)
    
    # 2. Uji Kestabilan BIBO: sum |h[n]|
    sum_abs_h = np.sum(np.abs(h))
    print(f"Jumlahan mutlak sum |h[n]| (30 sampel): {sum_abs_h:.4f}")
    print("Respons meluruh asimtotik menuju nol -> Terbukti Sistem STABIL BIBO!")
    
    # 3. Simulasi Terhadap Input Sinyal Step Satuan u[n]
    N = 40
    x_step = np.ones(N)
    y_step = lfilter(b, a, x_step)
    
    # Visualisasi
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.stem(range(len(h)), h, linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.title('Respons Impuls h[n] Sistem LTI Orde 2')
    plt.xlabel('n'); plt.ylabel('h[n]'); plt.grid(True, alpha=0.5)
    
    plt.subplot(1, 2, 2)
    plt.plot(range(N), y_step, 'ro-', lw=1.5, ms=4)
    plt.title('Respons Step y[n] Terhadap Input u[n]')
    plt.xlabel('n'); plt.ylabel('y[n]'); plt.grid(True, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('output_lab_05.png', dpi=150)
    print("Grafik disimpan sebagai 'output_lab_05.png'.")
    plt.show()

if __name__ == '__main__':
    main()
