"""Ejercicio 10: Cargar dos listas de números A y B.
Se solicita construir e imprimir tres nuevas listas C, D y E que contengan:
• La concatenación de los valores pares de A con los impares de B.*
• La concatenación de los valores pares de A con el reverso de los valores pares de B.
("valores pares" o "valores impares" se refiere a los elementos propiamente dichos y no a sus posiciones).
• La intercalación de los elementos de A y B."""

import random
#Funcion cargar lista
def cargarlista():
    lista=[]
    n=int(input("ingrese numero:"))
    for i in range(n):
        lista.append(random.randint(0,30))
    print(lista)
    return lista

#func lista c
def listaC(listaa,listab):
    lista=[]
    for i in range(len(listaa)):
        if listaa[i]%2==0:
            lista.append(listaa[i])
    for j in range(len(listab)):
        if listab[j]%2==1:
            lista.append(listab[j])
    print(lista)
    


#func lista d
def listaD(listaa,listab):
    lista=[]
    for i in range(len(listaa)):
        if listaa[i]%2==0:
            lista.append(listaa[i])
    for j in range(len(listab)-1,0,-1):
        if listab[j]%2==0:
            lista.append(listab[j])
    print(lista)


#funnc lista e
def listaE(listaa,listab):
    lista=[]
    cont=0
    while cont<len(listaa) and cont<len(listab):
        lista.append(listaa[cont])
        lista.append(listab[cont])
        cont+=1
    if cont==len(listaa):
        for i in range(cont,len(listab)):
            lista.append(listab[cont])
            cont+=1
    else:
        for i in range(cont,len(listaa)):
            lista.append(listaa[cont])
            cont+=1
    print(lista)
    return lista
            



A=cargarlista()
B=cargarlista()
C=listaC(A,B)
D=listaD(A,B)
E=listaE(A,B)