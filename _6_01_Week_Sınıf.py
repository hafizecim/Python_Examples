class Calisan(): # global (sınıfın özelliklerini kullanır)
    kabiliyet=[]
    unvan='isci'
    ad=""
    soyad=""

print(Calisan.unvan)
print(Calisan.ad)

c1=Calisan()
c1.ad="ayse"
c1.soyad="ayvaci"
c1.kabiliyet.append("bilgisayra")
c1.kabiliyet.append("c++")

print(c1.kabiliyet)

c2=Calisan()
c2.ad="mehmet"
c2.kabiliyet.append("elektrik")
print(c2.ad)