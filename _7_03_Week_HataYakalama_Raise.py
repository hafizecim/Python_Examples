# raise: “Burada bir sorun var, yakalansın!” diyerek hata oluşturur.
# except: “Bakalım bir sorun olmuş mu?” diyerek bu hatayı yakalar ve çökmeyi önler.

#                 🔥 raise ve except Farkı
# Özellik           / raise	                              / except
# Görevi	        / Hata fırlatır (yani "oluşturur")	  / Fırlatılan hatayı yakalar
# Ne zaman çalışır	/ Belirli bir koşul gerçekleştiğinde  / Bir hata oluştuğunda
# Nerede kullanılır	/ try bloğu içinde veya bağımsız	  / try bloğunun hemen sonrasında
# Kullanımı	        / raise Exception("mesaj")	          / except Exception as e:

# 🧨 raise nedir?
# Raise = “Ben burada hata olduğunu biliyorum, fırlatıyorum!” demek.
# 🛡️ except nedir?
# Except = “Bir yerde hata olmuşsa, ben yakalayıp güzelce mesaj göstereyim” demek.

#Raise = HATA FIRLATIR
#Except = HATA YAKALAR

# Raise ne yapar? | Hata oluşturur
# Except ne yapar? | Hata yakalar
# Raise olursa ne olur? | Hata fırlatılır, program durur ❌
# Except olursa ne olur? | Hata olsa bile durmaz, güzel mesaj verir ✅

# Kullanıcıdan bölünecek sayıyı alır (string olarak gelir, int'e çevrilir)
bolunen = int(input("bolunecek sayi:"))

# Eğer kullanıcı 10 sayısını girerse, bilinçli olarak bir istisna (hata) fırlatılır
# raise: elle hata oluşturmak için kullanılır
if bolunen == 10:
    raise Exception("10'a bölünme yapılamaz")  # İstisna mesajı: kullanıcıya gösterilecek hata açıklaması  # ❌ hata fırlatılır

# Eğer yukarıdaki raise çalışmazsa, burası çalışır:
# Kullanıcıdan bölen alınır
bolen = int



