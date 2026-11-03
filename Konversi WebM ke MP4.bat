@echo off
title Konversi Video Kuliah WebM ke MP4 1080p (FFmpeg)
color 0a

echo ========================================================
echo   KONVERSI REKAMAN VIDEO KULIAH WEBM KE MP4 FULL HD
echo   Universitas Nusantara Manado - DSP (Gede Erik Aktama)
echo ========================================================
echo.

set FFMPEG_BIN=D:\Music\Lagu Antigravity\node_modules\ffmpeg-static\ffmpeg.exe

if not exist "%FFMPEG_BIN%" (
    echo [ERROR] ffmpeg.exe tidak ditemukan di %FFMPEG_BIN%
    pause
    exit /b
)

if "%~1"=="" (
    echo [PANDUAN] Cara menggunakan:
    echo Cukup DRAG ^& DROP file video hasil unduhan .webm ke atas file .bat ini!
    echo Atau letakkan file video .webm di folder ini dan jalankan kembali script ini.
    echo.
    set /p INPUT_FILE="Masukkan nama file video (contoh: Pertemuan_01_Video_Kuliah.webm): "
) else (
    set INPUT_FILE=%~1
)

if not exist "%INPUT_FILE%" (
    echo [ERROR] File "%INPUT_FILE%" tidak ditemukan!
    pause
    exit /b
)

set OUTPUT_FILE=%~dpn1_1080p_YouTube.mp4

echo.
echo Mengonversi: "%INPUT_FILE%"
echo Menjadi MP4: "%OUTPUT_FILE%"
echo.
"%FFMPEG_BIN%" -y -i "%INPUT_FILE%" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -c:a aac -b:a 320k "%OUTPUT_FILE%"

if %errorlevel% equ 0 (
    echo.
    echo [SELESAI] Video MP4 berhasil dibuat: "%OUTPUT_FILE%"
) else (
    echo.
    echo [ERROR] Terjadi kegagalan saat konversi.
)

pause

