#Ejercicio 30: Leer un número natural N. Calcular e imprimir los primeros N términos de la sucesión geométrica de razón 3,
#cuyos primeros términos son 1, 3, 9, 27, 81..... es decir 3**0, 3**1, 3**2, 3**3....
N=int(input("Ingrese un número natural N:"))
potencia=0
while potencia<N:
    print(3**potencia)
    potencia=potencia+1