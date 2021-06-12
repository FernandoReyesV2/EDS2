"""num=20
nombre="ana"
print(num,type(num))
print(nombre,type(nombre))

def mensaje(msg):
    print(msg)

mensaje("mi primer programa en python")
mensaje2("mi segundo programa en python")"""


class sintaxis:
    instancia =0 #atributo clase

    #__init__ metodo constructor
    def __init__(self,dato= "llamando al constructor"):
        self.frase=dato #atributo de instancia
        sintaxis.instancia = sintaxis.instancia+1

    def usoVariables(self):
        edad,_peso=50, 70.5
        nombres = "Daniel Vera"
        tipo_Sexo = "M"
        civil = true
        #tuplas = ()
        usuario=()
        usuario=("dchiki", "1234", "chiki@gmail.com")
        #usuario[3]="milagro"
        #listas = [] coleciones mutables
        materias = []
        materias = ["programacion web", "php", "poo"]
        aux=materias[1]
        materias[1]="python"
        materias.append("go")
        #print(materias,aux, materias[1])
        #diccionario = {}
        docente = {}
        docente = {"nombre":"Daniel", "edad": 50, "activo": true}
        edad = docente["edad"]
        docente["edad"] = 51
        docente["carrera"]="IS"
        #print(docente, edad, docente["edad"])
        #print(usuario,usuario[0],usuario[0:2],usuario[-1])
        print(materias, materias[2:], materias[:3])
        #presentacion con format
        #print(""mi nombre es {}, tengo ´{} años"".format(nombres, edad))



#print("sintaxis antes de instancia es: {}".format(sintaxis.instancia))
ejer1 = sintaxis() #instancia la clase sintaxis y crea el objeto
#print("sintaxis de  ejer 1 es: {}".format(sintaxis.instancia))
#ejer2 = sintaxis("instancia2")
#print(ejer1.frase)
#print("sintaxis de ejer2e es: {}".format(sintaxis.instancia))
#print("sintaxis nuevamente de ejer es:  {}".format(sintaxis.instancia))
#print(ejer2.frase)