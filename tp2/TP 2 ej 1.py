Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: F:\UADE\1er año\PYTHON\module.py =================
hola mundo
>>> n=input("tu mamá")
tu mamá
>>> n
''
>>> n
''
>>> n=input("4")
4
>>> n=int(n)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    n=int(n)
ValueError: invalid literal for int() with base 10: ''
>>> n=input(4)
4
>>> n=int(n)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    n=int(n)
ValueError: invalid literal for int() with base 10: ''
>>> 
=============================== RESTART: Shell ===============================
>>> #Ejercicio 1: Indicar el valor de la variable X después de la ejecución de las siguientes secuencias de comandos:

>>> #1-a
>>> m=2
>>> x=4
>>> y=x+m
>>> y
6
>>> x
4
>>> #1-b
>>> a=3
>>> b=4
>>> x=a*a-b
>>> x
5
>>> #1-c
>>> x=3
>>> h=x*(-4)+2
>>> x=y
>>> x
6
>>> #me tomó el valor de y del punto anterior
>>> #Ejercicio 2: Desarrollar un programa que permita ingresar dos números enteros A y B a través del teclado. Imprimir su suma y su diferencia.
>>> #File-->nuevo archivo para CADA uno

