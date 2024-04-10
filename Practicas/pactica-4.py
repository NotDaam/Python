usuarios_autenticados = {"Pedro":"123", "Damian":"321", "Pedrinho":"111"}

usuario = input("Ingrese su Usuario: ")
password = input("Ingrese su Contraseña: ")
intentos = 0

if usuario in usuarios_autenticados:
    while intentos < 3:
        if (usuarios_autenticados[usuario] == password):
            print("-Acceso Correcto")
            break
        else:
            print("--Contraseña Incorrecta")
            password = input("Vuelve a intertarlo: ")
            intentos += 1
            if intentos == 3:
                 print("--Intenta de nuevo más tarde. Si necesita ayuda con su contraseña, comuniquese con Soporte")
else:
    print("El Usuario no existe")
