
kelime=open("C:\\Users\USER\Desktop\kelimeler.txt","r") #aradığımız kelimeler için kelime adında dosya oluşturur
str=kelime.read().split('\n')
print("\nMetinde Aranan Kelimeler:\n")
print(str)
print("\nMetindeki kelimelerimizin sayısı:\n")
dosya=open('C:\\Users\USER\Desktop\kitaplar\metin.txt',encoding="utf8") #metnin bulunduğu dosyayı oluşturur
r=dosya.read()
i=0
while(i<100): #döngüyü arayacağımız kelime sayısına göre başlatır
    x=r.count(str[i])
    print(str[i],"->",x)
    i+=1


