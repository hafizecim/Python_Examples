# 🧮 İf Koşulları ile Karşılaştırma
a = 30  # a'ya 30 atanıyor
b = 80  # b'ye 80 atanıyor

if a > b:  # a, b'den büyük mü?
    print(a, "büyük sayı")  # Eğer a, b'den büyükse bu yazdırılır.

if b > a:  # b, a'dan büyük mü?
    print(b, "büyük sayı")  # Eğer b, a'dan büyükse bu yazdırılır.

print("Ayşe")  # Bu her durumda yazdırılacak, çünkü if bloklarına bağlı değil

# 🎯 Yaş bazlı koşullu ifadeler
yas = int(input("Yaşınızı giriniz: "))  # Kullanıcıdan yaş girmesini istiyoruz

if yas == 18:  # Eğer yaş 18 ise
    print("Sınır yaş")  # 18 için özel mesaj
elif yas < 0:  # Eğer yaş negatif bir sayı ise
    print("Yeni doğmuş")  # Geçersiz yaş için mesaj
elif yas < 18:  # Eğer yaş 18'den küçükse
    print("Çocuksun")  # 18 yaşından küçük için mesaj
elif yas > 18:  # Eğer yaş 18'den büyükse
    print("Orta yaş")  # 18 yaşından büyük için mesaj

sayi = int(input("Bir sayi giriniz: "))
if sayi % 2 == 0:
    print(sayi, "Sayi cifttir.")
else:
    print(sayi, "Sayi tek sayidir")

print("************** HESAP MAKİNESİ **************")
sayi3 = int(input("Bir sayi giriniz: "))
sayi4 = int(input("Bir sayi giriniz: "))

print("Toplama = +")
print("Fark = -")
print("Bolme = /")
print("Carpma = *")
secim = ''
secim = (input("Bir islem giriniz: "))

if (secim == '+' or secim == '-' or secim == '/' or secim == '*'):
    if (secim == '+'):
        print("Toplam", sayi3 + sayi4)
    elif (secim == '-'):
        print("Fark:", sayi3 - sayi4)
    elif (secim == '/'):
        # Sıfıra bölme kontrolü
        if sayi4 == 0:
            print("Hata: Bir sayıyı sıfıra bölemezsiniz!")
        else:
            print("Bolum", sayi3 / sayi4)
    elif (secim == '*'):
        print("Carpim", sayi3 * sayi4)
else:
    print("Yanlış bir seçim yaptınız. Lütfen geçerli bir işlem seçin.")

print("************** HESAP MAKİNESİ FORMATLI **************")
sayi1 = int(input("sayi giriniz:"))
sayi2 = int(input("sayi giriniz:"))
print("toplam için :+ fark için: - bolum için: / carpma için: * kalansız bolme: // us alma: **")
secim = input("yapmak istediğiniz işlemi:")

if secim == "+":
    print("toplam:", sayi1 + sayi2)
elif secim == "-":
    print("fark:", sayi1 - sayi2)
elif secim == "*":
    print("carpım:", sayi1 * sayi2)
elif secim == "/":
    print("bölüm:", sayi1 / sayi2)
elif secim == "//":
    print("tam bolme:", sayi1 // sayi2)
elif secim == "**":
    print("us alma:", sayi1 ** sayi2)
else:
    print("bu işlem tanımlı degil")
