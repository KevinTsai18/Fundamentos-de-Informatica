#Ejercicio 20: Leer A y B enteros positivos y verificar que A >= B. Una vez hecha esta verificación,
#dividir A sobre B mediante restas sucesivas, es decir sin utilizar el operador de división.
#Ejemplo 5 dividido 2:
#• Restamos el dividendo menos el divisor: 5 - 2 = 3
#• Repetimos esta resta tantas veces como sea posible: 3 - 2 = 1
#• Al ser el resultado (1) menor que el divisor (2), detenemos el proceso.
#• Este resultado es el resto de la división, mientras que el cociente se obtiene contando la cantidad de restas que se efectuaron.
#Imprimir dividendo, divisor, cociente y resto.
A=int(input("Ingrese un número entero positivo"))
B=int(input("Ingrese otro número entero positivo"))
cociente=0
resto=0
if A>=B:
    dividendo=A
    divisor=B
else:
    dividendo=B
    divisor=A
print(dividendo, "es el dividendo")
print(divisor, "es el divisor")
while not divisor>dividendo:
    dividendo=dividendo-divisor
    cociente=cociente+1
resto=dividendo
print(cociente, "es el cociente")
print(resto, "es el resto")