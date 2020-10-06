"""
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

sayi = float(input("sayı: ))
result = (sayi > 0) and (sayi <= 100)
print(f"sayı 0-100 arasında mı: {result}")


"""
# sayi = float(input("sayı: "))
# result = (sayi > 0) and (sayi <= 100)
# if (result):
#     print("sayı 0-100 arasındadır.")
# else:
#     print("sayı 0-100 arasında değildir.")


"""

2- Girilem bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi = int(input(sayı: ))
result = (sayi > 0) and (sayi %2 == 0)
print(f"girilen sayı pozitif çift sayı mı: {result}")

"""
# sayi = int(input("sayı: "))
# if(sayi > 0):
# if(sayi % 2 == 0):
#     print("girilen sayı pozitif çift sayıdır.")
# else:
#     print("girilen sayılı pozitif tek sayıdır.")
# else:
#     print("girilen sayı negatiftir.")


"""

3- Email ve parola bilgileri ile giriş kontorlü yapınız.

email = "email@sadikturan.com"
password = "abc123"

girilenEmail = input("email: ")
girilenPassword = input("parola: ")

result = (girilenEmail == email) and (girilenPassword == password)
print(f"uygulamaya giriş başarılı mı: {result}")

"""
# email = "email@sadikturan.com"
# password = "abc123"

# girilenEmail = input("email: ")
# girilenPassword = input("parola: ")

# if(girilenEmail == email):
#     if (girilenPassword == password):
#         print("uygulamaya giriş başarılı.")
#     else:
#         print("parolanız yanlış.")

# else:
#     print("email bilgisi yanlış.")

"""
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

result = (a > b) and (a > c)
print(f"a en büyük sayıdır: {result}")
result = (b > a) and (b > c)
print(f"b en büyük sayıdır: {result}")
result = (c > a) and (c > b)
print(f"c en büyük sayıdır: {result}")

"""
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if (a > b) and (a > c):
#     print("a en büyük sayıdır.")
# elif (b > a) and (b > c):
#     print("b en büyük sayıdır.")
# elif (c > a) and (c > b):
#     print("c en büyük sayıdır.")


"""
5- Kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalama hesaplayınız.
   Eğer ortalama 50 ve üstüyse geçti değilse kaldı yazdırın.
   a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input("vize1: "))
vize2 = float(input("vize2: "))
final = float(input("final: "))

ortalama = ((vize1 + vize2)/2) * 0.6 + (final * 0.4)
result = (ortalama>=50) and (final>=50)
result = (ortalama>=50) or (final>=70)

print(f" öğrencinin ortalaması: {ortalama} ve geçme notu: {result}")

"""
# vize1 = float(input("vize1: "))
# vize2 = float(input("vize2: "))
# final = float(input("final: "))

# ortalama = ((vize1 + vize2)/2) * 0.6 + (final * 0.4)
# result = (ortalama>=50) and (final>=50)
# result = (ortalama>=50) or (final>=70)

# if (ortalama >= 50):
#     if (final >= 50):
#         print("öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarılı.")
#     else:
#         print("öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarısız. Finalden en az 50 almalısınız.")
# else:
#     print("öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarısız")

# if (ortalama >= 50):
#     print("öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarılı.")
# else:
#     if (final >= 70):
#         print("öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarılı. Finalden en az 79 aldığınız için geçtiniz.")
#     else:
#         print("öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarısız.")

"""
6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
   Formül: (kilo / boy uzunluğunun karesi)
   Aşağıdaki tabloya göre kişi hangi gruba girmektedir
   0-18.4 => Zayıf
   18.5-24.9 => Normal
   25.0-29.9 => Fazla Kilolu
   30.0-34.9 => Şişman(Obez)



name = inpyut("adınız: ")
kg = float(input("kilonuz: "))
hg = float(input("boyunuz: "))

index = (kg) / (hg **2)
zayif = (index >= 0) and (index <=18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu = (index > 24.9) and (index <= 29.9)
obez = (index > 29.9) and (index <= 34.9)

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}")

"""

# name = input("adınız: ")
# kg = float(input("kilonuz: "))
# hg = float(input("boyunuz: "))

# index = (kg) / (hg **2 )
# if (index >= 0) and (index <=18.4):
#     print("{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf.")
# elif(index > 18.4) and (index <= 24.9):
#     print("{name} kilo indeksin: {index} ve kilo değerlendirmen normal.")
# elif(index > 24.9) and (index <= 29.9):
#     print("{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu.")
# elif(index > 29.9) and (index <= 34.9):
#     print("{name} kilo indeksin: {index} ve kilo değerlendirmen obez.")
# else:
#     print("bilgileriniz yanlış.")