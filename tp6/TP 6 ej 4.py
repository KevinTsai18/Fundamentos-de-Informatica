"""Ejercicio 4: Invertir aquellos valores ubicados en posiciones impares de una lista (EJ1)."""



#Func
def serie1_20():
    lista=[]
    n=int(input("Ingrese un número entre 1 y 20:"))
    if n==-1:
        print("No se ingresaron datos")
    else:
        while n!=-1:
            while n>20 or n<1:
                n=int(input("Error. Ingrese un número entre 1 y 20:"))
            lista.append(n)
            n=int(input("Ingrese un número entre 1 y 20:"))
    return lista



#Prog ppal.
lista_ej4=serie1_20()
print(lista_ej4)
largo=len(lista_ej4)
largo=largo-1
if largo%2==0:
    for p in range(0,largo//2,2):
        temporal=lista_ej4[largo]
        lista_ej4[largo]=lista_ej4[p]
        lista_ej4[p]=temporal
        largo=largo-2
else:
    for p in range(0,largo//2,2):
        temporal=lista_ej4[largo-1]
        lista_ej4[largo-1]=lista_ej4[p]
        lista_ej4[p]=temporal
        largo=largo-2
print(lista_ej4)