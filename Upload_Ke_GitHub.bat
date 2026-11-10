@echo off
title Upload Materi Perkuliahan ke GitHub (dsp-kuliah)
color 0b
echo ========================================================
echo   UPLOAD MATERI DSP KE GITHUB (Universitas Nusantara)
echo ========================================================
echo.
echo Mengunggah seluruh materi ke: https://github.com/gedeaktama/dsp-kuliah.git
echo.
echo Catatan:
echo Jika muncul pop-up jendela otorisasi GitHub di layar:
echo Silakan klik "Sign in with your browser" untuk mengizinkan.
echo.
git push -u origin main --force
echo.
if %errorlevel% equ 0 (
    echo ========================================================
    echo   [BERHASIL] Seluruh materi berhasil diunggah ke GitHub!
    echo ========================================================
    echo Sekarang kembali ke browser Anda di halaman GitHub Pages tadi:
    echo 1. Refresh halaman (F5)
    echo 2. Klik tombol SAVE di sebelah main
    echo 3. Selesai! Website langsung aktif.
) else (
    echo ========================================================
    echo   [PERHATIAN] Terjadi kendala saat upload.
    echo ========================================================
    echo Pastikan komputer terhubung ke internet dan Anda sudah
    echo login ke akun GitHub Anda di browser.
)
echo.
pause
