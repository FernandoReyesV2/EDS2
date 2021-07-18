#FUNCIONES SIN RETORNO
def mensaje():
    frase = "hola que tal"
    for car in frase:
        print(car)
def vocales (frase):
    for car in frase:
        if car in ("a","e","i","o","u"):
            print(car)

#LLAMADA A FUNCIONES
mensaje()
oracion = input("Ingrese oracion: ")
vocales(oracion)

#METODOS SIN RETORNO
class Cadena:
    def mensaje(self):
        frase = "hola que tal"
        for car in frase:
            print(car)

    def vocales(self,frase):
        for car in frase:
            if car in ("a","e","i","o","u"):
                print(car)

#LLAMDA A METODOS
cad = Cadena()
cad.mensaje()
cad.vocales("Hola que tal")








