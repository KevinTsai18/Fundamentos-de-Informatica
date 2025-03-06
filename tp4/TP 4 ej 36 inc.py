"""Ejercicio 36: Por cada empleado de una empresa se leen tres datos:
N° de legajo, sueldo básico y antigüedad en la empresa.
Emitir un listado que informe el número de legajo y el salario de los empleados,
calculando el salario de la siguiente forma: Al sueldo básico se le debe sumar un 5% por año de antigüedad,
agregando un 25% adicional si la misma supera los 10 años.
El lote de datos finaliza cuando se ingresa un 0 (cero) como número de legajo."""
legajo=int(input("Ingrese su número de legajo:"))
sueldo=int(input("Ingrese su sueldo básico:"))
ant=int(input("Ingrese sus años de antigüedad:"))
while legajo!=0:
    