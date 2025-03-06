#Ejercicio 17: Para las mismas series del ejercicio anterior,
#informar el término de mayor valor que sea menor a un tope ingresado previamente.
#Ejemplo: Para las series a), b) y c), si se ingresa el valor 10 como tope se deberá informar 9, 10 y 7 respectivamente.
#SERIE C
n=1
termino=0
tope=int(input("Ingrese un tope"))
while termino<20:
    print(n+termino)
    n=n+termino
    termino=termino+1
    if n<=tope:
        mayor=n
print("El mayor valor anterior al tope es:", mayor)
    