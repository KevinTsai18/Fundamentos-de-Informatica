#Ejercicio 12: Leer dos números A y B enteros positivos.
#Calcular el producto A * B por sumas sucesivas e imprimir el resultado.
#Ejemplo: 4 * 3 = 4 + 4 + 4 (4 sumado 3 veces).
A=int(input("Ingrese un número entero positivo:"))
B=int(input("Ingrese otro número entero positivo:"))
cant=0
P=0
while cant!=B:
    P=P+A
    cant=cant+1
print("A*B=", P)