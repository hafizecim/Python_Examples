# Öğrenci sınıfı
class Ogrenci:
    def __init__(self, ad, soyad):
        self.ad = ad  # Öğrencinin adı
        self.soyad = soyad  # Öğrencinin soyadı
        self.dersler = []  # Öğrencinin aldığı derslerin listesi

    # Ders ekleme metodu
    def ders_ekle(self, ders_adi):
        self.dersler.append(ders_adi)  # Ders adı listeye eklenir
        print(f"{ders_adi} dersi başarıyla eklendi.")

    # Dersleri görüntüleme metodu
    def dersleri_goruntule(self):
        if self.dersler:
            print(f"{self.ad} {self.soyad} adlı öğrencinin dersleri:")
            for ders in self.dersler:
                print(ders)
        else:
            print(f"{self.ad} {self.soyad} adlı öğrencinin aldığı ders yok.")

    # Ders değiştirme metodu (dersin adı değiştirilir)
    def ders_degistir(self, eski_ders, yeni_ders):
        if eski_ders in self.dersler:
            index = self.dersler.index(eski_ders)  # Eski dersin indeksini bul
            self.dersler[index] = yeni_ders  # Yeni dersle değiştir
            print(f"{eski_ders} dersi {yeni_ders} olarak değiştirildi.")
        else:
            print(f"{eski_ders} dersi bulunamadı. Değiştirme işlemi yapılmadı.")

# Öğrenci nesnesi oluşturuluyor
ogrenci1 = Ogrenci("Ayse", "Yılmaz")
ogrenci2 = Ogrenci("Ahmet", "Kara")

# Dersler ekleniyor
ogrenci1.ders_ekle("Matematik")
ogrenci1.ders_ekle("Fizik")
ogrenci2.ders_ekle("Kimya")
ogrenci2.ders_ekle("Biyoloji")

# Dersler görüntüleniyor
ogrenci1.dersleri_goruntule()
ogrenci2.dersleri_goruntule()

# Ders değiştirme işlemi
ogrenci1.ders_degistir("Fizik", "Kimya")  # Fizik dersini Kimya ile değiştiriyor
ogrenci1.ders_degistir("Biyoloji", "Edebiyat")  # Biyoloji dersi olmadığı için değiştirme işlemi yapılmaz

# Dersler yeniden görüntüleniyor
ogrenci1.dersleri_goruntule()
ogrenci2.dersleri_goruntule()
