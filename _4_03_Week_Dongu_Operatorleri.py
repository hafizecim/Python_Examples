# Boş bir liste oluşturup 0'dan 5'e kadar sayıları ekleme
sayılar1 = []
for x in range(6):
    sayılar1.append(x)
print(sayılar1)

# Liste üreteci (list comprehension) ile 0'dan 9'a kadar sayıların karelerini alma
sayılar = [x**2 for x in range(10)]
print(sayılar)

# Koşullu liste üreteçleri
sayılar = [x**2 for x in range(10) if x % 2 == 0]
print(sayılar)

sayılar = [a if a % 2 == 0 else 'tek' for a in range(1, 10)]
print(sayılar)

# İç içe liste üretimi
sayılar = [[a, b] for a in range(3) for b in range(2)]
print(sayılar)

# zip kullanımı
l1 = [1, 4, 6, 7, 9]
l2 = ['a', 'b', 'c']
l3 = [4.8, 5.7, 9.1]
a = list(zip(l1, l2, l3))
print(a)

# range kullanımı
liste = list(range(10))
print(liste)

# Matris oluşturma
matris = [[a for a in range(3)] for b in range(2)]
print(matris)

# Matris elemanlarını yazdırma
for i in range(2):
    for j in range(3):
        print(matris[i][j])

# 3x3 matris oluşturma
a = [
    [5, 9, 2],
    [2, 5, 12],
    [4, 3, 6]
]

# Matrisin belirli elemanlarını yazdırma
print(a[2][2])
print(a[1][2])

# Satır toplamlarını hesaplama
for i in range(3):
    satırtop = 0
    for j in range(3):
        satırtop += a[i][j]
    print(f'{i}. satır toplamı: {satırtop}')

# Sütun toplamlarını hesaplama
for i in range(3):
    sutuntop = 0
    for j in range(3):
        sutuntop += a[j][i]
    print(f'{i}. sütun toplamı: {sutuntop}')

# Girilen sayıya kadar olan asal sayıları bulma
sayi = int(input("Bir sayı girin: "))
print(f"{sayi} sayısına kadar olan asal sayılar:")
for i in range(2, sayi + 1):
    asal = True
    for j in range(2, i):
        if i % j == 0:
            asal = False
            break
    if asal:
        print(i, end=" ")
print()  # Yeni satıra geçmek için

# Girilen sayının asal olup olmadığını kontrol etme
sayi = int(input("Sayı giriniz: "))

i = 2
while i <= sayi:
    kontrol = True
    for j in range(2, i):
        if i % j == 0:
            kontrol = False
            break
    if kontrol:
        print(f'{i} asal sayı')
    i += 1


