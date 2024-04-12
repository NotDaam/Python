from urllib import request
from urllib.error import URLError

list_palabras = ["Bellaco", "Inútil", "Tonto", "Puto", "Miseria", "Sonso", "Baboso"]
def palabras_ofensivas(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('La URL ' + url + ' no existe')
    else:
        contenido = f.read()
        pagina = contenido.split()
        palabras = []
        for l in list_palabras:
            for con in pagina:
                if l in con.decode():
                    palabras.append(l)

        return palabras
         
url = 'https://www.revistagq.com/la-buena-vida/articulos/221-insultos-en-castellano-que-deberias-saber/19728'
print(palabras_ofensivas(url))