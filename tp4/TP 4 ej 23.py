#Ejercicio 23: Leer un número natural M. Calcular e imprimir:
#• La sumatoria de los números naturales menores o iguales que M.
#• La productoria de los números naturales mayores o iguales que M y menores que M*2.
M=int(input("Ingrese un número natural:"))
N=1
suma=0
producto=M
while N<=M:
    suma=suma+N
    N=N+1
while M<=N<M*2:
    producto=producto*N
    N=N+1
print(suma)
print(producto)