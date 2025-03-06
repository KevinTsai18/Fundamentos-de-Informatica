"""Ejercicio 6: Devolver True si el número entero recibido como primer parámetro es múltiplo 
del segundo, o False en caso contrario. Ejemplo: esmultiplo(40,8) devuelve True 
y esmultiplo(50,3) devuelve False."""


#Func
def esmultiplo(a,b):
    t=0
    while b*t<=a:
        m=b*t
        t=t+1
    if m==a:
        m=True
    else:
        m=False
    return m


#Prog ppal.
x=int(input("Ingrese un número entero:"))
y=int(input("Ingrese otro número entero:"))
mult=esmultiplo(x,y)
if mult==True:
    print(x, "es multiplo de", y)
else:
    print(x, "no es multiplo de", y)