# Calisan sınıfı, personel bilgilerini tutan bir yapıdır.
class Calisan():
    unvan = "isci"
    def __init__(self):
        self.kabiliyet = []
        self.ad = ""
        self.soyad = ""

def personel_ekle(self, isim, soyad, k):
    self.ad = isim
    self.soyad = soyad
    self.kabiliyet.append(k)


def gorontole(self):
    print(self.ad, self.soyad, self.kabiliyet)


a = Calisan()
a.personel_ekle("Ayşe", "Ayvaci", "PC")
a.gorontole()  # Çıktı: Ayşe Ayvaci ['PC']


b = Calisan()
b.personel_ekle("Hafize", "Şenyıl", "PC")
b.gorontole()  # Çıktı: Hafize Şenyıl ['PC']

