import random


class Dusman:

    def __init__(self,isim="Dusman",kalan_can=500,saldiri_gucu=10,mermi_sayisi=5):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim+" saldiriyor.")
        harcanan_mermi=random.randrange(0,10)
        print(str(harcanan_mermi)+" kadar mermi harcandi.")
        self.mermi_sayisi-=harcanan_mermi
        return(harcanan_mermi,self.saldiri_gucu)

    def saldiriyaugra(self,harcanan_mermi,saldiri_gucu):
        print("Vuruldum")
        self.kalan_can-=(harcanan_mermi*saldiri_gucu)

    def mermibittimi(self):
        if(self.mermi_sayisi<=0):
            print(self.isim + "konusuyor: Mermi bitti, oyundan cikiyorum!")
            return True
        return False

    def hayattami(self):
        if(self.kalan_can<=0):
            print("oluyorummmm")

    def print(self):
        print("Degerler basiliyor...")
        print("Isim:",self.isim)
        print("Kalan can:",self.kalan_can)
        print("Saldiri gucu:",self.saldiri_gucu)
        print("Mermi sayisi:",self.mermi_sayisi)

dusmanlar = []
i=0
while(i<10):
    rastgelecan=random.randrange(100,200)
    rastgelesaldiri=random.randrange(10,20)
    rastgelemermi=random.randrange(20,30)
    yenidusman=Dusman("Dusman"+str(i+1),rastgelecan,rastgelesaldiri,rastgelemermi)
    dusmanlar.append(yenidusman)
    i+=1

for dusman in dusmanlar:
    dusman.print()

