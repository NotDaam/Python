notas= []
suma = 0
for x in range(3):
    nota = int(input("Ingrese la nota: "))
    notas.append(nota)
    suma = suma + nota

promedio = suma / 3
print(notas)
print(f"Promedio: {promedio}")
if promedio < 1.7:
    print("Reprobado")
else:
    print("Aprobado")


