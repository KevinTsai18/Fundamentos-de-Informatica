#vEjercicio 18: Para las mismas series y topes del ejercicio anterior,
#informar el resultado de la sumatoria de los términos calculados hasta cada tope.
"""SERIE B"""
n=1
x1=0
suma=0
tope=int(input("Ingrese un tope"))
while x1<tope:
    x1=n*(-1)**n
    n=n+1
    suma=suma+x1
print(suma)