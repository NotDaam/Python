#Tipos de Strings

nombre = "Damian"
password = 123

print("Su nombre es ", nombre, " y su contraseña ", password)
print("Su nombre es " + nombre + " y su contraseña " + str(password))
print("Su nobre es {} y su contraseña {}".format(nombre, password))
print("Su nombre es %s y su contraseña %d" % (nombre, password))
print(f"Su nombre es {nombre} y su contraseña {password}")