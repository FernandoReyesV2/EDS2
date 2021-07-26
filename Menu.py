import os
from calculadora import CalCientifica, CalEstandar

class Menu:
    def __init__(self,titulo,opciones):
        self.titulo=titulo
        self.opciones=opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija opcion[1...{}]: ".format(len(self.opciones)))
        return opc

opc = ""
while opc != "5":
    os.system("cls")
    men = Menu("Menu principal",["1.Calculadora","2.Operación Numeros","3.Tratamiento de Listas","4.Operaciones de Cadenas","5.Salir"])
    opc= men.menu()
    if opc == "1":
        opc1 = ""
        while opc1 != "10":
            os.system("cls")
            men1 = Menu("Menu Calculadora",["1.Suma","2.Resta","3.Multiplicacion","4.Divison","5.Exponente","6.Valor Absoluto","7.Circunferencia","8.Area Circulo","9.Area Cuadrado","10.Salir"])
            opc1 = men1.menu()
            if opc1 =="1":
                os.system("cls")
                print("Suma de dos numeros")
                n1 = int(input("ingrese numero1: "))
                n2 = int(input("ingrese numero2: "))
                cal = CalEstandar(n1,n2)
                print(("El resultado de {}+{}={}".format(n1,n2,cal.suma())))
                input("presiona una tecla para continuar...")

            elif opc1 == "2":
                os.system("cls")
                print("Resta de dos numeros")
                n1 = int(input("ingrese numero1: "))
                n2 = int(input("ingrese numero2: "))
                cal= CalEstandar(n1,n2)
                print("El resultado de la resta {}-{}={}".format(n1,n2,cal.resta()))
                input("presiona una tecla para continuar...")

            elif opc1 == "3":
                os.system("cls")
                print("Multiplicación de dos numeros")
                n1 = int(input("ingrese numero1: "))
                n2 = int(input("ingrese numero2: "))
                cal = CalEstandar(n1,n2)
                print("El resultado de la multiplicacion {}*{}={}".format(n1,n2,cal.multiplicacion()))
                input("presiona una tecla para continuar...")

            elif opc1 == "4":
                print("Divison de dos numeros")
                n1 = int(input("ingrese numero1: "))
                n2 = int(input("ingrese numero2: "))
                cal = CalEstandar(n1,n2)
                print("El resultado de la divison {}/{}={}".format(n1,n2,cal.division()))
                input("presiona una tecla para continuar...")

            elif opc1 == "5":
                print("Exponente de un numero")
                n1 = int(input("Ingrese base: "))
                n2 = int(input("Ingrese exponente: "))
                cal = CalEstandar(n1,n2)
                print("El resultado de {}**{}={}".format(n1,n2,cal.Exponente()))
                input("presiona una tecla para continuar...")

            elif opc1 == "6":
                print("Valor absoluto de un numero")
                numero = int(input("Ingrese un numero: "))
                cal = CalEstandar(0,0)
                print("El valor absoluto de {} es {}".format(numero, cal.valorAbsoluto(numero)))
                input("presiona una tecla para continuar...")

            elif opc1 == "7":
                print("La circunferencia del radio")
                radio = int(input("Ingrese el radio: "))
                cal = CalCientifica(0,0)
                print("La circunferencia del radio {} es {}".format(radio, cal.circunferencia(radio)))
                input("presiona una tecla para continuar...")

            elif opc1 == "8":
                print("El Area de un circulo")
                radio = int(input("Ingrese el radio: "))
                cal = CalCientifica(0,0)
                print("El area del circulo con el radio {} es {}".format(radio,cal.AreaCirculo(radio)))
                input("presiona una tecla para continuar...")

            elif opc1 == "9":
                print("El Area del cuadrado")
                lado = int(input("Ingrese el valor de un lado:"))
                cal = CalCientifica(0,0)
                print("El ara del cuadrado con los lados {} es {}".format(lado,cal.AreaCuadrado(lado)))
                input("presiona una tecla para continuar...")

            elif opc1 == "10":
                pass

            else:
                print("---Opcion no Valida---")
                input("presiona una tecla para continuar...")

    elif opc == "2":
        opc2 = ""
        while opc2 != 11:
            os.system("cls")
            men2 = Menu("Menu Operacion Numeros", ["1.Presentar los numeros de 1 a n", "2.Sumar los numeros de 1 a n", "3.Multiplo de cualquiera numero", "4.Presentar los divisores de  un numero","5.Numero Primo","6.Factorial de caulquier numero","7.Fibonacci de una serie de n numeros","8.Perfecto","9.Primos gemelos","10.Numeros amigos","11.Salir"])
            opc2 = men2.menu()
            if opc2 == "1":
                input("presiona una tecla para continuar...")

    elif opc == "10":
        print("Gracias por usar el sistema")
    else:
        print("---Opcion no valida---")

print("Lo esperamos en una proxima ocasion")



# menu2 = Menu("Menu listas",["1.recorrido","2.buscar","3.Salida"]
# menu2.menu()