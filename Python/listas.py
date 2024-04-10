calificaciones = [1,2,3,4,5]
alumnos = ["Damian", "Len", "Fabrizio", "Axel", "Ivan"]
lista_variada = [True, False, "No Pasó", [4.5, 3.5]]

print("Estudiante: ", alumnos[1])
print("Calificacion. ", calificaciones[3])
print("Lista dentro de otra: ", lista_variada[3][0])
print("Imprimir un rango o slices: ", alumnos[1:2])
print(lista_variada)

alumnos.append("Isaias")
print(alumnos)

alumnos.remove("Axel")
print(alumnos)
