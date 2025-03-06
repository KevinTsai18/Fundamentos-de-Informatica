"""Ejercicio 3: Imprimir una columna de asteriscos, donde su altura se recibe como parámetro."""

#Func
def alt_ast(a):
    while a!=0:
        print("*")
        a=a-1


#Prog ppal.
n=int(input("Ingrese la altura de la columna de asteriscos:"))
while n<0:
    n=int(input("Medida inválida. Ingrese una altura válida:"))
columna=alt_ast(n)