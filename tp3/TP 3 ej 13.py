#Ejercicio 13: Diseñar un programa que calcule y muestre el sueldo neto de un empleado en
#base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa
#el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es
#casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
#También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social:
#3%, Sindicato: 3%
#Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (‘s’ o ‘c’). Se debe informar: (reemplazar los 9 por los
#valores que correspondan)
#Estado Civil: Soltero/Casado
#Sueldo básico Antigüedad Descuentos Importe
# $ 999.99 99 años + 999.99
#Jubilación - 999,99
#Obra Social - 999,99
#Sindicato - 999,99
#------------
#Sueldo Neto 999,99

#Para darle formato 
#print("Es civil: s/c")
#print("sueldo basico          antigüedad          descuento       ")

EsCivil=input("Ingerse su estado civil (s=soltero, c=casado):")
Sueldo=int(input("Ingrese su sueldo básico:"))
Ant=int(input("Ingrese su/s año/s de antigüedad:"))
Jub=Sueldo*11/100
ObSoc=Sueldo*3/100
Sind=ObSoc
if EsCivil=="s":
    Incr=Sueldo/20
if EsCivil=="c":
    Incr=Sueldo*7/100
print("Sueldo básico            Antigüedad     Descuentos     Importe ")
print("  $", Sueldo,"             ", Ant, "años                      +",Incr*Ant+Sueldo)
print("                             Jubilación:-", Jub)
print("                            Obra Social:-", ObSoc)
print("                              Sindicato:-", Sind)
print("                                         -------------------------------")
print("                             Sueldo Neto ", Incr*Ant+Sueldo-Jub-ObSoc-Sind)
