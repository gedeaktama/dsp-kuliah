"""
Laboratorium 11: Transformasi-Z, Diagram Pole-Zero & Analisis Kestabilan Sistem
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 3 (CPL-A, CPL-B)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk, freqz

def main():
    print("=== LAB 11: PERANCANGAN FILTER NOTCH 60 HZ DENGAN POLE-ZERO BIDANG-Z ===")
    
    Fs = 600.0  # Frekuensi sampling = 600 Hz
    F_notch = 60.0 # Frekuensi dengung yang dibatalkan = 60 Hz
    w0 = 2 * np.pi * (F_notch / Fs) # w0 = 0.2 pi
    
    # 1. Letakkan Zero tepat pada lingkaran satuan di e^(+- j w0)
    # (z - e^(j w0))(z - e^(-j w0)) = z^2 - 2 cos(w0) z + 1
    # 2. Letakkan Pole tepat di belakang zero pada jari-jari r = 0.95 untuk mempersempit notch
    r = 0.95
    b = [1.0, -2 * np.cos(w0), 1.0]
    a = [1.0, -2 * r * np.cos(w0), r ** 2]
    
    # Hitung Pole dan Zero
    z, p, k = tf2zpk(b, a)
    print("Zero Sistem:", np.round(z, 4))
    print("Pole Sistem:", np.round(p, 4))
    print("Apakah Seluruh Pole di Dalam Lingkaran Satuan (|p| < 1)?", np.all(np.abs(p) < 1.0))
    
    # Hitung Respons Frekuensi
    w, h = freqz(b, a, worN=1024, fs=Fs)
    
    plt.figure(figsize=(12, 5))
    
    # Plot 1: Diagram Pole-Zero
    plt.subplot(1, 2, 1)
    theta = np.linspace(0, 2*np.pi, 200)
    plt.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.5, label='Lingkaran Satuan')
    plt.plot(np.real(z), np.imag(z), 'bo', ms=8, label='Zero (Meredam)')
    plt.plot(np.real(p), np.imag(p), 'rx', ms=10, mew=2, label='Pole (Resonansi)')
    plt.axhline(0, color='gray', lw=0.5); plt.axvline(0, color='gray', lw=0.5)
    plt.title('Diagram Pole-Zero Filter Notch 60 Hz'); plt.axis('equal'); plt.legend(); plt.grid(True, alpha=0.3)
    
    # Plot 2: Respons Frekuensi Notch yang Sangat Tajam
    plt.subplot(1, 2, 2)
    plt.plot(w, 20 * np.log10(np.abs(h) + 1e-6), 'b-', lw=1.5)
    plt.axvline(F_notch, color='r', linestyle='--', label='Cutoff 60 Hz')
    plt.title('Respons Frekuensi: Redaman Sempurna pada Tepat 60 Hz')
    plt.xlabel('Frekuensi (Hz)'); plt.ylabel('Magnitude (dB)'); plt.ylim([-60, 5]); plt.legend(); plt.grid(True, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('output_lab_11.png', dpi=150)
    print("Grafik disimpan sebagai 'output_lab_11.png'.")
    plt.show()

if __name__ == '__main__':
    main()
