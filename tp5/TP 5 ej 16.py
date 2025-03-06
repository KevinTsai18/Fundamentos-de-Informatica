"""Ejercicio 16: Realizar una función que calcule y devuelva la sumatoria
de los términos de la sucesión de Fibonacci entre dos números de término dados,
los que se reciben como parámetros."""


#Mandar por mail!!!


#Func
def sumfib(a,b):
    fib1=1
    fib2=1
    if a<b:
        menor=a
        mayor=b
    else:
        menor=b
        mayor=a
    if menor==1 and mayor==2:
        suma=2
    elif menor==1:
        suma=2
        cont=2
        while cont<b:
            fib3=fib1+fib2
            suma=suma+fib3
            fib1=fib2
            fib2=fib3
            cont=cont+1
    else:
        cont=2
        while cont<menor:
            fib3=fib1+fib2
            fib1=fib2
            fib2=fib3
            cont=cont+1
        suma=fib3
        while cont>=menor and cont<mayor:
            fib3=fib1+fib2
            suma=suma+fib3
            fib1=fib2
            fib2=fib3
            cont=cont+1
    return suma
        
#Prog ppal.
x=int(input("Ingrese un número de término:"))
y=int(input("Ingrese otro número de término:"))
resultado=sumfib(x,y)
print(resultado)