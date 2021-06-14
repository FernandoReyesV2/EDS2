class For:
    def __init__(self):
        pass

    def usoFor(self):
        #ciclo repetitivo de incrementos o decrementos se ejecuta por verdadero
        nombre= "Daniel"
        datos = ["Daniel", 50, True]
        numeros = (2,4,6,8)
        docente = {"nombre":"Daniel","edad":50,'fac':'faci'}
        listaNotas = [(30,40),(20,40),(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady", "final":"60"},{"nombre":"Danny","final":90}]
        #se ejecuta desde inicio hasta el limite
        #for con range() o for con colecciones
        #for i in range(5): #rango (0,1,2,3,4)
        #    print(i,end=" ")
        #print()
        #for i in range(1,5):  # rango (1,2,3,4)
        #    print(i,end=" ")
        #print()
        #for i in range(2,10,2):  # rango (2,4,6,8)
        #    print(i,end=" ")
        #print()
        #for i in range(12,3,-3): #rango (12,9,6)
        #    print(i,end=" ")

        #lon = len(nombre)
        #for pos in range(lon):
        #    print(pos, nombre[pos])
        #lon= len(nombre)
        #for pos in range(lon):
        #    if pos%2 == 0 and pos !=0:
        #        print(pos, nombre[pos])
        #vocal = ("a","e","i","o","u")
        #for elem in datos:
        #    print(elem, end=" ")
        #for elem in nombre:
        #    print(elem, end=" ")

        #lon = len(datos)
        #for pos in range(lon):
        #        print(pos, datos[pos])

        #for pos, valor in enumerate(datos):
        #   print(pos, valor)

        #for clave,valor  in docente.items():
        #    print(clave, valor,end=" ")

        #for  notas in listaNotas:
        #    for nota in notas:
        #        print (nota, end=" ")
        #    print("saliendo del for interno")

        #print(listaNotas)
        #for notas in listaNotas:
        #    acum=0
        #    for nota in notas:
        #        acum=acum+nota
        #    print(acum/len(notas),end=" ")

        print("\ndicionario de notas")
        print(listaAlumnos)
        for alumnos in listaAlumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave, ":", valor, end=" ")
            print()



bucle = For()
bucle.usoFor()