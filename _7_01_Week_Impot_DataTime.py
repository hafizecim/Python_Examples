# datetime modülünü içe aktarır (tarih ve saat işlemleri için kullanılır)
import datetime
import locale # türkçe için

print(datetime.datetime.now()) # Şu anki tarih ve saati yazdırır (örnek: 2025-04-19 12:48:35.123456)
suan = datetime.datetime.now() # 'suan' adında bir değişkene şu anki tarih ve saat atanır
print(suan) # 'suan' değişkenini yazdırır
print(suan.month) # Ay bilgisini yazdırır (örnek: 4, yani Nisan)
print(suan.year) # Yıl bilgisini yazdırır (örnek: 2025)

# Tarihi okunabilir bir string olarak verir (örnek: Sat Apr 19 12:48:35 2025)
print(datetime.datetime.ctime(suan))

# Tarih nesnesinden sadece yılı alır ve string olarak döner (örnek: '2025')
print(datetime.datetime.strftime(suan, "%Y"))

# Yıl, ay ismi (metin olarak) ve gün ismini (metin olarak) birlikte döner
# (örnek: '2025 April Saturday')
print(datetime.datetime.strftime(suan, "%Y %B %A"))

# Türkçe yerel ayarları etkinleştir
locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')  # Linux ve Mac için
# locale.setlocale(locale.LC_TIME, 'turkish')   # Windows için alternatif

suan = datetime.datetime.now()

# Yıl, ay adı ve gün adı Türkçe olarak yazdırılır
print(datetime.datetime.strftime(suan, "%Y %B %A"))

# ******* type dönüşüm ********
# Türkçe tarih ve saat içeren bir string tanımlanır
saat = "19 Nisan 2025 saat 12:49:50"

# 'strptime' fonksiyonu ile string ifade, datetime nesnesine dönüştürülür
# Format: '%d %B %Y saat %H:%M:%S'
# %d : Gün (19)
# %B : Ay adı (Nisan) — bu Türkçe olduğu için locale ayarı gerekebilir
# %Y : Yıl (2025)
# %H : Saat (12)
# %M : Dakika (49)
# %S : Saniye (50)
sonuc = datetime.datetime.strptime(saat, '%d %B %Y saat %H:%M:%S')