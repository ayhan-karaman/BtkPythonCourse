"""
Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın kdv oranı nedir? (%18)

Ayhan Karaman
05321234567
info@ayhankaraman.com
Kocaeli

Satın Alınan Ürünler

Ürün adı: Kablosuz Mouse
Fiyatı: 550 TL

Ürün adı: Kablosuz Klavye
Fiyatı: 650 TL

Ürün adı: Dizüstü Bilgisayar
Fiyatı: 55.000 TL

"""

urun1Ad = "Kablosuz Mouse"
urun1Fiyat = 550

urun2Ad = "Kablosuz Klavye"
urun2Fiyat = 650

urun3Ad = "Dizüstü Bilgisayar"
urun3Fiyat = 55000


kdvOrani = 0.18

subTotal = urun1Fiyat + urun2Fiyat + urun3Fiyat
total = subTotal * kdvOrani



print("Toplam ürün fiyatı: " + str(subTotal))
print("Toplam kdv oranı: " + str(kdvOrani))
print("Toplam ödenecek miktar: " + str(total))


