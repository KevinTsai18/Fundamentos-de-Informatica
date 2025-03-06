"""Ejercicio 13: Devolver los últimos N dígitos de un número entero pasado como parámetro.
El valor de N también debe ser pasado como parámetro.
Devolver el número completo si N es demasiado grande.
Ejemplo: ultimosdigitos(12345,3) devuelve 345, y ultimosdigitos(12345,8) devuelve 12345."""


#Func
def ultimosdigitos(a,b):
    if a<0:
        a=a*(-1)
    cifras=a%(10**b)
    return cifras



#Prog ppal
x=int(input("Ingrese un número entero:"))
n=int(input("Ingrese los últimos n dígitos que desea:"))
while n<=0:
    n=int(input("Valor inválido.Ingrese los últimos n dígitos que desea:"))
resultado=ultimosdigitos(x,n)
print(resultado)