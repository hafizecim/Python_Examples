# Fonksiyon tanımlama
def yazdir():
    print("Ayşe")

def toplama(a, b):
    return a + b

sonuc = toplama(8, 9)
print(sonuc)
yazdir()

# Faktöriyel hesaplayan fonksiyon
def faktoriyel(n):
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc

print(faktoriyel(5))  # Örnek olarak 5! hesaplandı
sonuc=toplama(8,9)
print(sonuc)
yazdir()


#permitasyon n!/(n-r)!
def permitasyon(n,r):
    sonuc=faktoriyel(n)/faktoriyel(n-r)
    return sonuc

p=permitasyon(5,3)
print(p)


#kombinasyon = n! / (n – r)! * r
def kombinasyon(n,r):
    return faktoriyel(n) // (faktoriyel(r) * faktoriyel(n - r))

k=kombinasyon(5,3)
print(k)



print("hafize", end=".")
print("senyil")

print("hafize", "senyil", sep="/")
print("senyil")



def yazdir_bilgi(ad):
    print("Benim adim",ad)
yazdir_bilgi("hafize") #çıktıyı değeri ad ı buradan alıyor

def yazdir_bilgi2(ad="admin"): #çıktıyı değeri ad ı buradan alıyor
    print("Benim adim",ad)
yazdir_bilgi2()
yazdir_bilgi2("hafize")

def toplama2(*sayilar): #demet
    print(type(sayilar))
    sonuc=0
    for i in sayilar:
        sonuc=sonuc+i
    return sonuc
sonuc=toplama2(2,3,4,5,6,7,8)
print(sonuc)

def islem(*sayilar): #demet (sınırsız sayıda değerler göndermek içi tumple kullanıyoruz
    print(type(sayilar))
    s1=0
    s2=0
    for i in range(3):
        s1=s1+sayilar[i]
    s1=s1*5
    print(s1)
    for j in range(2,6):
         s2=s2*sayilar[j]
    print(s2)
    s1=s1+s2
    return s1
s1=islem(2,3,4,5,6,7,8)
print(s1)

def bilgi(**par): # sözlük ( defualt olarak göndermek istersek sözlük kullanıyoruz
    print(type(par))
    for key, val in par.items():
        print("{}:{} ".format(key,val))

bilgi(ad="Hafize", yas="32", mail="hotmail")


















