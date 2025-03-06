"""Ejercicio 15: Leer dos listas de números M y N, ambas ordenadas de menor a mayor.
Generar e imprimir una tercera lista que resulte de intercalar los elementos de M y N.
La nueva lista también debe quedar ordenada, sin utilizar ningún método de ordenamiento."""
import random

#funcion ordenar
def ordenar(lista):
    for i in range(1,len(lista)):
        aux=lista[i]
        j=i
        while j>0 and lista[j-1]>aux:
            lista[j]=lista[j-1]
            j=j-1
        lista[j]=aux
    return lista






# funcion ingresar lista
def ingresarlista():
    lista=[]
    for i in range(8):
        lista.append(random.randint(0,50))
    ordenar(lista)
    print(lista)
    return lista

#funcion intercalar listas
def intercalar(v1,v2):
    lista=[]
    k=0
    l=0
    while k<len(v1) and l<len(v2):
        if v1[k]<v2[l]:
            lista.append(v1[k])
            k=k+1
        else:
            lista.append(v2[l])
            l=l+1
    if k==len(v1):
        while l<len(v2):
            lista.append(v2[l])
            l=l+1
    else:
        while k<len(v1):
            lista.append(v1[k])
            k=k+1 
    print(lista)




#prog ppal
M=ingresarlista()
N=ingresarlista()
P=intercalar(M,N)