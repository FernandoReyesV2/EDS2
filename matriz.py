class Matriz:
    def __init__(self,matriz):
        self.matriz = matriz

    def ingresar(self,dato):
        pass

    def presentar(self):
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                #print(columna[col],end=" ")
                print(self.matriz[fila][col],end=" ")
            print("")

numeros = [[10,20,30],[60,80,90],[25,35,55]]
# print(numeros[0],numeros[0][1])
mat = Matriz(numeros)
mat.presentar()