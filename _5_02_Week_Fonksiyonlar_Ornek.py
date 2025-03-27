# öğrenciye ait belirisz sayıda not ve adı soy adı gönderilercek 5 sınav notu ortalama
# ad soy ad key values ile notlar tumple ile
print("*********** 1. Yontem *************")
def ogrenci_bilgi(**par):
    for key, val in par.items():
        print("{}:{} ".format(key, val))

ogrenci_bilgi(ad="hafize", soyadi="senyil")

def ogrenci_not(*notlar):
    toplam = 0
    for i in range(len(notlar)):  # i, indeks olarak kullanılmalı
        if i < 5:  # Sadece ilk 5 notu hesaba kat
            toplam += notlar[i]
        else:
            break
    ortalama = toplam / 5  # Sabit 5 sınav üzerinden ortalama alınıyor
    return ortalama

ortalama = ogrenci_not(40, 50, 90, 60, 70)  # 5 not gönderildi
print("ortalama: ",ortalama)

print("*********** 2. Yontem *************")

def ogrenci(*notlar, **bilgi):
    ort=0
    for i in notlar:
        ort+=i
    ort=ort/len(notlar)

    for key, val in bilgi.items():
        print("{}:{} ".format(key, val))
    print("ortalama:", ort )
ogrenci(80,40,60,ad="hafize",soyad="senyil")

