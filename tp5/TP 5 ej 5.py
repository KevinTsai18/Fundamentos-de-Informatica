"""Ejercicio 5:Devolver el máximo entre dos números recibidos como parámetros."""
#Función para comparar
def comparación(a,b):
    if a>b:
        mayor=a
    elif b>a:
        mayor=b
    else:
        mayor=a
    return mayor


#Programa ppal
x=int(input("Ingrese un número:"))
y=int(input("Ingrese otro número:"))
mayor=comparación(x,y)
print("El mayor número es", mayor)