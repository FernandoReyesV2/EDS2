import os
def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def borrarPantalla():
    os.system("cls")

def mensaje(msg,f,c):
    pass

gotoxy(20,3);print("Menu Principal")
gotoxy(18,4);print("1) Pilas")
gotoxy(18,5);print("2) Colas")
gotoxy(18,6);print("3) Colas")
gotoxy(18,8);print("Elija Opcion:[1...3]: ")
gotoxy(39,8);
opc = input()