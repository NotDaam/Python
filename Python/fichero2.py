from urllib import request
from urllib.error import URLError

def ver_contenido(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('La URL ' + url + ' no existe')
    else:
        contenido = f.read()
        return contenido

def contar_palabra(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('La URL ' + url + ' no existe')
    else:
        contenido = f.read()
        return len(contenido.split())
    
url = 'https://es.wikipedia.org/wiki/Python'
print(ver_contenido(url))
print("\n------------------------------------------\n")
print(f'Hay {contar_palabra(url)} palabras')