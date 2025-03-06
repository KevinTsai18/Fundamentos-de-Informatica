"""Desarrollar un programa que genere un número entero al azar de cuatro cifras
y proponerle al usuario que lo descubra,
ingresando valores repetidamente hasta hallarlo.
En cada intento el programa mostrará mensajes indicando si el número ingresado es mayor o menor que el valor secreto.
Permitir que el usuario abandone al ingresar -1.
Informar la cantidad de intentos realizada al terminar el juego,
haciendo que el usuario ingrese su nombre ###si mejoró la mejor marca de intentos obtenida hasta el momento.###
Luego mostrar la lista de los 5 mejores puntajes y preguntar si se desea jugar otra vez,
reiniciando el juego en caso afirmativo."""

import random

#Func checkear numero con secreto
def checknum(secreto,ingreso):
    if ingreso>secreto:
        print("El número que ingresó es mayor al secreto")
    elif ingreso<secreto:
        print("El número que ingresó es menor al secreto")


#Func juego
def funcjuego(cantpunt,intentos,puntos,n,listanombre):
    while n!=-1:
        n=int(input("Ingrese el número que cree que es:"))
        NS=random.randint(1000,9999)
        #print(NS)
        while n!=NS and n!=-1:    
            checknum(NS,n)
            n=int(input("Ingrese el número que cree que es:"))
            intentos=intentos+1
        if n==NS:
            print("Número encontrado!")
            cantpunt.append(intentos)
            nombre=input("Ingrese su nombre")
            listanombre.append(nombre)
        puntos=intentos
        intentos=0
    if n==-1:
        print("Fin del juego")
    largo=len(cantpunt)
    if largo<=1:
        print(cantpunt)
        print(listanombre)
    else:
        for i in range(largo-1):
            for j in range(i+1,largo):
                if cantpunt[i]>cantpunt[j]:
                    auxpunt=cantpunt[i]
                    auxnom=listanombre[i]
                    cantpunt[i]=cantpunt[j]
                    listanombre[i]=listanombre[j]
                    cantpunt[j]=auxpunt
                    listanombre[j]=auxnom
        print(cantpunt)
        print(listanombre)
        if largo>5:
            listadef=[]
            nombredef=[]
            for k in range(5):
                listadef.append(cantpunt[k])
                nombredef.append(listanombre[k])
            print(listadef)
            print(nombredef)
    continuar()

#Funcion continue
def continuar():
    print("Desea seguir jugando?")
    resp=input()
    if resp=="si":
        cantpunt=[]
        intentos=0
        puntos=0
        n=0
        listanombre=[]
        funcjuego(cantpunt,intentos,puntos,n,listanombre)
    else:
        print("Fin del juego")



#Prog ppal
cantpunt=[]
intentos=0
puntos=0
n=0
listanombre=[]
funcjuego(cantpunt,intentos,puntos,n,listanombre)