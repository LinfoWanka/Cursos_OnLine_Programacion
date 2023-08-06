# Creando una clase en Python
# Clases, objetos y metodos
# Herencia con Python

# clase padre
class calcularIMC:
    def __init__(self,peso,estatura): # constructor por default / self es el propio dato de esa clase
        self.peso=peso
        self.estatura=estatura

    def imprimirIMC(self):
        self.imc=self.peso/(self.estatura*self.estatura)
        print("El IMC es: " +str(self.imc))

# clase hija
# Herencia (proviene de la clase padre llamada calcularIMC) Hereda caracteristicas y acciones o funciones
class motrarPesoIdeal(calcularIMC): # recibe datos de la clase padre
    def imprimirPeso(self):
        if self.imc < 18.5:
            print("Peso Bajo")
        else:
            if self.imc >18.5 and self.imc < 29.9:
                print("Peso Normal")
            else:
                if self.imc > 29.9:
                    prin("Obesidad")


# Instancia (creacion de un objeto a partir de una clase)
objCalcularIMC=calcularIMC(80,1.7)
objCalcularIMC.imprimirIMC()

obj2CalcularIMC=calcularIMC(50,1.7)
obj2CalcularIMC.imprimirIMC()

obj3CalcularIMC=motrarPesoIdeal(30,1.7)
obj3CalcularIMC.imprimirIMC()
obj3CalcularIMC.imprimirPeso()

