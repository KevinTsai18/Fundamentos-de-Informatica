#Ejercicio 17: Para las mismas series del ejercicio anterior,
#informar el término de mayor valor que sea menor a un tope ingresado previamente.
#Ejemplo: Para las series a), b) y c), si se ingresa el valor 10 como tope se deberá informar 9, 10 y 7 respectivamente.
#SERIE B
n=1
x1=0
mayor=0
tope=int(input("Ingrese un tope"))
while x1<=tope:
    x1=n*(-1)**n
    n=n+1
    if x1>mayor and x1<=tope:
        mayor=x1
print("El mayor valor anterior al tope es:", mayor)