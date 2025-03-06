"""Ejercicio 19: A partir de la lista SECUENCIAS generada en el ejercicio anterior,
imprimir la secuencia más larga almacenada en la misma.
Si hubiera varias secuencias con la misma longitud máxima deberán mostrarse todas las que correspondan."""

import random

#Func cargar lista random
def listarandom(N):
    lista=[]
    for c in range(N):
        lista.append(random.randint(1,20))
    return lista


#Func secuencias:
def funcsec(lista):
    largo=len(lista)
    SECUENCIAS=[]
    LIM=20
    for i in range(largo):
        if lista[i]<=LIM:
            SECUENCIAS.append(lista[i])
            LIM=LIM-lista[i]
        else:
            SECUENCIAS.append(0)
            LIM=20
            SECUENCIAS.append(lista[i])
            LIM=LIM-lista[i]
    return(SECUENCIAS)

#Func calcular mayor secuencias
def calcmayor(sec):
    largosec=len(sec)
    lista1=[]
    mayorlista=[]
    for j in range(largosec):
        if sec[j]!=0:
            lista1.append(sec[j])
        else:
            if len(lista1)>=len(mayorlista):
                mayorlista=lista1
                #print(mayorlista)
            lista1=[]
    lista2=[]
    for k in range(largosec):
        if sec[k]!=0:
            lista2.append(sec[k])
        else:
            if len(lista2)==len(mayorlista):
                print(lista2)
            lista2=[]


#Prog ppal
N=int(input("Ingrese la cantidad de números enteros:"))
lista=listarandom(N)
print(lista)
SECUENCIAS=funcsec(lista)
print(SECUENCIAS)
calcmayor(SECUENCIAS)