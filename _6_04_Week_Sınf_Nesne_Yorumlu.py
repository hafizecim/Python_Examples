# 1. Calisan sınıfı tanımlanıyor
class Calisan():
    unvan = "isci"  # Sınıf düzeyinde tanımlı bir unvan (tüm çalışanlar için aynı)

    def __init__(self):
        self.kabiliyet = []  # Her çalışan için boş bir kabiliyet listesi başlatılır
        self.ad = ""         # Çalışanın adı başlangıçta boş
        self.soyad = ""      # Çalışanın soyadı başlangıçta boş

    def personel_ekle(self, isim, soyad, k):
        self.ad = isim       # Çalışanın adını belirler
        self.soyad = soyad   # Çalışanın soyadını belirler
        self.kabiliyet.append(k)  # Çalışanın kabiliyetini listeye ekler

    def personel_goruntule(self):
        print(self.ad, self.soyad, self.kabiliyet)  # Çalışanın bilgilerini yazdırır

"""
Açıklama:
Calisan Sınıfı: Çalışanları temsil eden bir sınıf. İçinde adı, soyadı ve 
kabiliyetleri saklayacak özellikler ve bu bilgileri eklemek/görüntülemek için metodlar var.
__init__ Metodu: Nesne oluşturulduğunda çalışan özellikleri başlatır.
personel_ekle Metodu: Çalışanın adı, soyadı ve kabiliyeti ekler.
personel_goruntule Metodu: Çalışanın bilgilerini ekrana yazdırır.
"""

# Nesne oluşturma
a = Calisan()  # Calisan sınıfından a isminde bir nesne oluşturuluyor
a.personel_ekle("Ayşe", "Ayvaci", "PC")  # a nesnesine bilgi ekliyoruz
a.personel_goruntule()  # a nesnesinin bilgilerini görüntülüyoruz

b = Calisan()  # Yeni bir Calisan nesnesi oluşturuluyor
b.personel_ekle("Hafize", "Şenyıl", "PC")  # b nesnesine bilgi ekliyoruz
b.personel_goruntule()  # b nesnesinin bilgilerini görüntülüyoruz

"""
Açıklama:
Nesne oluşturma: a = Calisan() şeklinde, Calisan sınıfından bir nesne (örneğin Ayşe Ayvaci) oluşturuluyor.
Metod çağırma: a.personel_ekle(...) ile bu nesnenin bilgileri giriliyor ve
a.personel_goruntule() ile de ekrana yazdırılıyor.
"""

"""
Çıktı
Ayşe Ayvaci ['PC']
Hafize Şenyıl ['PC']
"""

"""
Sonuç ve Özet
Sınıflar (classes) Python'da benzer özelliklere sahip nesneleri tanımlamak için kullanılır.
Nesneler (objects) ise sınıflardan oluşturulan somut varlıklardır.
Metodlar sınıf içinde tanımlanan fonksiyonlardır ve nesnenin özelliklerini değiştirebilir.
__init__ metodu, her nesne oluşturulduğunda çalışarak başlangıç değerlerini ayarlar.
"""