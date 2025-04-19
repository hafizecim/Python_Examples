# Sınıf tanımı
class Araba:
    def __init__(self, model, renk):
        self.model = model
        self.renk = renk

    def bilgi_ver(self):
        print(f"Bu araba {self.model} modelinde ve {self.renk} renktedir.")

# Nesne oluşturma
araba1 = Araba("Toyota", "Kırmızı")
araba2 = Araba("BMW", "Mavi")

# Nesnenin metodunu kullanma
araba1.bilgi_ver()  # Bu araba Toyota modelinde ve Kırmızı renktedir.
araba2.bilgi_ver()  # Bu araba BMW modelinde ve Mavi renktedir.

"""
Python'da sınıf ve nesne arasındaki fark şu şekildedir:

Sınıf (Class): Sınıf, bir nesnenin nasıl davranacağını ve özelliklerini tanımlayan bir şablondur.
Yani, sınıf bir tür "plan" ya da "taslak" gibi düşünülebilir. Sınıf içinde, 
nesnelerin sahip olacağı özellikler (değişkenler) ve davranışlar (metodlar) tanımlanır. 
Sınıf, bir nesne yaratılmadan önce var olan bir yapı olup, nesnelerin oluşturulmasına rehberlik eder.

Nesne (Object): Nesne, sınıfın bir örneğidir. Bir sınıf tanımlandığında, 
bu sınıfın bir nesnesini oluşturabiliriz. 
Nesne, sınıfın içinde tanımlanan özellikleri ve davranışları gerçek hayata uyarlayarak, 
somut bir varlık haline gelir. Yani, sınıf bir şablonken, 
nesne bu şablon üzerinden oluşturulmuş somut bir varlıktır.

"""