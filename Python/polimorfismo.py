class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        return "Anda caminando"

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
 
    def avanza(self):
        return "Anda en bicicleta"

if __name__== "__main__":
    persona = Persona('Damian')
    print(persona.avanza())

    ciclista = Ciclista('Pedro')
    print(ciclista.avanza())