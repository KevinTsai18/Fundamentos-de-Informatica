#Ejercicio 11: Leer diez números enteros e imprimir el mayor.
mayor=int(input("Ingrese un número:"))
cant=1
while cant<10:
    n=int(input("Ingrese un número:"))
    if n>mayor:
        mayor=n
    cant=cant+1
print("El mayor número es:", mayor)
