import os
from PIL import Image, ImageFile
from natsort import natsorted

# Yarım inmiş dosyaları okumaya zorla
ImageFile.LOAD_TRUNCATED_IMAGES = True

img_folder = "images"
output_pdf_name = "sonuc_dosyasi.pdf"

print(f"'{img_folder}' klasörü taranıyor...")

if not os.path.exists(img_folder):
    print("HATA: Klasör bulunamadı.")
    exit()

dosyalar = []
for f in os.listdir(img_folder):
    if f.upper().startswith("IMG_"):
        dosyalar.append(f)

sirali_dosyalar = natsorted(dosyalar)

if not sirali_dosyalar:
    print("HATA: Dosya bulunamadı!")
    exit()

print(f"Toplam {len(sirali_dosyalar)} dosya bulundu. Temizlenerek belleğe alınıyor...")

imagelist = []
first_image = None 

# RAM şişmemesi için resimleri optimize ederek açacağız
for i, dosya_adi in enumerate(sirali_dosyalar):
    tam_yol = os.path.join(img_folder, dosya_adi)
    
    try:
        # 1. Resmi aç
        img = Image.open(tam_yol)
        
        # 2. Renk modunu RGB yap
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # 3. SİHİRLİ DOKUNUŞ: Resmi sıfır bir tuvale kopyala
        # Bu işlem dosyanın bozuk metadata/header bilgilerini siler.
        clean_img = Image.new("RGB", img.size)
        clean_img.paste(img)
        
        # 4. Listeye ekle
        if first_image is None:
            first_image = clean_img
        else:
            imagelist.append(clean_img)
            
        # İlerleme çubuğu
        if i % 20 == 0:
            print(f"Temizlenen: {i+1}/{len(sirali_dosyalar)}")
            
    except Exception as e:
        print(f"\nATLANDI: {dosya_adi} - Sebep: {e}")

print("-" * 30)

if first_image:
    print(f"Tüm dosyalar temizlendi. PDF yazılıyor (Bu işlem birkaç saniye sürebilir)...")
    try:
        # Kaydederken 'JPEG' formatını zorlamıyoruz, Pillow kendi halletsin
        first_image.save(
            output_pdf_name, 
            "PDF", 
            resolution=100.0, 
            save_all=True, 
            append_images=imagelist
        )
        print(f"\n✅ BAŞARILI! '{output_pdf_name}' oluşturuldu.")
    except Exception as e:
        print(f"❌ Kaydetme hatası: {e}")
else:
    print("PDF oluşturulacak görüntü yok.")

input("\nÇıkmak için Enter'a bas...")