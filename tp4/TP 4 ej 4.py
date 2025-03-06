#Ejercicio 4: Realizar un programa para ingresar desde el teclado un conjunto de números e informar el último elemento ingresado en una posición par.
#Finalizar la lectura de datos con el valor -1. 
#Ejemplos: Si la secuencia es 3 7 4 5 6 7 9 -1 el valor a informar es 7 Si la secuencia es 3 7 4 5  -1 el valor a informar es 5
n=int(input("Ingrese un número o -1 para finalizar:"))
cant=1
while n!=-1:
    cant=cant+1
    if cant%2==0:
        valor=n
    n=int(input("Ingrese un número o -1 para finalizar:"))
print(valor)
    
    
    