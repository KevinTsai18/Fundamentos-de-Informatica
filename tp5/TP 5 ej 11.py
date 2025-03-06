"""Ejercicio 11: Adaptar el programa que utiliza la fórmula de Newton para calcular
la raíz cuadrada de un número positivo N (de la práctica anterior) para que trabaje como una función."""

#Func
def form_N(n):
    a=n/2
    raiz=(n/a+a)/2
    while raiz-a>0.0001:
        a=raiz
        raiz=(n/a+a)/2
    return raiz


#Prog ppal.
n=int(input("Ingrese un número positivo"))
resultado=form_N(n)
print(resultado)
