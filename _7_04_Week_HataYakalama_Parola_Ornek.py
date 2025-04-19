# Kullanıcıdan parola girmesini ister
parola = input("Parolanızı girin: ")

# Türkçe karakterleri kontrol et
turkce_karakterler = "çğıöşüÇĞİÖŞÜ"

# Her harfi kontrol eder
for harf in parola:
    if harf in turkce_karakterler:
        # Eğer Türkçe karakter varsa exception fırlatılır
        raise TypeError("Parolada Türkçe karakter kullanılamaz: " + harf)
      # raise Exception("Parolada Türkçe karakter kullanılamaz: " + harf) # bu satırda olur

# Eğer hata yoksa parolayı onayla
print("Parola başarıyla kabul edildi.")

# ******** 📌  2. yol ****************
# Özel hata sınıfı tanımlıyoruz (Exception sınıfından türeyerek)
class ParolaHatasi(Exception):
    def __init__(self, mesaj):
        super().__init__(mesaj)

# Türkçe karakterler listesi
turkce_karakterler = "çğıöşüÇĞİÖŞÜ"

try:
    # Kullanıcıdan parola alınır
    parola = input("Parolanızı girin: ")

    # Parolada Türkçe karakter var mı kontrol edilir
    if any(harf in turkce_karakterler for harf in parola):
        # Varsa özel hata fırlatılır
        raise ParolaHatasi("Parolada Türkçe karakter kullanılamaz!")

    # Eğer hata yoksa başarılı mesajı verilir
    print("Parola başarıyla kabul edildi.")

# Eğer özel hata yakalanırsa, kullanıcıya gösterilir
except ParolaHatasi as hata:
    print("HATA:", hata)


# Basit bir yol sadece küçük açıklamalı bir örnek
try:
    parola = "şifre"
    if "ş" in parola:
        raise Exception("Parolada Türkçe karakter olmaz")  # 💣 hata fırlat
    print("Parola kabul edildi")
except:
    print("Hata var ama biz yakaladık, program durmadı 😇")  # 🛡️ yakala

