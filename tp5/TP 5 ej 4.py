"""Ejercicio 4: Verificar si un número es par o impar, devolviendo True o False respectivamente."""
#Función
def paridad(n):
    if n%2==0:
        par=True
    else:
        par=False
    return par


#Programa ppal.
n=int(input("Ingrese un número:"))
par=paridad(n)
if par==True:
    print(n, "es par.")
else:
    print(n, "es impar.")