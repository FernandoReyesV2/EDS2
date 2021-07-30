import re


class Cadena:
    def __init__(self, cadena):
        self.cadena1 = cadena

    def recorrerCadena(self):
        for i, caracter in enumerate(self.cadena1):
            print("Caracter ",caracter)

    def buscarCaracter(self, buscado):
        x = self.cadena1.find(buscado)
        if x != -1:
            return x
        else:
            return "error"

    def listaPosiciones(self, caracter):
        res=[]
        for pos1 in range(len(self.cadena1)):
            for pos2 in range(len(caracter)):
                if self.cadena1[pos1]==caracter[pos2]:
                    res.append(pos1)
        return res

    def listaPalabras(self):
        lista = self.cadena1.split()
        return lista

    def cadenaLista(self,lista):
        return "".join(map(str,lista))

    def insertarDato(self, buscado, posicion):
        lista = self.cadena1.split()
        lista.insert(posicion,buscado)
        return lista

    def eliminarOcurrencias(self, buscado):
        if buscado == str(buscado):
            elim = self.cadena1.split(buscado)
            return elim
        if buscado == int(buscado):
           return self.cadena1[:buscado] + self.cadena1[buscado+1:]

    def retornaValor(self, posicion):
        lista = list(self.cadena1)
        aux = lista[posicion]
        x = self.cadena1.replace(aux,"")
        return aux,x

    def concatenarCadena(self, dato):
        self.cadena1 = self.cadena1 + " "
        return self.cadena1 + dato

listaprueba = ["hola, lo unico que hay en este mundo",2,4,"hello"]
cadenaprueba = "Lo unico que hay en este mundo"
cadenaprueba2 = " en este mundo lo unico que hay"
cad = Cadena(cadenaprueba)
print(cad.recorrerCadena())
print("2 Buscar Caracter: ",cad.buscarCaracter("y"))
print("3 Retornar una lista con la posicion: ", cad.listaPosiciones("unico"))
print("4 Retornar una lista con las palabras de la cadena: ", cad.listaPalabras())
print("5 Lista a Cadena: ", cad.cadenaLista(listaprueba))
print("6 Insertar un dato: ",cad.insertarDato("insertado",2))
print("7 Eliminar ocurrencias: ",cad.eliminarOcurrencias(0))
print("8 Retornar cadena: ",cad.retornaValor(7))
print("9 Concatenar: ",cad.concatenarCadena(cadenaprueba2))
