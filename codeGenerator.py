import qrcode
import random
import urllib.parse
import os
import base64

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
    os.system(f'start {img_file}')

    with open(img_file, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    print(my_string)
    
    
