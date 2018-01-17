import sqlite3
kAdi="kullaniciAdi"
Parola="parola"
con=sqlite3.connect('database.db')
baglanti=con.cursor()
def tabloOlustur():
    baglanti.execute("CREATE TABLE IF NOT EXISTS kadro (ad TEXT,soyad TEXT,yas INT)")

def veriEkle():
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Lionel','Messi',30)")
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Philippe','Coutinho',25)")
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Andres','Iniesta',33)")
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Aleix','Vidal',28)")
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Samuel','Umtiti',24)")
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Luis','Suarez',30)")
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Gerard','Deulofeu',23)")
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Yerry','Mina',23)")
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Sergi','Roberto',25)")
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Lucas','Digne',24)")
    baglanti.execute("INSERT INTO kadro(ad,soyad,yas) VALUES('Jasper','Cillessen',28)")

tabloOlustur()
veriEkle()
def verileriGoster():
    baglanti.execute("SELECT * FROM kadro")
    con.commit()

veriEkle()
kullanici=input("Kullanici adiniz:")
parola=input("Parolaniz:")
if((kullanici==kAdi) and (parola==Parola)):
    verileriGoster()
    tum=baglanti.fetchall()
    print(tum)
else:
    print("Lutfen bilgileri dogru giriniz")
con.close()
