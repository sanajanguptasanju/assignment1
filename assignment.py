import requests
from bs4 import BeautifullSoup4

req=requests.get("https://en.wikipedia.org/wiki/S")

soup=BeautifullSoup(req,'html')
sum=soup.find_all('div',class_="mw-parser-output")

l==17
for l in range(17,50):
    print(sum.select("p:nth-of-type")("+str(l)+"))
