# Şehirler ve onların kodlarını içeren bir sözlük oluşturuluyor 🏙️
iller = {"konya": "42", "ankara": "06"}

# Tüm sözlüğü ekrana yazdırma 📜
print(iller)  # Çıktı: {'konya': '42', 'ankara': '06'}

# "konya" anahtarına karşılık gelen değeri yazdırma 🏷️
print(iller["konya"])  # Çıktı: 42

# "ankara" anahtarına karşılık gelen değeri yazdırma 🏷️
print(iller["ankara"])  # Çıktı: 06

# "konya" anahtarına karşılık gelen değeri get() metodu ile alma 🧐
# get() metodu, anahtar yoksa None döndürür
print(iller.get("konya"))  # Çıktı: 42

# "konya" anahtarının değerini "98" olarak güncelleme 🔄
iller["konya"] = "98"

# "istanbul" anahtarını ve değerini ekleme ➕
iller["istanbul"] = "34"

# "konya" anahtarına ait anahtar-değer çiftini pop() metodu ile kaldırma ❌
iller.pop("konya")

# Alternatif olarak del komutları ile de eleman silinebilir:
# del iller["ankara"]  # Bu, "ankara" anahtarını ve değerini siler
# del iller  # Bu, tüm sözlüğü siler

# popitem() metodu ile son eklenen anahtar-değer çiftini kaldırma ⬇️
iller.popitem()  # Bu, "istanbul" anahtarını ve değerini siler.

# Yapılan işlemlerden sonra sözlüğü yazdırma 📜
print(iller)  # Çıktı: {'ankara': '06'}

# Sözlükteki tüm anahtarları döngü ile yazdırma 🔄
for i in iller.keys():  # Tüm anahtarlar üzerinde gezinme
    print(i)  # Çıktı: 'ankara'  (tek anahtar kaldı)

# *************** ATAMA (  x=y ile x=y.copy()  ) **************
# İlk kod bloğu
a, b = 12, 10  # a'ya 12, b'ye 10 atanıyor
a = b  # a'nın değeri b'nin değeriyle değiştirilir, yani a = 10 olur
b = 6  # b'ye yeni bir değer atanır, yani b = 6 olur
print(a, b)  # Çıktı: 10 6
# Bu çıktıyı alırsınız çünkü a 10'a, b ise 6'ya atanmıştır

# İkinci kod bloğu
x = ["ayse", "fatma"]  # x listesi oluşturuluyor
y = ["ayse", "fatma"]  # y listesi oluşturuluyor
x = y.copy()  # y'nin bir kopyası x'ye atanır, bu x ve y'nin bağımsız hale gelmesini sağlar

y[0] = "kivi"  # y'nin ilk elemanı "kivi" olarak değiştirilir
print(x, y)  # Çıktı: ['ayse', 'fatma'] ['kivi', 'fatma']
# x, y'nin kopyası olduğu için x değişmeden kalır, ancak y'deki değişiklikler x'yi etkilemez


# İkinci kod bloğu
x = ["ayse", "fatma"]  # x listesi oluşturuluyor
y = ["ayse", "fatma"]  # y listesi oluşturuluyor
x = y  # x, y'nin referansını alır, yani x ve y aynı listeyi işaret eder

y[0] = "kivi"  # y'nin ilk elemanı "kivi" olarak değiştirilir
print(x, y)  # Çıktı: ['kivi', 'fatma'] ['kivi', 'fatma']
# Burada x ve y, aynı listeyi işaret ettikleri için y'deki değişiklik x'yi de etkiler.
