"""Ejercicio 11: Dada una lista ordenada de números llamada A y un nuevo número N,
desarrollar un programa que agregue el elemento N dentro de la lista A,
respetando el ordenamiento existente.
El programa deberá detectar automáticamente si el ordenamiento es ascendente o descendente antes de realizar la inserción."""
import random

#Func cargarlista
def cargarlista():
    lista=[]
    #for i in range(10):
        #lista.append(random.randint(0,20))
    n=int(input("Ingrese un numero:"))
    while n!=-1:
        lista.append(n)
        n=int(input("Ingrese un numero:"))
    print(lista)
    return lista



#Func ordenar asc
def ordenarasc(listaA):
    lista=[]
    for h in range(len(listaA)):
        lista.append(listaA[h])
    desord=True
    while desord:
        desord=False
        for i in range(len(listaA)-1):
            if lista[i]>lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                desord=True
    print(lista)
    return lista


#func ordenardesc
def ordenardesc(listaA):
    lista=[]
    for h in range(len(listaA)):
        lista.append(listaA[h])
    desord=True
    while desord:
        desord=False
        for i in range(len(listaA)-1):
            if lista[i]<lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                desord=True
    print(lista)
    return lista


#metodo insercion
def metodoinsercionasc(lista):
    for i in range(1,len(lista)):
        aux=lista[i]
        j=i
        while j>0 and lista[j-1]>aux:
            lista[j]=lista[j-1]
            j=j-1
        lista[j]=aux
    print(lista)
    
    
    
def metodoinserciondesc(lista):
    for i in range(1,len(lista)):
        aux=lista[i]
        j=i
        while j>0 and lista[j-1]<aux:
            lista[j]=lista[j-1]
            j=j-1
        lista[j]=aux
    print(lista)




#Prog ppal
A=cargarlista()
Aasc=ordenarasc(A)
Adesc=ordenardesc(A)
N=int(input("Ingrese un número:"))
for i in range(len(A)):
    if A[i]==Aasc[i]:
        ordenascendente=True
    else:
        ordenascendente=False
for j in range(len(A)):
    if A[j]==Adesc[j]:
        ordendescendente=True
    else:
        ordendescendente=False
if ordenascendente==True and ordendescendente==False:
    A.append(N)
    metodoinsercionasc(A)
elif ordendescendente==True and ordenascendente==False:
    A.append(N)
    metodoinserciondesc(A)




