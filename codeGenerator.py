import qrcode
import random
import urllib.parse
import os
import time

number = random.randint(100000, 9000000)

qr_link = input("QR Kod oluşturmak istediğiniz Linki yazın: ")

parsed_url = urllib.parse.urlparse(qr_link)
if not parsed_url.scheme or not parsed_url.netloc:
    print("Hata: Geçerli bir URL girilmedi. Lütfen bir URL girin.")
else:
    img_type = input("Dosya türünü seçin (png veya jpeg): ").lower()

    data = f'{qr_link}{number}'
    img = qrcode.make(data)
    
    if img_type == 'png':
        img_file = f'{number}.png'
        img.save(img_file)
    elif img_type == 'jpeg':
        img_file = f'{number}.jpeg'
        img.save(img_file)
    else:
        print("Geçersiz dosya türü seçtiniz. Sadece 'png' veya 'jpeg' kabul edilir.")
    
    print(f"{img_file} dosyası oluşturuldu ve 10 saniye sonra silinecek.")
    os.system(f'start {img_file}')
    time.sleep(10)
    os.system('taskkill /F /FI "IMAGENAME eq Microsoft.Photos.exe"')
    os.remove(img_file)  
