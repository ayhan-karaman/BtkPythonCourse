"""
    Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
    Alan: πr²
    Çevre: 2πr

    Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
    mil = km / 1.609344
"""
pi = 3.14

r = float(input("Yarı Çap: "))

area = pi * (r ** 2)

perimeter = 1 * pi * r

print("Alan: " + str(area))
print("Çevre: " + str(perimeter))

distance = input("KM: ")

mil = float(distance) / 1.609344
mil = round(mil, 2)

print(distance +  " KM=" + str(mil) + " MIL")

