class Ordernar:
    def __init__(self,lista):
        self.lista=lista

    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)

    def recorrerEnumarate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)

    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos,self.lista[pos])

    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                enc=True
                break
        if enc==True:return pos
        else:return -1
        pass

    def ordenarAs(self):
        for pos in range(len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

lista= [2,3,1,5,8,10]
ord1=Ordernar(lista)
#ord1.recorrerElemento()
#ord1.recorrerEnumarate()
#ord1.recorrerRange()
#print(or1.buscar(3))
#print(ord1.buscar((3))
#buscado=9
#resp=ord1.buscar()
#if resp!=1:
#   print("El numero {} se encuentra en la posicion ({}) de la lista{}".format(buscado,resp,ord1.lista))
#else:
#    print("El numero {} no se encuentra en la lista {}".format(buscado,ord1.lista))
print(ord1.lista)
ord1.ordenarAs()
print(ord1.lista)
