class Tarea:
    def __init__(self):
        pass
    def calcularJornada(self):
        ht, he, het=0,0,0
        ph, phe, pt, ph8=0,0,0,0
        ht=int(input("Ingrese horas trabajadas: "))
        ph=float(input("Ingrese pago por horas: "))
        if ht > 40:
            he= ht-40
            if he > 8:
                het= he-8
                ph8= 8*ph*2
                phe= het*ph*3
            else:
                phe=0
                ph8=he*ph*2
            pt = 40*ph+ph8+phe
        else:
            pt=ht*ph
        print("Sobretiempo<8:{} Sobretiempo>8:{} Jornada:{} ".format(ph8,phe,pt))

    def factorial(self):
        n=int(input("Ingrese la cantidad de numeros: "))
        for i in range(n):
            num=int(input("Ingrese numero: "))
            acum=1
            for numero in range(num,1,-1):
                acum=acum*numero
            print("Numero={} Factorial={}".format(num,acum))


tarea=Tarea()
#tarea.calcularJornada()
tarea.factorial()