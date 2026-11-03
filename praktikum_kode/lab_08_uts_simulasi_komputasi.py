"""
Laboratorium 08: Kasus Ujian Terpadu (UTS) - Analisis Sinyal & Filtering Mandiri
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 1, CPMK 2, CPMK 3 (CPL-A, CPL-B)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz

def main():
    print("=== LAB 08: SIMULASI KASUS UJIAN TERPADU EVALUASI TENGAH SEMESTER (UTS) ===")
    
    # Skenario Soal: Sinyal sensor tercemar interferensi nada dengung 60 Hz pada Fs = 500 Hz
    Fs = 500.0
    N = 250 # Durasi 0.5 detik
    t = np.arange(N) / Fs
    
    # Sinyal bersih: Komponen informasi fisiologis frekuensi rendah 5 Hz
    sig_clean = np.sin(2 * np.pi * 5 * t)
    # Sinyal interferensi noise tajam 60 Hz
    noise = 0.8 * np.sin(2 * np.pi * 60 * t)
    x_noisy = sig_clean + noise
    
    # Rancang Filter FIR Moving Average 7-Titik
    b = np.ones(7) / 7.0
    a = [1.0]
    
    # Terapkan Filter
    y_filtered = lfilter(b, a, x_noisy)
    
    # Hitung SNR Sebelum vs Sesudah
    snr_in = 10 * np.log10(np.mean(sig_clean**2) / np.mean((x_noisy - sig_clean)**2))
    snr_out = 10 * np.log10(np.mean(sig_clean**2) / np.mean((y_filtered - sig_clean)**2))
    
    print(f"SNR Sebelum Pemfilteran : {snr_in:.2f} dB")
    print(f"SNR Setelah Pemfilteran : {snr_out:.2f} dB")
    print(f"Peningkatan Kualitas SNR: {snr_out - snr_in:+.2f} dB")
    
    plt.figure(figsize=(11, 4))
    plt.plot(t, x_noisy, 'lightgray', label='Input Tercemar Noise 60 Hz')
    plt.plot(t, sig_clean, 'g--', lw=1.5, label='Sinyal Bersih Asli (5 Hz)')
    plt.plot(t, y_filtered, 'b-', lw=1.8, label='Output Filter Moving Average')
    plt.title('Evaluasi UTS: Restorasi Sinyal Sensor dari Interferensi Noise')
    plt.xlabel('Waktu (detik)'); plt.ylabel('Amplitudo'); plt.legend(); plt.grid(True, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('output_lab_08.png', dpi=150)
    print("Grafik disimpan sebagai 'output_lab_08.png'.")
    plt.show()

if __name__ == '__main__':
    main()
