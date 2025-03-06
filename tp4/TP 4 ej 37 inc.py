#Ejercicio 37: Una empresa cuenta con 100 empleados,
#divididos en tres categorías A, B y C.
#Por cada empleado se lee su legajo, categoría y salario.
#Se solicita elaborar un informe que contenga:
#• Importe total de salarios pagados por la empresa.
#• Cantidad de empleados que ganan más de $20000.
#• Cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”.
#• Legajo del empleado que más gana. • Sueldo más bajo.
#• Importe total de sueldos por cada categoría.
#• Salario promedio.
imptotal=0
catA=0
catB=0
catC=0
emp=0
emp20000=0
emp5000C=0
legajomayorsal=0
salmenor=0
saltotalA=0
saltotalB=0
saltotalC=0
while emp<10
    legajo=int(input("Ingrese su número de legajo:"))
    categoria=input("Ingrese su categoría(A,B,C)"))
    salario=int(input("Ingrese su salario"))
    emp=emp+1
    imptotal=imptotal+salario
    if salario>20000:
        emp20000=emp20000+1
    if salario<5000 and categoria="C":
        emp5000C=emp5000C+1
print("Importe total:", imptotal)
print(