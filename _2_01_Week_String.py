"""********* 📌VERİ TYPE DONUSTURME ***********"""
x=1#int tamsayi
y=2.8#float-ondalik sayi
ders="python"#string
kontrol=True#boolean
print(x,y,ders,kontrol)

print(type(x))
print(type(y))
print(type(ders))
print(type(kontrol))

"""***** 📌KLAVYEDEN VERİ GİRİŞİ *****"""
a=input("1 sayi giriniz : ")
b=input("1 sayi giriniz : ")
print(type(a+b)) # <class 'str'> ---> çıktı string bu yüzden tür değişkeni yapılır

a_yeni=float(a) # type değişkeni yapıldı
b_yeni=float(b) # type değişkeni yapıldı
print(a_yeni+b_yeni)
print(type(a_yeni+b_yeni)) # <class 'float'> ✔ artık toplama gerçekleşti

z=int(kontrol) # true --> 1 dönüştürme
print(kontrol)

y_yeni="2.9" # string ifadeyi floata çevirme
y_yeni=float(y_yeni)
print(type(y_yeni))

"""****** 🔔KLAVYEDEN GİRİLEN DEĞERLER İLE NET MAAŞ HESABI ******"""
brut_maas=input("brut maas giriniz: ")
vergi_orani=input("Vergi orani giriniz: ")

brut_maas_yeni = float(brut_maas)
vergi_orani_yeni = float(vergi_orani)

# brut_maas=float(input("brut maas giriniz: ")) ---> kısa yolu
# vergi_orani=float(input("Vergi orani giriniz: ")) ---> kısa yolu

vergi = brut_maas_yeni * vergi_orani_yeni
net_maas = brut_maas_yeni - vergi

print("Net Maas: ", net_maas )
print(type(net_maas))

"""******** 🔔DİKDORTGENIN ALANI VE ÇEVRESINI HESAPLAMA *********"""
kisa_kenar = int(input("Kisa kenari giriniz: "))
uzun_kenar = int(input("Uzun kenari giriniz: "))

dikdortgen_alan = kisa_kenar*uzun_kenar
dikdortgen_cevre = 2*(kisa_kenar+uzun_kenar)

print("Dikdortgenin alani : ",dikdortgen_alan)
print("Dikdortgenin cevresi : ",dikdortgen_cevre)

"""************ 📌STRING *************"""
"""******* 📌BİRLEŞTİME *******"""
ad = "hafize"
soyad = "senyil"
yas=32
birlesik = ad + " " +soyad
print(birlesik)
print("benim adim {}  say adim {}  yasim {}".format(ad,soyad,yas )) #Yöntem 1
print("benim adim {0} say adim {1} yasim {2}".format(ad,soyad,str(yas) )) #Yöntem 2
print("benim adim {a} say adim {b} yasim {c}".format(a=ad,b=soyad,c=str(yas) )) #Yöntem 3

"""******* 📌BÖLME / PARÇALAMA *******"""
metin="Python Programlama Dersi"
sonuc=metin[0] # P
sonuc=metin[5] # n
sonuc=metin[-1] # i (sondan karakterleri almaya yarar - operatörü
sonuc=metin[7:18] # Programlama
sonuc=metin[19:24] # Dersi
sonuc=metin[-5:-1] # Dersi
sonuc=metin[:10] # metnin ilk 10 karakterini alır --> Python Pro
sonuc=metin[3:] #  metnin 3. indeksinden sonrasını alır (3. dahil)  --> hon Programlama Dersi
sonuc=metin[3:20:2] # metnin 3. indeksinden başlayarak 20. indekse kadar 2 adımla ilerler -->  hnPormaa
sonuc=metin[::-1] # metni tersten yazar --> isreD ammalorP nohtyP

"""****** 🔔String Ödev *******"""
# 1. karakter uzunl"ugu
# 2. metin içerisindeki python kelimesini bulma
# 3. metin içerisinde ilk 15 ve son 15 karakterini alma
# Metin tanımlama

text = "Python Programlama Dili  Python Programlama Dili Python"

# 1. Karakter uzunluğu
char_length = len(text)

# 2. "Python" kelimesini bulma
python_count = text.count("Python")

# 3. İlk 15 ve son 15 karakteri alma
first_15 = text[:15] # ilk 15 karakter
last_15 = text[-15:] # son 15 karakter

# Sonuçları ekrana yazdırma
print("Karakter Uzunluğu:", char_length)
print("'Python' Kelimesinin Sayısı:", python_count)
print("İlk 15 Karakter:", first_15)
print("Son 15 Karakter:", last_15)

print("python"*5) # yanyana 5 tane python yazar

"""****** Parçalama ********"""
metin = "Ayse, Fatma, Zehra, geldi "
sonuc=metin.split() # boşluklara göre parçalar
print(sonuc) # ['Ayse,', 'Fatma,', 'Zehra,', 'geldi']

sonuc=metin.split(",") # virgüle göre parçalar
print(sonuc) #  ['Ayse', ' Fatma', ' Zehra', ' geldi']
print(len(sonuc)) # 4

sonuc=metin.upper()
print("upper",sonuc) # upper AYSE, FATMA, ZEHRA, GELDI
sonuc=metin.lower()
print("lower",sonuc) # lower ayse, fatma, zehra, geldi
sonuc=metin.title()
print("title",sonuc) # title Ayse, Fatma, Zehra, Geldi
sonuc=metin.capitalize()
print("capitalize",sonuc) # capitalize Ayse, fatma, zehra, geldi
sonuc=metin.strip() # metodu, metnin başındaki ve sonundaki boşlukları temizler. Eğer boşluk dışında başka karakterler varsa, onları da temizler.
print("strip",sonuc) # strip Ayse, Fatma, Zehra, geldi
sonuc=metin.replace("Fatma","ali") # metodu, belirli bir alt dizeyi başka bir alt dize ile değiştirir
print("replace",sonuc) # replace Ayse, ali, Zehra, geldi

metin2 = "python dersi"
sonuc = metin2.find("ayse") # 📝python dersi içinde ayse olmadığı için hata ❌dönmemesi için if else yaptık
if sonuc != -1:
    print("Index:", sonuc)
else:
    print("Kelime bulunamadı.")

sonuc = metin2.find("ayse")
print("find:",  sonuc) #-1 ✅
# 📝startswith() -> Metin belirli bir kelimeyle başlıyor mu?
sonuc = metin2.startswith("python")
print("startswith:", sonuc)  # True ✅-> "python dersi" "python" ile başladığı için True döner.

# 📝endswith() -> Metin belirli bir harf/kelime ile bitiyor mu?
sonuc = metin2.endswith("p")
print("endswith:", sonuc)  # False ✅-> "python dersi" harfi "p" ile bitmediği için False döner.

# 📝isdigit() -> Metin tamamen rakamlardan mı oluşuyor?
sonuc = "1252".isdigit()
print("isdigit:", sonuc)  # True ✅-> "1252" sadece rakamlardan oluştuğu için True döner.

# 📝isalpha() -> Metin tamamen harflerden mi oluşuyor?
sonuc = "metin2".isalpha()
print("isalpha:", sonuc)  # False ✅-> "metin2" içinde rakam olduğu için False döner.




