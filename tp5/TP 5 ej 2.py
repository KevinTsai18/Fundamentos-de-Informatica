"""Ejercicio 2: Dados dos parámetros enteros A y B,
obtener A**B (A elevado a la B) mediante multiplicaciones sucesivas, utilizando la función del ejercicio 1."""

#Función para potenciar
def potencia(a,b):
    pot=1
    while b!=0:
        pot=pot*a
        b=b-1
    return pot

#Programa ppal.
x=int(input("Ingrese el número a elevar:"))
y=int(input("Ingrese su potencia:"))
resultado=potencia(x,y)
print("La potencia de", x, "elevado a", y, "es", resultado)