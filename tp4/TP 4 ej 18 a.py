#vEjercicio 18: Para las mismas series y topes del ejercicio anterior,
#informar el resultado de la sumatoria de los términos calculados hasta cada tope.
#SERIE A
n=0
suma=0
x1=0
x2=0
tope=int(input("Ingrese un tope"))
while x1<tope and x2<tope:
    x1=2**n
    suma=suma+x1
    x2=3**n
    suma=suma+x2
    n=n+1
print(suma)