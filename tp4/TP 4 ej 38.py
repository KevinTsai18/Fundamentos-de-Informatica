#Desarrollar un programa que lea un número N entero positivo y genere los elementos correspondientes a la conjetura de Ullman (en honor al matemático S. Ullman),
#que consiste en lo siguiente:
#• Si N es par, dividirlo por 2
#• Si es impar multiplicarlo por 3 y sumarle 1.
#• Utilizar este resultado como nuevo número N y repetir el proceso.
#• Al final se obtendrá el número 1, independientemente del número inicial.
#Por ejemplo, cuando el entero inicial es 26 la secuencia queda como 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
#El programa deberá informar también la cantidad de términos obtenidos.
N=int(input("Ingrese un número entero positivo:"))
T=1
print(N)
while N!=1:
    if N%2==0:
        N=N//2
        T=T+1
        print(N)
    else:
        N=N*3+1
        T=T+1
        print(N)
print("Cantidad de términos=", T)
