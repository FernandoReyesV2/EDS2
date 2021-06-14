class ciclo:

    def __init__(self,numero=5):
        self.numero = numero
        self.numero2 = 0

    def usoWhile(self):
        car = input("ingrese vocal")
        car = car.lower()
        while car not in ("a","e","i","o","u"):
            car1 = input("ingrese vocal").lower()

        print("su vocal es")
