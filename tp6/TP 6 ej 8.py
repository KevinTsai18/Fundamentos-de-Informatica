"""Ejercicio 8: Rellenar una lista con números enteros entre 0 y 100
obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa.
Tener en cuenta que el mínimo puede estar repetido,
en cuyo caso deberán mostrarse todas las posiciones que ocupe.
La carga de datos termina cuando se obtenga un 0 como número al azar,
el que no deberá cargarse en la lista."""

import random
#func ordenamiento
def seleccion(V):
    largo=len(V)
    j=0
    for i in range(largo-1):
        for j in range(i+1,largo):
            if V[i]>V[j]:
                aux=V[i]
                V[i]=V[j]
                V[j]=aux
    return V








#prog ppal
lista=[]
n=-1
while n!=0:
    n=random.randint(0,100)
    if n!=0:
        lista.append(n)
print(lista)
lista=seleccion(lista)
print()
print(lista)
print(lista[0])
largo=len(lista)
for c in range(largo):
    if lista[c]==lista[0]:
        print("Se encuentra en la posición", c)