class Persona:
    _siguiente = 0

    def __init__(self, nom, ced="9999999999", act=True):
        self.nombre = nom
        self.cedula = ced
        self.activo = act

    def mostrar(self):
        return " Nombre: {} - Cedula: {} ".format(self.nombre, self.cedula)


per1 = Persona("Daniel")
per2 = Persona("Erick",'0912314569',False)

personas = []

for c in range(2):
    nom = input("Ingrese Nombre")
    ced = input("Ingrese Cedula")
    per = Persona(nom,ced)
    personas.append(per)

for person in personas:
    print(person.mostrar())

class Empleado(Persona):
    def __init__(self,nom,ced,act,sueldo=400):
        Persona.__init__(self,nom,ced,act)
        self.__sueldo=sueldo

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, sue):
        self.__sueldo = sue


def __jornada(self):
    return self.sueldo / 30 * 7


emp = Empleado("Daniel", "0924192213", False, 500)
print(emp.mostrar() + " - Sueldo:" + str(emp.sueldo))


class Empleado(Persona):

    def __init__(self, nom, ced, act, sueldo=400):
        super(nom, ced, act)
        self.sueldo = sueldo

    def __jornada(self):
        return self.sueldo / 30 * 7

    def __jornada(self, dias=None):
        return self.sueldo if dias == None else self.sueldo / 30 * dias

    def mostrar(self):
        datos = super().mostrar()
        jornada1 = self.__jornada()
        jornada2 = self.__jornada(15)
        return "{} Jornada Semanal: ${:.2f} – Jornada Extra: ${:.2f}".format(datos,jornada1,jornada2)


emp = Empleado("Daniel", "0924192213", True)
emp.sueldo = 600
print(emp.mostrar() + " Sueldo:" + str(emp.sueldo))
