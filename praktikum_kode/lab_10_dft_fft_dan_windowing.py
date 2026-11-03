"""
Laboratorium 10: DFT, Fast Fourier Transform (FFT) & Dekoding DTMF Telepon
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 3, CPMK 5 (CPL-A, CPL-B, CPL-C)
"""

import numpy as np
import matplotlib.pyplot as plt

# Frekuensi Standar DTMF Telepon
DTMF_ROWS = [697, 770, 852, 941]       # Frekuensi Rendah
DTMF_COLS = [1209, 1336, 1477]         # Frekuensi Tinggi
KEYPAD = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

def generate_dtmf_tone(char, Fs=8000, duration=0.2):
    row_idx, col_idx = -1, -1
    for r in range(4):
        for c in range(3):
            if KEYPAD[r][c] == char:
                row_idx, col_idx = r, c; break
    t = np.linspace(0, duration, int(Fs * duration), endpoint=False)
    f_low = DTMF_ROWS[row_idx]
    f_high = DTMF_COLS[col_idx]
    tone = 0.5 * np.sin(2 * np.pi * f_low * t) + 0.5 * np.sin(2 * np.pi * f_high * t)
    return tone, f_low, f_high

def decode_dtmf_fft(tone, Fs=8000):
    N = len(tone)
    # Terapkan Window Hamming untuk meredam spectral leakage
    w = np.hamming(N)
    X = np.fft.fft(tone * w)
    freqs = np.fft.fftfreq(N, 1/Fs)
    
    pos_mask = freqs >= 0
    f_pos = freqs[pos_mask]
    mag = np.abs(X[pos_mask])
    
    # Deteksi frekuensi baris (grup rendah 600-1000 Hz)
    low_band_mask = (f_pos >= 600) & (f_pos <= 1000)
    detected_flow = f_pos[low_band_mask][np.argmax(mag[low_band_mask])]
    closest_row = min(DTMF_ROWS, key=lambda f: abs(f - detected_flow))
    
    # Deteksi frekuensi kolom (grup tinggi 1100-1600 Hz)
    high_band_mask = (f_pos >= 1100) & (f_pos <= 1600)
    detected_fhigh = f_pos[high_band_mask][np.argmax(mag[high_band_mask])]
    closest_col = min(DTMF_COLS, key=lambda f: abs(f - detected_fhigh))
    
    r_idx = DTMF_ROWS.index(closest_row)
    c_idx = DTMF_COLS.index(closest_col)
    return KEYPAD[r_idx][c_idx], closest_row, closest_col, f_pos, mag

def main():
    print("=== LAB 10: DEKODER NADA TELEPON DTMF MENGGUNAKAN FFT ===")
    char_target = '7'
    tone, f_l, f_h = generate_dtmf_tone(char_target)
    
    decoded_char, det_fl, det_fh, freqs, mag = decode_dtmf_fft(tone)
    print(f"Tombol Asli Ditekan   : {char_target} (Frekuensi: {f_l} Hz & {f_h} Hz)")
    print(f"Hasil Dekoding FFT     : {decoded_char} (Terdeteksi: {det_fl} Hz & {det_fh} Hz)")
    print(f"Status Pengenalan      : {'SUKSES 100%' if decoded_char == char_target else 'GAGAL'}")
    
    plt.figure(figsize=(9, 4))
    plt.plot(freqs, mag, 'b-', lw=1.2)
    plt.axvline(f_l, color='r', linestyle='--', label=f'Nada Rendah {f_l} Hz')
    plt.axvline(f_h, color='g', linestyle='--', label=f'Nada Tinggi {f_h} Hz')
    plt.title(f'Spektrum FFT Deteksi DTMF Tombol "{char_target}"')
    plt.xlabel('Frekuensi (Hz)'); plt.ylabel('Magnitude'); plt.xlim([500, 1700])
    plt.grid(True, alpha=0.5); plt.legend()
    plt.tight_layout()
    plt.savefig('output_lab_10.png', dpi=150)
    print("Grafik disimpan sebagai 'output_lab_10.png'.")
    plt.show()

if __name__ == '__main__':
    main()
