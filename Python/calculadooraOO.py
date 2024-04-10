class Calculadora:
    primer_numero = None
    segundo_numero = None
    resultado = 0.0
    historial = None

    def __init__(self, p, s):
        self.primer_numero = p
        self.segundo_numero = s
        self.resultado = 0.0
        self.historial = []

    def set_numero(self, p, s):
        self.primer_numero = p
        self.segundo_numero = s

    def get_suma(self):
        self.resultado = self.primer_numero + self.segundo_numero
        texto = str(self.primer_numero) + " + " + str(self.segundo_numero) + " = " + str(self.resultado)
        self.historial.append(texto)
        return self.resultado
    
    def get_resta(self):
        self.resultado = self.primer_numero - self.segundo_numero
        texto = str(self.primer_numero) + " - " + str(self.segundo_numero) + " = " + str(self.resultado)
        self.historial.append(texto)
        return self.resultado
    
    def get_resultado(self):
        return self.resultado

    def get_historial(self):
        return self.historial

if __name__ == "__main__":
    calc = Calculadora (12,15)
    print(calc.get_suma())
    calc.set_numero(10,10)
    print(calc.get_suma())
    calc.set_numero(100,99)
    print(calc.get_resta())
    print(calc.get_historial())
