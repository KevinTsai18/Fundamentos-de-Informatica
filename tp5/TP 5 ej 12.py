"""Ejercicio 12: Extraer un dígito de un número entero.
La función recibe como parámetros dos números enteros, uno será del que se extraiga el dígito
y el otro indica qué cifra se desea obtener.
La cifra de la derecha se considera la número 0.
Retornar el valor -1 si no existe el dígito solicitado.
Ejemplo: extraerdigito(12345,1) devuelve 4, y extraerdigito(12345,8) devuelve -1."""


#Func
def sección(a,b):
    if a<0:
        a=a*(-1)
    if b==0:
        cifra=a%10
    elif 10**b>a:
        cifra=-1
    else:
        b=b+1
        while b>0:
            cifra=a%10
            a=a//10
            b=b-1
    return cifra


#Prog ppal.
x=int(input("Ingrese un número entero:"))
y=int(input("Ingrese qué cifra desea obtener (0=última cifra):"))
resultado=sección(x,y)
print(resultado)