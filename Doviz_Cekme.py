from  bs4 import BeautifulSoup
import requests


## **** Dolar Kuru ****
url1= "https://www.google.com/finance/quote/USD-TRY?h1=tr"

sayfa = requests.get(url1)

html_sayfa=BeautifulSoup(sayfa.content, "html.parser")
dolar=html_sayfa.find("div",class_="YMlKec fxKbKc").getText()
print(dolar)
roundeddolar= round (float(dolar.replace(",",".")),2)
print(roundeddolar)
dolarmessage="Dolar = " + str(roundeddolar) + "TL"
print(dolarmessage)

## **** EUR Kuru ****
url2= "https://www.google.com/finance/quote/EUR-TRY"

sayfa2 = requests.get(url2)

html_sayfa2=BeautifulSoup(sayfa2.content, "html.parser")
euro=html_sayfa2.find("div",class_="YMlKec fxKbKc").getText()
print(euro)
roundedeuro= round(float(euro.replace(",",".")),2)
print(roundedeuro)
euromessage="Euro = " + str(roundedeuro) + "TL"
print(euromessage)