#Ejercicio 3: Realizar un programa para ingresar desde el teclado un conjunto de números e informar si la cantidad de elementos es impar o par,
#sin utilizar contadores. Finalizar la lectura de datos con el valor -1.
señal=0
n=int(input("Ingrese un número  o -1 para finalizar:"))
while n!=-1:
    if señal==0:
        señal=1
        n=int(input("Ingrese un número  o -1 para finalizar:"))
    else:
        señal=0
        n=int(input("Ingrese un número  o -1 para finalizar:"))
if señal==0:
    print("Es par")
else:
    print("Es impar")