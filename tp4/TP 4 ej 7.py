#Ejercicio 7: Realizar un programa para ingresar desde el teclado un conjunto de números y mostrar por pantalla el menor y el mayor de ellos.
#Finalizar la lectura de datos con un valor -1.
x=int(input("Ingrese un número o -1 para finalizar:"))
if x!=-1:
    y=int(input("Ingrese un número o -1 para finalizar:"))
    if y!=-1:
        if x>y:
            mayor=x
            menor=y
        else:
            mayor=y
            menor=x
        z=int(input("Ingrese un número o -1 para finalizar:"))
        while z!=-1:
            if z>mayor and z!=-1:
                mayor=z
                z=int(input("Ingrese un número o -1 para finalizar:"))
            if z<menor and z!=-1:
                menor=z
                z=int(input("Ingrese un número o -1 para finalizar:"))
        print(mayor, "y", menor)