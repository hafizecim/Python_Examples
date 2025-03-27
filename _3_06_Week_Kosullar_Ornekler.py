"""a = 45
b = 6
secim = "-"

if secim == "-":
    if a > b:
    print(f"{a}-{b}={a - b}")
else:
    print(f"{b}-{a}={b - a}")"""

print("*********** GİRİŞ *****************")
sifre = "admin"
kullanici = 1234
kullanici_giris = (input("Kullnici adi giriniz: "))
sifre_giris = int(input("Sifre giriniz: "))
if kullanici_giris == kullanici and sifre == sifre_giris:
    print("Kullanici adi ve sifre dogru")
elif kullanici_giris == kullanici or sifre == sifre_giris:
    print("Kullnici adi ve/veya sifre hatali")

print("************** HANGİ SAYİ BUYUK *****************")
sayi1 = int(input("Birici sayiyi giriniz: "))
sayi2 = int(input("İkinci sayiyi giriniz: "))
sayi3 = int(input("Ucuncu sayiyi giriniz: "))

if sayi1 > sayi2 and sayi1 > sayi3:
    print(sayi1, "Birinci sayi buyuktur")
elif sayi2 > sayi1 and sayi2 > sayi3:
    print(sayi2, "Ikinci sayi buyuktur")
elif sayi3 > sayi2 and sayi3 > sayi1:
    print(sayi3, "Ucuncu sayi buyuktur")
else:
    print("Esitlik vardir")
    if (sayi1 == sayi2):
        print(sayi1, ": birinci sayi ve ", sayi2, ": ikinci sayi eşittir ve bu iki sayi büyüktür")
    elif (sayi1 == sayi3):
        print(sayi1, ": birinci sayi ve ", sayi3, ": ucuncu sayi eşittir ve ", sayi3, " sayisi buyuktur")
    elif (sayi2 == sayi3):
        print(sayi2, ": ikinci sayi ve ", sayi3, ": ucuncu sayi eşittir ve ", sayi3, " sayisi buyuktur")

print("**************** HAFR NOTU HESAPLAMA ********************")

vize = int(input("Vize Notu giriniz: "))
final = int(input("Final notu giriniz: "))

ortalama = vize * 0.4 + final * 0.6
print("Ortalama : ", ortalama)

if 0 <= ortalama <= 30:
    print("Harf notumuz FF dir kaldiniz")
elif 30 < ortalama <= 55:
    print("Harf notumuz DD dir kaldiniz")
elif 55 < ortalama <= 70:
    print("Harf notumuz CC dir geçtiniz")
elif 70 < ortalama <= 85:
    print("Harf notumuz BB dir geçtiniz")
elif 85 < ortalama <= 100:
    print("Harf notumuz AA dir geçtiniz")



print("**************** HAFR NOTU HESAPLAMA 2 ********************")

vize_2 = int(input("Vize Notu giriniz: "))
final_2 = int(input("Final notu giriniz: "))

ort = vize_2 * 0.4 + final_2 * 0.6
print("Ortalama : ", ort)

if ort > 100 or ort < 0:
    print("bu aralıkta bir not olamaz")
elif ort >= 86:
    print("AA")
elif ort >= 71:
    print("BB")
elif ort >= 56:
    print("cc")
elif ort >= 31:
    print("dd")
elif ort >= 0:
    print("ff")
