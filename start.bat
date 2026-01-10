

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