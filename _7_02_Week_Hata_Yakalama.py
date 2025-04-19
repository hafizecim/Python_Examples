# Hata türleri açıklaması:
# Programcı hataları (Error) → Yazım/sentaks hataları (örnek: yanlış yazılmış kod)
# Program kusurları (Bug) → Kod doğru çalışsa da istenmeyen sonuçlara yol açan mantık hataları
# İstisnalar (Exception) → Program çalışırken ortaya çıkan beklenmeyen durumlar (örnek: sıfıra bölme)

# Kullanıcıdan iki sayı alınır (string olarak alınır)
sayi1 = input("sayi giriniz:")
sayi2 = input("sayi giriniz:")

try:
    # Girilen değerleri tam sayıya çevirir
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)

    # Bölme işlemi yapılır
    print(sayi1, "/", sayi2, "=", sayi1 / sayi2)

# Eğer sayı girilmemişse (örneğin: 'abc'), ValueError oluşur
except ValueError:
    print("Sadece sayi giriniz.")

# Eğer ikinci sayı 0 ise, sıfıra bölme hatası oluşur
except ZeroDivisionError:
    sayi2 = 1  # Otomatik olarak 1 yaparak hatadan kaçınılır
    print(sayi1, "/", sayi2, "=", sayi1 / sayi2)

# NOT: Bu except bloğu çalışmaz çünkü ValueError ve ZeroDivisionError yukarıda ayrı ayrı ele alındı
# Bu blok anlamlı olması için yukarıdakiler kaldırılmalı veya bu tek blok kullanılmalı
# Ama biz burada exceptionaları bir bütün olarak görnek adına yorum satırına almadık
except (ValueError, ZeroDivisionError) as hata: # Ayrı ayrı exception fırlatmak yerine birleştirerek de fırlatılabilir
    print("Bir hata oluştu")
except: # Bilinmeyen başka bir hata olursa bu blok devreye girer
    print("Hata var")
finally:
    print("işlem sona erdi")
