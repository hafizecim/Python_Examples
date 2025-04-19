# Anne sınıfı tanımlanıyor
class Anne:
    def __init__(self):
        self.sac = "sarı"  # Anne'nin saç rengi
        print(self.sac)

    def yazdir_anne(self):
        print("anne sınıfı")  # Anne'ye özel bir metot

    def goz_rengi(self):
        print("anne yesil")  # Anne'ye özel göz rengi


# Baba sınıfı tanımlanıyor
class Baba:
    def __init__(self):
        self.sac = "siyah"  # Baba'nın saç rengi
        print(self.sac)

    def yazdir_baba(self):
        print("baba sınıfı")  # Baba'ya özel bir metot

    def goz_rengi(self):
        print("kahve baba")  # Baba'ya özel göz rengi


# cocuk sınıfı hem Anne hem de Baba sınıfından miras alıyor (çoklu kalıtım)
class cocuk(Anne, Baba):
    def __init__(self):
        # Baba'nın constructor'ını çağırıyoruz
        Baba.__init__(self)
        # Eğer istenseydi Anne.__init__(self) de çağrılabilirdi

# cocuk sınıfından bir nesne oluşturuluyor
# ama çocuk sınıfında baba nın bilgilerini almak sitiyorsak babayı çağıran __init fonk çağrırız
c1 = cocuk()

# Baba sınıfından miras alınan metot çağrılıyor
c1.yazdir_baba()  # Çıktı: baba sınıfı

# Anne sınıfından miras alınan metot çağrılıyor
c1.yazdir_anne()  # Çıktı: anne sınıfı

# goz_rengi() hem Anne hem de Baba'da var, ama Anne önde olduğu için onunki çalışır (Method Resolution Order - MRO)
c1.goz_rengi()  # Çıktı: kahve baba
