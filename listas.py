class Lista:
    def __init__(self,tam=3):
        self.lista=[]
        self.longitud = 0
        self.size = tam

    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
        else:
            print("Lista está llena")

    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]

    def obtenerEliminando(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado = self.lista[pos]
            #self.lista[pos] = self.lista[:pos] + self.lista[pos+1:]
            listaAux = []
            for ind in range(pos):
                listaAux += [self.lista[ind]]
            for ind in range(pos+1,self.longitud):
                listaAux += [self.lista[ind]]
            self.longitud -= -1
            self.lista[pos] = listaAux
            return [self.lista,eliminado]

    def mostrar(self):
        print("{:3}{:9}{}".format("","lista","posicion"))
        for pos, ele in enumerate(self.lista):
            print("[{:10}] {:3}".format(ele,pos))

lista1 = Lista()
lista1.append("Daniel")
lista1.append(52)
lista1.append(True)
#lista1.append("Milagro")
#lista1.mostrar()
lista1.mostrar()
posicion = int(input("Ingrese posicion para obtener: "))
resp = lista1.obtenerEliminando(posicion)
if resp == None:
    print("Posicion no Valida. verifique la lista...!!!")
else:
    print("El elemento de la posicion: {} indicado es: {} ".format(posicion,resp))
