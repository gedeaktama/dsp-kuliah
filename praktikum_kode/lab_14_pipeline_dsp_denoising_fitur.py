"""
Laboratorium 14: Arsitektur Pipeline Pengolahan Sinyal End-to-End
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 5 (CPL-B, CPL-C)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt, detrend

class ModularDSPPipeline:
    def __init__(self, Fs=8000.0, bandpass_range=(200, 3200)):
        self.Fs = Fs
        self.sos = butter(4, bandpass_range, btype='bandpass', fs=Fs, output='sos')
        
    def process_frame(self, raw_data):
        # 1. DC Removal & Linear Detrend
        s_clean = detrend(raw_data - np.mean(raw_data))
        # 2. Bandpass SOS Filter
        s_filtered = sosfilt(self.sos, s_clean)
        # 3. Peak Normalization
        s_norm = s_filtered / (np.max(np.abs(s_filtered)) + 1e-9)
        
        # 4. Feature Extraction (ZCR & Energy)
        zcr = np.mean(np.abs(np.diff(np.sign(s_norm)))) / 2.0
        ste = np.mean(s_norm ** 2)
        
        return s_norm, zcr, ste

def main():
    print("=== LAB 14: PIPELINE MODULAR PENGOLAHAN SINYAL WICARA & DETEKSI VAD ===")
    pipe = ModularDSPPipeline(Fs=8000.0)
    
    # Simulasi Sinyal Wicara Sintetis (2 detik)
    Fs = 8000.0
    t = np.linspace(0, 2.0, int(Fs * 2.0))
    # Paket kata pada t=0.3 s.d. 0.8 dan t=1.2 s.d. 1.7
    speech = np.zeros_like(t)
    speech[2400:6400] = np.sin(2 * np.pi * 300 * t[2400:6400]) * 0.8
    speech[9600:13600] = np.sin(2 * np.pi * 450 * t[9600:13600]) * 0.9
    noisy_input = speech + 0.3 * np.random.randn(len(t)) + 1.2 # DC offset + noise
    
    cleaned, zcr, ste = pipe.process_frame(noisy_input)
    print(f"Rata-rata ZCR : {zcr:.4f}")
    print(f"Rata-rata STE : {ste:.4f}")
    print("Pipeline Berjalan Sukses Tanpa Hambatan!")

if __name__ == '__main__':
    main()
