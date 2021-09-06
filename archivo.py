class Texto:
    def __init__(self,nombreArchivo):
        self.archivo = nombreArchivo
        self.separador = separador

    def read(self):
        try:
            with open(self.archivo, 'r', encoding="UTF-8") as file:
                lista=[]
                for linea in file:
                    line = linea[:-1].split(self.separador)
                    print(linea[:-1])


    def write(self,datos,modo):
        with open(self.archivo, modo, encoding="UTF-8") as file:
            for dato in datos:
                file.write(dato+"\n")


arch1=Texto("estudiantes.txt")
arch1.write(["Marcos Vera","Ana Bohorquez","Miguel Vera"],"a")
arch1.read()
