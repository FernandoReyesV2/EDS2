class condicion:

    def __init__(self,num1,num2):
        self.numero1 = num1
        self.numero2 = num2
        numero = self.numero1 + self.numero2
        self.numero3 = numero

    def usoIf(self):
        print(self.numero3)

print("instancia de la clase")
cond1 = condicion(10,20)
cond1.usoIf()
print("Fin del programa")