import qrcode
import random
import urllib.parse

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
        img.save(f'{number}.png')
    elif img_type == 'jpeg':
        img.save(f'{number}.jpeg')
    else:
        print("Geçersiz dosya türü seçtiniz. Sadece 'png' veya 'jpeg' kabul edilir.")
