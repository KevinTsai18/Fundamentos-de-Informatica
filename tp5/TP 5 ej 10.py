"""Ejercicio 10: Escribir la función comparar(a,b) que reciba como parámetros dos números enteros
y devuelva 1 si el primero es mayor que el segundo,
0 si son iguales o -1 si el primero es menor que el segundo.
Ejemplo: comparar(4,2) devuelve 1, y comparar(2,4) devuelve -1."""


#Func
def comparación(a,b):
    if a>b:
        res_comp=1
    elif b>a:
        res_comp=-1
    else:
        res_comp=0
    return res_comp


#Prog ppal.
x=int(input("Ingrese un número entero:"))
y=int(input("Ingrese otro número entero:"))
resultado=comparación(x,y)
print(resultado)