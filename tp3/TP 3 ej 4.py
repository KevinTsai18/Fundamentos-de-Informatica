#Ejercicio 4: Ingresar dos números enteros A y B. Desarrollar un programa que determine si A es múltiplo de B y si B es múltiplo de A. Imprimir mensajes aclaratorios.
A=int(input("Ingrese un número entero:"))
B=int(input("Ingrese otro número entero:"))
if A%B==0:
    print(A, "es múltiplo de", B)
elif B%A==0:
    print(B, "es múltiplo de ", A)
else:
    print(A, "no es múltiplo de", B, "y", B, "no es múltiplo de", A)
