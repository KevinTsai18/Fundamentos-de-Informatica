#Ejercicio 2: Realizar un programa para ingresar desde el teclado un conjunto de números.
#Al finalizar mostrar por pantalla el primer y último elemento ingresado. Finalizar la lectura con el valor-1.
pn=int(input("Ingrese un número o -1 pára finalizar:"))
if pn!=-1:
    n=int(input("Ingrese otro número o -1 pára finalizar:"))
    if n!=-1:
        while n!=-1:
            un=n
            n=int(input("Ingrese otro número o -1 pára finalizar:"))
        print("1° número=", pn, "y último número=", un)
