title = "Python ile programlama dersleri"


# 1- 'title' değişkeni içerisinde karakater sayısı nedir?
print(f"Title değişkeninde ki karater sayısı:  {len(title)}" )

# 2- 'title' değişkeninde ki Python kelimesini alın.
p = "Python"
result = title[0:len(p)]
print(result)


# 3- 'title' değişkeninde ki ilk 5 ve son 5 karakteri alın
firstFive = title[:5]
lastFive = title[-5:]
print(f"Title değişkenin ilk 5 karakteri -> {firstFive}")
print(f"Title değişkenin son 5 karakteri -> {lastFive}")

# 4- 'title' değişkenini tersten yazdırın.
reverseTitle = title[::-1]
print(f"Title değişkeninin tersden yazılışı -> {reverseTitle}")

# 5- Klavyende girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırın.
     # Örnek/: Çınar isimli öğrencinin 1. notu: 60 2. notu: 60 ve not ortalaması 60 olarak hesaplanmıştır.

studentNameSurname = input("Öğrencinin adı soyadı: ")
firstNote = float(input("Birinci notu: "))
secondNote = float(input("İkinci notu: "))

avarege = (firstNote + secondNote) / 2

print(f"{studentNameSurname} isimli öğrencinin 1. Notu:{firstNote}, 2. Notu:{secondNote} ve Not Ortalaması:{avarege} olarak hesaplanmıştır.")