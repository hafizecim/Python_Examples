#******* Fonksiyonlarda Lambda  Kullanımı ********

def karesi(n):
    return n**2
print(karesi(5)) # 25

a=lambda n:n**2
print(type(a)) # <class 'function'>
print(a(4)) # 16
print(a(2)) # 4

b=lambda x,y:x+y
print(b(4,7)) #11

#📌***** Küp ve Kare Örneği *****
def islem(n):
    return lambda m:m**n

kare=islem(2) # m=2
print(kare(5)) # n=5 in karesi --> 25

kup=islem(3) # m=3
print(kup(5)) # n=5 in kübü --> 125


# ****** Map fonkisiyonu ******

sayilar =[1,5,7,9]

def kareAl(liste):
    for i in liste:
        print(i**2)

sonuc=list(map(karesi,sayilar))
print("sonuc:",sonuc) # sonuc: [1, 25, 49, 81]

sonuc=list(map(lambda n:n**2,sayilar))
print("lambda sonuc:" ,sonuc) # lambda sonuc: [1, 25, 49, 81]

sonuc=list(filter(lambda sayi:sayi%2==0,sayilar))
print("#filter sonuc:" ,sonuc) #filter sonuc: []





