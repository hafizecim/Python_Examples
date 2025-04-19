# Calisan sınıfı, personel bilgilerini tutan bir yapıdır.
class Calisan():
    # Sınıf düzeyinde bir "unvan" özelliği tanımlanıyor ve "isci" olarak varsayılacak.
    unvan = "isci"

    # __init__ metodu, sınıfın her örneği (nesnesi) oluşturulduğunda çalışacak bir yapıcı (constructor) metodudur.
    def __init__(self):
        # Kabiliyetler listesi her bir çalışan nesnesi için boş bir liste olarak başlatılır.
        self.kabiliyet = []
        # Çalışanın adı ve soyadı başlangıçta boş string olarak belirlenir.
        self.ad = ""
        self.soyad = ""

# personel_ekle metodu, çalışan bilgilerini (isim, soyad, kabiliyet) bir çalışan nesnesine ekler.
def personel_ekle(self, isim, soyad, k):
    # Çalışanın adını ve soyadını verilen parametrelerle güncelleriz.
    self.ad = isim
    self.soyad = soyad
    # Çalışanın kabiliyetine, verilen "k" parametresini ekleriz (örneğin, PC bilgisi).
    self.kabiliyet.append(k)

# gorontole metodu, çalışan bilgilerini ekrana yazdırır.
def gorontole(self):
    # Çalışanın adını, soyadını ve kabiliyetini yazdırır.
    print(self.ad, self.soyad, self.kabiliyet)


# a isminde bir Calisan nesnesi oluşturuluyor.
a = Calisan()
a.personel_ekle("Ayşe", "Ayvaci", "PC") # a nesnesine personel_ekle metodu ile isim, soyad ve kabiliyet bilgileri ekleniyor.
# a nesnesinin bilgilerini gorontole metodu ile ekrana yazdırıyoruz.
a.gorontole()  # Çıktı: Ayşe Ayvaci ['PC']

# b isminde başka bir Calisan nesnesi oluşturuluyor.
b = Calisan() # b nesnesine de personel_ekle metodu ile isim, soyad ve kabiliyet bilgileri ekleniyor.
b.personel_ekle("Hafize", "Şenyıl", "PC")
# b nesnesinin bilgilerini gorontole metodu ile ekrana yazdırıyoruz.
b.gorontole()  # Çıktı: Hafize Şenyıl ['PC']

"""
Sınıf, bir tür "model" iken, nesne bu modelin gerçek bir örneğidir.
Örneğin:
Calisan sınıfını tanımladık.
Bu sınıfın bir nesnesi “Ayşe Ayvaci” olabilir. 
Yani bir çalışanın adı, soyadı ve kabiliyet bilgilerini içeren bir nesne.
"""

"""
Sınıfın Yapıcı Metodu (__init__)
Python sınıflarında, her nesne oluşturulduğunda çalışan özel bir metoda __init__ denir. 
Bu metot, nesne oluşturulduğunda bazı başlangıç değerlerini ayarlamak için kullanılır.
Örneğin, Calisan sınıfında __init__ metodu, çalışanın ad, soyad, ve kabiliyet özelliklerini başlatır.
"""

"""
Metodlar ve Fonksiyonlar
Sınıf içinde tanımlanan fonksiyonlara metod denir. Bir sınıfın metodları, o sınıfın nesneleri üzerinde işlem yapabilir. 
Metodlar, nesneye ait özelliklere (değişkenlere) erişebilir ve bu özellikleri değiştirebilir.
Örneğin, personel_ekle ve gorontole metodları, çalışan bilgilerini ekler ve görüntüler.
"""

