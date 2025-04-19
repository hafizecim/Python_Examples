# Araç sınıfı
class Arac():
    # Sınıf düzeyinde bir değişken (sınıf düzeyinde paylaşılan)
    arac_sayisi = 0  # Başlangıçta araç sayısı 0 olarak tanımlanır
    arac_list = []  # Her bir araç nesnesi için arac_listesi

    # Yapıcı (constructor) metod
    def __init__(self, marka, model, yil):
        self.marka = marka  # Araç marka bilgisini alır
        self.model = model  # Araç model bilgisini alır
        self.yil = yil      # Araç üretim yılını alır
        Arac.arac_sayisi += 1  # Yeni bir araç oluşturuldukça arac_sayisi 1 artırılır

    # Araç bilgilerini ekrana yazdıran metod
    def arac_goruntule(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}")

    # Araç ekleme metodunu nesne düzeyinde ekliyoruz
    def arac_ekle(self):
        self.arac_list.append(self.marka)  # Araç markasını listeye ekler


# Araç nesneleri oluşturuluyor
arac1 = Arac("Toyota", "Corolla", 2020)
arac2 = Arac("Honda", "Civic", 2022)
arac3 = Arac("Ford", "Focus", 2021)

# Araç ekleme işlemi
arac1.arac_ekle()
arac2.arac_ekle()
arac3.arac_ekle()

# Her aracın markalarını ekrana yazdıralım
print(f"Arac1'in markası: {arac1.arac_list}")
print(f"Arac2'in markası: {arac2.arac_list}")
print(f"Arac3'in markası: {arac3.arac_list}")

# Sınıf düzeyinde tanımlanan arac_sayisi değişkenine erişiyoruz
print(f"Toplam araç sayısı: {Arac.arac_sayisi}")  # Çıktı: Toplam araç sayısı: 3
print(Arac.arac_goruntule(arac1))
print(Arac.arac_list)

""" ÇIKTI
Arac1'in markası: ['Toyota']
Arac2'in markası: ['Honda']
Arac3'in markası: ['Ford']
Toplam araç sayısı: 3
Marka: Toyota, Model: Corolla, Yıl: 2020
None
['Toyota', 'Honda', 'Ford']
"""

"""
Açıklamalar:
arac_list:
Artık arac_list, her bir araç nesnesine ait olacak şekilde tanımlanmış durumda. 
Her araç nesnesinin kendi markalarını tutacak.
arac_ekle Metodu:
Bu metot, yalnızca her bir araç nesnesine ait arac_list'e aracın markasını ekler.
Her araç nesnesi, kendi markasını bu listeye ekler.
"""

"""
Her araç nesnesi, kendi markasını tutan bir arac_list'e sahip olur ve arac_ekle metodu sayesinde, 
markalar yalnızca o nesnenin listesine eklenir.
"""