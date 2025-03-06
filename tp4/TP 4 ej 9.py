#Ejercicio 9: Leer cien números e imprimir su promedio.
cant=0
suma=0
while cant<100:
    n=int(input("Ingrese un número:"))
    suma=suma+n
    cant=cant+1 
print(suma/cant)