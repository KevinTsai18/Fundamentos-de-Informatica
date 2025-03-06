#Ejercicio 25: Leer dos números naturales A y B.
#Calcular AB mediante productos sucesivos y mostrar el resultado.
#Tener en cuenta que A y B pueden ser nulos.
A=int(input("Ingrese un número natural:"))
B=int(input("Ingrese otro número natural:"))
resultado=0
n=0
while n<B:
    resultado=resultado+A
    n=n+1
print(resultado)