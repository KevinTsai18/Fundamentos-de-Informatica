"""Ejercicio 7: Dado un número entero, calcular su factorial. Ejemplo: fact(4) = 4*3*2*1 = 24."""
#Func
def func_fact(a):
    factorial=a
    if a>0:
        a=a-1
        while a!=0:
            factorial=factorial*a
            a=a-1
    elif a<0:
        a=a+1
        while a!=0:
            factorial=factorial*a
            a=a+1
    return factorial


#Prog ppal
n=int(input("Ingrese un número entero:"))
resultado=func_fact(n)
print("El factorial de", n, "es", resultado)