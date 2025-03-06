"""Ejercicio 28: Leer un número entero e invertir las cifras que contiene.
Imprimir por pantalla el número invertido. Por ejemplo, si se ingresa 1234 debe mostrar 4321."""
n=int(input("Ingrese un número:"))
inv=n%10
while n//10!=0:
    n=n//10
    resto=n%10
    inv=inv*10+resto
print(inv)