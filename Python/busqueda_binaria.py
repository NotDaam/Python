import random

def busqueda_binaria (lista, comienzo, final, valor_buscado):
    print (f'--- buscando {valor_buscado} entre {lista[comienzo]} y {lista[final - 1]}')

    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista [medio] == valor_buscado:
        print(f'Encontró {valor_buscado} Lista: {lista[medio]} Medio: {medio}')
        return True
    elif lista [medio] < valor_buscado:
        print(f'Buscando menor {valor_buscado} Lista: {lista[medio]} Medio: {medio} medio+1 {medio +1}')
        return busqueda_binaria(lista, medio + 1, final, valor_buscado)
    else:
        print(f'Buscando mayor {valor_buscado} Lista: {lista[medio]} Medio: {medio} medio-1 {medio -1}')
        return busqueda_binaria(lista, comienzo, medio - 1, valor_buscado)
    
if __name__ == '__main__':
    tamano_lista = int(input("Ingrese el tamaño de la lista: "))
    valor_buscado = int(input("Ingresa el valor que desee buscar en la lista: "))
    lista = []

    for i in range(tamano_lista):
        lista.append (random.randint(0, tamano_lista))

    lista = sorted(lista)
    
    existe = busqueda_binaria(lista, 0, len(lista), valor_buscado)

    print(lista)
    print(f"El número {valor_buscado} {"existe" if existe else "no está"} en la lista")
