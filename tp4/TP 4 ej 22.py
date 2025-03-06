#Ejercicio 22: Leer un número natural N. Calcular e imprimir los primeros N números naturales impares.
N=int(input("Ingrese un número natural:"))
cant=0
n_impar=1
while cant<N:
    print(n_impar)
    n_impar=n_impar+2
    cant=cant+1