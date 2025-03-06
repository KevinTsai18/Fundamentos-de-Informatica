#Realizar un programa que lea un número natural H e imprima un mensaje indicando si H es primo o no.
#Se dice que un número es primo cuando sólo es divisible por sí mismo y por la unidad.
H=n=int(input("Ingrese un número natural:"))
p=1
primo=0
while p<=H:
    if H%p==0:
        primo=primo+1
    p=p+1
if primo==2:
    print("Es primo")
else:
    print("No es primo")
    