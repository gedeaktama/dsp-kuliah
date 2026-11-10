# 💻 Modul Praktikum Komputasi Python — Pengolahan Sinyal Digital (DSP)

**Fakultas Ilmu Komputer, Universitas Nusantara Manado**  
**Dosen Pengampu:** Gede Erik Aktama, S.Pd., M.Pd. (NIDN: 0902109201)  
**Kurikulum:** Outcome-Based Education (OBE) & Standar Industri  

---

## 🚀 Panduan Menjalankan Kode Praktikum

Seluruh script dibuat modular menggunakan bahasa Python 3.9+ dengan pustaka standar komputasi ilmiah (`numpy`, `scipy`, `matplotlib`, `soundfile`).

### 1. Persiapan Lingkungan (Terminal / CMD / VS Code)
Pastikan Python sudah terpasang di komputer Anda, lalu jalankan:
```bash
pip install numpy scipy matplotlib soundfile
```

### 2. Menjalankan Modul Praktikum
Masuk ke direktori `praktikum_kode/` dan eksekusi skrip modul yang diinginkan:
```bash
python lab_01_pengenalan_sinyal_python.py
```

---

## 📚 Daftar Lengkap 15 Modul Praktikum

| No | File Skrip | Topik Praktikum | Pemetaan CPMK |
|---|---|---|---|
| 01 | `lab_01_pengenalan_sinyal_python.py` | Pengenalan Python, NumPy, Matplotlib & Visualisasi Sinyal Diskrit | CPMK 1 (CPL-A) |
| 02 | `lab_02_sinyal_diskrit_dan_operasi.py` | Sekuens Diskrit Elementer & Operasi Transformasi Sinyal | CPMK 1 (CPL-A) |
| 03 | `lab_03_sampling_kuantisasi_aliasing.py` | Sampling, Kuantisasi B-Bit, Rekonstruksi & Fenomena Aliasing | CPMK 1 (CPL-A) |
| 04 | `lab_04_pengujian_sifat_sistem.py` | Pengujian Empiris & Formal Sifat Sistem Waktu Diskrit (Linearitas & Time-Invariance) | CPMK 2 (CPL-A, CPL-B) |
| 05 | `lab_05_sistem_lti_dan_respons_impuls.py` | Simulasi Sistem LTI & Persamaan Beda LCCDE | CPMK 2 (CPL-A, CPL-B) |
| 06 | `lab_06_konvolusi_dan_korelasi.py` | Konvolusi Diskrit & Estimasi Time-Delay dengan Cross-Correlation | CPMK 2 (CPL-A, CPL-B) |
| 07 | `lab_07_respons_frekuensi_sistem.py` | Analisis Respons Frekuensi & Group Delay Sistem Diskrit | CPMK 3 (CPL-A, CPL-B) |
| 08 | `lab_08_uts_simulasi_komputasi.py` | Kasus Terpadu UTS: Analisis Sinyal & Filtering Mandiri | CPMK 1, 2, 3 (CPL-A, CPL-B) |
| 09 | `lab_09_dtft_spektrum_sinyal.py` | Discrete-Time Fourier Transform (DTFT) & Teorema Parseval | CPMK 3 (CPL-A, CPL-B) |
| 10 | `lab_10_dft_fft_dan_windowing.py` | Fast Fourier Transform (FFT), Windowing & Dekoding Nada DTMF | CPMK 3, 5 (CPL-A, B, C) |
| 11 | `lab_11_ztransform_dan_pole_zero.py` | Transformasi-Z, Diagram Pole-Zero & Kestabilan Sistem | CPMK 3 (CPL-A, CPL-B) |
| 12 | `lab_12_desain_filter_fir.py` | Perancangan Filter Digital Finite Impulse Response (FIR Windowing) | CPMK 4, 5 (CPL-B, CPL-C) |
| 13 | `lab_13_desain_filter_iir_vs_fir.py` | Desain Filter Digital IIR Butterworth (SOS) vs Analisis FIR | CPMK 4, 5 (CPL-B, CPL-C) |
| 14 | `lab_14_pipeline_dsp_denoising_fitur.py` | Arsitektur Pipeline Pengolahan Sinyal End-to-End Berbasis OOP | CPMK 5 (CPL-B, CPL-C) |
| 15 | `lab_15_proyek_terapan_dsp_audio_sensor.py` | Template Framework Proyek Terapan & Validasi Metrik Objektif (SNR/MSE) | CPMK 5, 6 (CPL-B, C, D) |

---
**Kembali ke Portal Kuliah:** Buka file `index.html` di direktori utama atau buka [dsp-kuliah](https://github.com/gedeaktama/dsp-kuliah).

