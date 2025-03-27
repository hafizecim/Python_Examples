# 🧮 Atama ve Matematiksel Operatörler
a = 5  # a'ya 5 atanıyor
b = 10  # b'ye 10 atanıyor

a += b  # a = a + b 🟰 a'nın değerine b'yi ekler, a = 15 olur
a -= b  # a = a - b ➖ a'dan b'yi çıkarır, a = 5 olur
b *= 5  # b = b * 5 ✖️ b'yi 5 ile çarpar, b = 50 olur
a /= b  # a = a / b ➗ a'yı b'ye böler, a = 0.1 olur
a **= b  # a = a ** b 💥 a'yı b üssü ile yükseltir, a = 0.1 ** 50 olur (çok küçük bir sayı)
b //= a  # b = b // a // b'yi a'ya böler ve tam kısmı alır, b = 5000000000000000 olur
print(a, b)  # Sonuçları yazdırır: a ve b'nin son değerleri

# ***********************************************#
# 📊 Tuple unpacking (Demet parçalama) kullanımı
sayılar = 1, 4, 8, 9, 7, 8, 7, 6  # Bir tuple (demet) oluşturuluyor

print(type(sayılar))  # <class 'tuple'> çıktısı verir, çünkü 'sayılar' bir demettir.

# Tuple unpacking işlemi:
a, *b, c, d = sayılar  # a'ya ilk değer, *b'ye orta kısımdaki değerler, c'ye sondan ikinci, d'ye ise son değer atanır
print(d)  # Son değeri yazdırır, çıktısı: 6
print(c)  # Sondan bir önceki değeri yazdırır, çıktısı: 7
"""
a, *b, c, d = sayılar: Burada tuple (demet) parçalama kullanıyoruz. *b ifadesi, ortadaki tüm değerleri bir liste olarak b'ye atar. a, c, ve d ise sırasıyla ilk, sondan bir önceki, ve son değeri alır.
a → İlk değer (1)
*b → Orta değerlerin tümü ([4, 8, 9, 7, 8, 7])
c → Sondan bir önceki değer (7)
d → Son değer (6)
"""

#referans: list, tuple, sozluk,
#value: string, int, float