#Ejercicio 6: Una editorial determina el precio de un libro según la cantidad de páginas que
#contiene. El costo básico del libro es de $125, más $2,20 por página con encuadernación rústica. Si el número de páginas supera las 300 la encuadernación
#debe ser en tela, lo que incrementa el costo en $80. Además, si el número de
#páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación que incrementa el costo en $136. Desarrollar un programa que
#calcule el costo de un libro dado el número de páginas.

páginas=int(input("Ingrese la cantidad de páginas del libro:"))
if páginas<=300:
    print("El costo del libro es de $",125+páginas*2.20)
elif 300<páginas<=600:
    print("El costo del libro es de $",125+80+páginas*2.20)
else:
    print("El costo del libro es de $",125+136+páginas*2.20)
