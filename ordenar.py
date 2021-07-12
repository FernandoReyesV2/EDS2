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

    def ordernarDes(self):
        for pos,ele in enumerate(self.lista):
            for sig in range(pos+1,len(self.lista)):
                if ele < self.lista[sig]:
                    aux=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

    def primer(self):
        return self.lista[0]

    def primerEliminado(self):
        primer=self.lista[0]
        auxlista=[]
        for pos in range(1,len(self.lista)):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return primer

    def primerEliminado2(self):
        primer = self.lista[0]
        self.lista=self.lista[1:]
        return primer

    def ultimo(self):
        return self.lista[-1]

    def insertar(self,num):
        self.ordenarAs()
        auxlista=[]
        for pos, ele in enumerate(numeros):
            if num < ele:
                break
        self.lista=self.lista[0:pos]+auxlista+self.lista[pos:]

    def insertar2(self,num):
        self.ordenarAs()
        auxlista=[]
        for pos, ele in enumerate(self.lista):
            if num < ele:
                break
        for i in range(pos):
            auxlista.append(self.lista[i]):
        auxlista.append(num)
        for j in range(pos, len((self.lista))):
            auxlista.append(self.lista[j])
        self.lista + auxlista

    def insetarOrden(self,num):
        self.lista.append(num)
        self.ordenarAs()

    def eliminar(self,num):
        enc=False
    for pos, ele in enumerate(self.lista):
        if num == ele:
            enc=True
            break
    if enc: self.lista=self.lista[0:pos]+self.lista[pos+1:]
    return enc

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
#print("Primer",ord1.primer())
#print("Ultimo",ord1.ultimo())
#print("Normal", ord1.lista)
#ord1.ordenarAs()
#print("Ascendente",ord1.lista)
#ord1.ordernarDes()
#print("Descendente",ord1.lista)
lista= [2,3,1,5,8,10]
# ord1=Ordernar(lista)
# print(ord1.lista)
# print("Primer Eliminado",ord1.primerEliminado())
# print(ord1.lista)
ord1=Ordernar(lista)
if ord1.eliminar(8)==True: print("El numero se elimino de la lista",ord1.lista)
else: print("El numero no se encuentra en la lista")