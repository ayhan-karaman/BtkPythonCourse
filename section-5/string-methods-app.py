courseName = "Btk Akademi Python ile Programlama Dersleri"
webSite = "https://www.btkakademi.gov.tr/"

# 1- ' Btk Akademi ' karakater dizisinin baş ve sondaki boşluk karakterlerini  siliniz.
company = courseName[:13]
print(company)
result1 = company.strip()
print(result1)
# 2- courseName değişkenindeki tüm karakterleri küçük harfe çeviriniz.
result2 = courseName.lower()
print(result2)
# 3- webSite değişkeninde kaç tane '.' karakteri vardır?
result3 = webSite.count('.')
print(result3)
# 4- webSite değişkeni 'https' ile mi başlıyor?
result4 = webSite.startswith('https')
print(result4)
# 5- webSite 'tr' ile mi bitiyor?
result5 = webSite.endswith('tr')
print(result5)
# 6- courseName içerisindeki tüm karakterler harflerden mi oluşuyor?
result6 = courseName.isascii()
print(result6)
# 7- courseName değişkenindeki tüm boşlukları '-' ile değiştiriniz.
result7 = courseName.replace(' ', '-')
print(result7)
# 8- courseName değişkenindeki Python kelimesini ReactJs ile değiştiriniz.
result8 = courseName.replace('Python', 'ReactJs')
print(result8)
# 9- webSite değişkeni 'www' içeriyor mu?
result9 = webSite.count('www') 
result9 = result9 > 0
print(result9)
# 10- courseName değişkenini listeye çeviriniz.
result10 = courseName.split()
print(result10)