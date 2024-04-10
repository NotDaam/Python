edad = int(input("Ingrese su edad "))

if (edad >=15 and edad < 18):
    print("Licencia con permiso de los padres")
elif (edad >= 18 and edad < 65):
    print("Licencia standard")
elif (edad >=65 and edad < 75):
    print("Debes elaborar un examen psicotecnico")
else:
    print("No puedes tener una licencia de conducir")

print("-------------------------------")

nro1 = int(input("Ingrese el primer número: "))
nro2 = int(input("Ingrese el segundo número: "))

if(nro1 > nro2):
    print(f"{nro1} es mayor que {nro2}")
    if(nro1 % 2 == 0):
        print("El nro es par")
    else:
        print("El nro es impar")
elif(nro1 < nro2):
    print(f"{nro2} es mayor que {nro1}")
    if(nro2 % 2 == 0):
        print("Es nro par")
    else:
        print("En nro impar")
else:
    print("Los nros ingresados son iguales")

print("----------------------------------------")

usuario = input("Ingrese su Usuario: ")
password = int(input("Ingrese su contraseña: "))

if(usuario == "Admin" and password == 123):
    print("Acceso correcto")
else:
    print("Acceso denegado")