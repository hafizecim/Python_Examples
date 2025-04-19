class Calisan(): #lokal
    unvan="isci"
    def __init__(self):
        self.kabiliyet=[]
        ad=""
        soyad=""

print(Calisan.unvan)
print(Calisan.ad)

c1=Calisan()
c1.ad="ayse"
c1.soyad="ayvaci"
c1.kabiliyet.append("bilgisayra")

print(c1.kabiliyet)

c2=Calisan()
c2.ad="mehmet"
c2.kabiliyet.append("elektrik")
print(c2.ad)