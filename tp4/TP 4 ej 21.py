#Ejercicio 21: Leer un número natural N. Calcular e imprimir los números naturales pares menores que N.
N=int(input("Ingrese un número natural:"))
while N>0:
    N=N-1
    if N%2==0 and N!=0:
        print(N)
