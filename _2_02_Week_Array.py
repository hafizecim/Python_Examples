#📌 list, tuple, set, dictionary
#📝 list özellikleri
# 1️⃣ sıralanbilir
# 2️⃣ güncelenebilir
# 3️⃣ arama yapabilrir
# 4️⃣tekrarlayan elemanlardan oluşabilir

# 📌 Karışık veri türlerine sahip bir liste tanımlıyoruz
liste = ["ayse", 5, "fatma", 45.8, True, [1, 7, 8]]

# 📝 Listenin 2. indeksindeki öğeyi yazdır (0'dan başladığı için 3. öğe)
print(liste[2])  # ➡️ "fatma"

# 🔢 Listenin 5. indeksindeki listenin 1. indeksindeki öğeyi yazdır
print(liste[5][1])  # ➡️ 7

# 📏 Listenin uzunluğunu (eleman sayısını) bul
print(len(liste))  # ➡️ 6

# 🔄 4. indeksdeki değeri değiştiriyoruz (True → False)
liste[4] = False
print(liste)  # ➡️ ["ayse", 5, "fatma", 45.8, False, [1, 7, 8]]

# 🔄 Liste içindeki 5. öğedeki iç listeyi değiştiriyoruz (iç liste [1, 7, 8] kısmında 3. elemanı 15 yapıyoruz).
liste[5][2] = 15

# 📝 Listeyi yazdırır.
print(liste)  # ➡️['ayse', 5, 'fatma', 45.8, True, [1, 7, 15]]

# 🔢 İlk üç öğeyi yazdırır.
print(liste[0:3])  # ➡️['ayse', 5, 'fatma']

# 🔄 İkinci indexten sonrasını yazdırır.
print(liste[2:])  # ➡️['fatma', 45.8, True, [1, 7, 15]]

# 🔙 Son üç öğeden ikincisini (geri sayarak) yazdırır. ani burada -3 (başlangıç) ve -1 (bitiş, dahil değil) arasındaki elemanları alır.
print(liste[-3:-1])  # ➡️[45.8, True]


"""******** 🔔YENİ LİSTE ÖRNEK ********"""
# 🚗 Arabalar adında bir liste oluşturuyoruz ve içine araba modelleri ekliyoruz.
arabalar = ["BMW", "Audi", "Mercedes", "Tesla", "Toyota"]  # 📝 Listeyi tanımladık

# 📝 Listeyi yazdırıyoruz.
print(arabalar)  # ['BMW', 'Audi', 'Mercedes', 'Tesla', 'Toyota']

# 🔢 Liste içindeki ilk arabayı yazdırıyoruz.
print(arabalar[0])  # BMW  (0. indexten ilk öğe)

# 🔢 Liste içindeki son arabayı yazdırıyoruz.
print(arabalar[-1])  # Toyota  (Son öğe -1 ile belirtilir)

# 🔄 Listenin ilk üç arabasını yazdırıyoruz.
print(arabalar[0:3])  # ['BMW', 'Audi', 'Mercedes']  (0. indexten 3. indexten bir önceki öğeye kadar)

# 🔄 Listenin 2. indexten sonrasını yazdırıyoruz.
print(arabalar[2:])  # ['Mercedes', 'Tesla', 'Toyota']  (2. indexten başlayıp sonrasını yazdırıyoruz)

# 🔄 Listeyi tersine çevirip yazdırıyoruz.
print(arabalar[::-1])  # ['Toyota', 'Tesla', 'Mercedes', 'Audi', 'BMW']  (Listeyi tersten yazdırır)

# ✨ Listeye yeni bir araba modeli ekliyoruz.
arabalar.append("Honda")  # 🚙 Yeni araba ekledik
print(arabalar)  # ➡️['BMW', 'Audi', 'Mercedes', 'Tesla', 'Toyota', 'Honda']  (Yeni araba eklenmiş)

# 🔹 Listeye belirli bir yere araba ekliyoruz (örneğin 2. indexe "Porsche").
arabalar.insert(2, "Porsche")  # 🚗 "Porsche"yi 2. indexe ekledik
print(arabalar)  # ➡️['BMW', 'Audi', 'Porsche', 'Mercedes', 'Tesla', 'Toyota', 'Honda']  ("Porsche" 2. indexte)

# ✂️ Listeyi bir arabaya kadar kesiyoruz (ilk 4 araba).
print(arabalar[:4])  # ➡️['BMW', 'Audi', 'Porsche', 'Mercedes']  (4. index dahil edilmez)

# 🔢 Liste elemanlarının sayısını yazdırıyoruz.
print(len(arabalar))  # ➡️7  (Listeye toplamda 7 araba eklendi)

# 📝 3. arabayı (index 2) değiştiriyoruz.
arabalar[2] = "Lexus"  # 🚗 3. arabayı Lexus olarak değiştirdik
print(arabalar)  # ➡️['BMW', 'Audi', 'Lexus', 'Mercedes', 'Tesla', 'Toyota', 'Honda']  (3. araba değiştirildi)

