import requests #internetten veri cekmeyi saglar

url="https://api.fixer.io/latest?base="

birinci=input("Birinci Doviz:")

ikinci=input("Ikinci Doviz:")

miktar=float(input("Miktar:"))

response=requests.get(url+birinci)

json_verisi=response.json()

print(json_verisi["rates"][ikinci]*miktar)
