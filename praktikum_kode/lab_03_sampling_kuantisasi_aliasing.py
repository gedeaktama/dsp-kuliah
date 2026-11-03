"""
Laboratorium 03: Sampling, Kuantisasi, Rekonstruksi & Aliasing
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 1 (CPL-A)
"""

import numpy as np
import matplotlib.pyplot as plt

def quantize_signal(x, bit_depth, v_min=-1.0, v_max=1.0):
    L = 2 ** bit_depth
    delta = (v_max - v_min) / L
    # Normalisasi ke indeks level kuantisasi
    q_index = np.round((x - v_min) / delta)
    q_index = np.clip(q_index, 0, L - 1)
    x_q = v_min + q_index * delta
    return x_q, delta

def main():
    print("=== LAB 03: SIMULASI SAMPLING, ALIASING & KUANTISASI B-BIT ===")
    
    # 1. Demonstrasi Aliasing Frekuensi Lipat
    F_signal = 70.0    # Frekuensi analog = 70 Hz
    Fs = 100.0         # Frekuensi sampling = 100 Hz (Nyquist Rate = 140 Hz, terjadi Aliasing!)
    t_end = 0.2
    
    t_dense = np.linspace(0, t_end, 1000)
    x_dense = np.cos(2 * np.pi * F_signal * t_dense)
    
    n = np.arange(0, int(Fs * t_end))
    t_sampled = n / Fs
    x_sampled = np.cos(2 * np.pi * F_signal * t_sampled)
    
    # Hitung Frekuensi Semu Hasil Aliasing: |70 - 100| = 30 Hz
    F_alias = abs(F_signal - Fs)
    x_alias_curve = np.cos(2 * np.pi * F_alias * t_dense)
    
    print(f"Frekuensi Asli  : {F_signal} Hz")
    print(f"Frekuensi Nyquist: {Fs/2} Hz")
    print(f"Frekuensi Semu  : {F_alias} Hz (Tampak seolah-olah gelombang 30 Hz!)")
    
    # 2. Simulasi Kuantisasi 3-Bit vs 8-Bit
    x_q3, delta3 = quantize_signal(x_dense, bit_depth=3)
    error_q3 = x_q3 - x_dense
    sqnr_theory_3bit = 6.02 * 3 + 1.76
    sqnr_meas_3bit = 10 * np.log10(np.mean(x_dense**2) / np.mean(error_q3**2))
    
    print(f"SQNR Teoretis 3-bit : {sqnr_theory_3bit:.2f} dB")
    print(f"SQNR Terukur 3-bit  : {sqnr_meas_3bit:.2f} dB")
    
    # Visualisasi
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(t_dense, x_dense, 'lightgray', lw=2, label='Sinyal Asli 70 Hz')
    plt.plot(t_dense, x_alias_curve, 'r--', lw=1.5, label='Frekuensi Semu 30 Hz (Aliased)')
    plt.stem(t_sampled, x_sampled, linefmt='b-', markerfmt='bo', basefmt='k-', label='Sampel Diskrit Fs=100Hz')
    plt.title('Fenomena Aliasing: 70 Hz Menyamar Menjadi 30 Hz')
    plt.xlabel('Waktu (detik)'); plt.ylabel('Amplitudo'); plt.legend(); plt.grid(True, alpha=0.5)
    
    plt.subplot(1, 2, 2)
    plt.plot(t_dense[:200], x_dense[:200], 'b-', label='Analog Murni')
    plt.step(t_dense[:200], x_q3[:200], 'r-', where='mid', label='Terkuantisasi 3-bit (8 Level)')
    plt.title('Efek Kuantisasi Amplitudo Kasar (3-Bit)')
    plt.xlabel('Waktu (detik)'); plt.ylabel('Amplitudo'); plt.legend(); plt.grid(True, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('output_lab_03.png', dpi=150)
    print("Grafik disimpan sebagai 'output_lab_03.png'.")
    plt.show()

if __name__ == '__main__':
    main()
