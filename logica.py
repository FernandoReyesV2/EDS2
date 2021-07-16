class Ejercicios:
    def __init__(self,datos):
        self.lista = datos

    def parImpar(self,numero):
        if numero%2 ==0:
            print("{} es par".format(numero))
        else:
            print("{} es impar".format(numero))

    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu = acu + i
            if numero == acu:
                print("{} es Perfecto".format(numero))
            else:
                print("{} no es perfecto".format(numero))

    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
             acu = acu + i
        return acu

    def divisores(self, num):
        cont = 1
        divisores = []
        while cont < num:
            rec = num % cont
            if rec == 0:
                divisores.append(cont)
            cont = cont + 1
        print(divisores)

class Programacion(Ejercicios):
    def __init__(self,valor):
        super().__init__(valor)
        self.dato = valor

    def divisores(self,num):
        divisores = []
        for cont in range(1, num):
            rec = num % cont
            if rec == 0:
                divisores.append(cont)
        return divisores


prog1 = Programacion(20)
print(prog1.divisores(4))
print(prog1.lista)


# div = prog1.divisores(6)
# lista = [1,2]
# lista2 = lista + div
# print(lista2)


# num = 6
# if prog1.perfecto2(num) == num:
#     print(num, "Es perfecto")
# else:
#     print(num, "No es perfecto")
# numeros = [3,6,24,28]
# perfectos = []
# for numero in numeros:
#     if prog1.perfecto2(numero) == numero:
#         perfectos.append(numero)
# print(perfectos)

# ejer = Ejercicios()
#num = int(input("Ingrese un numero: "))
#print("llamada 1")
#resp = ejer.perfecto2(num)
#if num == resp:
#    print("{} es Perfecto".format(num))
# else:
#    print("{} no es perfecto".format(num))
#input()
# lista = [3,5,6,8,24]
# print("llamada 2")
# perfectos=[]
# for num in lista:
#     if ejer.perfecto2(num)==num:
#         perfectos.append(num)
# print(perfectos)
#ejer.perfecto(num)
#input()
#print("llamada  3")
# ejer.perfecto(23)