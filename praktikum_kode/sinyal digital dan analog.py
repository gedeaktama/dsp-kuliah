"""Perbandingan sinyal analog dan digital.

Jalankan dengan: python "sinyal digital dan analog.py"
Memerlukan NumPy dan Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    # Parameter sinyal
    frekuensi = 2.0       # Hz
    amplitudo = 1.0
    fase = 0.0             # radian
    durasi = 1.0            # detik
    frekuensi_sampling = 20.0  # sampel per detik
    jumlah_bit = 3          # resolusi kuantisasi

    # Sinyal analog: waktu dan amplitudo dianggap kontinu.
    waktu_analog = np.linspace(0, durasi, 1000)
    sinyal_analog = amplitudo * np.sin(
        2 * np.pi * frekuensi * waktu_analog + fase
    )

    # Sampling: mengambil nilai sinyal hanya pada waktu tertentu.
    indeks = np.arange(int(durasi * frekuensi_sampling) + 1)
    waktu_sampel = indeks / frekuensi_sampling
    sinyal_sampel = amplitudo * np.sin(
        2 * np.pi * frekuensi * waktu_sampel + fase
    )

    # Kuantisasi: membulatkan amplitudo ke sejumlah level digital.
    jumlah_level = 2**jumlah_bit
    batas_bawah, batas_atas = -amplitudo, amplitudo
    level = np.linspace(batas_bawah, batas_atas, jumlah_level)
    indeks_level = np.rint(
        (sinyal_sampel - batas_bawah)
        / (batas_atas - batas_bawah)
        * (jumlah_level - 1)
    ).astype(int)
    sinyal_digital = level[indeks_level]

    # Tampilkan ringkasan dan beberapa nilai sampel.
    print("PERBEDAAN SINYAL ANALOG DAN DIGITAL")
    print("-" * 60)
    print("Analog : kontinu dalam waktu dan dapat memiliki amplitudo kontinu.")
    print("Digital: direpresentasikan sebagai sampel dengan level amplitudo terbatas.")
    print(f"Frekuensi sinyal     : {frekuensi:g} Hz")
    print(f"Frekuensi sampling   : {frekuensi_sampling:g} sampel/detik")
    print(f"Resolusi kuantisasi  : {jumlah_bit} bit ({jumlah_level} level)")
    print("\n n    waktu (s)   sampel analog   nilai digital")
    for n, t, analog, digital in zip(
        indeks[:10], waktu_sampel[:10], sinyal_sampel[:10], sinyal_digital[:10]
    ):
        print(f"{n:2d}    {t:6.3f}       {analog:8.3f}       {digital:8.3f}")

    # Visualisasi perbandingan.
    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    axes[0].plot(waktu_analog, sinyal_analog, color="royalblue", label="Sinyal analog x(t)")
    axes[0].set_title("Sinyal Analog: kontinu")
    axes[0].set_ylabel("Amplitudo")
    axes[0].grid(True, linestyle="--", alpha=0.5)
    axes[0].legend()

    axes[1].plot(waktu_analog, sinyal_analog, "--", color="lightgray", label="Sinyal analog (acuan)")
    axes[1].stem(
        waktu_sampel,
        sinyal_digital,
        linefmt="tab:orange",
        markerfmt="o",
        basefmt=" ",
        label=f"Sinyal digital ({jumlah_bit} bit)",
    )
    axes[1].set_title("Sinyal Digital: diskrit dalam waktu dan level amplitudo")
    axes[1].set_xlabel("Waktu (detik)")
    axes[1].set_ylabel("Amplitudo")
    axes[1].grid(True, linestyle="--", alpha=0.5)
    axes[1].legend()

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
