#Ejercicio 6: Realizar un programa para ingresar desde el teclado un conjunto de números e informar en forma separada la cantidad de elementos pares e impares ingresados.
#Finalizar la lectura de datos con el valor -1.
par=0
impar=0
n=int(input("Ingrese un número o -1 para finalizar:"))
while n!=-1:
    if n%2==0:
        par=par+1
        n=int(input("Ingrese un número o -1 para finalizar:"))
    else:
        impar=impar+1
        n=int(input("Ingrese un número o -1 para finalizar:"))
print("Cantidad de elementos pares:", par)
print("Cantidad de elementos impares:", impar)