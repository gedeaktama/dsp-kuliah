"""
Laboratorium 01: Pengenalan Lingkungan Python, NumPy, Matplotlib & Visualisasi Sinyal
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 1 (CPL-A)
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=== LAB 01: VISUALISASI SINYAL KONTINU VS DISKRIT ===")
    
    # 1. Parameter Sinyal
    F_signal = 5.0     # Frekuensi analog = 5 Hz
    Fs = 40.0          # Frekuensi sampling = 40 Hz (Memenuhi Nyquist Fs > 2*F)
    duration = 1.0     # Durasi waktu pengamatan = 1.0 detik
    
    # 2. Pendekatan Sinyal Analog Kontinu (Grid Waktu Rapat)
    t_analog = np.linspace(0, duration, 1000)
    x_analog = np.sin(2 * np.pi * F_signal * t_analog)
    
    # 3. Pembangkitan Sinyal Diskrit (Sampled)
    n_indices = np.arange(0, int(Fs * duration))
    t_discrete = n_indices / Fs
    omega = 2 * np.pi * (F_signal / Fs) # Frekuensi sudut ternormalisasi (rad/sampel)
    x_discrete = np.sin(omega * n_indices)
    
    print(f"Frekuensi Sinyal       : {F_signal} Hz")
    print(f"Frekuensi Sampling     : {Fs} Hz")
    print(f"Frekuensi Sudut Diskrit: {omega:.4f} rad/sampel ({omega/np.pi:.3f} pi rad/sampel)")
    print(f"Jumlah Sampel Diskrit  : {len(x_discrete)} titik")
    
    # 4. Visualisasi Grafik
    plt.figure(figsize=(12, 5))
    
    # Subplot 1: Sinyal Analog
    plt.subplot(1, 2, 1)
    plt.plot(t_analog, x_analog, 'b-', lw=1.5, label='Analog x(t)')
    plt.title('Representasi Sinyal Kontinu x(t)')
    plt.xlabel('Waktu (detik)'); plt.ylabel('Amplitudo')
    plt.grid(True, linestyle='--', alpha=0.6); plt.legend()
    
    # Subplot 2: Sinyal Diskrit (Stem Plot)
    plt.subplot(1, 2, 2)
    markerline, stemlines, baseline = plt.stem(n_indices, x_discrete, linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.setp(stemlines, 'linewidth', 1.2)
    plt.title(f'Representasi Sinyal Diskrit x[n] (Fs = {Fs} Hz)')
    plt.xlabel('Indeks Sampel n'); plt.ylabel('Amplitudo x[n]')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig('output_lab_01.png', dpi=150)
    print("Grafik berhasil disimpan sebagai 'output_lab_01.png'.")
    plt.show()

if __name__ == '__main__':
    main()
