#Ejercicio 3: Leer un número entero N y determinar si es un número natural (positivo y distinto de 0). Si lo es, imprimirlo junto con su doble. En caso contrario, imprimirlo junto con su triple.
N=int(input("Ingrese un número entero:"))
if N>0:
    print("N=", N)
    print("2N=", N*2)
else:
    print("N=", N)
    print("3N=", N*3)
