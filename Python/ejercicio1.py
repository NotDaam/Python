edad = 0
estatura = 0.0
peso = 0
nombre = ""

nombre = input("Hola, como te llamas? ")
edad = int(input("Que edad tines? "))
estatura = float (input("Cual es tu estatura? "))
peso = float (input("Cual es tu peso en kg? "))
imc = peso/(estatura*estatura)

print("Su imc es: ", imc)

if (edad >= 18 and edad <= 70):
    print("Es mayor de edad")
elif (edad < 18 and edad >= 11):
    print("Eres menor de edad")
else:
    print("Datos no validos ")
    