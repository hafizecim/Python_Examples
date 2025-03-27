#************ FOR DONGUSU **************
sayilar=[1,8,7,4,5] # liste kullanımı
print(sayilar[4])
for sayi in sayilar:
    print(sayi)

adlar=("ayse", "fatma" , "ali") # tuple (demet)
for ad in adlar:
    print(ad)

iller={'konya':42,'ankara':6} # sözlük kullanımı
for a,b in iller.items():
    print(a,b)

adres="Seydisehir/Konya" # string kullanımı
for c in adres:
    print(c)

ogrenciler=[["ayse", "avci", 40, 60, 70], ["ali", "can", 30, 50, 80]]
print(ogrenciler[0][2])
for ogrenci in ogrenciler:
   # ort= print(ogrenci[2]+ogrenci[3]+ogrenci[4])/3
   # print(ogrenci[0],ogrenci[1],ort)
    print(ogrenci[3])

for j in range(100): # belli bir aralıktaki sayıları döndürüyor
    print(j)

for j in range(50,100,5): # 50 den başla 100 kadar 5 er 5 er attırarak git
    print(j)

#************** Meyve Örneği ************
urunler = [
    {"ad": "elma", "fiyat": 50},
    {"ad": "armut", "fiyat": 40},
    {"ad": "cilek", "fiyat": 100},
    {"ad": "kiraz", "fiyat": 80},
    {"ad": "mandalina", "fiyat": 70}
]
en_pahali_meyve = urunler[0]
for meyve in urunler:
    if meyve["fiyat"] > en_pahali_meyve["fiyat"]:
        en_pahali_meyve = meyve
print("En pahali meyve: ", en_pahali_meyve['ad'], "Fiyat: ", en_pahali_meyve['fiyat'])

toplam_fiyat=0
for toplam in urunler:
    #toplam_fiyat= toplam["fiyat"]+toplam_fiyat
    toplam_fiyat+=toplam["fiyat"]
print("Toplam:", toplam_fiyat)