# ❌ Liste içindeki bir arabayı `del` komutuyla siliyoruz (örneğin, 2. indexteki Lexus).
del arabalar[2]  # 🗑️ Lexus'u listeden sildik
print(arabalar)  # ➡️['BMW', 'Audi', 'Mercedes', 'Tesla', 'Toyota', 'Honda']  (Lexus silindi)

# ✂️ Listenin son öğesini siliyoruz (pop ile).
silinen_araba = arabalar.pop()  # 🚗 Son arabayı sildik ve sakladık
print(silinen_araba)  # ➡️Honda  (Silinen araba)
print(arabalar)  # ➡️['BMW', 'Audi', 'Mercedes', 'Tesla', 'Toyota']  (Son araba silindi)

# ✂️ Belirli bir öğeyi (index 1'deki Audi'yi) `remove` ile siliyoruz.
arabalar.remove("Audi")  # 🗑️ Audi'yi listeden sildik
print(arabalar)  # ➡️['BMW', 'Mercedes', 'Tesla', 'Toyota']  (Audi silindi)

# 📝 Listeyi tamamen temizliyoruz.
arabalar.clear()  # 🧹 Listeyi tamamen temizledik
# 📝 Temizlenmiş listeyi yazdırıyoruz.
print(arabalar)  # ➡️[]  (Liste boş oldu)


"""******** 🔔YENİ ÖRNEK ********"""

# 🚗 Arabalar adında bir liste oluşturuyoruz ve içine bazı araba modelleri ekliyoruz.
arabalar = ["sahin", "Fiat", "BMW", "Audi"]  # 📝 Başlangıç listesi
print(arabalar)  # ['sahin', 'Fiat', 'BMW', 'Audi']  (Başlangıçtaki liste)

# ✨ Listeye yeni bir araba modeli ekliyoruz: "Tofas"  (append ile sonuna ekleniyor).
arabalar.append("Tofas")  # 🚙 Listenin sonuna "Tofas" ekledik
print(arabalar)  # ['sahin', 'Fiat', 'BMW', 'Audi', 'Tofas']  (Sonunda "Tofas" var)

# 🔄 Listeye belirli bir yere yeni araba ekliyoruz: 2. indexe "ford".
arabalar.insert(2, "ford")  # 🛠️ "ford"u 2. indexe ekledik
print(arabalar)  # ['sahin', 'Fiat', 'ford', 'BMW', 'Audi', 'Tofas']  ("ford" 2. indexte)

# 🗑️ "Fiat" modelini listeden çıkarıyoruz (remove ile).
arabalar.remove("Fiat")  # 🚗 "Fiat" modelini listeden kaldırdık
print(arabalar)  # ['sahin', 'ford', 'BMW', 'Audi', 'Tofas']  ("Fiat" silindi)

# ✂️ Listeyi kesip, 0. indexteki öğeyi (ilk arabanın "sahin") sileriz.
arabalar.pop(0)  # 🗑️ "sahin"i sildik (0. indexteki araba)
print(arabalar)  # ['ford', 'BMW', 'Audi', 'Tofas']  ("sahin" silindi)

# 🔥 `del arabalar[3]` ile 3. indexteki öğe (yani "Tofas") silinebilir, fakat şu an yorum satırı yapıldı.
# del arabalar[3]  # 🗑️ 3. indexteki öğeyi siler

# 🧹 Listeyi tamamen temizliyoruz.
arabalar.clear()  # 🧹 Tüm öğeleri listeden siler
print(arabalar)  # []  (Liste tamamen temizlendi, artık boş)

# 🚗 Listeye tekrar bazı arabalar ekliyoruz.
arabalar = ["sahin", "Fiat", "BMW", "Audi", "Tofas", "ford"]  # 📝 Yeniden liste oluşturuldu
print(arabalar)  # ['sahin', 'Fiat', 'BMW', 'Audi', 'Tofas', 'ford']

# 🔄 Listeyi tersine sıralıyoruz.
arabalar.sort(reverse=True)  # 🔄 Listeyi ters sıraya göre sıralıyoruz
print(arabalar)  # ['Tofas', 'sahin', 'ford', 'Fiat', 'BMW', 'Audi']  (Ters sıralı liste)

# 🏆 Listenin en büyük elemanını yazdırıyoruz (alfabetik sıralama yapılır).
print(max(arabalar))  # 'Tofas'  (En büyük alfabetik öğe)

# 🏅 Listenin en küçük elemanını yazdırıyoruz (alfabetik sıralama yapılır).
print(min(arabalar))  # 'Audi'  (En küçük alfabetik öğe)

# 🔍 "ford" kelimesinin listede kaç kere geçtiğini sayıyoruz.
print(arabalar.count("ford"))  # 1  ("ford" listede 1 kere var)

# 📝 Güncel listeyi yazdırıyoruz.
print(arabalar)  # ['Tofas', 'sahin', 'ford', 'Fiat', 'BMW', 'Audi']  (Liste sıralandı)

# 🔄 Listeyi tersine sıralıyoruz (reverse() ile).
arabalar.reverse()  # 🔄 Listeyi tersine çeviriyoruz
print(arabalar)  # ['ford', 'Tofas', 'Audi', 'BMW', 'Fiat', 'sahin']  (Liste tersine döndü)


