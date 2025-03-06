"""Ejercicio 15: Escribir una función que reciba como parámetros dos números enteros
y devuelva la concatenación de ambos. Por ejemplo concatenar(123,456) devuelve 123456."""



#Func
def concatenacion(a,b):
    if a<0:
        a=-a
    numero=b
    if b<0:
        b=-b
    concifb=1
    while numero//10!=0:
        numero=numero//10
        concifb+=1
    a=a*10**concifb
    numcon=a+b
    return numcon




#Prog ppal.
x=int(input("Ingrese un número entero:"))
y=int(input("Ingrese otro número entero:"))
resultado=concatenacion(x,y)
print(resultado)