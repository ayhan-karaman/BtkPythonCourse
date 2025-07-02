# Python'da veri tipi dönüşümleri(type conversions/type casting), 
# bir veri tipinden başka bir veri tipine dönüşüm işlemidir. 
# Python'da bu işlem genellikle yerleşik fonksiyonlarla yapılır.

# 1.) int() -> Tamsayıya dönüştürme
x = int("42") # string -> int
y = int(3.9)  # float -> int(kesir atılır)

# 2.) float() -> Ondalıklı sayıya dönüştürme
x = float("3.14") # string -> float
y = float(7)      # int -> float 

# 3.) str() -> Metne dönüştürme
x = str(123)   # int -> string
y = str(3.14)  # float -> string

# Örnek

number1 = int(input("Sayı 1: ")) # Kullanıcının girdiği sayısal string olarak alınır burada dönüştürme işlemi yapılarak sayısal değer int değerine döndürülür.
number2 = int(input("Sayı 2: ")) # Kullanıcının girdiği sayısal string olarak alınır burada dönüştürme işlemi yapılarak sayısal değer int değerine döndürülür.

total = number1 + number2

print(total)

# type()  Tip Kontrolü
x = True 
print(type(x)) # Yukardı değişkenin veri tipini öğrenmek için type() fonksiyonu kullanırız.
print(x)