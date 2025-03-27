# Lokal değişken sadece fonksiyon içinde geçerlidir.
# Global değişken program boyunca erişilebilir,
# ancak global anahtar kelimesi ile fonksiyonlar içinde de değiştirilebilir.

x=0
def fonk():
    x=1 # lokal bir değişken
    return x

print(x) # 0  Global x
print(fonk()) # 1  # Fonksiyondaki lokal x

y=0
def fonk2():
    global y # global bir değişkeni lokalde kullanabiliriz
    y=1
    return y

print(y) # 0 # Global y (fonksiyon çalıştırılmadan önce)
print(fonk2()) # 1 # Fonksiyondan dönen değer (fonksiyon çalıştırıldığında global y değişir)