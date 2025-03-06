#Ejercicio 17: Para las mismas series del ejercicio anterior,
#informar el término de mayor valor que sea menor a un tope ingresado previamente.
#Ejemplo: Para las series a), b) y c), si se ingresa el valor 10 como tope se deberá informar 9, 10 y 7 respectivamente.
#SERIE A
n=0
tope=int(input("Ingrese un tope"))
serie=0
while serie<=tope:
    serie=2**n
    if serie<=tope:
        x1=serie
    serie=3**n
    if serie<=tope:
        x2=serie
    if x1>x2:
        mayor=x1
    else:
        mayor=x2
    n=n+1
print("El mayor valor anterior al tope es", mayor)