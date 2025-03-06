#Ejercicio 5: Realizar un programa para ingresar desde el teclado un conjunto de números
#e informar los elementos ingresados menores a un valor ingresado previamente.
#Finalizar la lectura de datos con el valor -1.
menores=[]
tope=int(input("Ingrese el tope"))
n=int(input("Ingrese un número"))
while n!=-1:
    if n<tope:
        menores.append(n)
    n=int(input("Ingrese un número"))
print("Los números que son menores al tope son:", menores)