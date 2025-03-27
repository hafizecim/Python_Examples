sayac=0
while sayac<=100:
    if(sayac%2==0):
        print(sayac)
    sayac+=1

# mükemmel sayi olup olmadığını bulan sayi
# eğer bölenleriinin toplamı kendisine eşit ise
# 6 mükemmel sayidir

sayi = int(input("Bir sayı girin: "))

toplam = 0
i = 1

# While döngüsü ile 1'den sayının yarısına kadar bölenleri kontrol edelim
while i <= sayi // 2:
    if sayi % i == 0:
        toplam += i
    i += 1

# Toplam sayı ile aynıysa mükemmel sayıdır
if toplam == sayi:
    print(sayi ," sayi bir mükemmel sayıdır!")
else:
    print(sayi, " sayi bir mükemmel sayı değildir.")

# break and continue
i=0
while i<5:
    i+=1
    if i==2:
        continue
    print(i)
    if i==4:
        break
    print(i)

#sonsuz dongu True ile olur
top=0
while(True):
    sayi2=int(input("Sayi giriniz cıkış için 0 a basınız"))
    if  sayi2 == 0:
        break
    else:
        top=top+sayi2
print("Toplam:",top)

#************ listeleri ekleme ***********
liste = []
while True:
    liste_gir = input("Sayı giriniz (çıkış için 0'a basınız): ")
    if liste_gir == "0":
        break
    else:
        liste.append(int(liste_gir))
print("Liste:", liste)

sayilar=[]

#başka biryol
while(True):
    sayi3=int(input("sayi giriniz:"))
    if(sayi==0):
        break
    else:
        sayilar.append(sayi3)
print("eklendi")

sayilar.sort()
print(sayilar)


