# for range(v) – range(vi,vf)  - range(vi,vf,inc)
frase = input("Ingrese frase: ")
for indice in range(len(frase)):
    print(indice, '=', frase[indice])
# for in cadena - in(tupla) – in[lista]
for car in frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ("A","E","I","O","U"):
            continue
        else:
            cvoc=0

            cvoc = cvoc + 1
print('cantidad vocales:{}'.format(cvoc))
# Comprehension – [var for var in datos condicion]
[car for car in['a','e','i','o','u'] if car not in('a','i','o')]


