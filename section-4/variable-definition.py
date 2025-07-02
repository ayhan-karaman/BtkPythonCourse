# Bir önceki dersimizde değişken tanımlama kurallarını öğrendik bu dersde değişkenlere neden ihtiyaç duyulur onu anlamaya çalışacağız.


# Değişkeleri, programda saklamak ve gerektiğinde yeniden kullanmak için kullanırız.
   # Tıpkı bir kutuya isim verip içine bir şey koyup saklamak gibi

# Neden Önemlidir?
# 1-) Verileri tekrar tekrar kullanmak için
# 2-) Hesaplama yaparken ara değerleri tutmak için
# 3-) Kodun anlaşılır ve yönetilebir olması için
# 4-) Kullanıcılar alınan bilgileri korumak(saklamak) için


"""
Seneryo 1
Fiyat bilgilerini farklı sayfalarda kullanıcıya gösterdiğimizi düşünelim.
Her sayfada bu fiyatları tek tek yazmak yerine, değişkenler kullanarak bu bilgileri merkezi bir yerden kontrol edebiliriz.
Bu sayede kod tekrarı azalır ve yönetim kolaylaşır.
"""

"""
Seneryo 2
Diyelim ki ürün fiyatlarında bir güncelleme yapmamız gerekiyor.
Eğer fiyatları her sayfada manuel olarak yazdıysak, tek tek hepsini güncellememiz gerekir.
Ama fiyatlar bir değişkende tanımlıysa, sadece değişkeni güncelleyerek tüm sayfalarda otomatik olarak değişmesini sağlayabiliriz.
"""

"""
Seneryo 3
Birden fazla ürünümüz olduğunu ve bu ürünleri bir sayfada topladığımızı varsayalım. Ayrıca KDV eklememiz de gerekiyor.
Değişken kullanmazsak, her bir ürün için tekrar tekrar matematiksel işlem yapmamız gerekir.
Ancak fiyatları değişkenlerle tanımlarsak, sadece fiyat değişkenini güncelleyerek, matematiksel işlem kısmına dokunmadan tüm hesaplamalar güncel kalır.
"""

# Örnek:/
urunAFiyat = 6000
urunBFiyat = 3000 
kdvOrani = 0.20

print(urunAFiyat + (urunAFiyat * kdvOrani))
print(urunBFiyat + (urunBFiyat * kdvOrani))

urunToplami = urunAFiyat +  urunBFiyat
print(urunToplami + (urunToplami * kdvOrani))