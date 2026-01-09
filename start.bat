@echo off
TITLE PDF Birlestirici - Kurulum ve Baslatma

echo ---------------------------------------------------
echo PDF Birlestirici Baslatiliyor...
echo ---------------------------------------------------

:: 1. Python Yüklü mü Kontrolü
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [HATA] Python bilgisayarda yuklu degil veya PATH'e ekli degil!
    echo Lutfen Python'u kurup tekrar deneyin.
    pause
    exit
)

:: 2. VENV Kontrolü ve Kurulumu
if exist "venv" (
    echo [BILGI] Sanal ortam (venv) bulundu.
) else (
    echo [UYARI] Sanal ortam bulunamadi. Olusturuluyor...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [HATA] Venv olusturulamadi!
        pause
        exit
    )
    echo [OK] Venv basariyla olusturuldu.
)

:: 3. VENV Aktivasyonu
call venv\Scripts\activate

:: 4. Kütüphane Kontrolü (Pillow ve natsort var mı?)
:: Basit bir import denemesi yapıyoruz, hata verirse kuracağız.
python -c "import PIL, natsort" >nul 2>&1
if %errorlevel% neq 0 (
    echo [BILGI] Gerekli kutuphaneler eksik. Yukleniyor...
    pip install Pillow natsort
    echo [OK] Kutuphaneler yuklendi.
) else (
    echo [BILGI] Kutuphaneler zaten yuklu.
)

echo ---------------------------------------------------
echo Script Calistiriliyor...
echo ---------------------------------------------------
echo.

:: 5. Python Kodunu Çalıştır
python birlestir.py

echo.
echo Islem tamamlandi.
pause