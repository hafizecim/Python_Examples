
# Personel sınıfı tanımlanıyor. Herkes tarafından erişilebilir (public class)
class Personel:
    def __init__(self):
        # Public (her yerden erişilebilir) nitelikler
        self.ad = "hafize"
        self.soyad = "senyil"
        self.maas = 120000

        # Private (özel, dışarıdan doğrudan erişilemez) nitelik
        self.__tc = "12357"  # '__' öneki ile kapsülleme (encapsulation) sağlanır

    # Getter metodu: özel (__tc) veriyi okumak için kullanılır
    def get_tc(self):
        return self.__tc

    # Setter metodu: özel (__tc) veriyi değiştirmek için kullanılır
    def set_tc(self, y_tc):
        self.__tc = y_tc


# Personel sınıfından bir nesne oluşturuluyor
p1 = Personel()
p1.maas = 150000 # Maaş bilgisi dışarıdan doğrudan değiştiriliyor (public olduğu için)

# HATALI ERİŞİM: __tc özelliğine doğrudan erişim mümkün değil!
print(f"{p1.ad} {p1.soyad} adli kişinin  tc: {p1.tc} maas: {p1.maas}")
# Bu satır hata verir: 'Personel' object has no attribute 'tc'
# print(f"{p1.ad} {p1.soyad} adli kişinin  tc: {p1.tc} maas: {p1.maas}")

# Doğru kullanım: getter metoduyla özel alanı okuyoruz
tc = p1.get_tc()
p1.set_tc("7896325") # Setter metoduyla tc numarası güncelleniyor
tc = p1.get_tc() # Güncellenmiş tc tekrar getter ile alınıyor

# Ekrana bilgileri yazdırıyoruz
print(f"{p1.ad} {p1.soyad} adlı kişinin tc: {tc} maas: {p1.maas}")
