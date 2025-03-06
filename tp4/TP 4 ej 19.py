#Ejercicio 19: Leer un conjunto de números que representan edades de un grupo de personas,
#finalizando la lectura cuando se ingrese el número 999.
#Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos.
n=0
menores=0
mayores=0
suma_menor=0
suma_mayor=0
while n!=999:
    n=int(input("Ingrese una edad:"))
    if n<18:
        menores=menores+1
        suma_menor=suma_menor+n
    if n>=18 and n!=999:
        mayores=mayores+1
        suma_mayor=suma_mayor+n
print("Menores de 18 años:", menores, "personas")
print("Mayores o de 18 años:", mayores, "personas")
print("Promedio de menores:", suma_menor/menores)
print("Promedio de mayores:", suma_mayor/mayores)