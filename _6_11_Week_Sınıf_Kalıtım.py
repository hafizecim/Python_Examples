# Üst sınıf (base class) tanımlanıyor: Asker
class Asker:
    def __init__(self, isim, rutbe):
        self.isim = isim     # Askerin adı
        self.rutbe = rutbe   # Askerin rütbesi

    def yazdir(self):
        # Askerin adı ve rütbesi ekrana yazdırılır
        print(self.isim, self.rutbe)


# Subay sınıfı, Asker sınıfından miras alır (kalıtım)
# Herhangi bir ek özellik veya metod eklenmemiş, sadece Asker’in özelliklerini kullanır
class Subay(Asker):
    pass  # Henüz yeni özellik eklenmediği için boş bırakılır

# Er sınıfı da Asker sınıfından miras alır
class Er(Asker):
    pass  # Aynı şekilde, Er için de ek özellik veya metod tanımlanmadı


# Asker sınıfından bir nesne oluşturuluyor
a1 = Asker("Ali", "er")
a1.yazdir()  # Çıktı: Ali er

# Subay sınıfından bir nesne oluşturuluyor
s1 = Subay("Cemal", "subay")
s1.yazdir()  # Çıktı: Cemal subay

# Er sınıfından bir nesne oluşturuluyor
e1 = Er("Hasan", "er")
e1.yazdir()  # Çıktı: Hasan er
