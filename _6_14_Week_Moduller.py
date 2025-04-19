import math
import numpy
import random as rd # random modülünü rd takma adıyla kullanıyoruz
import _5_01_Week_Fonksiyonlar # kendimiz kütüphene yazmak istersek istediğimiz py dosyasının çağırabilririz
_5_01_Week_Fonksiyonlar.faktoriyel(5) # fonksiyoundan fktöryel heseplayan fonksiyonu çağırdık
_5_01_Week_Fonksiyonlar.yazdir()
_5_01_Week_Fonksiyonlar.toplama(1,4)

from _5_02_Week_Fonksiyonlar_Ornek import ogrenci_bilgi # kısıtlamlaı import etme

math.ceil(54.21) # yuvarlama işlemi
print(math.ceil(54.21))  # yukarı yuvarlama işlemi
print(math.floor(54.21))  # aşağı yuvarlama işlemi
print(math.sqrt(4))  # kare kök alma işlemi
print(math.pow(4,5))  # üs alma işlemi
print(math.log( 1))  # log alama
print(math.log10( 5))  # log alama


print(rd.random()) # 0.0 ile 1.0 arasında rastgele bir ondalıklı sayı üretir
print(rd.uniform(0.5, 8.6)) # Belirtilen aralıkta (0.5 ile 8.6 arasında) rastgele bir ondalıklı sayı üretir
print(rd.randint(45, 80)) # Belirtilen aralıkta (45 ile 80 arasında) rastgele bir tam sayı üretir (her iki sınır dahil)
print(rd.randrange(80)) # 0'dan 80'e kadar (80 hariç) rastgele bir tam sayı üretir

# Liste tanımlıyoruz
l1 = ["ali", "veli", "can", "ayse", "ajda"]

print(rd.choice(l1)) # Listeden rastgele bir eleman seçer (orijinal liste değişmez)
print(rd.shuffle(l1)) # Listeyi yerinde (in-place) rastgele karıştırır, yani sıralamasını değiştirir
print(l1)  # shuffle() sonucu görmek için listeyi yazdırıyoruz
print(rd.sample(l1,3)) # Belirtilen listeden tekrar etmeyen rastgele 3 eleman seçer (orijinal liste bozulmaz)

