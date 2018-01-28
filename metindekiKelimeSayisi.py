
list=open("C:\\Users\USER\Desktop\kelimeler.txt","r")
str=list.read().split('\n')
print("\nMetinde Aranan Kelimeler:\n")
print(str)
print("\nMetindeki kelimelerimizin sayısı:\n")
dosya=open('C:\\Users\SUMEYRA\Desktop\kitaplar\metin.txt',encoding="utf8")
r=dosya.read()
i=0
while(i<100):
    x=r.count(str[i])
    print(str[i],"->",x)
    i+=1


