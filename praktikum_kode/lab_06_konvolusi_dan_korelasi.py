"""
Laboratorium 06: Konvolusi Diskrit & Estimasi Time-Delay dengan Cross-Correlation
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 2 (CPL-A, CPL-B)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

def main():
    print("=== LAB 06: KONVOLUSI DISKRIT & DETEKSI GEMA RADAR (CROSS-CORRELATION) ===")
    
    # 1. Pembangkitan Pulsa Radar Pantulan
    np.random.seed(42)
    N_pulse = 40
    pulse = np.sin(2 * np.pi * 0.1 * np.arange(N_pulse)) * np.hanning(N_pulse)
    
    # Buat Sinyal Penerima dengan Delay Sejati D = 65 sampel + Noise Kuat
    D_true = 65
    N_total = 200
    received = np.zeros(N_total)
    received[D_true : D_true + N_pulse] = 0.8 * pulse
    # Tambahkan noise acak (SNR ~ 0 dB)
    received += 0.5 * np.random.randn(N_total)
    
    # 2. Hitung Cross-Correlation r_xy
    r_xy = correlate(received, pulse, mode='full')
    lags = np.arange(-len(pulse) + 1, len(received))
    
    # 3. Estimasi Delay dari Puncak Tertinggi (Peak Detection)
    peak_idx = np.argmax(r_xy)
    estimated_delay = lags[peak_idx]
    
    print(f"Delay Sejati (True Delay)      : {D_true} sampel")
    print(f"Delay Terestimasi (Correlation): {estimated_delay} sampel")
    print(f"Akurasi Deteksi                : {abs(D_true - estimated_delay) == 0} (100% Tepat!)")
    
    # Visualisasi
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(received, 'b-', alpha=0.7, label='Sinyal Radar Pantulan Tertutup Noise')
    plt.axvline(D_true, color='g', linestyle='--', label=f'Posisi Asli Target (n={D_true})')
    plt.title('Sinyal Masukan Radar Penerima (Sulit Melihat Target Secara Visual)')
    plt.xlabel('Indeks Sampel n'); plt.ylabel('Amplitudo'); plt.legend(); plt.grid(True, alpha=0.4)
    
    plt.subplot(2, 1, 2)
    plt.plot(lags, r_xy, 'r-', lw=1.5, label='Cross-Correlation r_xy[l]')
    plt.axvline(estimated_delay, color='k', linestyle=':', label=f'Puncak Deteksi (Lag={estimated_delay})')
    plt.title('Kurva Korelasi Silang: Puncak Tajam Mengunci Target Secara Sempurna!')
    plt.xlabel('Lag l'); plt.ylabel('Nilai Korelasi'); plt.legend(); plt.grid(True, alpha=0.4)
    
    plt.tight_layout()
    plt.savefig('output_lab_06.png', dpi=150)
    print("Grafik disimpan sebagai 'output_lab_06.png'.")
    plt.show()

if __name__ == '__main__':
    main()
