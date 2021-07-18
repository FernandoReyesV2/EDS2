#FUNCION CON RETORNO DE VALOR
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
        return summ/len(notas)

#LLAMADA A FUNCION
listanotas = [2,4,6,8,10]
prom = promedio(listanotas)
print("Primedio {}= {}".format(listanotas,prom))

class Notas:
    def promedio(self,notas):
        summ = 0
        for n in notas:
            summ += n
            return summ / len(notas)

#LLAMADA DEL METODO
listanotas=[2,4,6,8,10]
nota1 =Notas()
prom=nota1.promedio(listanotas)
print(listanotas, prom)