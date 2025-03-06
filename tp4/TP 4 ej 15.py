#Ejercicio 15: Leer diez números e imprimir el mayor,
#el menor y el rango del conjunto (El rango de un conjunto se calcula restando el mayor menos el menor).
x=int(input("Ingrese un número:"))
y=int(input("Ingrese un número:"))
cant=2
if x>y:
    mayor=x
    menor=y
else:
    mayor=y
    menor=x
while cant<10:
    n=int(input("Ingrese un número:"))
    cant=cant+1
    if n>mayor:
        mayor=n
    if n<menor:
        menor=n
print("El mayor número es", mayor)
print("El menor número es", menor)
print("El rango del conjunto es", mayor-menor)