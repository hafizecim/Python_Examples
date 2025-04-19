# Araç sınıfı
class Arac():
    # Sınıf düzeyinde bir değişken (sınıf düzeyinde paylaşılan)
    arac_sayisi = 0  # Başlangıçta araç sayısı 0 olarak tanımlanır

    # Yapıcı (constructor) metod
    def __init__(self, marka, model, yil):
        self.marka = marka  # Araç marka bilgisini alır
        self.model = model  # Araç model bilgisini alır
        self.yil = yil      # Araç üretim yılını alır
        Arac.arac_sayisi += 1  # Yeni bir araç oluşturuldukça arac_sayisi 1 artırılır

    # Araç bilgilerini ekrana yazdıran metod
    def arac_goruntule(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}")


# Araç nesneleri oluşturuluyor
arac1 = Arac("Toyota", "Corolla", 2020)
arac2 = Arac("Honda", "Civic", 2022)
arac3 = Arac("Ford", "Focus", 2021)


# Araçların bilgilerini görüntülüyoruz
arac1.arac_goruntule()  # Çıktı: Marka: Toyota, Model: Corolla, Yıl: 2020
arac2.arac_goruntule()  # Çıktı: Marka: Honda, Model: Civic, Yıl: 2022
arac3.arac_goruntule()  # Çıktı: Marka: Ford, Model: Focus, Yıl: 2021

# Sınıf düzeyinde tanımlanan arac_sayisi değişkenine erişiyoruz
print(f"Toplam araç sayısı: {Arac.arac_sayisi}")  # Çıktı: Toplam araç sayısı: 3


""" ÇIKTI
Marka: Toyota, Model: Corolla, Yıl: 2020
Marka: Honda, Model: Civic, Yıl: 2022
Marka: Ford, Model: Focus, Yıl: 2021
Toplam araç sayısı: 3

"""

"""
Açıklamalar:
Sınıf Düzeyinde Değişken (arac_sayisi):
arac_sayisi, sınıf düzeyinde tanımlanmış bir değişkendir ve tüm nesneler tarafından paylaşılır.
Bu değişken her yeni araç nesnesi oluşturulduğunda artırılır. Arac.arac_sayisi ifadesiyle sınıf düzeyindeki bu değişkene erişiyoruz.
Yeni Araç Nesnesi Eklendikçe arac_sayisi Artırılır:
Her Arac nesnesi oluşturulduğunda, yapıcı metotta (yani __init__ içinde) Arac.arac_sayisi 1 artırılır.
Bu, toplam araç sayısını takip etmek için kullanılır.
Sınıf Düzeyindeki Değişkene Erişim:
Sınıf düzeyinde tanımlanan değişkeni Arac.arac_sayisi şeklinde sınıf adıyla çağırabiliriz.
"""

"""
Sonuç: Bu örnekte, arac_sayisi değişkeni sınıf düzeyinde tanımlandı ve
her araç nesnesi oluşturulduğunda bu değişken güncellenerek toplam araç sayısını tutuyor. 
Bu tür değişkenler, tüm nesneler için ortak olan bilgileri tutmak amacıyla kullanılır.
"""