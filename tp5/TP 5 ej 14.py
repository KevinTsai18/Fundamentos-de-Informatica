"""Ejercicio 14: Obtener el dígito central de un número entero pasado como parámetro,
sólo si la cantidad de dígitos es impar. Si la longitud fuera par devolver -1.
Ejemplo: digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1."""


#Func
def digitocentral(a):
    if a<0:
        a=-a
    numero=a
    cant_cifras=1
    while numero//10!=0:
        numero=numero//10
        cant_cifras+=1
    if cant_cifras%2==0:
        centro=-1
    else:
        cant_cifras=(cant_cifras+1)//2
        while cant_cifras!=0:
            centro=a%10
            a=a//10
            cant_cifras-=1
    return centro
    



#Prog ppal.
x=int(input("Ingrese un número:"))
resultado=digitocentral(x)
print(resultado)

