#Ejercicio 24: El factorial de un número entero N mayor que cero se define como el producto de todos los enteros X tales que 0 < X <= N.
#Desarrollar un programa para calcular el factorial de un número dado.
#Deberán rechazarse las entradas inválidas (menores que 0).
N=int(input("Ingrese un número entero mayor que 0:"))
X=1
factorial=1
if N<=0:
    print("Entrada inválida")
while X<=N:
    factorial=factorial*X
    X=X+1
if N>0:
    print(factorial)