"""Ejercicio 8: Calcular el Máximo Común Divisor de dos enteros no negativos,
basándose en las siguientes fórmulas matemáticas:
• MCD(X,X) = X
• MCD(X,Y) = MCD(Y,X)
• Si X > Y => MCD(X,Y) = MCD(X-Y,Y).
Ejemplo: MCD(40,15) devuelve 5."""


#Func
def calcMCD(a,b):
    if a==b:
        mcd=a
    else:
        cont=1
        while cont<=a and cont<=b:
            if a%cont==0 and b%cont==0:
                mcd=cont
            cont=cont+1
    return mcd


#Prog ppal.
x=int(input("Ingrese un número natural:"))
while x<=0:
    x=int(input("Número inválido. Ingrese un número natural:"))
y=int(input("Ingrese un número natural:"))
while y<=0:
    y=int(input("Número inválido. Ingrese un número natural:"))
resultado=calcMCD(x,y)
print("El MCD de", x, "y", y, "es", resultado)