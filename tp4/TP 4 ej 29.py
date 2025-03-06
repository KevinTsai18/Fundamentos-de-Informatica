#Ejercicio 29: Juancito está descontento con su rendimiento en las clases de Programación.
#En su primer programa cometió un error, en el segundo dos, en el tercero cuatro, en el cuarto ocho y así sucesivamente.
#Las clases duran S semanas y debe realizar dos programas semanales.
#Diseñar un programa que lea S y calcule el número de errores que Juancito debe esperar cometer en su último programa,
#si mantiene constante su rendimiento actual. Resolver este problema utilizando dos estrategias distintas.
S=int(input("Ingrese la cantidad de semanas:"))
pot=1
sem=1
while sem<=S:
    error=2**pot
    pot=pot+2
    sem=sem+1
print(error) 