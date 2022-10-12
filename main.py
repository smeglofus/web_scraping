from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yb_webpage = response.text



#vyhledá název,url a počet hodnocení
soup = BeautifulSoup(yb_webpage, "html.parser")
nazev_hledej = soup.find_all(name="span", class_="titleline")

nazvy = []
odkazy = []
hodnoceni = []

for article in nazev_hledej:
    nazev = article.get_text()
    nazvy.append(nazev)
    url = article.find(name="a").get("href")
    odkazy.append(url)

pocty = soup.find_all(name="span", class_="score")
for pocet in pocty:
    pocet_bodu = pocet.get_text().split(" ")
    hodnoceni.append(int(pocet_bodu[0]))

print(nazvy)
print(odkazy)
print(hodnoceni)

index = hodnoceni.index(max(hodnoceni))
print(nazvy[index], odkazy[index], hodnoceni[index])