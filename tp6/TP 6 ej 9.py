"""Ejercicio 9: Dado una lista de N números (por ejemplo 5),
devolver una lista de N-1 valores booleanos,
tal que cada valor de este último arreglo
corresponde al resultado de la comparación de los pares de valores consecutivos del primer arreglo.
El valor booleano es True si el primer elemento del par es menor o igual que el siguiente, y False si no lo es. Ejemplo:
Lista original: 
4 2 8 8 6
Resultado:
F T T F"""
import random

cant=0
lista=[]
while cant<=5:
    lista.append(random.randint(0,20))
    cant+=1
print(lista)
cant=cant-1
nuevalista=[]
for i in range(cant):
    if lista[i]<=lista[i+1]:
        nuevalista.append("T")
    else:
        nuevalista.append("F")
print(nuevalista)
