class Calisan():
    def __init__(self,isim,maas,departman):
        print("Calisan sinifinin yapici fonksiyonu.")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgiler(self):
        print("Calisan sinifin bilgileri girilir.")
        print("isim:",self.isim,"\nmaas:",self.maas,"\ncalsitigi departman:",self.departman)
    def maas(self,zam_miktari):
        print("Maasa zam yapildi.")
        self.maas+=zam_miktari
    def departman_degistir(self,yenidepartman):
        print("Departman degistiriliyor.")
        self.departman=yenidepartman

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisisayisi):
        print("Yonetici sinifinin yapici fonksiyonu.")
        super().__init__(isim,maas,departman)
        self.kisisayisi=kisisayisi # ek ozellik
        super().bilgiler()
    def bilgiler(self):
        print("Yonetici sinifinin bilgileri gosteriliyor.")
        print("isim:", self.isim, "\nmaas:", self.maas, "\ncalsitigi departman:", self.departman,"\nKisi sayisi:",self.kisisayisi)
    def kisiartir(self,artir):
        print("Kisi sayisi artiriliyor...")
        self.kisisayisi+=artir


yonetici=Yonetici("Tom Shaltier",3000,"Insan Kaynaklari",23)
yonetici.bilgiler()
yonetici.kisiartir(10)
yonetici.bilgiler()