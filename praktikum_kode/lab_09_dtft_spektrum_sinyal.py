"""
Laboratorium 09: Discrete-Time Fourier Transform (DTFT) & Teorema Parseval
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 3 (CPL-A, CPL-B)
"""

import numpy as np
import matplotlib.pyplot as plt

def dtft(x, n, num_points=1000):
    w = np.linspace(-np.pi, np.pi, num_points)
    # Evaluasi deret jumlahan Fourier numerik
    X = np.dot(np.exp(-1j * np.outer(w, n)), x)
    return w, X

def main():
    print("=== LAB 09: ANALISIS SPEKTRUM DTFT & VALIDASI TEOREMA PARSEVAL ===")
    
    # Sekuens Uji: Sinyal Eksponensial Kausal x[n] = (0.7)^n u[n] (15 sampel)
    N = 15
    n = np.arange(N)
    x = (0.7) ** n
    
    w, X = dtft(x, n, num_points=2000)
    
    # 1. Validasi Teorema Parseval: E_time == E_freq
    E_time = np.sum(x ** 2)
    # Integrasi numerik trapesium pada domain frekuensi
    E_freq = (1.0 / (2 * np.pi)) * np.trapz(np.abs(X) ** 2, w)
    
    print(f"Energi Domain Waktu (sum |x|^2)     : {E_time:.6f}")
    print(f"Energi Domain Frekuensi (Parseval)  : {E_freq:.6f}")
    print(f"Selisih Relatif Numerik             : {abs(E_time - E_freq) / E_time * 100:.4f}%")
    
    # Visualisasi Spektrum Magnitude & Phase
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(w / np.pi, np.abs(X), 'b-', lw=1.5)
    plt.title('Magnitude Spectrum |X(e^jw)| (Karakteristik Low-Pass)')
    plt.xlabel('Frekuensi w / pi'); plt.ylabel('|X(e^jw)|'); plt.grid(True, alpha=0.5)
    
    plt.subplot(1, 2, 2)
    plt.plot(w / np.pi, np.angle(X), 'r-', lw=1.5)
    plt.title('Phase Spectrum angle X(e^jw)')
    plt.xlabel('Frekuensi w / pi'); plt.ylabel('Fase (radian)'); plt.grid(True, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('output_lab_09.png', dpi=150)
    print("Grafik disimpan sebagai 'output_lab_09.png'.")
    plt.show()

if __name__ == '__main__':
    main()
