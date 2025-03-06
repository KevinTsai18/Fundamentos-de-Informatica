#Ejercicio 27: Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene.
#Ejemplo: Si se ingresa 12345 debe imprimir 5.
cifras=1
n=int(input("Ingrese un número entero"))
while n//10!=0:
    n=n//10
    cifras=cifras+1
print(cifras)