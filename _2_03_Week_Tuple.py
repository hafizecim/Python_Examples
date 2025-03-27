# Tuple (demet): değiştirilemez (immutable) bir veri yapısıdır ve genellikle aşağıdaki durumlar için kullanılır:
# 1️⃣ elemanlar değiştirilemez
# 2️⃣ ekleme silme işlemi yapılamaz

#Özet:
# Değiştirilemez veri saklama (immutable): Sabit koordinatlar veya sabit kimlik bilgileri.
# Fonksiyonlarda Birden Fazla Değer Döndürme:
# Sözlüklerde anahtar olarak kullanma: Çiftleri anahtar olarak kullanma.
# Veri bütünlüğü sağlama: Veritabanı kayıtları veya kullanıcı bilgileri gibi değişmemesi gereken veriler
# Daha hızlı ve hafif veri yapıları: Değiştirilmeyen küçük veri kümeleri.
# İterasyon ve Paketleme için kullanılır
# Veri yapılarında kullanımı (koordinatlar, RGB, tarih-zaman, vb.).
# Tuple'lar, verilerin değişmemesi gerektiği durumlar için güçlü bir araçtır ve Python'da verimli ve güvenli veri yönetimi sağlar.

"""******** 🔔Tuple Örnek *********"""
# 🍏 Meyve adlarını içeren bir tuple oluşturuyoruz.
meyveler = ("muz", "elma", "armut")  # 📝 Tuple: ("muz", "elma", "armut")

# 🔍 2. indexteki öğeyi yazdırıyoruz (0'dan başlayarak sayılır).
print(meyveler[2])  # armut 🥝 (2. indexteki "armut" öğesini yazdırıyoruz)

# ⚙️ Tuple'ı listeye dönüştürüp, sonra 2. indexteki öğeyi değiştiriyoruz.
b = list(meyveler)  # 🔄 Tuple'ı listeye dönüştürdük: ["muz", "elma", "armut"]
b[2] = "kivi"  # ✂️ 2. indexteki "armut"u "kivi" ile değiştirdik
print(b)  # ['muz', 'elma', 'kivi']  (Değişiklik sonrası liste)

# 🔄 Listeyi tekrar tuple'a dönüştürüyoruz.
meyveler = tuple(b)  # 🧳 Listeyi tekrar tuple'a dönüştürdük: ("muz", "elma", "kivi")
print(meyveler)  # ('muz', 'elma', 'kivi')  (Yeni tuple)

# 🧑‍💻 Küme (set) oluşturuyoruz. Setler sırasız ve indekslenemez.
sayılar = {1, 4, 5, 7, 9}  # Başlangıçta sayıların bulunduğu bir küme

# ➕ Küme'ye 15 sayısını ekliyoruz.
sayılar.add(15)  # Küme sonuna 15 sayısını ekliyoruz
print(sayılar)  # {1, 4, 5, 7, 9, 15}  (15 eklendikten sonra küme)

# 🔄 Küme'ye bir liste ekliyoruz (update metodu ile).
sayılar.update([78, 89])  # Küme'ye 78 ve 89 sayıları ekleniyor
print(sayılar)  # {1, 4, 5, 7, 9, 15, 78, 89}  (Listeyi kümeye ekledik)
## sıralanamaz indexlenemez, döngülerler erişim sağlanır

# ❌ Küme'den 78 sayısını çıkarıyoruz.
sayılar.remove(78)  # Kümeden 78 sayısını siliyoruz
print(sayılar)  # {1, 4, 5, 7, 9, 15, 89}  (78 çıktı)

# 🔀 Kümeden rastgele bir öğe çıkarıyoruz.
sayılar.pop()  # Kümeden rastgele bir öğe çıkartılır (indekslenemez)
print(sayılar)  # Kümeden rastgele bir öğe çıktı (sonuç değişken olabilir) {4, 5, 7, 9, 15, 89} (Bir öğe rastgele çıkarıldı.)

# 🔄 Küme'yi başka bir küme ile güncelliyoruz.
a = {12, 26, 78}  # Yeni bir küme oluşturuyoruz
sayılar.update(a)  # Küme'yi 'a' kümesiyle güncelliyoruz
print(sayılar)  # Küme güncellenmiş olur --> { 4, 5, 7, 9, 15, 89, 12, 26, 78}

# 🧑‍🤝‍🧑 İki kümenin birleşimi (union).
c = sayılar.union(a)  # 'sayılar' ve 'a' kümelerinin birleşimi
print(c)  # { 4, 5, 7, 9, 15, 89, 12, 26, 78}  (Birleşim kümesi)

# 🔎 Kümenin son halini yazdırıyoruz.
print(sayılar)  # Kümenin son hali Çıktı: { 4, 5, 7, 9, 15, 89, 12, 26, 78}
