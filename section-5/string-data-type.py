#🧵 Python'da string (str) Veri Tipi
# 📌 Tanım:
# String, karakterlerin bir araya gelmesiyle oluşan metinsel veri tipidir. 
# Python'da string'ler, 'tek tırnak veya "çift tırnak" ile tanımlanır.

kursAd = "Python programlama kursu"
kursAciklama = 'Güzel Kurs'
kursSuresi = "20 Saat"

msj = "Kurs adı: " + kursAd + " Açıklama: " + kursAciklama + " Süresi: " + kursSuresi

# print(msj)

# Python'da stringler indexleme ile karaterlere erişilebilir.

# msj[-1] şeklinde indexleme yaparsak sağdan sola doğru bir index'leme yapar ve en sağdaki karakteri alır.
""" Örnek """
# print(msj[-1])

# msj[1] şeklinde indexleme yaparsak soldan sağa doğru bir index'leme yapar ve en soldaki karakteri alır.
""" Örnek """
# print(msj[1])