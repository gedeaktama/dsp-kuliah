"""
Laboratorium 15: Template Framework Proyek Terapan & Validasi Metrik DSP
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 5, CPMK 6 (CPL-B, CPL-C, CPL-D)
"""

import numpy as np

def compute_snr(clean_ref, processed_signal):
    noise = clean_ref - processed_signal
    p_signal = np.mean(clean_ref ** 2)
    p_noise = np.mean(noise ** 2)
    if p_noise < 1e-12: return 999.0
    return 10.0 * np.log10(p_signal / p_noise)

def compute_mse(clean_ref, processed_signal):
    return np.mean((clean_ref - processed_signal) ** 2)

def main():
    print("=== LAB 15: LOGGING METRIK DAN PERBANDINGAN BASELINE PROYEK AKHIR ===")
    
    # Simulasi Ground Truth Sinyal Murni
    N = 1000
    clean = np.sin(np.linspace(0, 20*np.pi, N))
    raw_noisy = clean + 0.6 * np.random.randn(N) # Input SNR rendah
    
    # Metode 1: Baseline Moving Average Sederhana
    filtered_baseline = np.convolve(raw_noisy, np.ones(5)/5.0, mode='same')
    
    # Metode 2: Solusi Rekayasa Mahasiswa (Filter FIR Optimal)
    from scipy.signal import firwin, lfilter
    h = firwin(31, 0.15, window='hamming')
    filtered_proposed = lfilter(h, 1.0, raw_noisy)
    
    snr_in = compute_snr(clean, raw_noisy)
    snr_base = compute_snr(clean, filtered_baseline)
    snr_prop = compute_snr(clean, filtered_proposed)
    
    mse_base = compute_mse(clean, filtered_baseline)
    mse_prop = compute_mse(clean, filtered_proposed)
    
    print(f"{'Metode':<25} | {'SNR (dB)':<10} | {'Delta SNR':<10} | {'MSE':<10}")
    print("-" * 62)
    print(f"{'Input Raw Noisy':<25} | {snr_in:8.2f} dB | {'---':<10} | {compute_mse(clean, raw_noisy):.6f}")
    print(f"{'Baseline Moving Average':<25} | {snr_base:8.2f} dB | {snr_base - snr_in:+6.2f} dB | {mse_base:.6f}")
    print(f"{'Proposed FIR Filter':<25} | {snr_prop:8.2f} dB | {snr_prop - snr_in:+6.2f} dB | {mse_prop:.6f}")
    print("Logging Metrik Proyek Selesai & Terverifikasi!")

if __name__ == '__main__':
    main()
