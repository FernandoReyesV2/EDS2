class Cadena:
    def __init__(self, cadena):
        self.cadena1 = cadena

    def recorrerCadena(self):
        for i, caracter in enumerate(self.cadena1):
            print(i, caracter)

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

    def cadenaLista(self):
        pass

    def insertarDato(self, buscado, posicion):
        x = self.cadena1.replace(buscado, posicion)
        return x

    def eliminarOcurrencias(self, buscado):
        elim = self.cadena1.split(buscado)
        return elim

    def retornaValor(self, posicion):
        aux = []


    def concatenarCadena(self, dato):
        self.cadena1 = self.cadena1 + " "
        return self.cadena1 + dato


#cadenaprueba = "Lo unico que hay en este mundo"
#cad = Cadena(cadenaprueba)
#print("primero: ",cad.recorrerCadena())
# print("Buscar Caracter: ",cad.buscarCaracter("y"))
#print("Retornar una lista con la posicion: ", cad.listaPosiciones("unico"))
#print("Retornar una lista con las palabras de la cadena: ", cad.listaPalabras())
#print("Insertar un dato: ",cad.insertarDato("mundo","PUTA"))
#print("Eliminar ocurrencias: ",cad.eliminarOcurrencias("hola"))
# print("Concatenar: ",cad.concatenarCadena("jalabola"))
