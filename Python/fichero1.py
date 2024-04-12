texto = input("Introdice un texto: ")
nombre_fichero = 'archivo-' + texto + '.txt'
f = open(nombre_fichero, 'w')

for x in range(100):
    f.write(f'{texto} {x}\n')

f.close()