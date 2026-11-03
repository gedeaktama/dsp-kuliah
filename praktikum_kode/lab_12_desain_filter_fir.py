"""
Laboratorium 12: Perancangan Filter Digital Finite Impulse Response (FIR)
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 4, CPMK 5 (CPL-B, CPL-C)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, lfilter

def main():
    print("=== LAB 12: PEMFILTERAN SINYAL AUDIO DENGAN FILTER FIR WINDOWING ===")
    
    # Parameter Sinyal
    Fs = 8000.0
    duration = 0.5
    t = np.linspace(0, duration, int(Fs * duration), endpoint=False)
    
    # Sinyal suara nada rendah 400 Hz + Derau Peluit Mengganggu 3000 Hz
    s_audio = np.sin(2 * np.pi * 400 * t)
    s_whistle = 0.7 * np.sin(2 * np.pi * 3000 * t)
    raw_noisy = s_audio + s_whistle
    
    # Desain Filter FIR Low-Pass: Cutoff = 1500 Hz, Window = Hamming, 51-Tap
    numtaps = 51
    F_cutoff = 1500.0
    h_fir = firwin(numtaps, cutoff=F_cutoff, window='hamming', fs=Fs)
    
    # Jalankan Pemfilteran
    clean_audio = lfilter(h_fir, 1.0, raw_noisy)
    
    # Evaluasi Spektrum FFT
    N = len(raw_noisy)
    f_axis = np.fft.fftfreq(N, 1/Fs)[:N//2]
    fft_raw = np.abs(np.fft.fft(raw_noisy))[:N//2]
    fft_clean = np.abs(np.fft.fft(clean_audio))[:N//2]
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(t[:150], raw_noisy[:150], 'r-', alpha=0.7, label='Terkontaminasi 3000 Hz')
    plt.plot(t[:150], clean_audio[:150], 'b-', lw=1.8, label='Hasil Filter FIR')
    plt.title('Bentuk Gelombang Waktu Sebelum vs Sesudah')
    plt.xlabel('Waktu (detik)'); plt.ylabel('Amplitudo'); plt.legend(); plt.grid(True, alpha=0.5)
    
    plt.subplot(1, 2, 2)
    plt.plot(f_axis, fft_raw, 'r--', label='Spektrum Input (Ada Spike 3000 Hz)')
    plt.plot(f_axis, fft_clean, 'b-', label='Spektrum Bersih (Spike 3000 Hz Hilang!)')
    plt.title('Spektrum Frekuensi: Peluit 3000 Hz Ditekan Habis')
    plt.xlabel('Frekuensi (Hz)'); plt.ylabel('Magnitude'); plt.legend(); plt.grid(True, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('output_lab_12.png', dpi=150)
    print("Grafik disimpan sebagai 'output_lab_12.png'.")
    plt.show()

if __name__ == '__main__':
    main()
