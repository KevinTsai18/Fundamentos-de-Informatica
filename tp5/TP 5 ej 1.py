"""Ejercicio 1: Dados dos parámetros numéricos, calcular y devolver el resultado de la multiplicación de ambos
utilizando sólo sumas. """

#Función para multiplicar
def multiplicación(a,b):
    prod=0
    while b!=0:
        prod=prod+a
        b=b-1
    return prod

#Programa ppal.
x=int(input("Ingrese un número:"))
y=int(input("Ingrese un número:"))
resultado=multiplicación(x,y)
print("El producto entre", x, "y", y, "es", resultado)