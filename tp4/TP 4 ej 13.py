#Ejercicio 13: Leer diez números e imprimir el menor de ellos, indicando además el número de orden con que fue leído.
menor=int(input("Ingrese un número:"))
cant=1
while cant<10:
    n=int(input("Ingrese un número:"))
    cant=cant+1
    if n<menor:
        menor=n
        orden=cant
print(menor)
print(orden)