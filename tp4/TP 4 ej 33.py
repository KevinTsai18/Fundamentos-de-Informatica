""" La raíz cuadrada de un número positivo n puede calcularse mediante la siguiente fórmula de Newton:
donde a es una aproximación a .
Al aplicar repetidamente esta fórmula reemplazando a por la aproximación obtenida en el paso anterior,
se obtiene cada vez una aproximación mejor.
Desarrollar un programa que calcule la raíz cuadrada aproximada de un número entero positivo n,
utilizando como primera aproximación a n/2. Detener el proceso cuando la diferencia entre dos cálculos sucesivos sea menor a 0,0001.
"""
n=int(input("Ingrese un número positivo"))
a=n/2
raiz=(n/a+a)/2
while raiz-a>0.0001:
    a=raiz
    raiz=(n/a+a)/2
print(raiz)