import urllib.request
from bs4 import BeautifulSoup
import re

url_base = "https://lopezobrador.org.mx/transcripciones/page/"

lista_discursos = []

for pagina in range(1,200):
    html_page = urllib.request.urlopen(url_base + str(pagina))
    soup = BeautifulSoup(html_page,features="lxml")

    for link in soup.findAll('a', attrs={'href': re.compile("^https://lopezobrador.org.mx/20")}):
        lista_discursos.append(link.get('href'))

    print(f"Pagina: {pagina}")


lista_discursos = list(dict.fromkeys(lista_discursos))
print(f"Discursos: " + str(len(lista_discursos)))
count = 0
for discurso in lista_discursos:
    html_page = urllib.request.urlopen(discurso)
    soup = BeautifulSoup(html_page,features="lxml")
    text = soup.find_all('p')
    f = open(f"texto/disc_{count}.txt", "w")

    for elem in text:
        f.write(elem.get_text() + "\n")

    f.close()
    count = count + 1
