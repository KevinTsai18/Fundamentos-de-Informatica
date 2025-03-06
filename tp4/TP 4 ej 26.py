#Ejercicio 26: Calcular e imprimir la suma de los números enteros comprendidos entre dos números enteros A y B ingresados por teclado.
#Tener en cuenta que A puede ser mayor, menor o igual que B.
A=int(input("Ingrese un número entero:"))
B=int(input("Ingrese otro número entero:"))
suma=0
if A>B:
    mayor=A
    menor=B
else:
    mayor=B
    menor=A
n=menor+1
while menor<n<mayor:
    suma=suma+n
    n=n+1
print(suma)