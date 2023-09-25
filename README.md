
# Qr Kod Oluşturucu

Proje kişinin: istediği doğrultuda qr kod oluşturmasını sağlar.


## Kullanım/Örnekler

```python
import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
```

  
## Bilgisayarınızda Çalıştırın

Projeyi klonlayın

```bash
  git clone https://github.com/bunshiin/qr-code-generator.git
```



Gerekli paketleri yükleyin

```bash
pip install qrcode
```



  
![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png)

    
