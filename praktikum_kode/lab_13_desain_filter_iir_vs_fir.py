"""
Laboratorium 13: Desain Filter Digital IIR & Analisis Komparasi FIR vs IIR
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 4, CPMK 5 (CPL-B, CPL-C)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt, firwin, lfilter
import time

def main():
    print("=== LAB 13: KOMPARASI KINERJA FILTER IIR (BUTTERWORTH) VS FIR (HAMMING) ===")
    
    Fs = 2000.0
    Fc = 100.0 # Low-pass Cutoff = 100 Hz
    
    # 1. Filter IIR Butterworth Orde 4 (Format SOS)
    sos_iir = butter(4, Fc, btype='low', fs=Fs, output='sos')
    
    # 2. Filter FIR Window Hamming (Butuh Orde ~61 untuk atenuasi setara)
    h_fir = firwin(61, Fc, window='hamming', fs=Fs)
    
    # Pembangkitan Sinyal Uji Panjang (100,000 sampel)
    N_samples = 100000
    test_signal = np.random.randn(N_samples)
    
    # Uji Waktu Komputasi IIR
    t0 = time.time()
    for _ in range(20):
        y_iir = sosfilt(sos_iir, test_signal)
    t_iir = (time.time() - t0) / 20.0
    
    # Uji Waktu Komputasi FIR
    t0 = time.time()
    for _ in range(20):
        y_fir = lfilter(h_fir, 1.0, test_signal)
    t_fir = (time.time() - t0) / 20.0
    
    print(f"Jumlah Koefisien IIR : 24 koefisien (SOS Biquad)")
    print(f"Jumlah Koefisien FIR : 61 koefisien")
    print(f"Waktu Eksekusi IIR   : {t_iir*1000:.3f} ms")
    print(f"Waktu Eksekusi FIR   : {t_fir*1000:.3f} ms")
    print(f"Rasio Kecepatan IIR  : {t_fir / t_iir:.2f}x Lebih Cepat!")

if __name__ == '__main__':
    main()
