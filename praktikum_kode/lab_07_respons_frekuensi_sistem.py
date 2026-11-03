"""
Laboratorium 07: Analisis Respons Frekuensi & Group Delay Sistem Diskrit
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 3 (CPL-A, CPL-B)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, group_delay

def main():
    print("=== LAB 07: RESPONS FREKUENSI & GROUP DELAY FILTER DIGITAL ===")
    
    # Bandingkan Moving Average 5-Titik (FIR Linear Phase) vs Lowpass IIR Orde-1
    # Filter 1: Moving Average 5-Tap
    b_fir = np.ones(5) / 5.0
    a_fir = [1.0]
    
    # Filter 2: IIR Low-Pass
    b_iir = [0.2]
    a_iir = [1.0, -0.8]
    
    # Hitung Respons Frekuensi
    w, h_fir = freqz(b_fir, a_fir, worN=1024)
    _, h_iir = freqz(b_iir, a_iir, worN=1024)
    
    # Hitung Group Delay
    _, gd_fir = group_delay((b_fir, a_fir), w=1024)
    
    w_norm = w / np.pi
    
    plt.figure(figsize=(12, 5))
    
    # Magnitude Response (dB)
    plt.subplot(1, 2, 1)
    plt.plot(w_norm, 20 * np.log10(np.abs(h_fir) + 1e-6), 'b-', label='Moving Average 5-Tap (FIR)')
    plt.plot(w_norm, 20 * np.log10(np.abs(h_iir) + 1e-6), 'r--', label='Recursive Lowpass (IIR)')
    plt.title('Magnitude Response (dB)')
    plt.xlabel('Frekuensi w / pi'); plt.ylabel('Gain (dB)'); plt.ylim([-60, 5])
    plt.grid(True, alpha=0.5); plt.legend()
    
    # Group Delay
    plt.subplot(1, 2, 2)
    plt.plot(w_norm, gd_fir, 'b-', lw=2, label='FIR Group Delay = 2.0 Sampel (Konstan!)')
    plt.title('Group Delay FIR: Fase Linier Sempurna Tanpa Distorsi')
    plt.xlabel('Frekuensi w / pi'); plt.ylabel('Keterlambatan (Sampel)')
    plt.ylim([0, 5]); plt.grid(True, alpha=0.5); plt.legend()
    
    plt.tight_layout()
    plt.savefig('output_lab_07.png', dpi=150)
    print("Grafik disimpan sebagai 'output_lab_07.png'.")
    plt.show()

if __name__ == '__main__':
    main()
