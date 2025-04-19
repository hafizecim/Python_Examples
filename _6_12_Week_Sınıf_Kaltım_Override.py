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
    def __init__(self, isim, rutbe, yil): # Subay sınıfına özgü __init__ (constructor) metodu
        # 1. yöntem: Üst sınıfın __init__ metodunu doğrudan sınıf adıyla çağırmak
        Asker.__init__(self, isim, rutbe)  # 🔹 Bu doğru kullanım (manual çağrı)

        # 2. yöntem: super() ile üst sınıfın __init__ metodunu çağırmak (Pythonic tercih)
        super().__init__(isim, rutbe)  # 🔹 Bu da çalışır ama iki defa çağırma olur ⚠️

        self.yil = yil  # Subay sınıfına özel yeni bir özellik

    # Asker sınıfındaki yazdir() metodunu override ediyoruz
    def yazdir(self): # OVERRIDE ( YUKARIDAKİ YAZDIR METODUNU EZİYOR)
        # Subay'a özgü yazdırma işlemi (isim, rütbe ve yıl bilgisi)
        print(self.isim, self.rutbe, self.yil)


# Er sınıfı da Asker sınıfından miras alır
class Er(Asker):
    pass  # Aynı şekilde, Er için de ek özellik veya metod tanımlanmadı


# Asker sınıfından bir nesne oluşturuluyor
a1 = Asker("Ali", "er")
a1.yazdir()  # Çıktı: Ali er

# Subay sınıfından bir nesne oluşturuluyor
s1 = Subay("Cemal", "subay",10)
s1.yazdir()  # Çıktı: Cemal subay

# Er sınıfından bir nesne oluşturuluyor
e1 = Er("Hasan", "er")
e1.yazdir()  # Çıktı: Hasan er


# Çok katmanlı miras alma:
# Çoklu miras alma:



