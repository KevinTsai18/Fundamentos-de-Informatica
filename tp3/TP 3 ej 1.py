#Ejercicio 1: Ingresar dos números A y B e imprimir el mayor, o cualquiera si son iguales
A=int(input("Ingrese un número:"))
B=int(input("Ingrese otro número:"))
if A>B:
    print(A, "es el mayor valor")
elif B>A:
    print(B, "es el mayor valor")
else:
    print("Los valores son iguales", A)
