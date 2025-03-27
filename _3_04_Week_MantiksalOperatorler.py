# 🧠 Mantıksal Operatörler: and, or, not
a = 20  # a'ya 20 atanıyor
b = 5   # b'ye 5 atanıyor

# 🟢 AND Operatörü (ve):
# 1 ve 1 = 1
# 1 ve 0 = 0
# 0 ve 0 = 0
print(a > b and a == b)  # a > b doğru (True), a == b yanlış (False) → False

# 🔵 OR Operatörü (veya):
# 1 veya 1 = 1
# 1 veya 0 = 1
# 0 veya 0 = 0
print(a > b or a == b)  # a > b doğru (True) → True

# 🔴 NOT Operatörü (değil):
# a > b doğru (True), not(True) → False
print(not(a > b))  # a > b doğru (True), not(True) False yapar

#******** ORNEK ***************

# 🔢 Kullanıcıdan sayı girmesini istiyoruz
sayi = int(input("Sayı giriniz: "))  # Kullanıcıdan bir tam sayı alıyoruz

# 🟢 AND Operatörü: Hem koşul sağlanmalı (sayı >= 0 ve sayi <= 50)
sonuc = sayi >= 0 and sayi <= 50  # Sayı 0 ile 50 arasında mı?
print(sonuc)  # Sonuç, True veya False olacak

# 🔵 OR Operatörü: Herhangi biri doğru olursa (sayı >= 0 veya sayi <= 50)
sonuc = sayi >= 0 or sayi <= 50  # Sayı ya 0'dan büyük ya da 50'den küçük mü?
print(sonuc)  # Sonuç, True veya False olacak
