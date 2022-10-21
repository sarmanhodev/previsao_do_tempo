import requests
from bs4 import BeautifulSoup

while True:
    search=str(input("\nBusca por cidade ou país =>  "))

    url=f"https://www.google.com/search?&q=Weatherin{search}"

    r = requests.get(url)
    s = BeautifulSoup(r.text,"html.parser")
    update= s.find("div", class_="BNeawe").text

    print(update)