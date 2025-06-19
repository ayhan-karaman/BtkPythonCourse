# Geçersiz Tanımlar 
"""
1-) Değikenler Rakam ile başlayamaz 
Örnek:/  
    3isim = "Ali"
    4yas = 20 
Yukarıdaki örnekler değişkenlerin hatalı yazımın göstermektedir.
----------------------------------------------------------------------------------------------------------------
2-) Değişkenler içerisinde özel karakterler(,-*/, vs) kullanılamaz yalnızca (alt tire)'_' kullanılabilir.
Örnek:/ 
add?ress = "İstanbul"
department@ = "Developer"

Yukarıdaki örnekler değişkenlerin hatalı yazımın göstermektedir.

-----------------------------------------------------------------------------------------------------------------

3-) Değişken isimleri  Python'un özel anahtar kelimelerinden oluşamaz.
Bu Kelimeler:
    and, as, assert, break, class, continue, def, del, elif, else, except,
    False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal,
    not, or, pass, raise, return, True, try, while, with, yield
    
"""


# Geçerli Tanımlar

# Case Sensitive -> Büyük/Küçük harf duyarlılığı 
# değişkenler küçük büyük harf duyarlıdır. Aşağıdaki değişkenler aslında bir birinden farklı değişkenlerdir
yas = 10 
Yas = 20
YAS = 30
print(yas) # Output: 10
print(Yas) # Output: 20
print(YAS) # Output: 30


# Camel Case
firstName = "Ayhan" # => Kelimenin ilk harfi küçük sonraki kelimelerin ilk harfi büyük yazılır. Bunada camelCase denir.

# Pascal Case
FirstName = "Ali" # Her kelimenin ilk harfi büyük olur bu şekilde de kullanılabilir, kültürel kullanım açısından Camel Case tercih edilir.

# Multiple Assignment(Çoklu Atama)

x, y, z = 100, 200, 300 # Bu değişkenlere `multiple assignment(çoklu atama)` denir.  Sırasıyla; x = 100, y = 200, z = 300 değerlerini alır;

print(x) # Output: 100
print(y) # Output: 200
print(z) # Output: 300


# Chain Assignment(Zincirleme Atama)

a = b = c = 50 # Bu değişkenlere `chain assignment(zincirleme atama)` denir. Her birine ayrı ayrı(a = 50, b=50, c=50) değer atamak yerine tek seferde zincirleme şeklinde değer atanabilir.
print(a) # Output: 50
print(b) # Output: 50
print(c) # Output: 50