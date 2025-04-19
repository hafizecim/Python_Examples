class Araba():
    adet=0
    arac_liste=[]

    def __init__(self,ma,mo,y):
        self.model=mo
        self.marka=ma
        self.yil=y
        self.arac_ekle()

    def arac_listele(self):
        print(self.model,self.marka,self.yil)

    def arac_ekle(self):
        self.arac_liste.append(self.marka)
        self.adet+=1

    def arac_g(self):
        print(self.arac_liste)

    def guncelle(self,ilk,ikici):
        for i in range ( len(self.arac_liste)):
            print(self.arac_liste[i])
            if  self.arac_liste[i]==ilk:
                self.arac_liste[i]==ikici


a1=Araba("BMW","i5","2000")
a2=Araba("Ford","arac","2020")
"""a1.adet+=1
a1.marka="BMW"
a1.model="i5"
a1.yil="2020"""

a1.arac_listele()
a2.arac_listele()
a1.arac_g()
print(Araba.arac_liste)

#değişitirme
a2.model="fiat"
a2.arac_listele()
Araba.arac_g()

#değişitirme metod ile
a2.guncelle("fiat", "fort")
a2.arac_listele()
Araba.arac_g()