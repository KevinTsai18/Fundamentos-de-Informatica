"""Ejercicio 18: Ingresar por teclado un número N y construir una lista llamada SECUENCIAS
con N números enteros al azar entre 1 y 20.
Esta lista se caracterizará porque sus valores deben encontrarse divididos
en secuencias de números separadas por ceros, cuya suma no sea mayor que 20.
Para eso se deberá agregar un elemento de valor 0 a fin de separar cada secuencia de la siguiente,
cuidando que ninguna secuencia sume más de 20. Agregar un 0 adicional al final de la lista
y mostrar la lista obtenida por pantalla. Ejemplo:
Valor de N ingresado: 11
Números al azar generados: 5, 2, 9, 6, 4, 15, 3, 19, 12, 1, 5
Lista SECUENCIAS construida:
5 2 9 0 6 4 0 15 3 0 19 0 12 1 5 0"""
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



#Prog ppal
N=int(input("Ingrese la cantidad de números enteros:"))
lista=listarandom(N)
print(lista)
SECUENCIAS=funcsec(lista)
print(SECUENCIAS)